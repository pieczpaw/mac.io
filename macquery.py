import sys, requests, json


#check if there is additional parameter (mac address)
if len(sys.argv) == 1:
    print("\n\nUsage:\n"
        "               macquery.py \"mac:address\""
        "\nExample:\n"
        "                macquery.py A1:B2:C3:D4:E5:F6:\n\n"
        "Exiting...\n")
    exit()
else:
    MAC = str(sys.argv[1])

api_base = 'https://api.macaddress.io/v1?apiKey=at_QCXnxzanB3rP9GOyMl7v6s6MlHXi9&output=json&search='
search = api_base + MAC
response = requests.get(search)
response = response.json()

if response:
    print("Device: " + MAC + " was developed by: " + response['vendorDetails']['companyName'])
else:
    print("Device with MAC: " + MAC + " was not found in our database!")
