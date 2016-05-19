import sys


class View:
    @staticmethod
    def output(data):
        [print(m) for m in data]

    @staticmethod
    def console_help():
        print("""
footballtable [option] [args]
options:
-a, --add <country> <team1> <team2> <team1 goals> <team2 goals> <date> <month> <year>
-t, --team= <team>
-h, --help""")

    @staticmethod
    def render_menu():
        """
        Write on screen menu
        :return null
        """
        print("""
- Space to view all matches
- e to exit
- s to search
- a to add""")
