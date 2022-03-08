#!/usr/bin/env python3
'''1. Where I am?'''
import requests


def sentientPlanets():
    '''method that returns the list of names of the home planets of all
       sentient species'''

    species = []
    planets = []
    url = 'https://swapi-api.hbtn.io/api/species/?format=json'

    while True:

        request = requests.get(url).json()
        species += request.get('results')
        next_page = request.get('next')
        if next_page:
            url = next_page
        else:
            break

    for specie in species:

        try:
            if specie.get('designation') == 'sentient' or\
                    specie.get('classification') == 'sentient':
                planet_url = specie.get('homeworld')
                if planet_url:
                    name = requests.get(planet_url).json().get('name')
                    planets.append(name)

        except Exception as e:
            print(e, specie.get('name'))
            continue

    return planets
