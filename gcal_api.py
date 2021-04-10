from googleapiclient import sample_tools
from datetime import datetime, timedelta


def event_start(event):
    if 'date' in event['start'].keys():
        return event['start']['date']
    else:
        return event['start']['dateTime']


def _create_service():
    return sample_tools.init('', 'calendar', 'v3', __doc__, __file__, scope='https://www.googleapis.com/auth/calendar.events')


class GoogleCalendarManager:
    def __init__(self):
        self._service, self._flags = _create_service()
        self._calendars = self._get_calendars()['items']

    def _get_calendar_id(self, calendar_name):
        for cal in self._calendars:
            if cal['summary'] == calendar_name:
                return cal['id']
        else:
            return None

    def _get_calendars(self):
        return self._service.calendarList().list().execute()

    def get_events(self, calendar_name, order_by=None, time_min=None, time_max=None, max_results=None):
        if time_max is not None:
            time_max = (datetime.strptime(time_max, "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%dT00:00:00+00:00")
        if time_min is not None:
            time_min = datetime.strptime(time_min, "%Y-%m-%d").strftime("%Y-%m-%dT00:00:00+00:00")
        event_list = self._service.events().list(calendarId=self._get_calendar_id(calendar_name), orderBy=order_by, timeMin=time_min, timeMax=time_max, maxResults=max_results).execute()['items']
        return sorted(event_list, key=lambda e: event_start(e))

    def get_calendars(self):
        return self._calendars


if __name__ == "__main__":
    pass
