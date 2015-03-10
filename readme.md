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
*link = integrator.get_xml_link(local_xml_debug=False,
                                local_html_debug=False)
*flight_info = integrator.get_results(link)
*print(flight_info)

Of course you first have to fill the plan dictionary and the
simbrief_query_settings dictionary. These dictionaries consist of key-value
pairs where the keys are input field names, checkbox names, select names at
the called form html file. Supply inputs as strings (even the numbers),
checkboxes with the value True and selects with the strings that are visible
on the screen, not in the html code.
All parameters are advised to be filled out that is offered at the API page,
see: http://www.simbrief.com/forum/viewtopic.php?f=6&t=243
It is advised to fix some of the simbrief_query_settings in the implementation,
e.g.: planformat, units, notams

**Keys detailed**
[plan]:
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
aircraft (e.g.: 'P05' equals +5%), valid values: M30..P30
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
- climb: climb profile for the aircraft (e.g.: '250/300/78'), valid values
are aircraft specific
- cruise: cruise profile for the aircraft (e.g.: 'LRC'), valid values
are aircraft specific
- descent: descent profile for the aircraft (e.g.: '80/280/250'), valid values
are aircraft specific
- civalue: costindex (e.g.: 'AUTO'), valid values: AUTO, 0..100, it is only
taken into consideration if the cruise profile is 'CI'

[simbrief_query_settings]:
- planformat: flight plan format (e.g.: lido, aal, aca, afr, awe,
baw, ber, dal, dlh, jbu, jza, ryr, uae, ual, ual f:wz)
- units: weight (e.g.: 'LBS' or 'KGS')
- navlog: (e.g.: True)
- etops: (e.g.: True)
- stepclimbs: (e.g.: True)
- tlr: runway analysis (e.g.: True)
- notams: include notams (e.g.: True)
- firnot: FIRNOTAMs (e.g.: True)
- maps: map detail level (e.g.: 'Simple', 'Detailed', 'None')

**Aircraft specific possibilities**
[B736, B737, B738]:
- climb profile: '250/280/78'
- cruise profile: 'CI', 'LRC', 'M75', 'M78', 'M79', 'M80'
- descent profile: '78/280/250'

[B763]:
- climb profile: '250/290/78'
- cruise profile: 'CI', 'LRC', 'M76', 'M78', 'M80', 'M82', 'M84'
- descent profile: '79/290/250'

[CRJ2]:
- climb profile: 'AUTO'
- cruise profile: '290/M72'
- descent profile: 'AUTO'

[DH8D]:
- climb profile: 'I-850', 'II-850', 'III-850', 'I-900', 'II-900', 'III-900'
- cruise profile: 'ISC', 'LRC', 'HSR', 'MCR'
- descent profile: 'I-850', 'II-850', 'III-850'

[T154]:
- climb profile: 'AUTO'
- cruise profile: '300/M80'
- descent profile: 'AUTO'