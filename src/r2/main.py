import logging

from r2.actions.action_dispatcher import ActionsDispatcher
from r2.helpers.constants import record_and_replay_ascii_logo
from r2.install import Installation


def main():
    print(record_and_replay_ascii_logo)

    install()
    start_logging()

    actions_dispatcher = ActionsDispatcher()
    actions_dispatcher.process_application()


def start_logging():
    logging.basicConfig(filename=f"{Installation.LOGS_DIR}/r2_custom")


def install():
    Installation()


if __name__ == '__main__':
    main()
