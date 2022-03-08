#!/usr/bin/env python3
'''3. What will be next?'''
import requests
import time


if __name__ == "__main__":

    url = 'https://api.spacexdata.com/v4/launches/upcoming'
    request = requests.get(url)
    launches_to_sort = request.json()
    sorting_dict = {}

    for i in range(len(launches_to_sort)):
        launch = launches_to_sort[i]
        if launch.get('date_unix') in sorting_dict:
            continue
        sorting_dict.update({launch.get('date_unix'): i})

    idx = sorting_dict[sorted(sorting_dict.keys())[0]]
    launch = launches_to_sort[idx]
    launch_name = launch.get('name')
    rocket_id = launch.get('rocket')
    date = launch.get('date_local')

    rocket_url = 'https://api.spacexdata.com/v4/rockets/' + rocket_id
    r_rocket = requests.get(rocket_url)
    rocket_name = r_rocket.json().get('name')
    launch_id = launch.get('launchpad')

    launchpad_url = 'https://api.spacexdata.com/v4/launchpads/' + launch_id
    r_launchpad = requests.get(launchpad_url)
    launchpad_name = r_launchpad.json().get('name')
    launchpad_locality = r_launchpad.json().get('locality')

    print("{} ({}) {} - {} ({})".format(launch_name,
                                        date,
                                        rocket_name,
                                        launchpad_name,
                                        launchpad_locality))
