import requests
import time
import DBQueries
import DBConstants
import json
import Parser as ps


class JsonToData:
# date -> data no header
# ch -> charset
# length -> tamanho do ficheiro
    def __init__(self):
        headers = {
        'accept': 'application/json',
        }
        #api_url = "http://ucras.di.uminho.pt/v1/games/"
        #response = requests.get(api_url, headers=headers)
        #self.data = response.json()
        #self.headers = response.headers
        json_object = json.dumps(self.data)
        with open("sample.json", "w") as outfile: 
            outfile.write(json_object)
    
    @staticmethod
    def parse_header(header):
        date = header["Date"]
        _,charset = header["Content-Type"].split(';')
        _,ch = charset.split('=')
        length = header["Content-Length"]
        return date,ch,length

    def atualiza(self):
        while True: #Infinite loop
            #Execute the function
            headers = { 'accept': 'application/json',}
            api_url = "http://ucras.di.uminho.pt/v1/games/"
            response = requests.get(api_url, headers=headers)
            self.data = response.json()
            self.date,self.ch,self.length = JsonToData.parse_header(response.headers)
            time.sleep(600) #Wait 600s (10 min) before re-entering the cycle

    

#jds = JsonToData()