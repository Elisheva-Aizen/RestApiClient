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
  
    def get_replay(self,serial): #api get request with serial
        try :
        response = requests.get(f"{self.base_url}/api/responses?serial={serial}")
        return response.json()
        except Exception as e:
        raise Exception(f"Error occurred while processing get request for serial {serial}:{str(e)}")
        
    def send_request(self,response_1,response_2): #api post request
        def get_data(): #get JSON data
            try:
            data = {
                "serial": 3,
                "message": {
                    "subset": {
                        "general": {
                            "information": {
                                "date": date(2021,2,1),
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
            except Exception as e:
            raise Exception(f"Error occurred while getting data for posting request: {str(e)}")
        get_data()    
        Try:
        response = requests.post(f"{self.base_url}/api/process", json=data)
        except Exception as e:
        raise Exception(f"Error occurred while processing post request: {str(e)}")
