"""Tells Windows scheduler to run app.py once a week.
TODO: get this to work with Linux too"""

import os
import sys
import app


os.system('schtasks /Create /SC HOURLY /TN WeeklyOrders /TR "%s %s"' % (sys.executable, app.__file__))
