#  Google Calendar TOOLS
#
#  Google calendar management tool
#  author: sdejongh@he2b.be

import os
from cli_parser import cli_parser
from gcal_api import GoogleCalendarManager
from printer import calendar_list_printer, events_printer, default_printer
from datetime import datetime, timedelta
from config import DATE_FORMAT


# Add command
def command_add(command_args):

    if command_args.calendar:
        active_calendar = command_args.calendar
    else:
        active_calendar = calendar_manager.get_default_calendar()
        if active_calendar is None:
            print('ERROR: default calendar not set')
            exit()

    if command_args.duration:
        duration = command_args.duration
    else:
        duration = calendar_manager.get_default_event_duration()

    if args.attendees:
        attendees = command_args.attendees
    else:
        attendees = None
    calendar_manager.insert_event(active_calendar, command_args.title, command_args.start_date, command_args.start_time, duration, attendees)


# List command
def command_list(command_args):
    calendar_list_printer(calendar_manager.get_calendars())


# Show command
def command_show(command_args):
    min_time = command_args.startDate

    # Display only one day if no end date is given
    if command_args.endDate is None:
        max_time = min_time
    else:
        max_time = command_args.endDate

    # Displays events for the current week
    if command_args.w:
        min_time = datetime.now() - timedelta(days=(datetime.now().weekday()))
        max_time = min_time + timedelta(days=6)
        min_time, max_time = min_time.strftime(DATE_FORMAT), max_time.strftime(DATE_FORMAT)

    # Displays events for the current month
    if command_args.m:
        min_time = datetime.now().replace(day=1)
        max_time = min_time.replace(month=min_time.month + 1) - timedelta(days=1)
        min_time, max_time = min_time.strftime(DATE_FORMAT), max_time.strftime(DATE_FORMAT)

    if command_args.calendar:
        active_calendar = command_args.calendar
    else:
        active_calendar = calendar_manager.get_default_calendar()
        if active_calendar is None:
            print('ERROR: default calendar not set')
            exit()

    events_printer(calendar_manager.get_events(active_calendar, time_min=min_time, time_max=max_time, max_results=None))


def command_default(command_args):
    if command_args.calendar:
        if calendar_manager.calender_exists(command_args.calendar):
            calendar_manager.set_default_calendar(command_args.calendar)
        else:
            print('ERROR: Calendar not found')
            exit()
    if command_args.duration:
        calendar_manager.set_default_event_duration(command_args.duration)

    if command_args.timezone:
        calendar_manager.set_default_timezone(command_args.timezone)

    if command_args.reset:
        if os.path.exists('.gcaltools'):
            os.remove('.gcaltools')
            calendar_manager.reload()
        else:
            print('WARNING: .gcaltools not found, nothing to delete!')

    default_printer(calendar_manager.get_user_preferences())


# CLI command switch
cli_command_switch = {
    'add': command_add,
    'list': command_list,
    'show': command_show,
    'default': command_default
}


if __name__ == "__main__":
    # Create Google Calendar Manager
    calendar_manager = GoogleCalendarManager()

    # Configure command line argument parser
    parser = cli_parser(calendar_manager)
    args = parser.parse_args()

    # Execute function for args.command
    cli_command_switch[args.command](args)
