import requests
import datetime
now = datetime.date.today()
print()

#for India
print("For India: 18+ Vaccine availability")
states = requests.get("https://cdn-api.co-vin.in/api/v2/admin/location/states")
for state in states.json()['states']:
    print(state['state_name'])
    stateUrl = 'https://cdn-api.co-vin.in/api/v2/admin/location/districts/'+str(state['state_id'])
    #print(stateUrl)
    disctricts = requests.get(stateUrl)
    for disctrict in disctricts.json()['districts']:
        print (disctrict['district_name'])
        districtUrl = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=' + str(disctrict['district_id']) +"&date=" +str(now.strftime("%d-%m-%Y"))
        #print (districtUrl)
        vaccineByDistrict = requests.get(districtUrl)

        for center in vaccineByDistrict.json()['centers']:
            for sessions in center['sessions']:
                if(sessions['available_capacity']>0):
                    if (sessions['min_age_limit']!=45):
                        print("Date: ", sessions['date'], "Capacity: ", sessions['available_capacity'], "Vaccine: ", sessions['vaccine'])
                        print("Name of the Center: ", center['name'])

#for Maharashtra
# print("For Maharashtra: 18+ Vaccine availability")
# disctricts = requests.get("https://cdn-api.co-vin.in/api/v2/admin/location/districts/21")
# for disctrict in disctricts.json()['districts']:
#     print (disctrict['district_name'])
#     districtUrl = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=' + str(disctrict['district_id']) +"&date=" +"01-05-2021"
# #    print (districtUrl)
#     vaccineByDistrict = requests.get(districtUrl)
# # print("For 45 and above: ")
#     for center in vaccineByDistrict.json()['centers']:
#         for sessions in center['sessions']:
#             if(sessions['available_capacity']>0):
#                 if (sessions['min_age_limit']!=45):
#                     print("Date: ", sessions['date'], "Capacity: ", sessions['available_capacity'], "Vaccine: ", sessions['vaccine'])
#                     print("Name of the Center: ", center['name'])

#for Nashik
#
# print("For Nashik: 18+ Vaccine availability")
# vaccineByDistrict = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=389&date=01-05-2021')
#
# print("For 45 and above: ")
# for center in vaccineByDistrict.json()['centers']:
#     for sessions in center['sessions']:
#         if(sessions['available_capacity']>0):
#             if (sessions['min_age_limit']!=45):
#                 print("Date: ", sessions['date'], "Capacity: ", sessions['available_capacity'], "Vaccine: ", sessions['vaccine'])
#                 print("Name of the Center: ", center['name'])
#
#
