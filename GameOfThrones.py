# --url https://www.anapioficeandfire.com/api/houses

import requests  #used to send HTTP requests in python
import argparse  #used for passing command line arguments
import json  #imports the json library when working with json data

try:
    parser = argparse.ArgumentParser()  # creates a ArgumentParser object witch will handle the c-l-arguments
    parser.add_argument("--url", help="Url, required", required=True) # adds an argument witch takes in a url witch is inserted into the edit configuration
    args, unknown = parser.parse_known_args()  # args will contain the parsed arguments and unknown contains the unknown arguments

    response = requests.get(args.url)  # sends a GET request to the url then the response is storen in the response variable
    houses = response.json()  # this parses the response to the houses variable in a json format

    for house in houses:  # then we loop for the house in houses output the house["name"] atributte
        print(house["name"]) # you can change this to output whatever u want like url, name, and the other attributes that u can gain from this

except Exception as e:  # this prints any exeptions that come by if there are any
    print(e)