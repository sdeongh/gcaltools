import sys
from oauth2client import client
from googleapiclient import sample_tools

SCOPES = ['https://www.googleapis.com/auth/calendar.events', 'https://www.googleapis.com/auth/calendar', 'https://www.googleapis.com/auth/calendar.addons.execute']

def main(argv):
    print(argv)
    service, flags = sample_tools.init(argv, 'calendar', 'v3', __doc__, __file__, scope=SCOPES)
    try:
        calendar_list = service.calendarList().list().execute()
        for calendar_list_entry in calendar_list['items']:
            print(calendar_list_entry['summary'])

    except client.AccessTokenRefreshError:
        print('The credentials have been revoked or expired, please re-run'
              'the application to re-authorize.')

if __name__ == '__main__':
    main(sys.argv)
