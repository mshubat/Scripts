import webbrowser
import datetime
import time

'''
This script helps a stackoverflow user get the enthusiast
achievement of visiting the site for 30 consecutive days.

Requirements:
- Must have logged into site with cookies enabled before running.
'''


def updateachiever(visits):
    timestring = "times"
    daystring = "days"

    if (visits == 1):
        timestring = "time"
    elif (visits == 29):
        daystring = "day"

    print("------")
    print("You have visited stackoverflow {} {}. Only {} {} left."
          .format(visits, timestring, 30-visits, daystring))
    print("------")


def visitsite():
    visits = 0
    newday = True
    stored_day = datetime.datetime.now().timetuple().tm_yday

    while (visits < 30):
        if newday:
            webbrowser.open('http://www.stackoverflow.com/')
            visits += 1
            newday = False
            updateachiever(visits)

        time.sleep(1800)  # Sleep for 1800s = 1/2hr

        # Get the current day.
        currentday = datetime.datetime.now().timetuple().tm_yday

        # if the current day is different from stored day, then it is a new day
        if(stored_day != currentday):
            stored_day = currentday
            newday = True


if __name__ == "__main__":
    visitsite()
