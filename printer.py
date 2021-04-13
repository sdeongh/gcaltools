from datetime import datetime
from prettytable import PrettyTable


def calendar_list_printer(calendar_list):
    table = PrettyTable()
    table.field_names = ["Calendar Name", "Calendar ID"]
    for cal in calendar_list:
        table.add_row([cal['summary'], cal['id']])

    table.padding_width = 2
    table.align = "l"
    print(table)


def events_printer(event_list):
    table = PrettyTable()
    table.field_names = ["Start Date", "End Date", "Title", "Attendees"]

    for e in event_list:
        if 'date' in e['start'].keys():
            start_date = datetime.fromisoformat(e['start']['date']).strftime('%a %d %b %Y (all day)')
            end_date = datetime.fromisoformat(e['end']['date']).strftime('%a %d %b %Y (all day)')
        else:
            start_date = datetime.fromisoformat(e['start']['dateTime']).strftime('%a %d %b %Y --- %H:%M')
            end_date = datetime.fromisoformat(e['end']['dateTime']).strftime('%a %d %b %Y --- %H:%M')

        if "attendees" in e.keys():
            attendees_string = ", ".join([att['email'] for att in e['attendees']])
        else:
            attendees_string = "n/a"

        table.add_row([start_date, end_date, e['summary'], attendees_string])

    table.padding_width = 2
    table.align = "l"
    print(table)


def default_printer(user_preferences):
    table = PrettyTable()
    table.field_names = ["Setting", "Value"]

    for setting in sorted(user_preferences.keys()):
        table.add_row([setting, user_preferences[setting]])

    table.padding_width = 2
    table.align = "l"
    print(table)
