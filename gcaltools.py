#  Google Calendar TOOLS
#
#  Google calendar management tool
#  author: sdejongh@he2b.be

from cli_parser import cli_parser
from gcal_api import GoogleCalendarManager
from cli_command import CliCommand

if __name__ == "__main__":
    # Create Google Calendar Manager
    calendar_manager = GoogleCalendarManager()

    # Create CLI Commands Manager
    cli_commands = CliCommand(calendar_manager)

    # Configure command line argument parser
    parser = cli_parser()
    args = parser.parse_args()

    # Execute function for args.command
    cli_commands.execute_cmd(args.command, args)
