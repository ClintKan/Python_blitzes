import requests

url = "https://api.travelpayouts.com/v2/prices/month-matrix"

querystring = {"currency":"usd","show_to_affiliates":"true","origin":"NYC","destination":"LAX"}

headers = {'x-access-token': '2160a9f9ca2fa3d348f4a3a32504538e'}

response = requests.request("GET", url, headers=headers, params=querystring)

# ---------------------------------------------------------------------------------------------

#Qn/Challenge: Return details of a flight departing on October 21st
# ---------------------------------------------------------------------------------------------

#print(response) # prints the response code; 200 if Ok, anything else s'mthn is iffy

#print(response.json()) # prints the whole data set pulled by the api

raw_data = response.json() # best to write the data (line 13 )to a variable

print(f"\n {type(raw_data)}") # understand what type of data you're getting back

print(f"\n {raw_data.keys()}") # to see the raw_data's keys it has

print(f"\n {type(raw_data["data"])}") # to see the type of data 'data' is

print(f"\n {raw_data['data'][0]}") #as a list, this is a test data-set extraction

print(f"\n {len(raw_data["data"])}") #to know how many items are in raw_data['data'] 

temp_data = len(raw_data["data"])

# to look and only return details of a flight departing on October 21st
for i in range(30):
    if raw_data['data'][i]["depart_date"] == '2024-10-21':
        print(f"\n Found it: \n {raw_data['data'][i]}")


