from actions.action import Action
from actions.core.flask_server import FlaskServer
from configuration import Configuration


class RecordAction(Action):
    ACTION = "record"
    PARAM_NAME = "ACTION"

    def fill_parser_arguments(self):
        self.parser.add_argument("target", help="Target service URI ", type=str, nargs=1)
        self.parser.add_argument("--package", help="Define a package name", type=str, nargs=1, default='default')
        self.parser.add_argument('-s', '--save', help="Save all incoming content the package folder", default=True)
        self.parser.add_argument('-o', '--overwrite', help="Overwrite all existing files in the package folder",
                                 default=False)

    def process_action(self, configuration):
        target = configuration.target[0]
        package = configuration.package

        Configuration(TARGET=target, PACKAGE_NAME=package, MODE=1).save()
        FlaskServer(target=target, package=package, save=configuration.save, overwrite=configuration.overwrite,
                    mode=0).serve()
