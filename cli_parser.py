import argparse
import re
from datetime import datetime
from utils import today_date
from config import __VERSION, COLORS

email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')


def valid_date(date_string):
    try:
        return datetime.strptime(date_string, "%Y-%m-%d")
    except ValueError:
        msg = "Not a valid date: '{0}'. \nCorrect format is: YYYY-MM-DD".format(date_string)
        raise argparse.ArgumentTypeError(msg)


def valid_time(time_string):
    try:
        return datetime.strptime(time_string, "%H:%M")
    except ValueError:
        msg = "Not a valid time: '{0}'. \nCorrect format is: HH:MM".format(time_string)
        raise argparse.ArgumentTypeError(msg)


def valid_attendees(attendees_string):
    msg = "Not a attendees list: '{0}'. \nCorrect format is: user@email.com,user2@email.com".format(attendees_string)
    email_list = attendees_string.split(',')
    try:
        for email in email_list:
            if not email_pattern.match(email):
                raise argparse.ArgumentTypeError(msg)
        return email_list
    except ValueError:
        raise argparse.ArgumentTypeError(msg)


def cli_parser():
    parser = argparse.ArgumentParser()
    sub_parser = parser.add_subparsers(dest='command')
    sub_parser_auth(sub_parser)
    sub_parser_add(sub_parser)
    sub_parser_list(sub_parser)
    sub_parser_show(sub_parser)
    sub_parser_default(sub_parser)
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __VERSION)
    return parser


def sub_parser_auth(sub_parser):
    sub_parser.add_parser('remoteauth', help="Google API Auth without local webserver.")


def sub_parser_add(sub_parser):
    add_parser = sub_parser.add_parser('add', help="Add event to calendar")
    add_parser.add_argument('-c', '--calendar', type=str, help="Calendar name")
    add_parser.add_argument('title', type=str, help="Event title")
    add_parser.add_argument('start_date', type=valid_date, help="Event start time, format: YYYY-MM-DD")
    add_parser.add_argument('start_time', type=valid_time, help="Event start time, format: HH:MM")
    add_parser.add_argument('-d', '--duration', type=int, help="Event duration (minutes)")
    add_parser.add_argument('-a', '--attendees', type=valid_attendees, help="List of emails of attendees", required=False)
    add_parser.add_argument('-o', '--override-color', type=str, choices=[c for c in sorted(COLORS.keys())], help="List of emails of attendees", default="")


def sub_parser_list(sub_parser):
    sub_parser.add_parser('list', help="Lists available calendars")


def sub_parser_show(sub_parser):
    show_parser = sub_parser.add_parser('show', help="Displays calendar")
    display_group = show_parser.add_mutually_exclusive_group()
    display_group.add_argument('-w', action='store_true', help="Displays calendar for current week")
    display_group.add_argument('-m', action='store_true', help="Displays calendar for current month")
    show_parser.add_argument('-c', '--calendar', type=str, help="Calendar name")
    show_parser.add_argument('startDate', type=valid_date, help="First date to search for events", default=today_date(), nargs="?")
    show_parser.add_argument('endDate', type=valid_date, help="Last date to search for events", nargs="?")


def sub_parser_default(sub_parser):
    default_parser = sub_parser.add_parser('default', help="Show user's default preferences")
    setting_group = default_parser.add_mutually_exclusive_group()
    setting_group.add_argument('-c', '--calendar', type=str, help="Set default calendar")
    setting_group.add_argument('-d', '--duration', type=int, help="Set default event duration")
    setting_group.add_argument('-r', '--reset', help="Erase .gcaltools file (resets all user preferences)", action="store_true")
    setting_group.add_argument('-t', '--timezone', type=str, help="Set default time zone (IANA format ie: \"Europe/Brussels\")")
