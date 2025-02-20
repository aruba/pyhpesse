# pyhpesse
## HPE Aruba Networking Security Service Edge (SSE) SDK
This package has been developed in Python v3.9 to utilise the full functionality of the HPE Aruba Networking Security Service Edge (SSE) API environment. Each available REST API command is available for use in this module. All responses from HPE Aruba Networking Security Service Edge (SSE) API are in JSON format (converted into a Python dictionary object). Any changes  with the API are logged within the Audit Log.

This package has been uploaded to https://pypi.org/ and is also available to install via https://github.com/aruba/pyhpesse. 
These instructions will also available at https://developer.arubanetworks.com/ in due course.
Installation instructions and usage instructions are also provided below. 

## Available API Categories  
The following describes the available top level functionality of the HPE Aruba Networking Security Service Edge (SSE) SDK API available within this Python Package. 
- API Service - ApplicationGroups
- API Service - Applications
- API Service - Connectors
- API Service - ConnectorZones
- API Service - CustomIpCategory
- API Service - Groups
- API Service - IpFeedCategory
- API Service - Locations
- API Service - SslExclusions
- API Service - SubLocations
- API Service - Tunnels
- API Service - Users
- API Service - WebCategory

_This package comes without any warranties and should be used at your own risk._

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
login = HPESecureServiceEdgeApiLogin(api_token="your API Token","verify_ssl=False)
```

Find an API you want to use, by prefixing  `AdminApi.`  in your IDE and Intellisense will show the available APIs available. Each of the top level API category names are available as a module. 

The example below prints the status of the SSE Connectors. You must pass in the login variable to execute to function correctly.

```python
print(AdminApi.status_connectors(login)) 
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

# Further Usage Examples

## Make a new Tunnel
This script makes a new tunnel based on parameters below and if the location does not exist, it will create it.

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
```python
from pyhpesse import *

# Your API Key
#######################
apiSecretToken = "Your_Secret_Token"
#######################

# Delete Tunnel Parameters
#######################
tunnelToDelete = "YourNameToDelete"
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
