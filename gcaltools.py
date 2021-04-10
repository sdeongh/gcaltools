#  Google Calendar TOOLS
#
#  Google calendar management tool
#  author: sdejongh@he2b.be

from cli_parser import cli_parser
from gcal_api import GoogleCalendarManager
from printer import calendar_list_printer, events_printer
from datetime import datetime, timedelta


if __name__ == "__main__":

    # Configure command line argument parser
    parser = cli_parser()
    args = parser.parse_args()

    # Create Google Calendar Manager
    calendar_manager = GoogleCalendarManager()

    # Display list of all available calendars
    if args.command == 'list':
        calendar_list_printer(sorted(calendar_manager.get_calendars(), key=lambda calendar: calendar['summary']))

    # Displays list of events
    if args.command == 'show':
        minTime = args.startDate

        # Display only one day if no end date is given
        if args.endDate is None:
            maxTime = minTime
        else:
            maxTime = args.endDate

        # Displays events for the current week
        if args.w:
            minTime = datetime.now() - timedelta(days=(datetime.now().weekday()))
            maxTime = minTime + timedelta(days=6)
            minTime, maxTime = minTime.strftime("%Y-%m-%d"), maxTime.strftime("%Y-%m-%d")

        # Displays events for the current month
        if args.m:
            minTime = datetime.now().replace(day=1)
            maxTime = minTime.replace(month=minTime.month+1) - timedelta(days=1)
            minTime, maxTime = minTime.strftime("%Y-%m-%d"), maxTime.strftime("%Y-%m-%d")

        events_printer(calendar_manager.get_events(args.calendar, time_min=minTime, time_max=maxTime, max_results=None))
