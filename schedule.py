"""Tells Windows scheduler to run app.py once a week."""

import os
import sys
import app
import crontab

COMMAND = (sys.executable, app.__file__)


def register_windows():
    os.system('schtasks /Create /SC HOURLY /TN WeeklyOrders /TR "%s %s"' % COMMAND)


def register_unix():
    """Untested; probably shouldn't break anything, but might not work"""
    cron = crontab.CronTab(user=True)
    job = cron.new(command="%s %s" % COMMAND)
    job.week.every(1)


if sys.platform == "win32" or sys.platform == "cygwin":
    register_windows()
elif sys.platform == "linux": # someone with a mac, can you see if this works for "darwin"/OSX too?
    register_unix()
