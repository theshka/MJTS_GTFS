# Import Google TransitFeed
import transitfeed
from transitfeed import ServicePeriod

# Version
mjts_version = "0.0.2"

# New Schedule
schedule = transitfeed.Schedule()

# Create Agency
schedule.AddAgency("Moose Jaw Transit Service", "http://www.moosejaw.ca/?service=city-of-moose-jaw-transit-division",
                   "America/Regina")

# Calendars
service_periods = []

## Weekday
service_periods.append(ServicePeriod(id="weekday"))
service_periods[0].SetWeekdayService()
service_periods[0].SetStartDate("20151005")
service_periods[0].SetEndDate("20161005")
### Holidays/No Service Days
service_periods[0].SetDateHasService('20151224', False)
service_periods[0].SetDateHasService('20151225', False)
service_periods[0].SetDateHasService('20151226', False)

## Saturday
service_periods.append(ServicePeriod(id="saturday"))
service_periods[1].SetDayOfWeekHasService(5)
service_periods[1].SetStartDate("20151005")
service_periods[1].SetEndDate("20161005")
### Holidays/No Service Days
service_periods[1].SetDateHasService('20151224', False)
service_periods[1].SetDateHasService('20151225', False)
service_periods[1].SetDateHasService('20151226', False)

#Add all service period objects to the schedule
schedule.SetDefaultServicePeriod(service_periods[0], validate=True)
schedule.AddServicePeriodObject(service_periods[1], validate=True)

# Fares

# Routes
## 1- Athabasca East
ABE = schedule.AddRoute(short_name="1", long_name="Athabasca East",
                          route_type="Bus")
## 2- Sunningdale
SUN = schedule.AddRoute(short_name="2", long_name="Sunningdale",
                          route_type="Bus")
## 3- Athabasca West
ABW = schedule.AddRoute(short_name="3", long_name="Athabasca West",
                          route_type="Bus")
## 4- Westmonut
WES = schedule.AddRoute(short_name="4", long_name="Westmount",
                          route_type="Bus")

# Stops
## Athabasca East Stops
abe_1001 = schedule.AddStop(lng=-105.535112, lat=50.391708, name = "Main St. N @ High St. W")
abe_1002 = schedule.AddStop(lng=-105.537392, lat=50.391613, name = "High St. W @ 1st Ave. NW")
abe_1003 = schedule.AddStop(lng=-105.537371, lat=50.396825, name = "1st Ave. NW @ Caribou St. W")
abe_1004 = schedule.AddStop(lng=-105.534774, lat=50.396845, name = "Caribou St. E @ Main St. N")
abe_1005 = schedule.AddStop(lng=-105.531893, lat=50.396877, name = "Caribou St. E @ 1st Ave. NE")
abe_1006 = schedule.AddStop(lng=-105.528183, lat=50.396880, name = "Caribou St. E @ Ross Cres.@3rd Ave. NE")
abe_1007 = schedule.AddStop(lng=-105.524750, lat=50.396858, name = "Caribou St. E @ 4th Ave. NE")
abe_1008 = schedule.AddStop(lng=-105.524557, lat=50.398884, name = "4th Ave. NE @ Oxford St. E")
abe_1009 = schedule.AddStop(lng=-105.524633, lat=50.400889, name = "4th Ave. NE @ Hall St. E")
abe_1010 = schedule.AddStop(lng=-105.524658, lat=50.402656, name = "4th Ave. NE @ Saskatchewan St. E")
abe_1011 = schedule.AddStop(lng=-105.527507, lat=50.402627, name = "Saskatchewan St. E @ 3rd Ave. NE")
abe_1012 = schedule.AddStop(lng=-105.531771, lat=50.402648, name = "Saskatchewan St. E @ 1st Ave. NE")
abe_1013 = schedule.AddStop(lng=-105.534698, lat=50.406387, name = "Town & Country Dr. @ Main St. N")
abe_1014 = schedule.AddStop(lng=-105.533552, lat=50.412926, name = "Main St. East Service Road @ Thatcher Dr. E")
abe_1015 = schedule.AddStop(lng=-105.527029, lat=50.419106, name = "Dr. F.H. Wigmore Regional Hospital")
abe_1016 = schedule.AddStop(lng=-105.521458, lat=50.411943, name = "Highland Rd. @ Thatcher Dr. E")
abe_1017 = schedule.AddStop(lng=-105.515950, lat=50.411921, name = "Thatcher Dr. E @ Chester Rd")
abe_1018 = schedule.AddStop(lng=-105.511780, lat=50.411853, name = "Thatcher Dr. E @ 9th Ave. NE")
abe_1019 = schedule.AddStop(lng=-105.511762, lat=50.407610, name = "9th Ave. NE @ Prairie Oasis Trailer Court")
abe_1020 = schedule.AddStop(lng=-105.511820, lat=50.404814, name = "9th Ave. NE @ Lakeview Trailer Court")
abe_1021 = schedule.AddStop(lng=-105.511825, lat=50.396861, name = "9th Ave. NE @ Caribou St. E")
abe_1022 = schedule.AddStop(lng=-105.508979, lat=50.396846, name = "Caribou St. E @ 10th Ave. NE")
abe_1023 = schedule.AddStop(lng=-105.505852, lat=50.395337, name = "11th Ave. NE @ Athabasca St. E")
abe_1024 = schedule.AddStop(lng=-105.508771, lat=50.395345, name = "Athabasca St. E @ 10th Ave. NE")
abe_1025 = schedule.AddStop(lng=-105.511806, lat=50.395353, name = "Athabasca St. E @ 9th Ave. NE")
abe_1026 = schedule.AddStop(lng=-105.515020, lat=50.395332, name = "Athabasca St. E @ 8th Ave. N")
abe_1027 = schedule.AddStop(lng=-105.517468, lat=50.395330, name = "Athabasca St. E @ 7th Ave. NE")
abe_1028 = schedule.AddStop(lng=-105.517468, lat=50.393499, name = "7th Ave. NE @ Ominica St. E")
abe_1029 = schedule.AddStop(lng=-105.517431, lat=50.392565, name = "7th Ave. NE @ Fairford St. E")
abe_1030 = schedule.AddStop(lng=-105.519853, lat=50.392563, name = "Fairford St. E @ 6th Ave. NE")
abe_1031 = schedule.AddStop(lng=-105.524809, lat=50.392491, name = "Fairford St. E @ 4th Ave. NE")
abe_1032 = schedule.AddStop(lng=-105.527268, lat=50.392518, name = "Fairford St. E @ 3rd Ave. NE")
abe_1033 = schedule.AddStop(lng=-105.529674, lat=50.391562, name = "High St. E @ 2nd Ave. NE")
abe_1034 = schedule.AddStop(lng=-105.532080, lat=50.391564, name = "High St. E @ 1st Ave. N")

## Sunningdale Stops
sun_2001 = schedule.AddStop(lng=-105.534554, lat=50.391816, name = "Main St. N @ High St. W")
sun_2002 = schedule.AddStop(lng=-105.534547, lat=50.395128, name = "Main St. N @ Athabasca St. E")
sun_2003 = schedule.AddStop(lng=-105.534606, lat=50.397097, name = "Main St. N @ Caribou St. E")
sun_2004 = schedule.AddStop(lng=-105.534628, lat=50.400801, name = "Main St. N @ Hall St. E")
sun_2005 = schedule.AddStop(lng=-105.532141, lat=50.404088, name = "Town & Country Dr. @ Civic Centre Dr.")
sun_2006 = schedule.AddStop(lng=-105.534698, lat=50.406387, name = "Town & Country Dr. @ Main St. N")
sun_2007 = schedule.AddStop(lng=-105.536385, lat=50.412762, name = "Thatcher Dr. W @ Main St. West Service Road")
sun_2008 = schedule.AddStop(lng=-105.538747, lat=50.413823, name = "Woodlilly Dr. @ Arrowhead Rd.")
sun_2009 = schedule.AddStop(lng=-105.538403, lat=50.415286, name = "Woodlilly Dr. @ Aster Cres.")
sun_2010 = schedule.AddStop(lng=-105.538396, lat=50.416217, name = "Woodlilly Dr. @ Buttercup Cres.")
sun_2011 = schedule.AddStop(lng=-105.538564, lat=50.418213, name = "Woodlilly Dr. @ Crocus Rd.")
sun_2012 = schedule.AddStop(lng=-105.539069, lat=50.419862, name = "Woodlilly Dr. @ Dahlia Cres. S")
sun_2013 = schedule.AddStop(lng=-105.541255, lat=50.422278, name = "Woodlilly Dr. @ Dahlia Cres. N")
sun_2014 = schedule.AddStop(lng=-105.541936, lat=50.422491, name = "Woodlilly Dr. @ Flax Rd.")
sun_2015 = schedule.AddStop(lng=-105.550880, lat=50.423054, name = "Woodlilly Dr. @ Calypso Dr.")
sun_2016 = schedule.AddStop(lng=-105.554598, lat=50.420152, name = "Woodlilly Dr. @ Iris Dr.")
sun_2017 = schedule.AddStop(lng=-105.554614, lat=50.417789, name = "Woodlilly Dr. @ Lewry Cres.")
sun_2018 = schedule.AddStop(lng=-105.554574, lat=50.413746, name = "Woodlilly Dr. @ Thorn Cres.")
sun_2019 = schedule.AddStop(lng=-105.565848, lat=50.413261, name = "Thatcher Dr. W @ 11th Ave. NW")
sun_2020 = schedule.AddStop(lng=-105.565889, lat=50.411244, name = "11th Ave. NW")
sun_2021 = schedule.AddStop(lng=-105.565857, lat=50.409446, name = "11th Ave. NW @ Normandy Dr.")
sun_2022 = schedule.AddStop(lng=-105.562648, lat=50.409395, name = "Normandy Dr. @ General Cres.")
sun_2023 = schedule.AddStop(lng=-105.561139, lat=50.409373, name = "Normandy Dr. @ Marshall Cres. E")
sun_2024 = schedule.AddStop(lng=-105.557632, lat=50.404846, name = "9th Ave. NW @ MacDonald St. W")
sun_2025 = schedule.AddStop(lng=-105.552479, lat=50.404839, name = "MacDonald St. W @ 7th Ave. NW")
sun_2026 = schedule.AddStop(lng=-105.549693, lat=50.404847, name = "MacDonald St. W @ 6th Ave. NW")
sun_2027 = schedule.AddStop(lng=-105.545519, lat=50.404871, name = "MacDonald St. W @ 4th Ave. NW")
sun_2028 = schedule.AddStop(lng=-105.542706, lat=50.404874, name = "MacDonald St. W @ 3rd Ave. NW")
sun_2029 = schedule.AddStop(lng=-105.538524, lat=50.404879, name = "MacDonald St. W @ Redland Ave. NW")
sun_2030 = schedule.AddStop(lng=-105.534626, lat=50.403219, name = "Main St. N @ Saskatchewan St. W")
sun_2031 = schedule.AddStop(lng=-105.534832, lat=50.400466, name = "Main St. N @ Hall St. W")
sun_2032 = schedule.AddStop(lng=-105.534842, lat=50.398715, name = "Main St. N @ Oxford St. W")
sun_2033 = schedule.AddStop(lng=-105.534848, lat=50.397655, name = "Main St. N @ Ross St. W")
sun_2034 = schedule.AddStop(lng=-105.534821, lat=50.395524, name = "Main St. N @ Athabasca St. W")
sun_2035 = schedule.AddStop(lng=-105.534837, lat=50.394191, name = "Main St. N @ Stadacona St. W")
sun_2036 = schedule.AddStop(lng=-105.534783, lat=50.391786, name = "Main St. N @ High St. W")

## Athabasca West Stops
abw_3001 = schedule.AddStop(lng=-105.534557, lat=50.391898, name = "Main St. N @ High St. W")
abw_3002 = schedule.AddStop(lng=-105.534583, lat=50.393453, name = "Main St. N @ Ominica St. E")
abw_3003 = schedule.AddStop(lng=-105.534585, lat=50.394379, name = "Main St. N @ Stadacona St. E")
abw_3004 = schedule.AddStop(lng=-105.534759, lat=50.395276, name = "Main St. N @ Athabasca St. E")
abw_3005 = schedule.AddStop(lng=-105.534775, lat=50.397846, name = "Main St. N @ Ross. St. E")
abw_3006 = schedule.AddStop(lng=-105.535097, lat=50.398949, name = "Oxford St. W @ Main St. N")
abw_3007 = schedule.AddStop(lng=-105.538723, lat=50.398908, name = "Oxford St. W @ Redland Ave. N")
abw_3008 = schedule.AddStop(lng=-105.544121, lat=50.398931, name = "Oxford St. W @ Henleaze Ave. N")
abw_3009 = schedule.AddStop(lng=-105.549653, lat=50.398924, name = "Oxford St. W @ 6th Ave. NW")
abw_3010 = schedule.AddStop(lng=-105.553907, lat=50.398914, name = "Oxford St. W @ Monk Ave. N")
abw_3011 = schedule.AddStop(lng=-105.557577, lat=50.398907, name = "Oxford St. W @ 9th Ave. NW")
abw_3012 = schedule.AddStop(lng=-105.561411, lat=50.398498, name = "Albert St. N @ 10th Ave. NW")
abw_3013 = schedule.AddStop(lng=-105.565239, lat=50.398485, name = "Albert St. N @ 11th Ave. NW")
abw_3014 = schedule.AddStop(lng=-105.565233, lat=50.400107, name = "11th Ave. NW @ Carleton St. W")
abw_3015 = schedule.AddStop(lng=-105.565290, lat=50.403271, name = "11th Ave. NW @ Grace St. W")
abw_3016 = schedule.AddStop(lng=-105.568479, lat=50.403016, name = "Grace St. W @ Gordon Rd. N")
abw_3017 = schedule.AddStop(lng=-105.573261, lat=50.401748, name = "Grace St. W @ 13th Ave. NW")
abw_3018 = schedule.AddStop(lng=-105.577126, lat=50.399929, name = "Grace St. W @ Prince Charles Pl.")
abw_3019 = schedule.AddStop(lng=-105.578960, lat=50.399818, name = "Grace St. W @ Holdsworth Cres.")
abw_3020 = schedule.AddStop(lng=-105.582893, lat=50.399815, name = "Grace St. W @ Corman Cres.")
abw_3021 = schedule.AddStop(lng=-105.584158, lat=50.402874, name = "Thatcher Dr. W @ Rutherford St. W")
abw_3022 = schedule.AddStop(lng=-105.582415, lat=50.406247, name = "Thatcher Dr. W @ 13th Ave. NW")
abw_3023 = schedule.AddStop(lng=-105.581528, lat=50.405857, name = "13th Ave. NW @ Pascoe Dr. W")
abw_3024 = schedule.AddStop(lng=-105.579708, lat=50.404858, name = "13th Ave. NW @ Mayberry Cres.")
abw_3025 = schedule.AddStop(lng=-105.577642, lat=50.403978, name = "13th Ave. NW @ Regal Cres.")
abw_3026 = schedule.AddStop(lng=-105.574382, lat=50.402371, name = "13th Ave. NW @ Gordon Rd. N")
abw_3027 = schedule.AddStop(lng=-105.571680, lat=50.400022, name = "13th Ave. NW @ Carleton St. W")
abw_3028 = schedule.AddStop(lng=-105.571753, lat=50.397651, name = "13th Ave. NW @ Montgomery St. W")
abw_3029 = schedule.AddStop(lng=-105.574652, lat=50.396813, name = "Caribou St. W @ 14th Ave. NW")
abw_3030 = schedule.AddStop(lng=-105.574611, lat=50.395229, name = "Athabasca St. W @ 14th Ave. NW")
abw_3031 = schedule.AddStop(lng=-105.571741, lat=50.395244, name = "Athabasca St. W @ 13th Ave. NW")
abw_3032 = schedule.AddStop(lng=-105.568876, lat=50.395249, name = "Athabasca St. W @ 12th Ave. NW")
abw_3033 = schedule.AddStop(lng=-105.565239, lat=50.395252, name = "Athabasca St. W @ 11th Ave. NW")
abw_3034 = schedule.AddStop(lng=-105.561386, lat=50.395247, name = "Athabasca St. W @ 10th Ave. NW")
abw_3035 = schedule.AddStop(lng=-105.557595, lat=50.395267, name = "Athabasca St. W @ 9th Ave. NW")
abw_3036 = schedule.AddStop(lng=-105.554396, lat=50.395343, name = "Athabasca St. W @ 8th Ave. NW")
abw_3037 = schedule.AddStop(lng=-105.549513, lat=50.395326, name = "Athabasca St. W @ 6th Ave. NW")
abw_3038 = schedule.AddStop(lng=-105.544721, lat=50.395335, name = "Athabasca St. W @ 4th Ave. NW")
abw_3039 = schedule.AddStop(lng=-105.539796, lat=50.395328, name = "Athabasca St. W @ 2nd Ave. NW")
abw_3040 = schedule.AddStop(lng=-105.534759, lat=50.395276, name = "Athabasca St. W @ Main St. N")
abw_3041 = schedule.AddStop(lng=-105.534585, lat=50.394379, name = "Main St. N @ Stadacona St. W")
abw_3042 = schedule.AddStop(lng=-105.534583, lat=50.393453, name = "Main St. N @ Ominica St. W")

## Westmount Stops
wes_4001 = schedule.AddStop(lng=-105.534838, lat=50.391840, name = "Main St. N @ High St. W")
wes_4002 = schedule.AddStop(lng=-105.534796, lat=50.389692, name = "Main St. N @ Manitoba St. E")
wes_4003 = schedule.AddStop(lng=-105.531977, lat=50.389588, name = "Manitoba St. E @ 1st Ave. NE")
wes_4004 = schedule.AddStop(lng=-105.534579, lat=50.385164, name = "Main St. S @ Home St. W")
wes_4005 = schedule.AddStop(lng=-105.534661, lat=50.384244, name = "Lillooet St. W @ Main St. S")
wes_4006 = schedule.AddStop(lng=-105.539767, lat=50.384217, name = "Lillooet St. W @ 2nd Ave. SW")
wes_4007 = schedule.AddStop(lng=-105.542239, lat=50.384208, name = "Lillooet St. W @ 3rd Ave. SW")
wes_4008 = schedule.AddStop(lng=-105.544732, lat=50.383928, name = "4th Ave. SW @ Lillooet St. W")
wes_4009 = schedule.AddStop(lng=-105.545133, lat=50.382475, name = "Coteau St. W @ 4th Ave. SW")
wes_4010 = schedule.AddStop(lng=-105.549483, lat=50.382410, name = "Coteau St. W @ 6th Ave. SW")
wes_4011 = schedule.AddStop(lng=-105.551911, lat=50.382406, name = "Coteau St. W @ 7th Ave. SW")
wes_4012 = schedule.AddStop(lng=-105.557565, lat=50.382390, name = "Coteau St. W @ 9th Ave. SW")
wes_4013 = schedule.AddStop(lng=-105.561365, lat=50.382375, name = "Coteau St. W @ 10th Ave. SW")
wes_4014 = schedule.AddStop(lng=-105.565221, lat=50.382406, name = "Coteau St. W @ 11th Ave. SW")
wes_4015 = schedule.AddStop(lng=-105.568985, lat=50.382233, name = "Coteau St. W @ 12th Ave. SW")
wes_4016 = schedule.AddStop(lng=-105.572540, lat=50.382258, name = "Coteau St. W @ Iroquois Dr.")
wes_4017 = schedule.AddStop(lng=-105.573745, lat=50.382241, name = "Coteau St. W @ Manitou Cres.")
wes_4018 = schedule.AddStop(lng=-105.576257, lat=50.382249, name = "Coteau St. W @ Souix Cres.")
wes_4019 = schedule.AddStop(lng=-105.578646, lat=50.382265, name = "Coteau St. W @ Cree Cres.")
wes_4020 = schedule.AddStop(lng=-105.580592, lat=50.380492, name = "16th Ave. SW @ Grandview Pl.")
wes_4021 = schedule.AddStop(lng=-105.580552, lat=50.378086, name = "16th Ave. SW @ Hastings St. W")
wes_4022 = schedule.AddStop(lng=-105.580547, lat=50.377234, name = "Warner St. W @ 16th Ave. SW")
wes_4023 = schedule.AddStop(lng=-105.577552, lat=50.377240, name = "Warner St. W @ 15th Ave. SW")
wes_4024 = schedule.AddStop(lng=-105.574645, lat=50.377239, name = "Warner St. W @ 14th Ave. SW")
wes_4025 = schedule.AddStop(lng=-105.571804, lat=50.377236, name = "Warner St. W @ 13th Ave. SW")
wes_4026 = schedule.AddStop(lng=-105.568900, lat=50.377231, name = "Warner St. W @ 12th Ave. SW")
wes_4027 = schedule.AddStop(lng=-105.568807, lat=50.379043, name = "Vaughan St. W @ 12th Ave. SW")
wes_4028 = schedule.AddStop(lng=-105.565020, lat=50.379014, name = "Vaughan St. W @ 11th Ave. SW")
wes_4029 = schedule.AddStop(lng=-105.561514, lat=50.379021, name = "Vaughan St. W @ 10th Ave. SW")
wes_4030 = schedule.AddStop(lng=-105.560026, lat=50.376368, name = "Bradley St.")
wes_4031 = schedule.AddStop(lng=-105.557551, lat=50.378756, name = "9th Ave SW @ Keith St. W")
wes_4032 = schedule.AddStop(lng=-105.557554, lat=50.379603, name = "Vaughan St. W @ 9th Ave. SW")
wes_4033 = schedule.AddStop(lng=-105.554339, lat=50.379635, name = "Vaughan St. W @ 8th Ave. SW")
wes_4034 = schedule.AddStop(lng=-105.551891, lat=50.379588, name = "Vaughan St. W @ 7th Ave. SW")
wes_4035 = schedule.AddStop(lng=-105.551908, lat=50.381473, name = "7th Ave. SW @ Duffield St. W")
wes_4036 = schedule.AddStop(lng=-105.549454, lat=50.381451, name = "Duffield St. W @ 6th Ave. SW")
wes_4037 = schedule.AddStop(lng=-105.547078, lat=50.381470, name = "Duffield St. W @ 5th Ave. SW")
wes_4038 = schedule.AddStop(lng=-105.544654, lat=50.381472, name = "Duffield St. W @ 4th Ave. SW")
wes_4039 = schedule.AddStop(lng=-105.544352, lat=50.382358, name = "4th Ave. SW @ Coteau St. W")
wes_4040 = schedule.AddStop(lng=-105.541103, lat=50.382374, name = "Coteau St. W @ Tapley Ave.")
wes_4041 = schedule.AddStop(lng=-105.538289, lat=50.382384, name = "Coteau St. W @ Scott St.")
wes_4042 = schedule.AddStop(lng=-105.534662, lat=50.382365, name = "Coteau St. W @ Main St. S")
wes_4043 = schedule.AddStop(lng=-105.532026, lat=50.382365, name = "Coteau St. W @ 1st Ave. SE")
wes_4044 = schedule.AddStop(lng=-105.529560, lat=50.382381, name = "2nd Ave. SE @ Coteau St. E")
wes_4045 = schedule.AddStop(lng=-105.531974, lat=50.384236, name = "Lillooet St. E @ 1st Ave. SE")
wes_4046 = schedule.AddStop(lng=-105.531973, lat=50.385158, name = "1st Ave. SE @ Home St. E")
wes_4047 = schedule.AddStop(lng=-105.529648, lat=50.389584, name = "2nd Ave. NE @ Manitoba St. E")
wes_4048 = schedule.AddStop(lng=-105.529674, lat=50.391562, name = "High St. E @ 2nd Ave. NE")
wes_4049 = schedule.AddStop(lng=-105.531760, lat=50.391626, name = "High St. E @ 1st Ave. NE")

# Trips
##ABE Trip 1- 7:15:00 - Depart
trip = ABE.AddTrip(schedule, headsign="To Downtown via Athabasca East")
trip.AddStopTime(abe_1001, stop_time='7:15:00')#timepoint
trip.AddStopTime(abe_1002, stop_time='7:17:00')
trip.AddStopTime(abe_1003, stop_time='7:17:30')
trip.AddStopTime(abe_1004, stop_time='7:18:00')
trip.AddStopTime(abe_1005, stop_time='7:18:30')
trip.AddStopTime(abe_1006, stop_time='7:19:00')
trip.AddStopTime(abe_1007, stop_time='7:20:00')#timepoint
trip.AddStopTime(abe_1008, stop_time='7:21:00')
trip.AddStopTime(abe_1009, stop_time='7:22:00')
trip.AddStopTime(abe_1010, stop_time='7:23:00')#timepoint
trip.AddStopTime(abe_1011, stop_time='7:24:00')
trip.AddStopTime(abe_1012, stop_time='7:25:00')
trip.AddStopTime(abe_1013, stop_time='7:27:00')
trip.AddStopTime(abe_1014, stop_time='7:29:00')#timepoint
trip.AddStopTime(abe_1015, stop_time='7:35:00')#timepoint
trip.AddStopTime(abe_1016, stop_time='7:40:00')#timepoint
trip.AddStopTime(abe_1017, stop_time='7:41:00')
trip.AddStopTime(abe_1018, stop_time='7:42:00')
trip.AddStopTime(abe_1019, stop_time='7:42:30')
trip.AddStopTime(abe_1020, stop_time='7:43:00')#timepoint
trip.AddStopTime(abe_1021, stop_time='7:43:30')
trip.AddStopTime(abe_1022, stop_time='7:44:00')
trip.AddStopTime(abe_1023, stop_time='7:44:30')
trip.AddStopTime(abe_1024, stop_time='7:45:00')
trip.AddStopTime(abe_1025, stop_time='7:45:30')
trip.AddStopTime(abe_1026, stop_time='7:46:00')#timepoint
trip.AddStopTime(abe_1027, stop_time='7:46:30')
trip.AddStopTime(abe_1028, stop_time='7:47:00')
trip.AddStopTime(abe_1029, stop_time='7:47:30')
trip.AddStopTime(abe_1030, stop_time='7:48:00')
trip.AddStopTime(abe_1031, stop_time='7:48:30')
trip.AddStopTime(abe_1032, stop_time='7:49:00')#timepoint
trip.AddStopTime(abe_1033, stop_time='7:49:30')
trip.AddStopTime(abe_1034, stop_time='7:50:00')
##ABE Trip 2 - 7:55:00 - Depart
trip = ABE.AddTrip(schedule, headsign="To Downtown via Athabasca East")
trip.AddStopTime(abe_1001, stop_time='7:55:00')#timepoint
trip.AddStopTime(abe_1002, stop_time='7:55:30')
trip.AddStopTime(abe_1003, stop_time='7:56:00')
trip.AddStopTime(abe_1004, stop_time='7:57:00')
trip.AddStopTime(abe_1005, stop_time='7:58:00')
trip.AddStopTime(abe_1006, stop_time='7:59:00')
trip.AddStopTime(abe_1007, stop_time='8:00:00')#timepoint
trip.AddStopTime(abe_1008, stop_time='8:01:00')
trip.AddStopTime(abe_1009, stop_time='8:02:00')
trip.AddStopTime(abe_1010, stop_time='8:03:00')#timepoint
trip.AddStopTime(abe_1011, stop_time='8:05:00')
trip.AddStopTime(abe_1012, stop_time='8:07:00')
trip.AddStopTime(abe_1013, stop_time='8:08:00')
trip.AddStopTime(abe_1014, stop_time='8:09:00')#timepoint
trip.AddStopTime(abe_1015, stop_time='8:15:00')#timepoint
trip.AddStopTime(abe_1016, stop_time='8:20:00')#timepoint
trip.AddStopTime(abe_1017, stop_time='8:20:30')
trip.AddStopTime(abe_1018, stop_time='8:21:00')
trip.AddStopTime(abe_1019, stop_time='8:22:00')
trip.AddStopTime(abe_1020, stop_time='8:23:00')#timepoint
trip.AddStopTime(abe_1021, stop_time='8:23:30')
trip.AddStopTime(abe_1022, stop_time='8:24:00')
trip.AddStopTime(abe_1023, stop_time='8:24:30')
trip.AddStopTime(abe_1024, stop_time='8:25:00')
trip.AddStopTime(abe_1025, stop_time='8:25:30')
trip.AddStopTime(abe_1026, stop_time='8:26:00')#timepoint
trip.AddStopTime(abe_1027, stop_time='8:26:30')
trip.AddStopTime(abe_1028, stop_time='8:27:00')
trip.AddStopTime(abe_1029, stop_time='8:28:00')
trip.AddStopTime(abe_1030, stop_time='8:29:00')
trip.AddStopTime(abe_1031, stop_time='8:30:00')
trip.AddStopTime(abe_1032, stop_time='8:31:00')#timepoint
trip.AddStopTime(abe_1033, stop_time='8:32:00')
trip.AddStopTime(abe_1034, stop_time='8:33:00')
##ABE Trip 3 - 8:35:00 - Depart
trip = ABE.AddTrip(schedule, headsign="To Downtown via Athabasca East")
trip.AddStopTime(abe_1001, stop_time='8:35:00')#timepoint
trip.AddStopTime(abe_1002, stop_time='8:35:30')
trip.AddStopTime(abe_1003, stop_time='8:36:00')
trip.AddStopTime(abe_1004, stop_time='8:37:00')
trip.AddStopTime(abe_1005, stop_time='8:38:00')
trip.AddStopTime(abe_1006, stop_time='8:39:00')
trip.AddStopTime(abe_1007, stop_time='8:40:00')#timepoint
trip.AddStopTime(abe_1008, stop_time='8:41:00')
trip.AddStopTime(abe_1009, stop_time='8:42:00')
trip.AddStopTime(abe_1010, stop_time='8:43:00')#timepoint
trip.AddStopTime(abe_1011, stop_time='8:44:00')
trip.AddStopTime(abe_1012, stop_time='8:46:00')
trip.AddStopTime(abe_1013, stop_time='8:47:30')
trip.AddStopTime(abe_1014, stop_time='8:49:00')#timepoint
trip.AddStopTime(abe_1015, stop_time='8:55:00')#timepoint
trip.AddStopTime(abe_1016, stop_time='9:00:00')#timepoint
trip.AddStopTime(abe_1017, stop_time='9:00:30')
trip.AddStopTime(abe_1018, stop_time='9:01:00')
trip.AddStopTime(abe_1019, stop_time='9:02:00')
trip.AddStopTime(abe_1020, stop_time='9:03:00')#timepoint
trip.AddStopTime(abe_1021, stop_time='9:03:30')
trip.AddStopTime(abe_1022, stop_time='9:04:00')
trip.AddStopTime(abe_1023, stop_time='9:04:30')
trip.AddStopTime(abe_1024, stop_time='9:05:00')
trip.AddStopTime(abe_1025, stop_time='9:05:30')
trip.AddStopTime(abe_1026, stop_time='9:06:00')#timepoint
trip.AddStopTime(abe_1027, stop_time='9:08:00')
trip.AddStopTime(abe_1028, stop_time='9:09:00')
trip.AddStopTime(abe_1029, stop_time='9:09:30')
trip.AddStopTime(abe_1030, stop_time='9:10:00')
trip.AddStopTime(abe_1031, stop_time='9:10:30')
trip.AddStopTime(abe_1032, stop_time='9:11:00')#timepoint
trip.AddStopTime(abe_1033, stop_time='9:12:00')
trip.AddStopTime(abe_1034, stop_time='9:13:00')
##ABE Trip 4 - 9:15:00 - Depart
trip = ABE.AddTrip(schedule, headsign="To Downtown via Athabasca East")
trip.AddStopTime(abe_1001, stop_time='9:15:00')#timepoint
trip.AddStopTime(abe_1002, stop_time='9:17:00')
trip.AddStopTime(abe_1003, stop_time='9:17:30')
trip.AddStopTime(abe_1004, stop_time='9:18:00')
trip.AddStopTime(abe_1005, stop_time='9:18:30')
trip.AddStopTime(abe_1006, stop_time='9:19:00')
trip.AddStopTime(abe_1007, stop_time='9:20:00')#timepoint
trip.AddStopTime(abe_1008, stop_time='9:21:00')
trip.AddStopTime(abe_1009, stop_time='9:22:00')
trip.AddStopTime(abe_1010, stop_time='9:23:00')#timepoint
trip.AddStopTime(abe_1011, stop_time='9:24:00')
trip.AddStopTime(abe_1012, stop_time='9:25:00')
trip.AddStopTime(abe_1013, stop_time='9:27:00')
trip.AddStopTime(abe_1014, stop_time='9:29:00')#timepoint
trip.AddStopTime(abe_1015, stop_time='9:35:00')#timepoint
trip.AddStopTime(abe_1016, stop_time='9:40:00')#timepoint
trip.AddStopTime(abe_1017, stop_time='9:41:00')
trip.AddStopTime(abe_1018, stop_time='9:42:00')
trip.AddStopTime(abe_1019, stop_time='9:42:30')
trip.AddStopTime(abe_1020, stop_time='9:43:00')#timepoint
trip.AddStopTime(abe_1021, stop_time='9:43:30')
trip.AddStopTime(abe_1022, stop_time='9:44:00')
trip.AddStopTime(abe_1023, stop_time='9:44:30')
trip.AddStopTime(abe_1024, stop_time='9:45:00')
trip.AddStopTime(abe_1025, stop_time='9:45:30')
trip.AddStopTime(abe_1026, stop_time='9:46:00')#timepoint
trip.AddStopTime(abe_1027, stop_time='9:46:30')
trip.AddStopTime(abe_1028, stop_time='9:47:00')
trip.AddStopTime(abe_1029, stop_time='9:47:30')
trip.AddStopTime(abe_1030, stop_time='9:48:00')
trip.AddStopTime(abe_1031, stop_time='9:48:30')
trip.AddStopTime(abe_1032, stop_time='9:49:00')#timepoint
trip.AddStopTime(abe_1033, stop_time='9:49:30')
trip.AddStopTime(abe_1034, stop_time='9:50:00')
##ABE Trip 5 - 9:55:00 - Depart
trip = ABE.AddTrip(schedule, headsign="To Downtown via Athabasca East")
trip.AddStopTime(abe_1001, stop_time='9:55:00')#timepoint
trip.AddStopTime(abe_1002, stop_time='9:55:30')
trip.AddStopTime(abe_1003, stop_time='9:56:00')
trip.AddStopTime(abe_1004, stop_time='9:57:00')
trip.AddStopTime(abe_1005, stop_time='9:58:00')
trip.AddStopTime(abe_1006, stop_time='9:59:00')
trip.AddStopTime(abe_1007, stop_time='10:00:00')#timepoint
trip.AddStopTime(abe_1008, stop_time='10:01:00')
trip.AddStopTime(abe_1009, stop_time='10:02:00')
trip.AddStopTime(abe_1010, stop_time='10:03:00')#timepoint
trip.AddStopTime(abe_1011, stop_time='10:05:00')
trip.AddStopTime(abe_1012, stop_time='10:07:00')
trip.AddStopTime(abe_1013, stop_time='10:08:00')
trip.AddStopTime(abe_1014, stop_time='10:09:00')#timepoint
trip.AddStopTime(abe_1015, stop_time='10:15:00')#timepoint
trip.AddStopTime(abe_1016, stop_time='10:20:00')#timepoint
trip.AddStopTime(abe_1017, stop_time='10:20:30')
trip.AddStopTime(abe_1018, stop_time='10:21:00')
trip.AddStopTime(abe_1019, stop_time='10:22:00')
trip.AddStopTime(abe_1020, stop_time='10:23:00')#timepoint
trip.AddStopTime(abe_1021, stop_time='10:23:30')
trip.AddStopTime(abe_1022, stop_time='10:24:00')
trip.AddStopTime(abe_1023, stop_time='10:24:30')
trip.AddStopTime(abe_1024, stop_time='10:25:00')
trip.AddStopTime(abe_1025, stop_time='10:25:30')
trip.AddStopTime(abe_1026, stop_time='10:26:00')#timepoint
trip.AddStopTime(abe_1027, stop_time='10:26:30')
trip.AddStopTime(abe_1028, stop_time='10:27:00')
trip.AddStopTime(abe_1029, stop_time='10:28:00')
trip.AddStopTime(abe_1030, stop_time='10:29:00')
trip.AddStopTime(abe_1031, stop_time='10:30:00')
trip.AddStopTime(abe_1032, stop_time='10:31:00')#timepoint
trip.AddStopTime(abe_1033, stop_time='10:32:00')
trip.AddStopTime(abe_1034, stop_time='10:33:00')
##ABE Trip 6 - 10:35:00 - Depart
trip = ABE.AddTrip(schedule, headsign="To Downtown via Athabasca East")
trip.AddStopTime(abe_1001, stop_time='10:35:00')#timepoint
trip.AddStopTime(abe_1002, stop_time='10:35:30')
trip.AddStopTime(abe_1003, stop_time='10:36:00')
trip.AddStopTime(abe_1004, stop_time='10:37:00')
trip.AddStopTime(abe_1005, stop_time='10:38:00')
trip.AddStopTime(abe_1006, stop_time='10:39:00')
trip.AddStopTime(abe_1007, stop_time='10:40:00')#timepoint
trip.AddStopTime(abe_1008, stop_time='10:41:00')
trip.AddStopTime(abe_1009, stop_time='10:42:00')
trip.AddStopTime(abe_1010, stop_time='10:43:00')#timepoint
trip.AddStopTime(abe_1011, stop_time='10:44:00')
trip.AddStopTime(abe_1012, stop_time='10:46:00')
trip.AddStopTime(abe_1013, stop_time='10:47:30')
trip.AddStopTime(abe_1014, stop_time='10:49:00')#timepoint
trip.AddStopTime(abe_1015, stop_time='10:55:00')#timepoint
trip.AddStopTime(abe_1016, stop_time='11:00:00')#timepoint
trip.AddStopTime(abe_1017, stop_time='11:00:30')
trip.AddStopTime(abe_1018, stop_time='11:01:00')
trip.AddStopTime(abe_1019, stop_time='11:02:00')
trip.AddStopTime(abe_1020, stop_time='11:03:00')#timepoint
trip.AddStopTime(abe_1021, stop_time='11:03:30')
trip.AddStopTime(abe_1022, stop_time='11:04:00')
trip.AddStopTime(abe_1023, stop_time='11:04:30')
trip.AddStopTime(abe_1024, stop_time='11:05:00')
trip.AddStopTime(abe_1025, stop_time='11:05:30')
trip.AddStopTime(abe_1026, stop_time='11:06:00')#timepoint
trip.AddStopTime(abe_1027, stop_time='11:08:00')
trip.AddStopTime(abe_1028, stop_time='11:09:00')
trip.AddStopTime(abe_1029, stop_time='11:09:30')
trip.AddStopTime(abe_1030, stop_time='11:10:00')
trip.AddStopTime(abe_1031, stop_time='11:10:30')
trip.AddStopTime(abe_1032, stop_time='11:11:00')#timepoint
trip.AddStopTime(abe_1033, stop_time='11:12:00')
trip.AddStopTime(abe_1034, stop_time='11:13:00')
##ABE Trip 7 - 11:15:00 - Depart
trip = ABE.AddTrip(schedule, headsign="To Downtown via Athabasca East")
trip.AddStopTime(abe_1001, stop_time='11:15:00')#timepoint
trip.AddStopTime(abe_1002, stop_time='11:17:00')
trip.AddStopTime(abe_1003, stop_time='11:17:30')
trip.AddStopTime(abe_1004, stop_time='11:18:00')
trip.AddStopTime(abe_1005, stop_time='11:18:30')
trip.AddStopTime(abe_1006, stop_time='11:19:00')
trip.AddStopTime(abe_1007, stop_time='11:20:00')#timepoint
trip.AddStopTime(abe_1008, stop_time='11:21:00')
trip.AddStopTime(abe_1009, stop_time='11:22:00')
trip.AddStopTime(abe_1010, stop_time='11:23:00')#timepoint
trip.AddStopTime(abe_1011, stop_time='11:24:00')
trip.AddStopTime(abe_1012, stop_time='11:25:00')
trip.AddStopTime(abe_1013, stop_time='11:27:00')
trip.AddStopTime(abe_1014, stop_time='11:29:00')#timepoint
trip.AddStopTime(abe_1015, stop_time='11:35:00')#timepoint
trip.AddStopTime(abe_1016, stop_time='11:40:00')#timepoint
trip.AddStopTime(abe_1017, stop_time='11:41:00')
trip.AddStopTime(abe_1018, stop_time='11:42:00')
trip.AddStopTime(abe_1019, stop_time='11:42:30')
trip.AddStopTime(abe_1020, stop_time='11:43:00')#timepoint
trip.AddStopTime(abe_1021, stop_time='11:43:30')
trip.AddStopTime(abe_1022, stop_time='11:44:00')
trip.AddStopTime(abe_1023, stop_time='11:44:30')
trip.AddStopTime(abe_1024, stop_time='11:45:00')
trip.AddStopTime(abe_1025, stop_time='11:45:30')
trip.AddStopTime(abe_1026, stop_time='11:46:00')#timepoint
trip.AddStopTime(abe_1027, stop_time='11:46:30')
trip.AddStopTime(abe_1028, stop_time='11:47:00')
trip.AddStopTime(abe_1029, stop_time='11:47:30')
trip.AddStopTime(abe_1030, stop_time='11:48:00')
trip.AddStopTime(abe_1031, stop_time='11:48:30')
trip.AddStopTime(abe_1032, stop_time='11:49:00')#timepoint
trip.AddStopTime(abe_1033, stop_time='11:49:30')
trip.AddStopTime(abe_1034, stop_time='11:50:00')
##ABE Trip 8 - 11:55:00 - Depart
trip = ABE.AddTrip(schedule, headsign="To Downtown via Athabasca East")
trip.AddStopTime(abe_1001, stop_time='11:55:00')#timepoint
trip.AddStopTime(abe_1002, stop_time='11:55:30')
trip.AddStopTime(abe_1003, stop_time='11:56:00')
trip.AddStopTime(abe_1004, stop_time='11:57:00')
trip.AddStopTime(abe_1005, stop_time='11:58:00')
trip.AddStopTime(abe_1006, stop_time='11:59:00')
trip.AddStopTime(abe_1007, stop_time='12:00:00')#timepoint
trip.AddStopTime(abe_1008, stop_time='12:01:00')
trip.AddStopTime(abe_1009, stop_time='12:02:00')
trip.AddStopTime(abe_1010, stop_time='12:03:00')#timepoint
trip.AddStopTime(abe_1011, stop_time='12:05:00')
trip.AddStopTime(abe_1012, stop_time='12:07:00')
trip.AddStopTime(abe_1013, stop_time='12:08:00')
trip.AddStopTime(abe_1014, stop_time='12:09:00')#timepoint
trip.AddStopTime(abe_1015, stop_time='12:15:00')#timepoint
trip.AddStopTime(abe_1016, stop_time='12:20:00')#timepoint
trip.AddStopTime(abe_1017, stop_time='12:20:30')
trip.AddStopTime(abe_1018, stop_time='12:21:00')
trip.AddStopTime(abe_1019, stop_time='12:22:00')
trip.AddStopTime(abe_1020, stop_time='12:23:00')#timepoint
trip.AddStopTime(abe_1021, stop_time='12:23:30')
trip.AddStopTime(abe_1022, stop_time='12:24:00')
trip.AddStopTime(abe_1023, stop_time='12:24:30')
trip.AddStopTime(abe_1024, stop_time='12:25:00')
trip.AddStopTime(abe_1025, stop_time='12:25:30')
trip.AddStopTime(abe_1026, stop_time='12:26:00')#timepoint
trip.AddStopTime(abe_1027, stop_time='12:26:30')
trip.AddStopTime(abe_1028, stop_time='12:27:00')
trip.AddStopTime(abe_1029, stop_time='12:28:00')
trip.AddStopTime(abe_1030, stop_time='12:29:00')
trip.AddStopTime(abe_1031, stop_time='12:30:00')
trip.AddStopTime(abe_1032, stop_time='12:31:00')#timepoint
trip.AddStopTime(abe_1033, stop_time='12:32:00')
trip.AddStopTime(abe_1034, stop_time='12:33:00')
##ABE Trip 9 - 12:35:00 - Depart
trip = ABE.AddTrip(schedule, headsign="To Downtown via Athabasca East")
trip.AddStopTime(abe_1001, stop_time='12:35:00')#timepoint
trip.AddStopTime(abe_1002, stop_time='12:35:30')
trip.AddStopTime(abe_1003, stop_time='12:36:00')
trip.AddStopTime(abe_1004, stop_time='12:37:00')
trip.AddStopTime(abe_1005, stop_time='12:38:00')
trip.AddStopTime(abe_1006, stop_time='12:39:00')
trip.AddStopTime(abe_1007, stop_time='12:40:00')#timepoint
trip.AddStopTime(abe_1008, stop_time='12:41:00')
trip.AddStopTime(abe_1009, stop_time='12:42:00')
trip.AddStopTime(abe_1010, stop_time='12:43:00')#timepoint
trip.AddStopTime(abe_1011, stop_time='12:44:00')
trip.AddStopTime(abe_1012, stop_time='12:46:00')
trip.AddStopTime(abe_1013, stop_time='12:47:30')
trip.AddStopTime(abe_1014, stop_time='12:49:00')#timepoint
trip.AddStopTime(abe_1015, stop_time='12:55:00')#timepoint
trip.AddStopTime(abe_1016, stop_time='13:00:00')#timepoint
trip.AddStopTime(abe_1017, stop_time='13:00:30')
trip.AddStopTime(abe_1018, stop_time='13:01:00')
trip.AddStopTime(abe_1019, stop_time='13:02:00')
trip.AddStopTime(abe_1020, stop_time='13:03:00')#timepoint
trip.AddStopTime(abe_1021, stop_time='13:03:30')
trip.AddStopTime(abe_1022, stop_time='13:04:00')
trip.AddStopTime(abe_1023, stop_time='13:04:30')
trip.AddStopTime(abe_1024, stop_time='13:05:00')
trip.AddStopTime(abe_1025, stop_time='13:05:30')
trip.AddStopTime(abe_1026, stop_time='13:06:00')#timepoint
trip.AddStopTime(abe_1027, stop_time='13:08:00')
trip.AddStopTime(abe_1028, stop_time='13:09:00')
trip.AddStopTime(abe_1029, stop_time='13:09:30')
trip.AddStopTime(abe_1030, stop_time='13:10:00')
trip.AddStopTime(abe_1031, stop_time='13:10:30')
trip.AddStopTime(abe_1032, stop_time='13:11:00')#timepoint
trip.AddStopTime(abe_1033, stop_time='13:12:00')
trip.AddStopTime(abe_1034, stop_time='13:13:00')
##ABE Trip 10 - 13:15:00 - Depart
trip = ABE.AddTrip(schedule, headsign="To Downtown via Athabasca East")
trip.AddStopTime(abe_1001, stop_time='13:15:00')#timepoint
trip.AddStopTime(abe_1002, stop_time='13:17:00')
trip.AddStopTime(abe_1003, stop_time='13:17:30')
trip.AddStopTime(abe_1004, stop_time='13:18:00')
trip.AddStopTime(abe_1005, stop_time='13:18:30')
trip.AddStopTime(abe_1006, stop_time='13:19:00')
trip.AddStopTime(abe_1007, stop_time='13:20:00')#timepoint
trip.AddStopTime(abe_1008, stop_time='13:21:00')
trip.AddStopTime(abe_1009, stop_time='13:22:00')
trip.AddStopTime(abe_1010, stop_time='13:23:00')#timepoint
trip.AddStopTime(abe_1011, stop_time='13:24:00')
trip.AddStopTime(abe_1012, stop_time='13:25:00')
trip.AddStopTime(abe_1013, stop_time='13:27:00')
trip.AddStopTime(abe_1014, stop_time='13:29:00')#timepoint
trip.AddStopTime(abe_1015, stop_time='13:35:00')#timepoint
trip.AddStopTime(abe_1016, stop_time='13:40:00')#timepoint
trip.AddStopTime(abe_1017, stop_time='13:41:00')
trip.AddStopTime(abe_1018, stop_time='13:42:00')
trip.AddStopTime(abe_1019, stop_time='13:42:30')
trip.AddStopTime(abe_1020, stop_time='13:43:00')#timepoint
trip.AddStopTime(abe_1021, stop_time='13:43:30')
trip.AddStopTime(abe_1022, stop_time='13:44:00')
trip.AddStopTime(abe_1023, stop_time='13:44:30')
trip.AddStopTime(abe_1024, stop_time='13:45:00')
trip.AddStopTime(abe_1025, stop_time='13:45:30')
trip.AddStopTime(abe_1026, stop_time='13:46:00')#timepoint
trip.AddStopTime(abe_1027, stop_time='13:46:30')
trip.AddStopTime(abe_1028, stop_time='13:47:00')
trip.AddStopTime(abe_1029, stop_time='13:47:30')
trip.AddStopTime(abe_1030, stop_time='13:48:00')
trip.AddStopTime(abe_1031, stop_time='13:48:30')
trip.AddStopTime(abe_1032, stop_time='13:49:00')#timepoint
trip.AddStopTime(abe_1033, stop_time='13:49:30')
trip.AddStopTime(abe_1034, stop_time='13:50:00')
##ABE Trip 11 - 13:55:00 - Depart
trip = ABE.AddTrip(schedule, headsign="To Downtown via Athabasca East")
trip.AddStopTime(abe_1001, stop_time='13:55:00')#timepoint
trip.AddStopTime(abe_1002, stop_time='13:55:30')
trip.AddStopTime(abe_1003, stop_time='13:56:00')
trip.AddStopTime(abe_1004, stop_time='13:57:00')
trip.AddStopTime(abe_1005, stop_time='13:58:00')
trip.AddStopTime(abe_1006, stop_time='13:59:00')
trip.AddStopTime(abe_1007, stop_time='14:00:00')#timepoint
trip.AddStopTime(abe_1008, stop_time='14:01:00')
trip.AddStopTime(abe_1009, stop_time='14:02:00')
trip.AddStopTime(abe_1010, stop_time='14:03:00')#timepoint
trip.AddStopTime(abe_1011, stop_time='14:05:00')
trip.AddStopTime(abe_1012, stop_time='14:07:00')
trip.AddStopTime(abe_1013, stop_time='14:08:00')
trip.AddStopTime(abe_1014, stop_time='14:09:00')#timepoint
trip.AddStopTime(abe_1015, stop_time='14:15:00')#timepoint
trip.AddStopTime(abe_1016, stop_time='14:20:00')#timepoint
trip.AddStopTime(abe_1017, stop_time='14:20:30')
trip.AddStopTime(abe_1018, stop_time='14:21:00')
trip.AddStopTime(abe_1019, stop_time='14:22:00')
trip.AddStopTime(abe_1020, stop_time='14:23:00')#timepoint
trip.AddStopTime(abe_1021, stop_time='14:23:30')
trip.AddStopTime(abe_1022, stop_time='14:24:00')
trip.AddStopTime(abe_1023, stop_time='14:24:30')
trip.AddStopTime(abe_1024, stop_time='14:25:00')
trip.AddStopTime(abe_1025, stop_time='14:25:30')
trip.AddStopTime(abe_1026, stop_time='14:26:00')#timepoint
trip.AddStopTime(abe_1027, stop_time='14:26:30')
trip.AddStopTime(abe_1028, stop_time='14:27:00')
trip.AddStopTime(abe_1029, stop_time='14:28:00')
trip.AddStopTime(abe_1030, stop_time='14:29:00')
trip.AddStopTime(abe_1031, stop_time='14:30:00')
trip.AddStopTime(abe_1032, stop_time='14:31:00')#timepoint
trip.AddStopTime(abe_1033, stop_time='14:32:00')
trip.AddStopTime(abe_1034, stop_time='14:33:00')
##ABE Trip 12 - 14:35:00 - Depart
trip = ABE.AddTrip(schedule, headsign="To Downtown via Athabasca East")
trip.AddStopTime(abe_1001, stop_time='14:35:00')#timepoint
trip.AddStopTime(abe_1002, stop_time='14:35:30')
trip.AddStopTime(abe_1003, stop_time='14:36:00')
trip.AddStopTime(abe_1004, stop_time='14:37:00')
trip.AddStopTime(abe_1005, stop_time='14:38:00')
trip.AddStopTime(abe_1006, stop_time='14:39:00')
trip.AddStopTime(abe_1007, stop_time='14:40:00')#timepoint
trip.AddStopTime(abe_1008, stop_time='14:41:00')
trip.AddStopTime(abe_1009, stop_time='14:42:00')
trip.AddStopTime(abe_1010, stop_time='14:43:00')#timepoint
trip.AddStopTime(abe_1011, stop_time='14:44:00')
trip.AddStopTime(abe_1012, stop_time='14:46:00')
trip.AddStopTime(abe_1013, stop_time='14:47:30')
trip.AddStopTime(abe_1014, stop_time='14:49:00')#timepoint
trip.AddStopTime(abe_1015, stop_time='14:55:00')#timepoint
trip.AddStopTime(abe_1016, stop_time='15:00:00')#timepoint
trip.AddStopTime(abe_1017, stop_time='15:00:30')
trip.AddStopTime(abe_1018, stop_time='15:01:00')
trip.AddStopTime(abe_1019, stop_time='15:02:00')
trip.AddStopTime(abe_1020, stop_time='15:03:00')#timepoint
trip.AddStopTime(abe_1021, stop_time='15:03:30')
trip.AddStopTime(abe_1022, stop_time='15:04:00')
trip.AddStopTime(abe_1023, stop_time='15:04:30')
trip.AddStopTime(abe_1024, stop_time='15:05:00')
trip.AddStopTime(abe_1025, stop_time='15:05:30')
trip.AddStopTime(abe_1026, stop_time='15:06:00')#timepoint
trip.AddStopTime(abe_1027, stop_time='15:08:00')
trip.AddStopTime(abe_1028, stop_time='15:09:00')
trip.AddStopTime(abe_1029, stop_time='15:09:30')
trip.AddStopTime(abe_1030, stop_time='15:10:00')
trip.AddStopTime(abe_1031, stop_time='15:10:30')
trip.AddStopTime(abe_1032, stop_time='15:11:00')#timepoint
trip.AddStopTime(abe_1033, stop_time='15:12:00')
trip.AddStopTime(abe_1034, stop_time='15:13:00')
##ABE Trip 13 - 15:15:00 - Depart
trip = ABE.AddTrip(schedule, headsign="To Downtown via Athabasca East")
trip.AddStopTime(abe_1001, stop_time='15:15:00')#timepoint
trip.AddStopTime(abe_1002, stop_time='15:17:00')
trip.AddStopTime(abe_1003, stop_time='15:17:30')
trip.AddStopTime(abe_1004, stop_time='15:18:00')
trip.AddStopTime(abe_1005, stop_time='15:18:30')
trip.AddStopTime(abe_1006, stop_time='15:19:00')
trip.AddStopTime(abe_1007, stop_time='15:20:00')#timepoint
trip.AddStopTime(abe_1008, stop_time='15:21:00')
trip.AddStopTime(abe_1009, stop_time='15:22:00')
trip.AddStopTime(abe_1010, stop_time='15:23:00')#timepoint
trip.AddStopTime(abe_1011, stop_time='15:24:00')
trip.AddStopTime(abe_1012, stop_time='15:25:00')
trip.AddStopTime(abe_1013, stop_time='15:27:00')
trip.AddStopTime(abe_1014, stop_time='15:29:00')#timepoint
trip.AddStopTime(abe_1015, stop_time='15:35:00')#timepoint
trip.AddStopTime(abe_1016, stop_time='15:40:00')#timepoint
trip.AddStopTime(abe_1017, stop_time='15:41:00')
trip.AddStopTime(abe_1018, stop_time='15:42:00')
trip.AddStopTime(abe_1019, stop_time='15:42:30')
trip.AddStopTime(abe_1020, stop_time='15:43:00')#timepoint
trip.AddStopTime(abe_1021, stop_time='15:43:30')
trip.AddStopTime(abe_1022, stop_time='15:44:00')
trip.AddStopTime(abe_1023, stop_time='15:44:30')
trip.AddStopTime(abe_1024, stop_time='15:45:00')
trip.AddStopTime(abe_1025, stop_time='15:45:30')
trip.AddStopTime(abe_1026, stop_time='15:46:00')#timepoint
trip.AddStopTime(abe_1027, stop_time='15:46:30')
trip.AddStopTime(abe_1028, stop_time='15:47:00')
trip.AddStopTime(abe_1029, stop_time='15:47:30')
trip.AddStopTime(abe_1030, stop_time='15:48:00')
trip.AddStopTime(abe_1031, stop_time='15:48:30')
trip.AddStopTime(abe_1032, stop_time='15:49:00')#timepoint
trip.AddStopTime(abe_1033, stop_time='15:49:30')
trip.AddStopTime(abe_1034, stop_time='15:50:00')
##ABE Trip 14 - 15:55:00 - Depart
trip = ABE.AddTrip(schedule, headsign="To Downtown via Athabasca East")
trip.AddStopTime(abe_1001, stop_time='15:55:00')#timepoint
trip.AddStopTime(abe_1002, stop_time='15:55:30')
trip.AddStopTime(abe_1003, stop_time='15:56:00')
trip.AddStopTime(abe_1004, stop_time='15:57:00')
trip.AddStopTime(abe_1005, stop_time='15:58:00')
trip.AddStopTime(abe_1006, stop_time='15:59:00')
trip.AddStopTime(abe_1007, stop_time='16:00:00')#timepoint
trip.AddStopTime(abe_1008, stop_time='16:01:00')
trip.AddStopTime(abe_1009, stop_time='16:02:00')
trip.AddStopTime(abe_1010, stop_time='16:03:00')#timepoint
trip.AddStopTime(abe_1011, stop_time='16:05:00')
trip.AddStopTime(abe_1012, stop_time='16:07:00')
trip.AddStopTime(abe_1013, stop_time='16:08:00')
trip.AddStopTime(abe_1014, stop_time='16:09:00')#timepoint
trip.AddStopTime(abe_1015, stop_time='16:15:00')#timepoint
trip.AddStopTime(abe_1016, stop_time='16:20:00')#timepoint
trip.AddStopTime(abe_1017, stop_time='16:20:30')
trip.AddStopTime(abe_1018, stop_time='16:21:00')
trip.AddStopTime(abe_1019, stop_time='16:22:00')
trip.AddStopTime(abe_1020, stop_time='16:23:00')#timepoint
trip.AddStopTime(abe_1021, stop_time='16:23:30')
trip.AddStopTime(abe_1022, stop_time='16:24:00')
trip.AddStopTime(abe_1023, stop_time='16:24:30')
trip.AddStopTime(abe_1024, stop_time='16:25:00')
trip.AddStopTime(abe_1025, stop_time='16:25:30')
trip.AddStopTime(abe_1026, stop_time='16:26:00')#timepoint
trip.AddStopTime(abe_1027, stop_time='16:26:30')
trip.AddStopTime(abe_1028, stop_time='16:27:00')
trip.AddStopTime(abe_1029, stop_time='16:28:00')
trip.AddStopTime(abe_1030, stop_time='16:29:00')
trip.AddStopTime(abe_1031, stop_time='16:30:00')
trip.AddStopTime(abe_1032, stop_time='16:31:00')#timepoint
trip.AddStopTime(abe_1033, stop_time='16:32:00')
trip.AddStopTime(abe_1034, stop_time='16:33:00')
##ABE Trip 15 - 16:35:00 - Depart
trip = ABE.AddTrip(schedule, headsign="To Downtown via Athabasca East")
trip.AddStopTime(abe_1001, stop_time='16:35:00')#timepoint
trip.AddStopTime(abe_1002, stop_time='16:35:30')
trip.AddStopTime(abe_1003, stop_time='16:36:00')
trip.AddStopTime(abe_1004, stop_time='16:37:00')
trip.AddStopTime(abe_1005, stop_time='16:38:00')
trip.AddStopTime(abe_1006, stop_time='16:39:00')
trip.AddStopTime(abe_1007, stop_time='16:40:00')#timepoint
trip.AddStopTime(abe_1008, stop_time='16:41:00')
trip.AddStopTime(abe_1009, stop_time='16:42:00')
trip.AddStopTime(abe_1010, stop_time='16:43:00')#timepoint
trip.AddStopTime(abe_1011, stop_time='16:44:00')
trip.AddStopTime(abe_1012, stop_time='16:46:00')
trip.AddStopTime(abe_1013, stop_time='16:47:30')
trip.AddStopTime(abe_1014, stop_time='16:49:00')#timepoint
trip.AddStopTime(abe_1015, stop_time='16:55:00')#timepoint
trip.AddStopTime(abe_1016, stop_time='17:00:00')#timepoint
trip.AddStopTime(abe_1017, stop_time='17:00:30')
trip.AddStopTime(abe_1018, stop_time='17:01:00')
trip.AddStopTime(abe_1019, stop_time='17:02:00')
trip.AddStopTime(abe_1020, stop_time='17:03:00')#timepoint
trip.AddStopTime(abe_1021, stop_time='17:03:30')
trip.AddStopTime(abe_1022, stop_time='17:04:00')
trip.AddStopTime(abe_1023, stop_time='17:04:30')
trip.AddStopTime(abe_1024, stop_time='17:05:00')
trip.AddStopTime(abe_1025, stop_time='17:05:30')
trip.AddStopTime(abe_1026, stop_time='17:06:00')#timepoint
trip.AddStopTime(abe_1027, stop_time='17:08:00')
trip.AddStopTime(abe_1028, stop_time='17:09:00')
trip.AddStopTime(abe_1029, stop_time='17:09:30')
trip.AddStopTime(abe_1030, stop_time='17:10:00')
trip.AddStopTime(abe_1031, stop_time='17:10:30')
trip.AddStopTime(abe_1032, stop_time='17:11:00')#timepoint
trip.AddStopTime(abe_1033, stop_time='17:12:00')
trip.AddStopTime(abe_1034, stop_time='17:13:00')
##ABE Trip 16 - 17:15:00 - Depart
trip = ABE.AddTrip(schedule, headsign="To Downtown via Athabasca East")
trip.AddStopTime(abe_1001, stop_time='17:15:00')#timepoint
trip.AddStopTime(abe_1002, stop_time='17:17:00')
trip.AddStopTime(abe_1003, stop_time='17:17:30')
trip.AddStopTime(abe_1004, stop_time='17:18:00')
trip.AddStopTime(abe_1005, stop_time='17:18:30')
trip.AddStopTime(abe_1006, stop_time='17:19:00')
trip.AddStopTime(abe_1007, stop_time='17:20:00')#timepoint
trip.AddStopTime(abe_1008, stop_time='17:21:00')
trip.AddStopTime(abe_1009, stop_time='17:22:00')
trip.AddStopTime(abe_1010, stop_time='17:23:00')#timepoint
trip.AddStopTime(abe_1011, stop_time='17:24:00')
trip.AddStopTime(abe_1012, stop_time='17:25:00')
trip.AddStopTime(abe_1013, stop_time='17:27:00')
trip.AddStopTime(abe_1014, stop_time='17:29:00')#timepoint
trip.AddStopTime(abe_1015, stop_time='17:35:00')#timepoint
trip.AddStopTime(abe_1016, stop_time='17:40:00')#timepoint
trip.AddStopTime(abe_1017, stop_time='17:41:00')
trip.AddStopTime(abe_1018, stop_time='17:42:00')
trip.AddStopTime(abe_1019, stop_time='17:42:30')
trip.AddStopTime(abe_1020, stop_time='17:43:00')#timepoint
trip.AddStopTime(abe_1021, stop_time='17:43:30')
trip.AddStopTime(abe_1022, stop_time='17:44:00')
trip.AddStopTime(abe_1023, stop_time='17:44:30')
trip.AddStopTime(abe_1024, stop_time='17:45:00')
trip.AddStopTime(abe_1025, stop_time='17:45:30')
trip.AddStopTime(abe_1026, stop_time='17:46:00')#timepoint
trip.AddStopTime(abe_1027, stop_time='17:46:30')
trip.AddStopTime(abe_1028, stop_time='17:47:00')
trip.AddStopTime(abe_1029, stop_time='17:47:30')
trip.AddStopTime(abe_1030, stop_time='17:48:00')
trip.AddStopTime(abe_1031, stop_time='17:48:30')
trip.AddStopTime(abe_1032, stop_time='17:49:00')#timepoint
trip.AddStopTime(abe_1033, stop_time='17:49:30')
trip.AddStopTime(abe_1034, stop_time='17:50:00')
##ABE Trip 17 - 17:55:00 - Depart
trip = ABE.AddTrip(schedule, headsign="To Downtown via Athabasca East")
trip.AddStopTime(abe_1001, stop_time='17:55:00')#timepoint
trip.AddStopTime(abe_1002, stop_time='17:55:30')
trip.AddStopTime(abe_1003, stop_time='17:56:00')
trip.AddStopTime(abe_1004, stop_time='17:57:00')
trip.AddStopTime(abe_1005, stop_time='17:58:00')
trip.AddStopTime(abe_1006, stop_time='17:59:00')
trip.AddStopTime(abe_1007, stop_time='18:00:00')#timepoint
trip.AddStopTime(abe_1008, stop_time='18:01:00')
trip.AddStopTime(abe_1009, stop_time='18:02:00')
trip.AddStopTime(abe_1010, stop_time='18:03:00')#timepoint
trip.AddStopTime(abe_1011, stop_time='18:05:00')
trip.AddStopTime(abe_1012, stop_time='18:07:00')
trip.AddStopTime(abe_1013, stop_time='18:08:00')
trip.AddStopTime(abe_1014, stop_time='18:09:00')#timepoint
trip.AddStopTime(abe_1015, stop_time='18:15:00')#timepoint
trip.AddStopTime(abe_1016, stop_time='18:20:00')#timepoint
trip.AddStopTime(abe_1017, stop_time='18:20:30')
trip.AddStopTime(abe_1018, stop_time='18:21:00')
trip.AddStopTime(abe_1019, stop_time='18:22:00')
trip.AddStopTime(abe_1020, stop_time='18:23:00')#timepoint
trip.AddStopTime(abe_1021, stop_time='18:23:30')
trip.AddStopTime(abe_1022, stop_time='18:24:00')
trip.AddStopTime(abe_1023, stop_time='18:24:30')
trip.AddStopTime(abe_1024, stop_time='18:25:00')
trip.AddStopTime(abe_1025, stop_time='18:25:30')
trip.AddStopTime(abe_1026, stop_time='18:26:00')#timepoint
trip.AddStopTime(abe_1027, stop_time='18:26:30')
trip.AddStopTime(abe_1028, stop_time='18:27:00')
trip.AddStopTime(abe_1029, stop_time='18:28:00')
trip.AddStopTime(abe_1030, stop_time='18:29:00')
trip.AddStopTime(abe_1031, stop_time='18:30:00')
trip.AddStopTime(abe_1032, stop_time='18:31:00')#timepoint
trip.AddStopTime(abe_1033, stop_time='18:32:00')
trip.AddStopTime(abe_1034, stop_time='18:33:00')
###ABE-Late Trip 1 - 18:35:00 - Depart
###ABE-Late Trip 2 - 19:15:00 - Depart


#SUN Trip 1 - 7:15:00 - Depart
trip = SUN.AddTrip(schedule, headsign="To Downtown via Sunningdale")
trip.AddStopTime(sun_2001, stop_time='7:15:00')
trip.AddStopTime(sun_2002, stop_time='7:16:00')
trip.AddStopTime(sun_2003, stop_time='7:17:00')
trip.AddStopTime(sun_2004, stop_time='7:18:00')
trip.AddStopTime(sun_2005, stop_time='7:20:00')
trip.AddStopTime(sun_2006, stop_time='7:20:30')
trip.AddStopTime(sun_2007, stop_time='7:21:00')
trip.AddStopTime(sun_2008, stop_time='7:22:00')
trip.AddStopTime(sun_2009, stop_time='7:22:30')
trip.AddStopTime(sun_2010, stop_time='7:23:00')
trip.AddStopTime(sun_2011, stop_time='7:24:30')
trip.AddStopTime(sun_2012, stop_time='7:25:00')
trip.AddStopTime(sun_2013, stop_time='7:26:00')
trip.AddStopTime(sun_2014, stop_time='7:27:00')
trip.AddStopTime(sun_2015, stop_time='7:28:00')
trip.AddStopTime(sun_2016, stop_time='7:28:30')
trip.AddStopTime(sun_2017, stop_time='7:29:00')
trip.AddStopTime(sun_2018, stop_time='7:29:30')
trip.AddStopTime(sun_2019, stop_time='7:30:00')
trip.AddStopTime(sun_2020, stop_time='7:35:00')
trip.AddStopTime(sun_2021, stop_time='7:38:00')
trip.AddStopTime(sun_2022, stop_time='7:39:00')
trip.AddStopTime(sun_2023, stop_time='7:40:00')
trip.AddStopTime(sun_2024, stop_time='7:41:00')
trip.AddStopTime(sun_2025, stop_time='7:41:30')
trip.AddStopTime(sun_2026, stop_time='7:42:00')
trip.AddStopTime(sun_2027, stop_time='7:42:30')
trip.AddStopTime(sun_2028, stop_time='7:43:00')
trip.AddStopTime(sun_2029, stop_time='7:43:30')
trip.AddStopTime(sun_2030, stop_time='7:44:00')
trip.AddStopTime(sun_2031, stop_time='7:45:00')
trip.AddStopTime(sun_2032, stop_time='7:46:00')
trip.AddStopTime(sun_2033, stop_time='7:47:00')
trip.AddStopTime(sun_2034, stop_time='7:48:00')
trip.AddStopTime(sun_2035, stop_time='7:49:00')
trip.AddStopTime(sun_2036, stop_time='7:50:00')
##SUN Trip 3 - 8:35:00 - Depart
##SUN Trip 4 - 9:15:00 - Depart
##SUN Trip 5 - 9:55:00 - Depart
##SUN Trip 6 - 10:35:00 - Depart
##SUN Trip 7 - 11:15:00 - Depart
##SUN Trip 8 - 11:55:00 - Depart
##SUN Trip 9 - 12:35:00 - Depart
##SUN Trip 10 - 13:15:00 - Depart
##SUN Trip 11 - 13:55:00 - Depart
##SUN Trip 12 - 14:35:00 - Depart
##SUN Trip 13 - 15:15:00 - Depart
##SUN Trip 14 - 15:55:00 - Depart
##SUN Trip 15 - 16:35:00 - Depart
##SUN Trip 16 - 17:15:00 - Depart
##SUN Trip 17 - 17:55:00 - Depart
###SUN-Late Trip 1 - 18:35:00 - Depart
###SUN-Late Trip 19 - 19:15:00 - Depart

#ABW Trip 1 - 7:15:00
trip = ABW.AddTrip(schedule, headsign="To Downtown via Athabasca West")
trip.AddStopTime(abw_3001, stop_time='7:15:00')
trip.AddStopTime(abw_3002, stop_time='7:15:30')
trip.AddStopTime(abw_3003, stop_time='7:16:00')
trip.AddStopTime(abw_3004, stop_time='7:16:30')
trip.AddStopTime(abw_3005, stop_time='7:17:00')
trip.AddStopTime(abw_3006, stop_time='7:17:30')
trip.AddStopTime(abw_3007, stop_time='7:18:00')
trip.AddStopTime(abw_3008, stop_time='7:18:30')
trip.AddStopTime(abw_3009, stop_time='7:19:00')
trip.AddStopTime(abw_3010, stop_time='7:20:00')
trip.AddStopTime(abw_3011, stop_time='7:21:00')
trip.AddStopTime(abw_3012, stop_time='7:21:30')
trip.AddStopTime(abw_3013, stop_time='7:22:00')
trip.AddStopTime(abw_3014, stop_time='7:22:30')
trip.AddStopTime(abw_3015, stop_time='7:23:00')
trip.AddStopTime(abw_3016, stop_time='7:23:30')
trip.AddStopTime(abw_3017, stop_time='7:24:00')
trip.AddStopTime(abw_3018, stop_time='7:25:00')
trip.AddStopTime(abw_3019, stop_time='7:25:30')
trip.AddStopTime(abw_3020, stop_time='7:26:00')
trip.AddStopTime(abw_3021, stop_time='7:27:00')
trip.AddStopTime(abw_3022, stop_time='7:28:00')
trip.AddStopTime(abw_3023, stop_time='7:29:00')
trip.AddStopTime(abw_3024, stop_time='7:30:00')
trip.AddStopTime(abw_3025, stop_time='7:32:00')
trip.AddStopTime(abw_3026, stop_time='7:33:00')
trip.AddStopTime(abw_3027, stop_time='7:35:00')
trip.AddStopTime(abw_3028, stop_time='7:36:00')
trip.AddStopTime(abw_3029, stop_time='7:38:00')
trip.AddStopTime(abw_3030, stop_time='7:39:00')
trip.AddStopTime(abw_3031, stop_time='7:39:30')
trip.AddStopTime(abw_3032, stop_time='7:40:00')
trip.AddStopTime(abw_3033, stop_time='7:41:00')
trip.AddStopTime(abw_3034, stop_time='7:42:00')
trip.AddStopTime(abw_3035, stop_time='7:43:00')
trip.AddStopTime(abw_3036, stop_time='7:44:00')
trip.AddStopTime(abw_3037, stop_time='7:45:00')
trip.AddStopTime(abw_3038, stop_time='7:46:00')
trip.AddStopTime(abw_3039, stop_time='7:47:00')
trip.AddStopTime(abw_3040, stop_time='7:48:00')
trip.AddStopTime(abw_3041, stop_time='7:49:00')
trip.AddStopTime(abw_3042, stop_time='7:50:00')
##ABW Trip 3 - 8:35:00 - Depart
##ABW Trip 4 - 9:15:00 - Depart
##ABW Trip 5 - 9:55:00 - Depart
##ABW Trip 6 - 10:35:00 - Depart
##ABW Trip 7 - 11:15:00 - Depart
##ABW Trip 8 - 11:55:00 - Depart
##ABW Trip 9 - 12:35:00 - Depart
##ABW Trip 10 - 13:15:00 - Depart
##ABW Trip 11 - 13:55:00 - Depart
##ABW Trip 12 - 14:35:00 - Depart
##ABW Trip 13 - 15:15:00 - Depart
##ABW Trip 14 - 15:55:00 - Depart
##ABW Trip 15 - 16:35:00 - Depart
##ABW Trip 16 - 17:15:00 - Depart
##ABW Trip 17 - 17:55:00 - Depart
###ABW-Late Trip 1 - 18:35:00 - Depart
###ABW-Late Trip 2 - 19:15:00 - Depart

#WES Trip 1 - 7:15:00 - Depart
trip = WES.AddTrip(schedule, headsign="To Downtown via Westmount")
trip.AddStopTime(wes_4001, stop_time='7:15:00')
trip.AddStopTime(wes_4002, stop_time='7:16:00')
trip.AddStopTime(wes_4003, stop_time='7:17:00')
trip.AddStopTime(wes_4004, stop_time='7:18:00')
trip.AddStopTime(wes_4005, stop_time='7:19:00')
trip.AddStopTime(wes_4006, stop_time='7:20:00')
trip.AddStopTime(wes_4007, stop_time='7:21:00')
trip.AddStopTime(wes_4008, stop_time='7:22:00')
trip.AddStopTime(wes_4009, stop_time='7:23:30')
trip.AddStopTime(wes_4010, stop_time='7:24:00')
trip.AddStopTime(wes_4011, stop_time='7:24:30')
trip.AddStopTime(wes_4012, stop_time='7:25:00')
trip.AddStopTime(wes_4013, stop_time='7:25:30')
trip.AddStopTime(wes_4014, stop_time='7:26:00')
trip.AddStopTime(wes_4015, stop_time='7:27:00')
trip.AddStopTime(wes_4016, stop_time='7:27:30')
trip.AddStopTime(wes_4017, stop_time='7:28:00')
trip.AddStopTime(wes_4018, stop_time='7:28:30')
trip.AddStopTime(wes_4019, stop_time='7:29:00')
trip.AddStopTime(wes_4020, stop_time='7:29:30')
trip.AddStopTime(wes_4021, stop_time='7:30:00')
trip.AddStopTime(wes_4022, stop_time='7:30:30')
trip.AddStopTime(wes_4023, stop_time='7:31:00')
trip.AddStopTime(wes_4024, stop_time='7:32:00')
trip.AddStopTime(wes_4025, stop_time='7:32:30')
trip.AddStopTime(wes_4026, stop_time='7:33:00')
trip.AddStopTime(wes_4027, stop_time='7:34:30')
trip.AddStopTime(wes_4028, stop_time='7:36:00')
trip.AddStopTime(wes_4029, stop_time='7:37:30')
trip.AddStopTime(wes_4030, stop_time='7:39:00')
trip.AddStopTime(wes_4031, stop_time='7:39:30')
trip.AddStopTime(wes_4032, stop_time='7:40:00')
trip.AddStopTime(wes_4033, stop_time='7:40:30')
trip.AddStopTime(wes_4034, stop_time='7:41:00')
trip.AddStopTime(wes_4035, stop_time='7:41:30')
trip.AddStopTime(wes_4036, stop_time='7:42:00')
trip.AddStopTime(wes_4037, stop_time='7:42:30')
trip.AddStopTime(wes_4038, stop_time='7:43:00')
trip.AddStopTime(wes_4039, stop_time='7:43:30')
trip.AddStopTime(wes_4040, stop_time='7:44:00')
trip.AddStopTime(wes_4041, stop_time='7:44:30')
trip.AddStopTime(wes_4042, stop_time='7:45:00')
trip.AddStopTime(wes_4043, stop_time='7:46:00')
trip.AddStopTime(wes_4044, stop_time='7:46:30')
trip.AddStopTime(wes_4045, stop_time='7:47:00')
trip.AddStopTime(wes_4046, stop_time='7:47:30')
trip.AddStopTime(wes_4047, stop_time='7:48:00')
trip.AddStopTime(wes_4048, stop_time='7:49:00')
trip.AddStopTime(wes_4049, stop_time='7:50:00')
##WES Trip 3 - 8:35:00 - Depart
##WES Trip 4 - 9:15:00 - Depart
##WES Trip 5 - 9:55:00 - Depart
##WES Trip 6 - 10:35:00 - Depart
##WES Trip 7 - 11:15:00 - Depart
##WES Trip 8 - 11:55:00 - Depart
##WES Trip 9 - 12:35:00 - Depart
##WES Trip 10 - 13:15:00 - Depart
##WES Trip 11 - 13:55:00 - Depart
##WES Trip 12 - 14:35:00 - Depart
##WES Trip 13 - 15:15:00 - Depart
##WES Trip 14 - 15:55:00 - Depart
##WES Trip 15 - 16:35:00 - Depart
##WES Trip 16 - 17:15:00 - Depart
##WES Trip 17 - 17:55:00 - Depart
###WES-Late Trip 1 - 18:35:00 - Depart
###WES-Late Trip 2 - 19:15:00 - Depart

# Validate The Feed
schedule.Validate()

# Output Feed
schedule.WriteGoogleTransitFeed('output/mjts_gtfs_' + mjts_version + '.zip')
