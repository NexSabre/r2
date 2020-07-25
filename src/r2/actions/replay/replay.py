from actions.action import Action


class ReplayAction(Action):
    ACTION = "replay"
    PARAM_NAME = "ACTION"

    def fill_parser_arguments(self):
        self.parser.add_argument("replay_filename", help="Filename of the replay", type=str, nargs=1)

    def process_action(self, configuration):
        pass
