import argparse
from utils import today_date
from config import __VERSION


def cli_parser(calendar_manager):
    parser = argparse.ArgumentParser()
    sub_parser = parser.add_subparsers(dest='command')
    sub_parser_add(sub_parser, calendar_manager)
    sub_parser_list(sub_parser, calendar_manager)
    sub_parser_show(sub_parser, calendar_manager)
    sub_parser_default(sub_parser, calendar_manager)
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __VERSION)
    return parser


def sub_parser_add(sub_parser, calendar_manager):
    add_parser = sub_parser.add_parser('add', help="Add event to calendar")
    add_parser.add_argument('-c', '--calendar', type=str, help="Calendar name")
    add_parser.add_argument('title', type=str, help="Event title")
    add_parser.add_argument('start_date', type=str, help="Event start time, format: YYYY-MM-DD")
    add_parser.add_argument('start_time', type=str, help="Event start time, format: HH:MM")
    add_parser.add_argument('-d', '--duration', type=int, help="Event duration (minutes) default: " + str(calendar_manager.get_default_event_duration()), default=calendar_manager.get_default_event_duration())
    add_parser.add_argument('-a', '--attendees', type=str, help="List of emails of attendees", default="")


def sub_parser_list(sub_parser, calendar_manager):
    sub_parser.add_parser('list', help="Lists available calendars")


def sub_parser_show(sub_parser, calendar_manager):
    show_parser = sub_parser.add_parser('show', help="Displays calendar")
    display_group = show_parser.add_mutually_exclusive_group()
    display_group.add_argument('-w', action='store_true', help="Displays calendar for current week")
    display_group.add_argument('-m', action='store_true', help="Displays calendar for current month")
    show_parser.add_argument('-c', '--calendar', type=str, help="Calendar name")
    show_parser.add_argument('startDate', type=str, help="First date to search for events", default=today_date(), nargs="?")
    show_parser.add_argument('endDate', type=str, help="Last date to search for events", nargs="?")


def sub_parser_default(sub_parser, calendar_manager):
    default_parser = sub_parser.add_parser('default', help="Show user's default preferences")
    setting_group = default_parser.add_mutually_exclusive_group()
    setting_group.add_argument('-c', '--calendar', type=str, help="Set default calendar")
    setting_group.add_argument('-d', '--duration', type=int, help="Set default event duration")
    setting_group.add_argument('-r', '--reset', help="Erase .gcaltools file (resets all user preferences)", action="store_true")
    setting_group.add_argument('-t', '--timezone', type=str, help="Set default time zone (IANA format ie: \"Europe/Brussels\")")
