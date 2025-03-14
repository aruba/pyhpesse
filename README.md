# pyhpesse
## HPE Aruba Networking Security Service Edge (SSE) SDK
This package has been developed in Python v3.9 to utilise the full functionality of the HPE Aruba Networking Security Service Edge (SSE) API environment. Each available REST API command is available for use in this module. All responses from HPE Aruba Networking Security Service Edge (SSE) API are in JSON format (converted into a Python dictionary object). Any changes with the API are logged within the Audit Log. 

When updates are made to the SSE API environment, the python package will be updated in due course. You may review the changes in the [release notes](RELEASE-NOTES.md) file.

This package has been uploaded to https://pypi.org/ and is also available to install via https://github.com/aruba/pyhpesse. 
These instructions will also available at https://developer.arubanetworks.com/ in due course.
Installation instructions and usage instructions are also provided below. 

> [!Warning]  
> _This package comes without any warranties and should be used at your own risk._

## Available API Categories  
The following describes the available top level functionality of the HPE Aruba Networking Security Service Edge (SSE) SDK API available within this Python Package. 
- API Service - Application Groups
- API Service - Applications
- API Service - Connectors
- API Service - Connector Zones
- API Service - Custom IP Categories
- API Service - Groups
- API Service - IP Feed Categories
- API Service - Locations
- API Service - SSL Exclusions
- API Service - Sub Locations
- API Service - Tunnels
- API Service - Users
- API Service - Web Categories

> [!Note]  
> Some API functions are limited releases (tunnels, locations, tags, applications) and functionality may be limited and change.

## HPE Aruba Networking Security Service Edge (SSE) SDK API Readiness 
These steps list what is required on the HPE Aruba Networking Security Service Edge Management Console:
1. Login as an administrator
2. Click Settings and Admin API
3. Click 'New API Token'
4. Fill in the form and click 'Submit' 
5. Note the 'API Access Token' value

If you need information, refer to the HPE Aruba Networking SSE configuration documentation for the API account -
https://docs.axissecurity.com/docs/axis-cloud-api-generate-token

# Python Requirements  
Ensure Python v3.9 or greater is installed on your operating system
# Package Installation

#### Method 1 - Installing Package from PyPi
Run the following in a command line terminal to install the pip package - ```pip3 install pyhpesse``` or ```pip install pyhpesse```. This may vary between Operating Systems. 

#### Method 2 - Installing Package from Github (not using Git.exe)
1. Click into the Aruba Github Repository where the latest version of pyhpesse is located 
2. Click Code (in green) and Download to Zip
3. Extract the zip file into a directory
4. Go into a command line terminal and change directory (cd) into the folder where you extracted the zipped file and then down one child folder. The folder contents should pyhpesse (FOLDER), LICENCE, pyproject.toml and README.md   
5. In your command line terminal type ```python3 -m build``` or ```python -m build```. This will create a folder called dist with a file containing a .gz extension. 
6. Run the following in a command line terminal to install the pip package - ```pip3 install pathtozip.gz``` or ```pip install pathtozip.gz```. This may vary between Operating Systems.

#### Method 3 - Installing Package from Github (using Git.exe)
1. Install Git for your Operating System from https://git-scm.com/download
2. Run the following in a command line terminal to install the pip package - ```pip3 install git+https://github.com/aruba/pyhpesse``` or ```pip install git+https://github.com/aruba/pyhpesse```. This may vary between Operating Systems. 

# Initial Usage Instructions

Within your favourite Python IDE environment, create an import reference

```python
from pyhpesse import *
```

Create a object to login into the API. The login object needs to be passed to use any function to use the API.  
Using client credentials

```python
login = HPESecureServiceEdgeApiLogin(api_token="your API Token")
```

> [!WARNING]  
> Never expose your credentials directly in your scripts. The above is just an example for completeness. 

Find an API you want to use, by prefixing  `AdminApi.`  in your IDE and Intellisense will show the available APIs. Each of the top level API category names are available within the module. 

The example below prints upto 500 local SSE users. You must pass in the login variable along with the pagenumber and pagesize to return the data of SSE users. 

```python
print(AdminApi.get_users(login,pagenumber=1,pagesize=500))
```

## Working Example
Below is an example of the initial usage instructions, which includes a console print to display the result.
```python
from pyhpesse import *
login = HPESecureServiceEdgeApiLogin(api_token="your API Token")
print(AdminApi.get_users(login,pagenumber=1,pagesize=500))
```

## Optional Function for Retrieving Token from a File
You can use a function to retrieve an API token from a file in the working directory, rather than specifying the token configuration directly in the code. This allows easy reuse of the token file across your scripts which are located in the same working directory. Follow these steps to retrieve the token from a file:
1. Create a file in the working directory, for example called 'token-sse.token'
2. Within the file, use the JSON structure and create an key name called access_token and within the key value, write the API Token value.
```json
{"access_token":"YourSecretToken"}
```
4. Retrieve the API Token from the file by creating an object for apiSecretToken using the get_token_from_file utility function from the Utils_SSE class and then use the apiSecretToken to initialize the HPESecureServiceEdgeApiLogin object, instead of directly specifying the API key directly in the script. An example is provided below. 
```python
from pyhpesse import *
apiSecretToken = Utils_SSE.get_token_from_file("token-sse.token")
login = HPESecureServiceEdgeApiLogin(api_token=apiSecretToken)
```

## Optional Parameters
The following detail the additional available parameters within the HPESecureServiceEdgeApiLogin class. The parameters have default values and are not required to be defined within the HPESecureServiceEdgeApiLogin object. 
```python
verify_ssl = False, #Disable SSL if required. By default, verify SSL is enabled.
url = "https://admin-api.axissecurity.com" #Modify the default URL for Axis API Services.
```

# Help

Once you have written a specific API  `AdminApi.function_name(`, placing your cursor over the command will show you help for the function and what the required parameters are (example is Visual Studio Code). The first parameter is always login.  
You may also read the help for the function by calling `help(AdminApi.function_name)`.  
Each function contains a brief help summary. 

# Python Package Upgrade Instructions

Once an update is available on the Python PyPi repository, you may upgrade your release by completing the following in a command line terminal - 

`pip3 install pyhpesse --upgrade`  
or  
`pip install pyhpesse --upgrade`

To install a specific version, execute the following command with x.x.x being the specific version number you want to install. 

`pip3 install pyhpesse==x.x.x`  
or  
 `pip install pyhpesse==x.x.x`
 
# Uninstall Package Package

To remove the Python pyhpesse package, type the following command into a command line terminal -  
`pip3 uninstall pyhpesse `  
or  
 `pip uninstall pyhpesse `

# Additional Usage Examples

The following section of the readme contains a few example scripts. There are many different ways to script and also many different available functions within the SSE API which is always expanding. 

> [!WARNING]  
> Never expose your credentials directly in your scripts. The below examples are just examples for completeness. 

## Make a new Tunnel
This example script makes a new tunnel based on parameters below and if the location does not exist, it will create it.

```python 
from pyhpesse import *

# Your API Key
#######################
apiSecretToken = "Your_Secret_Token"
#######################

# Make Tunnel Parameters
#######################
locationName = "YourLocationName"
tunnelAuthenticationID = "IPAddressOrFQDN"
tunnelAuthenticationPsk = "SecretPassword"
tunnelName = "YourTunnelName"
#######################

login = HPESecureServiceEdgeApiLogin(api_token=apiSecretToken)

# Looks for existing location name and gets the location ID
locationID = ""
locations = AdminApi.get_locations(login, pagenumber=1, pagesize=10)
for location in locations["data"]:
    if location["name"] == locationName:
        locationID = location["id"]
        print("Existing Location Used:", locationName)

# Makes a new location if it does not already exist and gets the location ID
if not locationID:
    newLocation = {"name": locationName}
    print("New Location:", AdminApi.new_locations(login, body=newLocation))
    updatedLocations = AdminApi.get_locations(login, pagenumber=1, pagesize=10)
    for location in updatedLocations["data"]:
        if location["name"] == locationName:
            locationID = location["id"]

# Creates a new tunnel using the location name's ID from above.
if locationID:
    newtunnel = {
        "authenticationID": tunnelAuthenticationID,
        "authenticationPsk": tunnelAuthenticationPsk,
        "locationID": locationID,
        "name": tunnelName,
    }
    print("New Tunnel Output: ", AdminApi.new_tunnels(login, body=newtunnel))
```

## Delete a Tunnel
The following example script deletes a tunnel by its name. 

```python
from pyhpesse import *

# Your API Key
#######################
apiSecretToken = "Your_Secret_Token"
#######################

# Delete Tunnel Parameters
#######################
tunnelToDelete = "TunnelNameToDelete"
#######################

login = HPESecureServiceEdgeApiLogin(api_token=apiSecretToken)
gt = AdminApi.get_tunnels(login,pagenumber=1,pagesize=100)

tunnelID = ""

print("Start print list of Tunnels:")
for tunnel in gt['data']:
    print(f'Tunnel Name: {tunnel['name']}, Tunnel ID:{tunnel['id']}')
    if tunnelToDelete == tunnel['name']:
        tunnelID = tunnel['id']
print("End print list of Tunnels.")

if tunnelID:
    print(f"Removing Tunnel: {tunnel['id']} associated with tunnel name {tunnelToDelete}")
    print(AdminApi.delete_tunnels(login,id=tunnelID))
else:
    print("Tunnel does not exist or has already been removed")
```
## Extract data from SSE
This script will export the following information from SSE: application groups, applications, custom ip categories, connectors, connector zones, groups, ip feed category, locations, ssl exclusions, tunnels and users. 
All the extracted data will be exported to csv and will exist in a csv folder where the script is executed. As this is an example script, it will only return upto 500 enteries per page (pagesize). If you have more than 500 enteries, you will need to script accordingly by adjusting the pagenumber value. 

``` python
from pyhpesse import *
import csv
import os

# Your API Key
#######################
apiSecretToken = "Your_Secret_Token"
#######################

login = HPESecureServiceEdgeApiLogin(api_token=apiSecretToken)

pageSize=500

results={}
results["applicationgroups"]=AdminApi.get_applicationgroups(login,pagenumber=1,pagesize=pageSize)
results["applications"]=AdminApi.get_applications(login,pagenumber=1,pagesize=pageSize)
results["customipcategory"]=AdminApi.get_customipcategory(login,pagenumber=1,pagesize=pageSize)
results["connectors"]=AdminApi.get_connectors(login,pagenumber=1,pagesize=pageSize)
results["connectorzones"]=AdminApi.get_connectorzones(login,pagenumber=1,pagesize=pageSize)
results["groups"]=AdminApi.get_groups(login,pagenumber=1,pagesize=pageSize)
results["ipfeedcategory"]=AdminApi.get_ipfeedcategory(login,pagenumber=1,pagesize=pageSize)                                            
results["locations"]=AdminApi.get_locations(login,pagenumber=1,pagesize=pageSize)
results["sslexclusions"]=AdminApi.get_sslexclusions(login,pagenumber=1,pagesize=pageSize)
results["tunnels"]=AdminApi.get_tunnels(login,pagenumber=1,pagesize=pageSize)
results["users"]=AdminApi.get_users(login,pagenumber=1,pagesize=pageSize)

def export_to_csv(data, file_name, sub_folder="csv"):
    """
    Exports the data to a CSV file. Parameters are described below
    
    :param The data to be exported (expected to be a dictionary with an 'data' key).
    :param file_name: The name of the CSV file to create.
    :param sub_folder: The subfolder where the CSV file will be saved.
    """

    if 'data' in data and data['data']:
        items = data['data']
    else:
        print(f"The 'data' list is empty for {file_name}. No CSV file will be created.")
        return

    headers = items[0].keys()

    if not os.path.exists(sub_folder):
        os.makedirs(sub_folder)

    file_name = f"{file_name}.csv"
    file_path = os.path.join(sub_folder, file_name)

    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)

        writer.writeheader()

        for item in items:
            writer.writerow(item)

        print(f"Data has been exported to {file_path}")

for result in results:
    export_to_csv(data=results[result],file_name=result,sub_folder="csv")
                   
```

## Create New Empty Tag Groups 
This example script creates an empty list of Tag Groups.

``` python
from pyhpesse import *

# Your API Key
#######################
apiSecretToken = "Your_Secret_Key"
#######################

## Parameters - List of Tags to Add 
######################
listOfTags=['TagGroup1','TagGroup2', ]
######################

login = HPESecureServiceEdgeApiLogin(api_token=apiSecretToken)
for tag in listOfTags:
    tags = {"name": tag}
    newtags = AdminApi.new_applicationgroups(login, body=tags)
    print(f'Adding new Application Group. Output Is:{newtags}')

```
