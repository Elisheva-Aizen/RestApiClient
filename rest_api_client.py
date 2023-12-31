import requests
from datetime import date

class RestAPIClient:
    def __init__(self,base_url):
        self._base_url= base_url

   @property
    def base_url(self):  #getter
        return self._base_url
 
   @base_url.setter
    def base_url(self, url):  #setter
        self._base_url=url
  
    def get_data(self,serial): #api get request with serial
        try :
            response = requests.get(f"{self.base_url}/api/responses?serial={serial}",timeout=30)
            response.raise_for_status() #raise an http error
            return response.json()
        except requests.exceptions.HTTPError as errh:
            raise Exception ("Get request http error:",str(errh))
        except requests.exceptions.RequestException as errr:
            raise Exception ("Error occured while processing get request:",str(errr))
        except Exception as err:
            raise Exception(str(err))
        
    def send_data(self,response_1,response_2): #api post request
        def get_json(): #get JSON data
            try:
                data = {
                    "serial": 3,
                    "message": {
                        "subset": {
                            "general": {
                                "information": {
                                    "date": "1-2-2021",
                                    "version": 3.00
                                },
                                "quantities": {
                                    "first": max(response_1["message"]["subset"]["general"]["quantities"]["first"],
                                                response_2["message"]["subset"]["general"]["quantities"]["first"]),
                                    "second": max(response_1["message"]["subset"]["general"]["quantities"]["second"],
                                                 response_2["message"]["subset"]["general"]["quantities"]["second"]),
                                    "third": max(response_1["message"]["subset"]["general"]["quantities"]["third"],
                                                response_2["message"]["subset"]["general"]["quantities"]["third"])
                                }
                            }
                        }
                    }
                }
                return data
            except Exception as err:
               raise Exception("Failed to get json data:",str(err))
        try:
            data=get_json()    
            response = requests.post(f"{self.base_url}/api/process", json=data,timeout=30)
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as errh:
            raise Exception ("Post request http error:",str(errh))
        except requests.exceptions.RequestException as errr:
            raise Exception ("Error occured while processing post request:" ,str(errr))
        except Exception as err:
               raise Exception(str(err))
