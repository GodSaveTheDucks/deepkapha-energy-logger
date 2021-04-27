import json
import requests
import datetime

class GetDataController(object):
    def __init__(self):
        self.urls = {
            'wind_farm_data': 'https://www.thecrownestate.co.uk/api/energy-map/wind-farm-data',}
    
    def generate_file_name(self):
        return str(datetime.datetime.now().timestamp())
        
    def execute(self,data_dir='data'):
        for filename, endpoint_url in self.urls.items():
            r = requests.get(endpoint_url)
            filename = ''.join([filename,generate_file_name()])
            with open(f'{data_dir}/{filename}.json', 'w') as fp:
                json.dump(r.json(), fp) 

controller = GetDataController()
controller.execute()