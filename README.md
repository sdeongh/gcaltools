# GCALTOOLS
Google Calendar Python Command Line manager

## Dependencies
* prettytable 2.1.0
* PyYAML 5.4.1
* pytz 2020.1
* XlsxWriter 1.3.6
* oauth2client 4.1.3
* google-api-python-client 2.1.0

## Run
```
usage: gcaltools.py [-h] [-v] {remoteauth,add,list,show,report,default,summary} ...

positional arguments:
  {remoteauth,add,list,show,report,default,summary}
    remoteauth          Google API Auth without local webserver.
    add                 Add event to calendar
    list                Lists available calendars
    show                Displays calendar
    report              Generates month occupation reports based on event attendees
    default             Show user's default preferences
    summary             Display events summary for given calendar.

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit

````

## Actual state
- [x] Listing available calendars
- [x] Display current week events
- [x] Display current month events
- [x] Display events for given date
- [x] Display events for given period
- [x] Create new event
- [x] Store User preferences in YAML file 
- [ ] Search for events
- [ ] Check for overlapping events based on attendees list
- [ ] Add events template for faster creation
- [x] Generate monthly report based on event attendees (XLSX format)
- [ ] Generate monthly report based on event attendees (MarkDown format)
- [x] Display events summary for given calendar (events count, events with attendees, ...)