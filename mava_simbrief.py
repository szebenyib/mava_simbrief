#needed for os specific separators
import os
#selenium is needed for browser manipulation
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
#urllib is needed to obtaing the xml
import urllib2
#xmlparser
from lxml import etree
from StringIO import StringIO
import lxml.html

class MavaSimbriefIntegrator():
    """Implements the integration with the excellent Simbrief pilot briefing
    system for MALEV Virtual."""

    def __init__(self,
            simbrief_query_settings=None,
            mava_simbrief_url=None,
            xml_link_fix_part=None):
        """Init the integrator with settings that are typical of our use.
        @param: simbrief_query_settings - a dictionary of query settings
        @param: mava_simbrief_url - url to the form that is sent to simbrief
        on the mava server
        @param: xml_link_fix_part = url to the simbrief website under which the
        xml is to be found"""
        if simbrief_query_settings is None:
            self.simbrief_query_settings = {
                'navlog': 0,
                'etops': 0,
                'stepclimbs': 0,
                'tlr': 0,
                'notams': 0,
                'firnot': 0,
                'detail': 'detail',
            }
        else:
            self.simbrief_query_settings = simbrief_query_settings
        if mava_simbrief_url is None:
            self.mava_simbrief_url = "http://flare.privatedns.org/mava_simbrief/simbrief_form.php"
        else:
            self.mava_simbrief_url = mava_simbrief_url
        if xml_link_fix_part is None:
            self.xml_link_fix_part = "http://www.simbrief.com/ofp/flightplans/xml/"
        else:
            self.xml_link_fix_part = xml_link_fix_part

    def get_xml_link(self,
            local_xml_debug=False,
            local_html_debug=False):
        """Obtains the link of the xml to be processed.
        @param local_xml_debug - if True then not the real location will be
        checked but the current working dir will be searched for 'xml.xml'
        @param local_html_debug - if True then not real mava_simbrief_url will
        be used but the current working dir will be searched for
        'mava_simbrief.html'
        @returns: the string of the xml link if it could be obtained and None
        otherwise"""
        #Finding xml_link
        is_briefing_available = False
        if local_xml_debug:
            xml_link = ("file://"
                        + os.getcwd()
                        + os.sep
                        + "xml.xml")
            is_briefing_available = True
        else:
            driver = webdriver.Firefox()
            if local_form_debug:
                driver.get("file://" + os.getcwd() + os.sep + "mava_simbrief.html")
                is_briefing_available = True
            else:
                driver.get(mava_simbrief_url)
            #Loading page
            button = driver.find_element_by_name("submitform")
            button.send_keys(Keys.RETURN)
            #Checking for results
            try:
                is_briefing_available = (WebDriverWait(driver, 120).
                    until(EC.presence_of_element_located((By.NAME, "hidden_is_briefing_available"))))
                xml_link_element = driver.find_element_by_name('hidden_link')
                xml_link_generated_part = xml_link_element.get_attribute('value')
                xml_link = xml_link_fix_part + xml_link_generated_part + '.xml'
                print xml_link
            finally:
                driver.quit()
        if is_briefing_available:
            return xml_link
        else:
            return None

    def get_results(self,
            xml_link):
        """Parses the xml for information.
        @param xml_link - a path to the xml file
        @return a dictionary of the found information"""
        #Setup variables
        ##Holds analysis data not used
        available_info = {}
        ##Holds analysis data to be used
        flight_info = {}
        ##Holds notams
        notams_list = []
        ##Notam counter
        i = 0
        #Obtaining the xml
        response = urllib2.urlopen(xml_link)
        xml_content = response.read()
        #Processing xml
        tree = etree.parse(StringIO(xml_content))
        context = etree.iterparse(StringIO(xml_content))
        for action, element in context:
            #Processing tags that occur multiple times
            ##NOTAMS
            if element.tag == 'notamdrec':
                notams_element_list = list(element)
                notam_dict = {}
                for notam in notams_element_list:
                    notam_dict[notam.tag] = notam.text
                notams_list.append(notam_dict)
                i += 1
            ##WEATHER
            elif element.tag == 'weather':
                weather_element_list = list(element)
                weather_dict = {}
                for weather in weather_element_list:
                    flight_info[weather.tag] = weather.text
            else:
                available_info[element.tag] = element.text
        #Processing plan_html
        ##Obtaining chart links
        image_links = []
        for image_link_a_element in lxml.html.find_class(available_info['plan_html'], 'ofpmaplink'):
            for image_link_tuple in image_link_a_element.iterlinks():
                if image_link_tuple[1] == 'src':
                    image_links.append(image_link_tuple[2])
        flight_info['image_links'] = image_links
        print available_info['icao_code']
        print available_info['pid']
        print sorted(available_info.keys())
        f = open('simbrief_plan.html', 'w')
        f.write(available_info['plan_html'])
        return flight_info

if __name__ == "__main__":
    mava_simbrief_url = "http://flare.privatedns.org/mava_simbrief/simbrief_form.php"
    xml_link_fix_part = "http://www.simbrief.com/ofp/flightplans/xml/"

    integrator = MavaSimbriefIntegrator()
    link = integrator.get_xml_link(local_xml_debug=True,
                                local_html_debug=True)
    flight_info = integrator.get_results(link)
    print flight_info

