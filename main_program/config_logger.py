import os
import logging
from logging.handlers import TimedRotatingFileHandler

LOG_DIR_PATH = '../log'
LOG_FILE = f'{LOG_DIR_PATH}/program.log'

if not os.path.isdir(LOG_DIR_PATH):
    os.mkdir(LOG_DIR_PATH)

file_log = TimedRotatingFileHandler(
    filename=LOG_FILE, when='midnight', interval=1, backupCount=7)
stream_log = logging.StreamHandler()

logging.basicConfig(
    format=(
        '%(asctime)s - %(name)s - %(levelname)s - (%(filename)s)'
        '.%(funcName)s(%(lineno)d) - %(message)s'),
    handlers=(file_log, stream_log),
    level='DEBUG'
)

logger = logging.getLogger(__name__)
