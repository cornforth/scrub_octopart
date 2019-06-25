#Author: Eric Cornforth
#Date:6/24/19
#Description:
#This program will do the following:
#   1. It will interface with Octoparts API
#   2. It will read in information from an excel spreadsheet
#   3. It will output an updated excel spreadsheet that includes Component information, Customer Type, Maufacturer, etc(more will be included as needed)
#   4. It will search scrub information off Octopart as needed


import json
import requests
import openpyxl



def main():
    print("We are in the main function\n")
    url = 'http://octopart.com/api/v3/parts'
    apikey = '?apikey=7d66949cfb786407c39f'
    
    #headers = {'pretty_print': 'true', 'apikey': apikey}
    #url += '&apikey=7d66949cfb786407c39f&pretty_print=true'
    #First we want to test our connection to Silicon Experts API by sending an authentification request
    response = get_account_info(url, apikey)

#Test for authentification
def get_account_info(url, apikey):
    #construct the authentication operation URL
    url += "/"
    url += "103cdb613d20cffb"#might have to ask octopart what this part of the code is, it's bothering me!!!!!!
    url += apikey#add in the api key
    url +="&pretty_print=true"
    response = requests.get(url)
    if checkstatus(response.status_code):
        return json.loads(response.content.decode('utf-8'))
    return None
    #Check the JSON output
#Search Octopart for a part using known part #
def mfnSearch(url, mfNumber):
    url += '&queries=[{"mpn":"SN74S74N"}]'
    #Construct the search URL
    url+= mfNumber
    searchURL = api_url_base.format("partsearch?partNumber=",mfNumber)
    #Send the request
    req = request
    #review the request
#Check the received Status Code for any errors
def checkstatus(statCode):
    if statCode == 200:
        print("Your request was successful\n")
        return true
    elif statCode == 403:
        print("You are forbidden from accessing this pertinent information!\n")
        print("Your apikey is invalid\n")
        print("Please contact Octopart at api@octopart.com\n")
    elif statCode == 404:
        print("Could not find the requested page Error: 404\n")
    elif statCode == 400:
        print("Bad Request Error: 400\n")
        print("Your request is missing an 'apikey' argument\n")
    elif statCode == 500:
        print("Internal Server Error: 400\n")
    elif statCode == 502:
        print("Bad Gateway: 502\n")
    elif statCode == 503:
        print("Service Unavailable: 503\n")
    else:
        print("There was some new error!\n")
        print (response.status_code, "\n")
    return False


if __name__ == "__main__":
   main()