from printer import calendar_list_printer, default_printer, events_printer
from datetime import datetime, timedelta
from config import DATE_FORMAT


class CliCommand:
    def __init__(self, calendar_manager):
        self._calendar_manager = calendar_manager

    @property
    def calendar_manager(self):
        return self._calendar_manager

    # Execute CLI command
    def execute_cmd(self, cli_command, command_args):
        if cli_command == 'add':
            self._command_add(command_args)
        elif cli_command == 'default':
            self._command_default(command_args)
        elif cli_command == 'list':
            self._command_list()
        elif cli_command == 'show':
            self._command_show(command_args)
        else:
            pass

    # gcaltools ADD command
    def _command_add(self, command_args):
        if command_args.calendar:
            active_calendar = command_args.calendar
        else:
            active_calendar = self.calendar_manager.get_default_calendar()
            if active_calendar is None:
                print('ERROR: default calendar not set')
                exit()

        if command_args.duration:
            duration = command_args.duration
        else:
            duration = self.calendar_manager.get_default_event_duration()

        if command_args.attendees:
            attendees = command_args.attendees
        else:
            attendees = None

        if command_args.override_color:
            color_name = command_args.override_color
        else:
            color_name = None

        self.calendar_manager.insert_event(active_calendar, command_args.title, command_args.start_date, command_args.start_time, duration, attendees, color_name)

    # gcaltools LIST command
    def _command_list(self):
        calendar_list_printer(self.calendar_manager.get_calendars())

    # gcaltools SHOW command
    def _command_show(self, command_args):
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
            active_calendar = self.calendar_manager.get_default_calendar()
            if active_calendar is None:
                print('ERROR: default calendar not set')
                exit()

        events_printer(self.calendar_manager.get_events(active_calendar, time_min=min_time, time_max=max_time, max_results=None))

    def _command_default(self, command_args):
        if command_args.calendar:
            if self.calendar_manager.calender_exists(command_args.calendar):
                self.calendar_manager.set_default_calendar(command_args.calendar)
            else:
                print('ERROR: Calendar not found')
                exit()
        if command_args.duration:
            self.calendar_manager.set_default_event_duration(command_args.duration)

        if command_args.timezone:
            self.calendar_manager.set_default_timezone(command_args.timezone)

        if command_args.reset:
            self.calendar_manager.reset_user_preferences()

        default_printer(self.calendar_manager.get_user_preferences())
