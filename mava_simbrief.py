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

mava_simbrief_url = "http://flare.privatedns.org/mava_simbrief/simbrief_form.php"
xml_link_fix_part = "http://www.simbrief.com/ofp/flightplans/xml/"

#driver = webdriver.Firefox()
##driver.get("file://" + os.getcwd() + os.sep + "mava_simbrief.html")
#driver.get(mava_simbrief_url)
#button = driver.find_element_by_name("submitform")
#button.send_keys(Keys.RETURN)
#
#is_briefing_available = False
#
#try:
#    is_briefing_available = (WebDriverWait(driver, 120).
#        until(EC.presence_of_element_located((By.NAME, "hidden_is_briefing_available"))))
#    xml_link_element = driver.find_element_by_name('hidden_link')
#    xml_link_generated_part = xml_link_element.get_attribute('value')
#    xml_link = xml_link_fix_part + xml_link_generated_part + '.xml'
#    print xml_link
#finally:
#    driver.quit()
#
is_briefing_available = True
xml_link = "file:///home/szebenyib/Dropbox/fs/mava_simbrief/xml.xml"
if is_briefing_available:
    response = urllib2.urlopen(xml_link)
    xml_content = response.read()
    tree = etree.parse(StringIO(xml_content))
    context = etree.iterparse(StringIO(xml_content))
    #Holds analysis data not used
    available_info = {}
    #Holds analysis data to be used
    flight_info = {}
    notams_list = []
    i = 0
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
    #Adding parts that occured multiple time
#    flight_info['notams'] = notams_list
#    print flight_info
    print available_info['icao_code']
    print available_info['pid']
    print sorted(available_info.keys())
    print '---'
    print flight_info
    f = open('simbrief_plan.html', 'w')
    f.write(available_info['plan_html'])
#    print etree.tostring(tree, pretty_print=True)
#    print etree.tostring(root)
#driver.get(

#try:
#    xmllocation = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "mydynel
#"mava_simbrief.html")
#browser = webbrowser.get('firefox')
#url = "file://" + os.getcwd() + os.sep + "mava_simbrief.html"
#browser.open_new(url)
