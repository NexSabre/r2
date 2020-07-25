from actions.action import Action
from actions.core.flask_server import FlaskServer
from configuration import Configuration


class ReplayAction(Action):
    ACTION = "replay"
    PARAM_NAME = "ACTION"

    def fill_parser_arguments(self):
        self.parser.add_argument("--package", help="Package name for the replay", type=str, nargs=1, default='default')

    def process_action(self, configuration):
        package = configuration.package

        Configuration(PACKAGE_NAME=package, MODE=1).save()
        FlaskServer(package=package, mode=1).serve()
