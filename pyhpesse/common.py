# (C) Copyright 2019-2026 Hewlett Packard Enterprise Development LP.
# Apache License 2.0

import json
import requests
import urllib3,urllib
from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode

urllib3.disable_warnings()


class HPESecureServiceEdgeApiLogin:
    def __init__(
        self,
        api_token,
        url="https://admin-api.axissecurity.com",
        verify_ssl=True,
        timeout=30,
    ):
        """
        This is the class constructor for HPE Aruba Security Admin API.

        This constructor is required to be created before any modules can be used and must contain the following function arguments:

        Mandatory Parameters:
        api_token (string): API Token for API Service. 
        
        Optional Parameters:
        url (string): Website for API Services  - https://admin-api.axissecurity.com
        verify_ssl (boolean): Validate web service cerificate - True/False
        timeout: (int): Timeout for web request. Default is 30 seconds.


        """
        self.url = url
        self.api_token = api_token
        self.verify_ssl = verify_ssl
        self.timeout = timeout

    def _send_request(
        self, url, method, query="", content_response_type="application/json"
    ):
        """Sends a request to the Axis Admin API URL
        :query: must contain the json request if model required
        :url: must contain the /url (e.g. /oauth)
        :method: must contain the post or get request type of method
        :content_response_type: by default is set as Application/Json however can be changed by the method if required and functionality exists.
        :api_token optional[]: must contain the api_token for the calls.
        """
        full_url_path = self.url + url

        if len(self.api_token):
            header = {
                "Authorization": "Bearer " + self.api_token,
                "accept": content_response_type,
            }

            method = method.lower()
            if method not in {"post", "patch", "put", "get", "delete"}:
                raise RuntimeError(
                    "A valid method must be supplied before sending a request to the HPE SSE Admin API"
                )
            else:

                response = requests.request(
                    method=method.upper(),
                    url=full_url_path,
                    json=query,
                    headers=header,
                    verify=self.verify_ssl,
                    timeout=self.timeout,
                )
                if response.status_code == 403:
                    print(f"Error. Check your credentials or access level. Status Code: {response.status_code}")
                    
                
                if "json" in content_response_type:
                    try:
                        return response.json()
                    except json.decoder.JSONDecodeError:
                        
                        return response.text
                else:
                    return response.content
        else:
            print("Problem logging into HPE SSE Admin API. ")

def _remove_empty_keys(keys):
    remove_empty_values_from_dict = []
    for item in keys:
        if keys[item] == "":
            remove_empty_values_from_dict.append(item)
        else:
            pass
    for removal in remove_empty_values_from_dict:
        del keys[removal]
    return keys


def _generate_parameterised_url(url, parameters=""):
    parameters = _remove_empty_keys(keys=parameters)

    if len(parameters) == 0:
        return url
    else:
        for key, value in parameters.items():
            if isinstance(value, dict):
                parameters[key] = json.dumps(
                    value, separators=(",", ":"), ensure_ascii=False
                )

        encoded_url = urllib.parse.urlencode(parameters)
        final_url = url + "?" + encoded_url
        return final_url

def _generate_encoded_relative_url(urlPath):
   urlPath = urlPath.strip().strip('"')
   parts = urlsplit(urlPath)
   encodedQuery=urlencode(parse_qsl(parts.query,keep_blank_values=True))
   return urlunsplit(("","",parts.path,encodedQuery,parts.fragment))