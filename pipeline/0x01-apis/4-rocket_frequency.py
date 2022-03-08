#!/usr/bin/env python3
'''4. How many by rocket?'''
import requests
import time


if __name__ == "__main__":

    url = 'https://api.spacexdata.com/v4/launches'
    request = requests.get(url)
    launches_list = request.json()
    launches = {}

    for launch in launches_list:
        rocket_id = launch.get('rocket')
        rocket_url = 'https://api.spacexdata.com/v4/rockets/' + rocket_id
        r_rocket = requests.get(rocket_url)
        j_rocket = r_rocket.json()
        rocket_name = j_rocket.get('name')

        if rocket_name not in launches:
            launches.update({rocket_name: 1})
        else:
            launches[rocket_name] += 1

    for key, value in reversed(
            sorted(
                launches.items(),
                key=lambda key: key[1]
            )):
        print("{}: {}".format(key, value))
