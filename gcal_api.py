import os
import yaml
from googleapiclient import sample_tools
from datetime import timedelta
from config import SCOPES, USER_PREFERENCES_FILE, COLORS
from pytz import timezone


def event_start(event):
    if 'date' in event['start'].keys():
        return event['start']['date']
    else:
        return event['start']['dateTime']


def _create_service():
    return sample_tools.init('', 'calendar', 'v3', __doc__, __file__, scope=SCOPES)


class GoogleCalendarManager:
    def __init__(self, use_api=True):
        if use_api:
            self._service, self._flags = _create_service()
            self._calendars = self._get_calendars()['items']
        self._load_user_preferences()

    def _load_user_preferences(self):
        if os.path.exists(USER_PREFERENCES_FILE):
            with open(USER_PREFERENCES_FILE) as file:
                self._preferences = yaml.load(file, Loader=yaml.FullLoader)
        else:
            self._preferences = {
                'default_calendar': None,
                'default_duration': 60,
                'default_timezone': self._calendars[0]['timeZone']

            }

    def reload(self):
        self._load_user_preferences()

    def _save_user_preferences(self):
        with open(USER_PREFERENCES_FILE, 'w') as file:
            yaml.dump(self._preferences, file)

    def _set_user_preference(self, setting, value):
        self._preferences[setting] = value
        self._save_user_preferences()

    def reset_user_preferences(self):
        if os.path.exists('.gcaltools'):
            os.remove('.gcaltools')
            self.reload()
        else:
            print('WARNING: .gcaltools not found, nothing to delete!')

    def get_default_calendar(self):
        return self._preferences['default_calendar']

    def set_default_calendar(self, calendar_name):
        self._set_user_preference('default_calendar', calendar_name)

    def get_default_event_duration(self):
        return self._preferences['default_duration']

    def set_default_event_duration(self, duration):
        self._set_user_preference('default_duration', duration)

    def get_default_timezone(self):
        return self._preferences['default_timezone']

    def set_default_timezone(self, time_zone):
        self._set_user_preference('default_timezone', time_zone)

    def get_user_preferences(self):
        return self._preferences

    def _get_calendar_id(self, calendar_name):
        for cal in self._calendars:
            if cal['summary'] == calendar_name:
                return cal['id']
        else:
            return None

    def _get_calendars(self):
        return self._service.calendarList().list().execute()

    def calender_exists(self, calendar_name):
        return True if self._get_calendar_id(calendar_name) is not None else False

    def get_events(self, calendar_name, order_by=None, time_min=None, time_max=None, max_results=None):
        if time_max is not None:
            time_max = timezone(self.get_default_timezone()).localize(time_max + timedelta(days=1)).isoformat()
        if time_min is not None:
            time_min = timezone(self.get_default_timezone()).localize(time_min).isoformat()

        event_list = self._service.events().list(calendarId=self._get_calendar_id(calendar_name), orderBy=order_by, timeMin=time_min, timeMax=time_max, maxResults=max_results).execute()['items']
        return sorted(event_list, key=lambda e: event_start(e))

    def get_calendars(self, sort_by_summary=True):
        if sort_by_summary:
            return sorted(self._calendars, key=lambda c: c['summary'])
        else:
            return self._calendars

    def insert_event(self, calendar_name, title, start_date, start_time, duration=None, attendees=None, color_name=None):
        calendar_id = self._get_calendar_id(calendar_name)
        if duration is None:
            duration = self.get_default_event_duration()
        body_start_time = timezone(self.get_default_timezone()).localize(start_date + timedelta(hours=start_time.hour, minutes=start_time.minute))
        body_end_time = body_start_time + timedelta(minutes=duration)

        body = {
            'summary': title,
            'start': {'dateTime': body_start_time.isoformat(), 'timZone': self.get_default_timezone()},
            'end': {'dateTime': body_end_time.isoformat()},
        }

        if attendees is not None:
            body['attendees'] = [{'email': attendee} for attendee in attendees]

        if color_name is not None:
            body['colorId'] = COLORS[color_name]

        self._service.events().insert(calendarId=calendar_id, body=body).execute()


if __name__ == "__main__":
    pass
