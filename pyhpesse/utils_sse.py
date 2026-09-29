# (C) Copyright 2019-2026 Hewlett Packard Enterprise Development LP.
# Apache License 2.0

import json
from pyhpesse.common import (_generate_encoded_relative_url,_generate_parameterised_url,HPESecureServiceEdgeApiLogin)

class Utils_SSE():
    def get_token_from_file(fileName):
        """
        Use this function to store the token locally in a file which is located in the working directory of the script. 
        The file must use the following structure:
        {"access_token":"your_secret_token"}
        """
        try:
            f = open(fileName, "r")
            content = f.read()
            jsonContent = json.loads(content)
            if jsonContent['access_token']:
                return jsonContent['access_token']
            else:
                raise ValueError({"status":"Error", "message":"Missing Access Token."})
     
        except KeyError as e:
            raise Exception({"status":"Error", "Message":"Missing 'access_token' key name. Ensure key name exists as per the function usage details."})
        except json.JSONDecodeError as e:
            raise Exception({"status":"Error", "Message":"Ensure a valid json file as described in the function usage details."})
        except FileNotFoundError as e:  
            raise Exception({"status":"Error", "Message":"Ensure the token file '"+ fileName+"' exists. "+e.strerror})

        except Exception as e:
            raise Exception({"status":"Error", "Message":e})
    def customRequest(self,urlPath:(str),method:(str),body=None,pagenumber=0,pagesize=0): 
        """
                Operation: Execute a custom API request against the HPE SSE API
        
                Parameter Name: login, Required: Mandatory, Type: object, Description: Login Variable associated with self

                Parameter Name: urlPath, Required: Mandatory, Type: String, Description: Url with Path Parameters 

                Parameter Name: method, Required: Mandatory, Type: String, Description: Method type: post, put, get. delete

                Parameter Name: body, Required: Mandatory, Type: Object, Description: Body Parameters

                Parameter Name: pagenumber, Required: Optional, Type: integer, Description: Page number, required with a get request.

                Parameter Name: pagesize, Required: Optional, Type: integer, Description: Number of results returned per page number, required with a get request.

        """

        if method is None:
            raise ValueError("The 'method' parameter is mandatory and cannot be empty.")

        allowedMethods = {"post","put","get","delete"}
        if method not in allowedMethods:
            raise ValueError("The 'method' parameter must contain one of the following parameters 'post,put,get,delete'")
                
        if urlPath is None:
            raise ValueError("The 'urlPath' parameter is mandatory and cannot be empty.")

        if not isinstance(body, dict) and not body == None:
            raise TypeError("The 'body' parameter must be a dictionary if usage is required.")

        if method == "get":
            if pagenumber == 0 or pagesize == 0:
                raise ValueError("The 'pagenumber' parameter and 'pagenumber' is mandatory and cannot be empty.")
            dict_query ={'pagenumber': pagenumber, 'pagesize': pagesize}
            urlPath = _generate_parameterised_url(parameters=dict_query, url=urlPath)
            
        else:
            urlPath = _generate_encoded_relative_url(urlPath)

        if isinstance(body, dict):
            return HPESecureServiceEdgeApiLogin._send_request(self, url=urlPath, query=body, method=method)
        else:
            return HPESecureServiceEdgeApiLogin._send_request(self, url=urlPath, method=method)
