
import json
import requests
import openpyxl

loginName = input("What is your Silicon Expert Username: \n")
apikey = input("Looks like we'll need you Silicon Expert Password: \n")
api_url_base = "https://app.siliconexpert.com/ProductAPI/search"

headers = {'login': loginName,'apiKey' : apikey, 'fmt':json}

def main():
    print("We are in the main function\n")
    #First we want to test our connection to Silicon Experts API by sending an authentification request
    if not auth():
        print ("we are not authentic!\n")
        exit()
    print ("Yo, we made it through the gate")
    #First we must acquire the list information from the excel spreadsheet

    #Once the information is acquired we send a search request for 




def auth():
    #construct the authentication operation URL
    authenticate = api_url_base.format("authenticateUser?login=", loginName, "&apiKey=", apikey)
    print(authenticate)
    response = requests.get(api_url_base, headers = headers)
    #Check the JSON output

def mfnSearch(mfNumber):
    #Construct the search URL
    searchURL = api_url_base.format("partsearch?partNumber=",mfNumber)
    #Send the request
    req = request

if __name__ == "__main__":
    main()