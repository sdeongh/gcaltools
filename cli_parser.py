import argparse
from utils import today_date
from config import __VERSION, default_args


def cli_parser():
    parser = argparse.ArgumentParser()
    sub_parser = parser.add_subparsers(dest='command')
    sub_parser_add(sub_parser)
    sub_parser_list(sub_parser)
    sub_parser_show(sub_parser)
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __VERSION)
    return parser


def sub_parser_add(sub_parser):
    add_parser = sub_parser.add_parser('add', help="Add event to calendar")
    add_parser.add_argument('calendar', type=str, help="Calendar name")
    add_parser.add_argument('title', type=str, help="Event title")
    add_parser.add_argument('start', type=str, help="Event start time, format: YYYYMMDD HH:MM")
    add_parser.add_argument('duration', type=int, help="Event duration (minutes) default: " + str(default_args['new_event_duration']), default=default_args['new_event_duration'])
    add_parser.add_argument('attendees', type=str, help="List of emails of attendees", default="")


def sub_parser_list(sub_parser):
    sub_parser.add_parser('list', help="Lists available calendars")


def sub_parser_show(sub_parser):
    list_parser = sub_parser.add_parser('show', help="Displays calendar")
    display_group = list_parser.add_mutually_exclusive_group()
    display_group.add_argument('-w', action='store_true', help="Displays calendar for current week")
    display_group.add_argument('-m', action='store_true', help="Displays calendar for current month")
    list_parser.add_argument('calendar', type=str, help="Calendar name")
    list_parser.add_argument('startDate', type=str, help="First date to search for events", default=today_date(), nargs="?")
    list_parser.add_argument('endDate', type=str, help="Last date to search for events", nargs="?")
