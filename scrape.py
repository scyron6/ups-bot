import requests
import json

from info import headers

def scrape_ups(tracking_number):

    s = requests.Session()
    s.get('https://www.ups.com/track')

    headers['x-xsrf-token'] = s.cookies.get('X-XSRF-TOKEN-ST')

    data = '{"Locale":"en_US","TrackingNumber":[' + str(tracking_number) + ']}'
    response = s.post('https://www.ups.com/track/api/Track/GetStatus', headers=headers, data=data)

    if (response.status_code != 200):
        return "Error"

    status = json.loads(response.text)
    if 'statusText' in status:
        return(status.get('statusText'))
    else:
        return "Error"