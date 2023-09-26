import requests
from province import ProvinceList
import time
import json

class ProvinceScraper:
    
   
    def __init__(self) -> None:
       self.province = ProvinceList()
       self.result = []
       
       
    def get_data(self, province, country):
        
        url = f'https://nominatim.openstreetmap.org/search?q={province},{country}&format=geojson&polygon_geojson=1&addressdetails=1'
        
        
        data = None
        while True:
            try:
                data = requests.get(url)
                break
            
            except:
                pass
        
        
        return data.json() 
    
    def clean_data(self, data):
        
        cleaned_data = data['features'][0]
        
        return cleaned_data

    def save_results_to_json(self, filename):
        with open(filename, 'w') as json_file:
            json.dump(self.result, json_file, indent=4)

    def process_data(self, name, data):
        
        result = {
            name: data
        }
        
        return result
    
    def get_provinces(self):
        
        list = self.province.get_list()
        
        for item in list:
            data = self.get_data(item, 'philippines')
            cleaned_data = self.clean_data(data)
            processed_data = self.process_data(item, cleaned_data)
            
            print(item)
            
            self.result.append(processed_data)
            time.sleep(1)
            
            print(f'{item} DONE' )
            print()
        
        self.save_results_to_json('province_results.json')
        
    @staticmethod
    def main():
        
        scrape = ProvinceScraper()
        scrape.get_provinces()

if __name__ == '__main__':
    
    ProvinceScraper.main()
        
        
