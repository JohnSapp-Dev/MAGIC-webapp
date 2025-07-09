import requests
import json
import pandas as pd
from json_class import Wait_time_object
from sqlalchemy_class import WaitTime



def get_wait_times(park_id):
    """
    get_post() is a function the creates a get request and calls an API defined by the url
    If successful the json text is returned

    """
    url = 'https://queue-times.com/parks/'+ str(park_id) +'/queue_times.json'

    try:
        response = requests.get(url)

        if response.status_code == 200:
            print("status code: ",response.status_code)
            response_json = json.loads(response.text)
            return response_json
        else:
            print('Error: ', response.status_code)
            return None
        
    except requests.exceptions.RequestException as e:
        print('Error: ',e)
        return None
    
def print_json(json_arr):
    for land in json_arr['lands']:
        print(f"\nLand: {land['name']} (ID; {land['id']})")

        if "rides" in land and len(land['rides']) > 0:
            for ride in land['rides']:
                print(f"Ride: {ride['name']} (Wait Time: {ride['wait_time']})")

def json_to_object(json_arr,park):
    ride_objects_list = []
    for land in json_arr['lands']:
        if "rides" in land and len(land['rides']) > 0:
            for ride in land['rides']:
               new_json_class = Wait_time_object(
                   ride['id'],
                   park,
                   land['name'],
                   ride['name'],
                   ride['is_open'],
                   ride['wait_time'],
                   ride['last_updated'])
               
               ride_objects_list.append(new_json_class)
    return ride_objects_list
    

def main():
    
    parks_dict = {
        'Magic Kingdom': 6,
        'EPCOT': 5,
        'Hollywood Studios' : 7,
        'Animal Kingdom' : 8
    }

    wait_time_data_dict = []
    for park in parks_dict:
        posts = get_wait_times(parks_dict[park])
        print("json text")
        """ print_json(posts) """
        

        json_object = json_to_object(posts,park)
        print("json Objects")
        for object in json_object:
            object.print()
            wait_time_data_dict.append({
            "ID": object.id,
            "Theme Park": object.theme_park,
            "Land": object.land,
            "Attraction": object.ride_name,
            "Is Open": object.is_open,
            "Wait Time": object.wait_time,
            "updated": object.updated
        })

    df = pd.DataFrame(wait_time_data_dict)
    WaitTime.data_to_mysql(df,'wait_times')
    

if __name__ == "__main__":
    main()