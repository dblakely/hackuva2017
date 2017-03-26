import pprint
import requests
from datetime import datetime
from collections import deque

APP_ID = '725737380921780'
SUPER_SECRET_KEY = 'c92312c38027f7c7af0a494e5e17def7'

ROOT = 'https://graph.facebook.com/'
ACCESS_TOKEN = '?access_token={}|{}'.format(APP_ID, SUPER_SECRET_KEY)

likes_url = lambda iid: ROOT + iid + '/likes' + ACCESS_TOKEN
events_url = lambda iid: ROOT + iid + '/events' + ACCESS_TOKEN

# print(likes_url("276409372373884"))
# print(events_url("276409372373884"))
#
# # print(requests.get(likes_url("276409372373884")).json())
# pprint.pprint(requests.get(events_url("276409372373884")).json()['data'])


class Scraper(object):
    def __init__(self, seed_id):
        self.queue = deque([seed_id])
        self.current_id = None

    def work(self):
        events = requests.get(events_url(self.current_id)).json()['data']
        for event in events:
            self.process_event(event)

        likes = requests.get(likes_url(self.current_id)).json()['data']
        for other_page_info in likes:
            if not other_page_info['id'] in self.queue:
                self.queue.append(str(other_page_info['id']))

    def advance(self):
        self.current_id = self.queue.popleft()

    def process_event(self, event):
        try:
            print("PROCESSED {}".format(event['name']))
            name = event['name']
            dt = event['start_time'] if event['start_time'][-1] == 'Z' else event['start_time'][:-5] + 'Z'

            location_name = ""
            try:
                location_name = event['place']['name']
            except KeyError:
                location_name = "Unknown"

            try:
                latitude = event['place']['location'].get('latitude') or "No"
                longitude = event['place']['location'].get('longitude') or "No"

                category = "Facebook"

                arguments = '?name={}&datetime={}&location_name={}&longitude={}&latitude={}&category={}'.format(
                    name, dt, location_name, longitude, latitude, category
                )
                url = 'http://localhost:8000/app/events/add' + arguments
                reps = requests.get(url).text

            except KeyError:
                print("Imma be that rebel!")
        except:
            print("Whoooooooo Weeeeeeeeeee; *waves cowboy hat while stratteling an unconditional try except*")




if __name__ == '__main__':
    print("I am become god, destroyer of worlds.")

    # QSU 276409372373884
    # UVA 12527153330

    scraper = Scraper('12527153330')

    while scraper.queue:
        scraper.advance()
        scraper.work()