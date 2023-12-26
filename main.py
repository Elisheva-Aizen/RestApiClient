from rest_api_client import RestAPIClient
import requests

def main():
  url="https://resttest10.herokuapp.com"
  
  #create an instace for RestAPIClient
  rest_api_client=RestAPIClient(url)
  
  ####Task_1####
  #get response for serial 1
  response_1=rest_api_client.get_data(1)
  print(response_1)
  #get response for serial 2
  response_2=rest_api_client.get_data(2)
  print(response_2)
  
  ####Task_2####
  #send posting request with the responses
  assert response_1 is not None and response_2 is not None,"response_1 or response_2 is None"
  try:
    response=rest_api_client.send_data(response_1,response_2)
    #check if posting is done successfully
    assert response.status_code=="200","Posting Request Failed"
    print ("correct")
  except Exception as err:
        raise Exception(err)
  
  if __name__ == "__main__":
    main()
