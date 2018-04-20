# Application 3 - Website Blocker
# It is a simple program that runs in the background and doesnt let the user
# enter into destructive (productivity wise) websites during the working hours
# We have to pass the liks to the websites that we are not able to access

# it is quite tricky to implement this, although the program only takse about
# 30 lines of code

# 101 - Application Architeture
# host file in windows folder
# to block a website we have to redirect entries to the blocked website list to
# a local IP address, like the IP address for our computer.
# In windows the hosts file is located at: C:\Windows\System32\drivers\etc

# 102 - Setting Up the Script

# 106 - Schedule the Python on windows
# how to run the python code in the background everytime login in the computer
# Instead of execute the normal python.exe we use the pythonw.exe, by just changing
# the extension of the file to .pyw
# Then the file would run directly when clicked
# to run the file everytime the computer starts we need to go to task manager in
# windows and add the file as a task, marking the checkbox "run with highest privileges"
# Set to run on startup and uncheck the setting to run only in power cord

from datetime import datetime as dt
import time

# the 'r' prefix in the path name means that we are passing a real string, without
# special characters
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
temp_host = 'hosts'
IP_redirect = "127.0.0.1"
blocked_sites = ["www.facebook.com","facebook.com"]

# to execute this we need to open the comand prompt as administrator and do
# a cd to the project directory, or copy the app3.py file to other directory
# and make a change directory (cd) to that path

# the hosts file will be modified based on the time. So, for instance, we can
# add the blocked sites to the file in the workhours, lets say, from 8 to 18,
# and remove the sites from the file in the remaining hours of the day
while True:
    # executes a portion of code depending on the computer time
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        # to access the host file we need to run a cmd as administrator
        # execute the python script from a cmd runned as administrator
        # it is a good idea to have a backyp of the hosts file
        # also, for testing, we can copy the file to our project directory
        # so we don't need to run as an administrator while we are testing
        # our script

        # we need to check if the host file arleady has lines to block websites
        # so first we will open it in read plus (we can read and write) mode
        with open(hosts_path, 'r+') as h_file:
            content=h_file.read()
            # iterates through the website list
            for site in blocked_sites:
                # check if the site is already in the host file
                if site in content:
                    # doesn't do anything in case the site is already there
                    pass
                else:
                    h_file.write("{} {}\n".format(IP_redirect,site))
        print('Working hours!')
    else:
        # we need to remove the websites from the host file, because now we are
        # not in working hours anymore
        # we need to save the content in a variable, check the lines associated
        # with the websites from that variable and then rewrite the content into
        # the file without the lines that has the websites in it
        with open(hosts_path, 'r+') as h_file:
            content =  h_file.readlines()
            # the pointer for the line position in the file is now in the las line
            # so any appended content will go in the end of the file
            # we need to append to the begining and then use the truncate method
            # to delete everything below the pointer
            # to set the pointer to the begining of the file we can use seek:
            h_file.seek(0)
            # content was saved as a list, with an element for each line of the file
            for line in content:
                # checks if any site from the blocked_sites list is not in the line
                if not any(site in line for site in blocked_sites):
                    h_file.write(line)
            h_file.truncate()
        print('Party time!')
    # 5 seconds delay between loop iteration
    time.sleep(5)
