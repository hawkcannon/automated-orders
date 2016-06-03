# automated-orders
Python tool for sending orders to a given email address weekly.

# Setup
First, make sure you have Python 3 installed, from https://www.python.org/downloads/ .

Pull the repository down and save it to any folder.

Edit orders.txt to contain the messages you want sent, with each order separated by a blank line. Lines with a # at the beginning
 will be ignored, in case you want to comment it for some reason.
 
Edit config.txt with the Gmail username and password you want to send the emails from, as well as the recipient's email and the subject 
 you want for the emails. This is extremely insecure, so it would probably be best to create an account just for sending these emails 
 that you don't care if it gets hacked.
 
Allow SMTP access for Gmail following these instructions: https://support.google.com/accounts/answer/6010255

To run the job once, run app.py. To schedule the job to run every week, run schedule.py.
