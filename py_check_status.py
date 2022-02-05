import requests
from requests.exceptions import HTTPError

try:
    response = requests.get('https://api.mcnulty.network/v1/zoom')
    response.raise_for_status()

    jsonResponse = response.json()
    in_meeting = jsonResponse["in_meeting"]

    if in_meeting:
    #    print("is in meeting")
       requests.get('http://0.0.0.0:5000/api/busy')
    else:
    #    print("not in meeting")
       requests.get('http://0.0.0.0:5000/api/available')


except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
