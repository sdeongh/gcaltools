# General variables

__VERSION = "0.2"

default_args = {
    'new_event_duration': 210,
    'time_zone': 'Europe/Brussels'
}

# NEVER CHANGE THIS
SCOPES = ['https://www.googleapis.com/auth/calendar.events', 'https://www.googleapis.com/auth/calendar', 'https://www.googleapis.com/auth/calendar.addons.execute']
DATE_FORMAT = "%Y-%m-%d"
GCAL_DATE_FORMAT = "%Y-%m-%dT00:00:00+00:00"
