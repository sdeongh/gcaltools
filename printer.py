from datetime import datetime


def calendar_list_printer(calendar_list):
    print('')
    print("| {:<30}|{}".format('CALENDAR', 'ID'))
    print('+' + '-' * 31 + '+' + '-' * 31)
    for cal in calendar_list:
        print("| {:<30}| {}".format(cal['summary'], cal['id']))


def events_printer(event_list):
    print('')
    print("| {:<25} | {:<25} | {} ({})".format('Start Date', 'End Date', 'Title', 'Attendees'))
    print("+" + "-"*27 + "+" + "-"*27 + "+" + "-"*27)

    for e in event_list:
        if 'date' in e['start'].keys():
            start_date = datetime.fromisoformat(e['start']['date']).strftime('%a %d %b %Y (all day)')
            end_date = datetime.fromisoformat(e['end']['date']).strftime('%a %d %b %Y (all day)')
        else:
            start_date = datetime.fromisoformat(e['start']['dateTime']).strftime('%a %d %b %Y --- %H:%M')
            end_date = datetime.fromisoformat(e['end']['dateTime']).strftime('%a %d %b %Y --- %H:%M')
        event_string = "| {:<25} | {:<25} | {}".format(start_date, end_date, e['summary'],)

        if 'attendees' in e.keys():
            event_string += " - ({})".format(", ".join([att['email'] for att in e['attendees']]))

        print(event_string)
