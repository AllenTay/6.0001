# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import re
from pytz import timezone
from soupsieve import select
import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

# MY OWN METHODftime 
def feeder(word):
    passer = str(word)
    part_one = ''
    for i in passer.lower():
        if i in string.punctuation:
            i = ' '
            part_one += i
        else:
            part_one += i

    part_two = ''
    for j in part_one.split():
        part_two += j + " "   

    return part_two

#======================
# Data structure design
#======================

# Problem 1

# TODO: NewsStory
class NewsStory(object):

    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate 

    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description 

    def get_link(self):
        return self.link

    def get_pubdate(self):
        return self.pubdate
        

#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError


# Problem 2
# TODO: PhraseTrigger
class PhraseTrigger(Trigger):
    
    def __init__(self, title):
        self.title = title

    def is_phrase_in(self, text):
        #Compare list to lists 
        box_one = feeder(self.title).split()
        box_two = feeder(text).split() #Box two is the broader bigger thing
        counter = len(box_one)
        ticker = False

        #First instance of purple in second
        if box_one[0] in box_two:
            nums = box_two.index(box_one[0])
            for i in range(counter):
                if box_two[nums] == box_one[i]:
                    counter -= 1
                if nums == len(box_two) - 1:
                    break
                nums += 1

        if counter == 0:
            ticker = True
    
        return ticker


    def evaluate(self, story):
        #Evaluate takes your core phrase and compares it to any statement you've been given 
        if PhraseTrigger.is_phrase_in(self, story) == True:
            return True
        else:
            return False
    
# Problem 3
# TODO: TitleTrigger
class TitleTrigger(PhraseTrigger):

    def __init__(self, title):
        PhraseTrigger.__init__(self, title)
        

    def evaluate(self, story):
        if PhraseTrigger.is_phrase_in(self, story.get_title()) == True:
            return True
        else:
            return False


# Problem 4
# TODO: DescriptionTrigger
class DescriptionTrigger(PhraseTrigger):

    def __init__(self, title):
        PhraseTrigger.__init__(self, title)
  

    def evaluate(self, story):
        if PhraseTrigger.is_phrase_in(self, story.get_description()) == True:
            return True
        else:
            return False


# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.

class TimeTrigger(Trigger):
    def __init__(self, time):
        date_str = time
        date = datetime.strptime(date_str, "%d %b %Y %H:%M:%S")
        date = date.replace(tzinfo=pytz.timezone("EST"))
        self.time = date
        
# Problem 6
# TODO: BeforeTrigger and AfterTrigger
class BeforeTrigger(TimeTrigger):

    def __init__(self, time):
        TimeTrigger.__init__(self, time)


    def evaluate(self, time):
        #Evaluate takes your core phrase and compares it to any statement you've been given 
        timer = time.get_pubdate()
        timer = timer.replace(tzinfo=pytz.timezone("EST"))
        
        if self.time > timer:
           return True
        else:
            return False
    

class AfterTrigger(TimeTrigger):

    def __init__(self, time):
        TimeTrigger.__init__(self, time)


    def evaluate(self, time):
        #Evaluate takes your core phrase and compares it to any statement you've been given 
        timer = time.get_pubdate()
        timer = timer.replace(tzinfo=pytz.timezone("EST"))

        if self.time < timer:
            return True
        else:
            return False

# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger
class NotTrigger(Trigger):
    def __init__(self, Trigger):
        self.Trigger = Trigger

    def evaluate(self, story):
        final = self.Trigger.evaluate(story)
        return not(final)
        
    
# Problem 8
# TODO: AndTrigger
class AndTrigger(Trigger):

    def __init__(self, Trigger1, Trigger2):
        self.Trigger1 = Trigger1
        self.Trigger2 = Trigger2
    
    def evaluate(self, story):
        final = self.Trigger1.evaluate(story) and self.Trigger2.evaluate(story)
        return final

# Problem 9
# TODO: OrTrigger

class OrTrigger(Trigger):

    def __init__(self, Trigger1, Trigger2):
        self.Trigger1 = Trigger1
        self.Trigger2 = Trigger2
    
    def evaluate(self, story):
        final = self.Trigger1.evaluate(story) or self.Trigger2.evaluate(story)
        return final


#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder
    # (we're just returning all the stories, with no filtering)
    version = []
    for i in stories:
        for j in triggerlist:
            if j.evaluate(i) == True:
                version.append(i)
    
    return version 

#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers
    second = []
    counter = {'TITLE':0, 'DESCRIPTION':0, 'AFTER':0, 'BEFORE':0, 'NOT':0, 'AND':0, 'OR':0}
    for i in lines:
        for j in counter.keys():
            if j in i:
                first = i.split(',')
                second.append(first)

    trigger_list = []
    name = ''
    for i in second:
        #Various types of triggers
        if i[1] == 'TITLE':
            name = i[0]
            name = TitleTrigger(i[2:])
            trigger_list.append(name)
        if i[1] == 'DESCRIPTION':
            name = i[0]
            name = DescriptionTrigger(i[2:])
            trigger_list.append(name)
        if i[1] == 'AFTER':
            name = i[0]
            name = AfterTrigger(str(i[2]))
            trigger_list.append(name)
        if i[1] == 'BEFORE':
            name = i[0]
            name = BeforeTrigger(str(i[2]))
            trigger_list.append(name)
        if i[1] == 'NOT':
            name = i[0]
            name = NotTrigger(i[2])
            trigger_list.append(name)
        if i[1] == 'AND':
            name = i[0]
            name = AndTrigger(i[2], i[3])
            trigger_list.append(name)
        if i[1] == 'OR':
            name = i[0]
            name = OrTrigger(i[2], i[3])
            trigger_list.append(name)

    return trigger_list
    #print(lines) # for now, print it so you see what it contains!



SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        #t1 = TitleTrigger("election")
        #t1,TITLE,Presidential Election
        #t2 = DescriptionTrigger("Trump")
        #t3 = DescriptionTrigger("Clinton")
        #t4 = AndTrigger(t2, t3)
        #triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            #stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

