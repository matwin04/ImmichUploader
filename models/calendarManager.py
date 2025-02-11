from http.client import responses

import requests
from ics import Calendar, Event
from datetime import datetime,timedelta
class calendarManager:
    def __init__(self):
        self.events = []
        self.externalCalendarUrl = " "

    def addEvent(self,title,start,end,description=""):
        event = {
            "title": title,
            "start": datetime.strptime(start, "%Y-%m-%d %H:%M"),
            "end": datetime.strptime(end, "%Y-%m-%d %H:%M"),
            "description": description
        }
        self.events.append(event)
    def loadExternalCalendar(self,url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            calendar = Calendar(response.text)
            self.externalCalendarUrl = url
            for event in calendar.evnets:
                self.events.append({

                })
