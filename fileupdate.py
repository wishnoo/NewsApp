import requests
import sys,os
import json
import datetime
import time

# Current utc time
date_value = datetime.datetime.utcnow()
i = 1
# diff_in_s = 11
# to assign a timedelta object we use the following statement
# diff_in_m = datetime.timedelta(minutes=2)
diff_in_m = 31
# text = "C:\\Users\\STEALTH\\Documents\\Python\\Newsapp\\text"
text = "text"
# datetime.timedelta object cannot be compared with int and only with datetime.timedelta object
# while diff_in_s > datetime.timedelta(seconds=10):

#------ for the first loop to run we give diff_in_m as 31 and then in every iteration diff_in_m is set
while diff_in_m > 30:

    top = open(os.path.join(text,"news.txt"), "w+")
    r = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=13ed18aed5aa424bb3afa52a4bfde4fe')
    data = r.json()
    top.write(json.dumps(data))
    top.close()

    #<------ write the data where category is business ------>
    business = open(os.path.join(text,"business.txt"),"w+")
    r = requests.get('https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=13ed18aed5aa424bb3afa52a4bfde4fe')
    data = r.json()
    business.write(json.dumps(data))
    business.close()

    #<------ write the data where category is science ------>
    science = open(os.path.join(text,"science.txt"),"w+")
    r = requests.get('https://newsapi.org/v2/top-headlines?country=us&category=science&apiKey=13ed18aed5aa424bb3afa52a4bfde4fe')
    data = r.json()
    science.write(json.dumps(data))
    science.close()

    #<------ write the data where category is health ------>
    health = open(os.path.join(text,"health.txt"),"w+")
    r = requests.get('https://newsapi.org/v2/top-headlines?country=us&category=health&apiKey=13ed18aed5aa424bb3afa52a4bfde4fe')
    data = r.json()
    health.write(json.dumps(data))
    health.close()

    #<------ write the data where category is sports ------>
    sports = open(os.path.join(text,"sports.txt"),"w+")
    r = requests.get('https://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey=13ed18aed5aa424bb3afa52a4bfde4fe')
    data = r.json()
    sports.write(json.dumps(data))
    sports.close()

    #<------ write the data where category is technology ------>
    technology = open(os.path.join(text,"technology.txt"),"w+")
    r = requests.get('https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=13ed18aed5aa424bb3afa52a4bfde4fe')
    data = r.json()
    technology.write(json.dumps(data))
    technology.close()

    #<------ Update time print ------>
    print("Updated on: ",datetime.datetime.now(),"- count:",i," !!!!")
    i+=1;
    date_value = datetime.datetime.utcnow()
    # time.sleep(11)
    # time.sleep(120)
    time.sleep(1860)
    temp = datetime.datetime.utcnow()
    diff = temp - date_value
    # diff_in_s = round(diff.total_seconds())
    diff_in_m = round((diff.total_seconds())/60.0)

    #print on screen
    if diff_in_m < 60:
        print ("diff:",diff_in_m,"minutes")
    elif diff_in_m == 60:
        print("diff:",diff_in_m/60,"hour")
    else:
        print("diff:",diff_in_m/60,"hours")
