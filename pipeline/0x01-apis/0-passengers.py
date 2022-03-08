#!/usr/bin/env python3
'''0. Can I join?'''
import requests


def availableShips(passengerCount):
    '''method that returns the list of ships that can hold a given number of
       passengers'''

    if passengerCount < 1:
        return []

    available_ships = []
    starships = []
    url = 'https://swapi-api.hbtn.io/api/starships/?format=json'

    while True:
        r = requests.get(url).json()
        starships += r.get('results')
        next_pag = r.get('next')
        if next_pag:
            url = next_pag
        else:
            break

    for ship in starships:
        try:
            if int(ship.get('passengers').replace(',', '')) >= passengerCount:
                available_ships.append(ship.get('name'))
        except Exception as e:
            continue

    return available_ships
