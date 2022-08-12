import logging
from logging.handlers import TimedRotatingFileHandler

file_log = TimedRotatingFileHandler(
    filename='log/program.log', when='midnight', interval=1, backupCount=7)
stream_log = logging.StreamHandler()

logging.basicConfig(
    format=(
        '%(asctime)s - %(name)s - %(levelname)s - (%(filename)s)'
        '.%(funcName)s(%(lineno)d) - %(message)s'),
    handlers=(file_log, stream_log),
    level='DEBUG'
)

logger = logging
