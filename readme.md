MALEV Virtual Simbrief Integration System
=========================================

# Installation

# Usage
Instantiate MavaSimbriefIntegrator with a plan and simbrief_query_settings
dictionary, plus the url to the simbrief_form.html and the url to the xml
at the simbrief webpage.

**Example**
*integrator = MavaSimbriefIntegrator(plan=plan,
                 simbrief_query_settings=simbrief_query_settings,
                 mava_simbrief_url="http://virtualairlines.hu/" \
                                   "mava_simbrief/simbrief_form.html,
                 xml_link_fix_part="http://www.simbrief.com/ofp/" \
                                     "flightplans/xml/")*

Of course you first have to fill the plan dictionary and the
simbrief_query_settings dictionary. These dictionaries consist of key-value
pairs where the keys are input field names, checkbox names, select names at
the called form html file. Supply inputs as strings (even the numbers),
checkboxes with the value True and selects with the strings that are visible
on the screen, not in the html code.
All parameters are advised to be filled out that is offered at the API page,
see: http://www.simbrief.com/forum/viewtopic.php?f=6&t=243

**Keys detailed**
[plan]
- airline: 3 letter ICAO identifier (e.g.: 'MAH')
- fltnum: desired flight number without airline identifier (e.g.: '764')
- type: 4 letter ICAO type designator (e.g.: 'B738'), see:
http://en.wikipedia.org/wiki/List_of_ICAO_aircraft_type_designators
- orig: 4 letter ICAO code of the departure airport (e.g.: 'LHBP')
- dest: 4 letter ICAO code of the arrival airport (e.g.: 'LSZH')
- altn: 4 letter ICAO code of the alternate airport (e.g.: 'LSGG')
- date: DDMMMYY (e.g.: 'DDMMMYY')
- deph: departure time, hour in zulu time (e.g.: '20')
- depm: departure time, minutes (e.g.: '00')
- route: (e.g.: 'GILEP DCT ARSIN UL851 SITNI UL856 NEGRA')
- fl: desired cruise level in feet without spaces (e.g.: '36000'), if left
empty or 'AUTO' then the system will choose the flight level
- steh: arrival time, hour in zulu time (e.g.: '22')
- steh: arrival time, minutes (e.g.: '05')
- reg: aircraft registration (e.g.: 'HA-LOC')
- fin: aircraft fin marker (e.g.: 'LOC')
- selcal: selcal code (e.g.: 'XXXX')
- cpt: pilot's name (e.g.: 'BALINT SZEBENYI')
- pid: pilot's internal id at virtual airline (e.g.: 'P008')
- fuelfactor: fuel burn multiplier used to tweak calculations to an add-on
aircraft (e.g.: 'P05' equals +5%)
- pax: number of passengers on board (e.g.: '100'), it is 230 lbs per pax with
bags, it is added to the empty weight to obtain the zero fuel weight
- cargo: additional commercial cargo in thousands (e.g.: '5.0'), it is
added to the empty weight to obtain the zero fuel weight
- manualzfw: overrides the calculated zfw of simbrief thereby disregarding 
pax and cargo information (e.g.: '42.7')
- taxiout: time to taxi out to the rwy at the departure airport in minutes
(e.g.: '10')
- taxiin: time to taxi from the rwy to the gate at the arrival airport in
minutes (e.g.: '4')
- resvrule: how much time to plan for with reserve fuel (e.g.: '45'), if
'AUTO' then it is 45 minutes for props and 30 for jets
- contpct: contingency fuel as additional percentage on the estimated fuel
(e.g.: '0.05'), if 'AUTO' then it is 5% or 15 minutes, whichever is higher
- addedfuel: extra fuel to add in thousands on captain's discretion above the
calculated value of the planning system (e.g.: '0.5')
- origrwy: planned departure runway (e.g.: '31L')
- destrwy: planned arrival runway (e.g.: '34')
        
        'climb': '250/300/78',
        'descent': '80/280/250',
        'cruise': 'LRC',
        'civalue': 'AUTO',
*
self.simbrief_query_settings = {
    'navlog': True,
    'etops': True,
    'stepclimbs': True,
    'tlr': True,
    'notams': True,
    'firnot': True,
    'maps': 'Simple',
}

plan = {
        'airline': 'MAH',
        'fltnum': '764',
        'type': 'B738',
        'orig': 'LHBP',
        'dest': 'LSZH',
        'date': '25FEB15',
        'deph': '20',
        'depm': '00',
        'route': 'GILEP DCT ARSIN UL851 SITNI UL856 NEGRA',
        'steh': '22',
        'stem': '05',
        'reg': 'HA-LOC',
        'fin': 'LOC',
        'selcal': 'XXXX',
        'pax': '100',
        'altn': 'LSGG',
        'fl': '36000',
        'cpt': 'BALINT SZEBENYI',
        'pid': 'P008',
        'fuelfactor': 'P000',
        'manualzfw': '42.7',
        'addedfuel': '2.5',
        'contpct': '0.05',
        'resvrule': '45',
        'taxiout': '10',
        'taxiin': '4',
        'cargo': '5.0',
        'origrwy': '31L',
        'destrwy': '34',
        'climb': '250/300/78',
        'descent': '80/280/250',
        'cruise': 'LRC',
        'civalue': 'AUTO',
    }