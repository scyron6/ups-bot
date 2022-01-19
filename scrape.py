import requests
import json

from info import headers

def scrape_ups(tracking_number):

    data = '{"Locale":"en_US","TrackingNumber":[' + str(tracking_number) + ']}'

    response = requests.post('https://www.ups.com/track/api/Track/GetStatus', headers=headers, data=data)
    if (response.status_code != 200):
        return "Error"
    status = json.loads(response.text)
    if 'statusText' in status:
        status = status.get('statusText')

    return (status)