# email-forwarder
A python script to forward Amazon emails

My family shares an Amazon Prime account. In order for each person to get the emails corresponding to their orders, I wrote this script to check for and forward emails.

### Setup
1. Install Redis and the Heroku command line tools
2. Create an .env file with the proper config variables
3. Run `heroku local worker` to run the worker
4. Run `python local_test.py` to queue a job
