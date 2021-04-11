#  Google Calendar TOOLS
#
#  Google calendar management tool
#  author: sdejongh@he2b.be

from cli_parser import cli_parser
from gcal_api import GoogleCalendarManager
from printer import calendar_list_printer, events_printer
from datetime import datetime, timedelta
from config import DATE_FORMAT


# Add command
def command_add(command_args):
    raise NotImplementedError


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

    events_printer(calendar_manager.get_events(command_args.calendar, time_min=min_time, time_max=max_time, max_results=None))


# CLI command switch
cli_command_switch = {
    'add': command_add,
    'list': command_list,
    'show': command_show,
}


if __name__ == "__main__":
    # Configure command line argument parser
    parser = cli_parser()
    args = parser.parse_args()

    # Create Google Calendar Manager
    calendar_manager = GoogleCalendarManager()

    # Execute function for args.command
    cli_command_switch[args.command](args)
