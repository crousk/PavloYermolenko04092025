from logtail import LogtailHandler
import logging
import sys

SOURCE_TOKEN = 'RNfEsvTJQ5dZRADj3y5fphog'
HOST = "s1516021.eu-nbg-2.betterstackdata.com"


def get_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.handlers = []

    handler = LogtailHandler(
        source_token=SOURCE_TOKEN,
        host=f'https://{HOST}',
    )
    logger.addHandler(handler)

    stream_handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger


logger = get_logger()
