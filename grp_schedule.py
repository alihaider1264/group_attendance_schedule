"""
Author: Ali Haider
Date: 08/07/2020

Output: Text file containing group schedule.
"""
from datetime import date
from datetime import timedelta
from datetime import datetime
import time
import logging as log
from pathlib import Path
import os
import sys

MWF = "MWF"
TR = "TR"
MODE1 = "A/B"
MODE2 = "A/B/C" 

def get_schedule(start, end, course, mode, meeting_days):
    day_names= ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat','Sun']
    day_count = (end - start).days + 1

    file_name = "schedule-"+course+".txt"
    f = open(file_name,"w")
    f.write(course+"\n"+mode+" "+meeting_days+"\n")
    if mode == MODE1:  f.write("Group 1\t\t\tGroup 2\n")
    elif mode == MODE2: f.write("Group 1\t\t\tGroup 2\t\t\tGroup 3\n")
    
    print_count = 0
    for single_date in (start + timedelta(n) for n in range(day_count)):
        #current_day = day_names[single_date.weekday()]
        current_day = single_date.weekday()
        if meeting_days == TR and mode == MODE1:
            if current_day == 1 or current_day == 3:
                f.write(str(day_names[single_date.weekday()]) + " " + str(single_date.strftime("%b %d %Y")) + "\t\t")
                if current_day == 3: f.write("\n")
        elif meeting_days == MWF and mode == MODE2:
            if current_day == 0 or current_day == 2 or current_day == 4:
                f.write(str(day_names[single_date.weekday()]) + " " + str(single_date.strftime("%b %d %Y")) + "\t\t")
                if current_day == 4: f.write("\n")
        elif meeting_days == TR and mode == MODE2:
            if current_day == 1 or current_day == 3:
                f.write(str(day_names[single_date.weekday()]) + " " + str(single_date.strftime("%b %d %Y")) + "\t\t")
                print_count += 1
                if print_count >= 3 : 
                    print_count = 0
                    f.write("\n")
        elif meeting_days == MWF and mode == MODE1:
            if current_day == 0 or current_day == 2 or current_day == 4:
                f.write(str(day_names[single_date.weekday()]) + " " + str(single_date.strftime("%b %d %Y")) + "\t\t")
                print_count += 1
                if print_count >= 2 : 
                    print_count = 0
                    f.write("\n")
    f.close()
    print("\n\nFile", file_name, "saved in the same folder as .py file.\n\n")


if __name__ == "__main__":
    course_start_date = date(2020,8,24) # Fall 2020 start date
    course_end_date = date(2020,12,18)  # Fall 2020 end date
    
    # CHANGE THE FOLLOWING THREE VARIABLES
    
    # MODE1 = "A/B" or MODE2 = "A/B/C"
    mode = MODE1
    
    # MWF or TR
    meeting_days = TR
    
    # UPDATE THIS WITH YOUR COURSE INFO
    course = "CSIT431-Fall2020"

    get_schedule(start=course_start_date, 
                            end=course_end_date,
                            course=course,
                            mode=mode,
                            meeting_days=meeting_days)