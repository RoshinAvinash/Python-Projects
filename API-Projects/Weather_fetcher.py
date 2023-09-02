import requests

#Here put your own API key, generate it in openweathermap.org website
API_KEY = ""

#Where we are sending the request to: 
#The end point, the URL we are sending request 
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

#Sending some query parameters: The things that we send along side this base URL telling it what data we want., so essentially what city we want to get the weather from.
city_name = input("Enter a city name: ")

#Now we have to build a kind of URL that looks similar to the BASE URL and also includes the city and my API key in it to be able to send request.
request_url = f"{BASE_URL}?q={city_name}&appid={API_KEY}"

#Since we are retrieving data, we use a get request
response = requests.get(request_url)

#response is going to contain the information associated with the city 
#However this response may have an error due to issue with the url or api key expired or etc
#So we have to check the response before we try to get the data 
if response.status_code == 200:
    #If successful we need to get the data 
    #Data is returned in json 
    data = response.json() #This will give the JSON data as a python dictionary
    
    #Now this data contains so many different items, so we need to access items depending on the need.
    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp'] - 273.15,2)
    
    print(f"Weather: {weather}")
    print(f"Temperature: {temperature} degrees celsius")

else:
    print("An Error occurred, Maybe Wrong city name.")
