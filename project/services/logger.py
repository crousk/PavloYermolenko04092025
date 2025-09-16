from logtail import LogtailHandler
import logging

source_token = "8G8mYATdJUPLTB9nf994yaic"
ingesting_host = "s1516019.eu-nbg-2.betterstackdata.com"

def get_logger():
    handler = LogtailHandler(
        source_token='$SOURCE_TOKEN',
        host='https://$INGESTING_HOST',
)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.handlers = []
    logger.addHandler(handler)
    return logger


logger = get_logger()