"""Front-end for do_work.py. Runs once by default."""
import os
import configparser
import do_work

CONFIG = configparser.ConfigParser()
CONFIG.read("config.txt")


def run_once():
    data_section = CONFIG["Data"]
    do_work.send_email(username=data_section["username"],
                       password=data_section["password"],
                       recipient=data_section["recipient"],
                       subject=data_section["subject"])


run_once()
os.system("pause")
