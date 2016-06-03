"""Module that picks a random message to send, then sends it through the configured setup."""

import random
import smtplib

MESSAGES = []


def init_messages():
    messages = []
    message_buffer = ""
    with open("orders.txt", "r") as order_file:
        for line in order_file.readlines():
            if len(line.lstrip()) > 0 and line.lstrip()[0] != "#":
                message_buffer += line
            elif len(line.lstrip()) == 0:
                messages.append(message_buffer[:])
                message_buffer = ""
    return messages


def choose_message(messages):
    all_messages = messages
    if len(messages) == 0:
        all_messages = init_messages()
    return random.sample(k=1, population=all_messages)[0]


def send_email(username, password, recipient, subject):
    server = smtplib.SMTP(host="smtp.gmail.com", port=587)
    server.ehlo()
    # check for errors in server
    server.starttls()
    server.login(user=username, password=password)
    server.sendmail(from_addr=username, to_addrs=[recipient], msg="""From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (username, recipient, subject, choose_message(MESSAGES)))
    server.close()
