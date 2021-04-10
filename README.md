# GCALTOOLS
Google Calendar Python Command Line manager

## Dependencies
* google-api-python-client
* oauth2client

## Run
```
usage: gcaltools.py [-h] [-v] {add,list,show} ...

positional arguments:
  {add,list,show}
    add            Add event to calendar   /!\ NOT YET IMPLEMENTED
    list           Lists available calendars
    show           Displays calendar

optional arguments:
  -h, --help       show this help message and exit
  -v, --version    show program's version number and exit


````

## Actual state
- [x] Listing available calendars
- [x] Display current week events
- [x] Display current month events
- [x] Display events for given date
- [x] Display events for given period
- [ ] Create new event
- [ ] Search for events
- [ ] Check for overlapping events based on attendees list