#!/usr/bin/env python3
'''2. Rate me is you can!'''
import requests
import sys
import time


if __name__ == "__main__":

    url = sys.argv[1]
    request = requests.get(url)

    if request.status_code != 200:
        if request.status_code == 403:

            reset_time = int(request.headers.get('X-Ratelimit-Reset'))
            now = time.time()
            minutes = reset_time - now
            minutes = round(minutes / 60)

            print("Reset in {} min".format(minutes))
            exit()

    user = request.json()

    location = user.get('location')

    if location:
        print(user.get('location'))
    else:
        print("Not found")
