# GCALTOOLS
Google Calendar Python Command Line manager

## Dependencies
* google-api-python-client
* oauth2client
* pytz
* pyyaml
* prettytable
* xlsxwriter

## Run
```
usage: gcaltools.py [-h] [-v] {remoteauth,add,list,show,report,default} ...

positional arguments:
  {remoteauth,add,list,show,report,default}
    remoteauth          Google API Auth without local webserver.
    add                 Add event to calendar
    list                Lists available calendars
    show                Displays calendar
    report              Generates month occupation reports based on event attendees
    default             Show user's default preferences

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