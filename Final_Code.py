#---------------------------------------------------- IMPORTING MODULES [START] -------------------------------------------------

from tkinter import *
from pandastable import Table, config
import pandas as pd
from win10toast import ToastNotifier
import tkinter.messagebox
toast = ToastNotifier()
from pymongo.mongo_client import MongoClient 
from pymongo.server_api import ServerApi

#---------------------------------------------------- IMPORTING MODULES [END] ---------------------------------------------------

#---------------------------------------------------- CONNECTING TO DB [START] -------------------------------------------------- 

uri = "mongodb+srv://user:r8zss2LZINqg3Jb7@cluster0.nhvpwbz.mongodb.net/?retryWrites=true&w=majority" #r8zss2LZINqg3Jb7

# Create a new client and connect to the server 
myclient = MongoClient(uri, server_api=ServerApi('1'))   # I don't know what the server_api=ServerApi('1') is for, but is was given by the sample code by mongo db :/

# Send a ping to confirm a successful connection 
try: 
    myclient.admin.command('ping') 
    print("Pinged your deployment. You successfully connected to MongoDB!")    
    toast.show_toast(
    "Connection Successful",
    f"You have connected to Mongo DB successfully",
    duration = 20,
    threaded = True,) 
except Exception as error: 
    print(error)
    toast.show_toast(
    "Error",
    f"Looks like we had an error connecting to Mongo DB \n Error: {error}",
    duration = 20,
    threaded = True,)

#---------------------------------------------------- CONNECTING TO DB [END] ----------------------------------------------------

#------------------------------------------- CREATING A CLUSTER WITH TODAYS DATE [START] ----------------------------------------

from datetime import date,timedelta

mydb = myclient["TestDatabase"]                    # Name of the data base here is "TestDataBase"

today = str(date.today())                          #These three lines are used to get day of week
year,month,day = today.split('-')                  #These three lines are used to get day of week
day_name = date(int(year), int(month), int(day))   #These three lines are used to get day of week
if day_name.strftime("%A") == 'Saturday':          #There is no school on saturday....
    today=str(date.today() - timedelta(days=1))
elif day_name.strftime('%A') == 'Sunday':          #There is no school on sunday......
    today=str(date.today()-timedelta(days=2))

collist = mydb.list_collection_names()             #List of all dates in the DB


if today in collist:                               #Setting the target collection as todays date if it exists in list of all dates in the DB
    mycol = mydb[today]
else:                                              #Creating a target collection as todays date if it does not exist in list if all the dates in the DB
    mycol = mydb[today]
    mydict = { "_id": "Mathematics", "CW": "Complete" ,'HW' : '-',  'status' : False}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)
    mydict = { "_id": "Physics", "CW": "Complete" ,'HW' : '-',  'status' : False}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)
    mydict = { "_id": "Chemistry", "CW": "Complete" ,'HW' : '-',  'status' : False}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)
    mydict = { "_id": "Biology", "CW": "Complete" ,'HW' : '-',  'status' : False}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)
    mydict = { "_id": "Artificial Intelligence", "CW": "Complete" ,'HW' : '-',  'status' : False}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)
    mydict = { "_id": "History", "CW": "Complete" ,'HW' : '-',  'status' : False}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)
    mydict = { "_id": "Political Science", "CW": "Complete" ,'HW' : '-',  'status' : False}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)
    mydict = { "_id": "Geography", "CW": "Complete" ,'HW' : '-',  'status' : False}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)
    mydict = { "_id": "Economics", "CW": "Complete" ,'HW' : '-',  'status' : False}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)
    mydict = { "_id": "Hindi", "CW": "Complete" ,'HW' : '-',  'status' : False}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)
    mydict = { "_id": "English", "CW": "Complete" ,'HW' : '-',  'status' : False}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)
    mydict = { "_id": "Drawing", "CW": "Complete" ,'HW' : '-',  'status' : False}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)

#------------------------------------------- CREATING A CLUSTER WITH TODAYS DATE [END] ------------------------------------------

#------------------------------------  A FUNCTION TO SET HM AS True WHERE THERE IS NO HOMEWORK [START] --------------------------

def fixstatus(Database="TestDatabase"):
    mydb = myclient[Database]
    for collection in [mydb.list_collection_names()][0][-5:-1]:
        mycol = mydb[collection]
        def check(sub,part=None):
            query = {"_id": sub}
            user = mycol.find(query)
            Part = None
            for result in user:
                if part == None:
                    Part = result
                else:
                    Part = result[part]
            return Part
        def update(sub,part,value):
            result = check(sub)
            if result == None:
                return "no value put in"
            else:
                result[part] = value
                mycol.delete_one( { '_id':sub } )
                x = mycol.insert_one(result)
                return (x.inserted_id)
        subjectlist = ['Mathematics',
                       'Physics',
                       'Chemistry',
                       'Biology',
                       'Artificial Intelligence',
                       'History',
                       'Political Science',
                       'Geography',
                       'Economics',
                       'Hindi',
                       'English',
                       'Drawing']
        for subject in subjectlist:
            hw = check(subject,'HW')
            cw = check(subject,'CW')
            if hw == '-' and cw == 'Complete':
                update(subject,'status',True)
    tkinter.messagebox.showinfo("Fix",  "List of pending work has been updated successfully")

#------------------------------------  A FUNCTION TO SET HM AS True WHERE THERE IS NO HOMEWORK [END] ----------------------------

#-------------------------------------------------  A FUNCTION TO CHECK TODAYS WORK [START] -------------------------------------

def check(sub,part=None,col=mydb[today]):
    query = {"_id": sub}
    user = col.find(query)
    Part = None
    for result in user:
        if part == None:
            Part = result
        else:
            Part = result[part]
    return Part

#-------------------------------------------------  A FUNCTION TO CHECK TODAYS WORK [END] ---------------------------------------

#--------------------------------------------  A FUNCTION TO UPDATE ANYTHING IN ANY DATE [START] --------------------------------

def update(sub,part,value,col=mydb[today]):
    result = check(sub)
    if result == None:
        return "no value put in"
    else:
        result[part] = value
        col.delete_one( { '_id':sub } )
        x = col.insert_one(result)
        return (x.inserted_id)

#--------------------------------------------  A FUNCTION TO UPDATE ANYTHING IN ANY DATE [END] ----------------------------------

#---------------------------------------- GETTING ALL THE PENDING WORK BY SCANNING EACH DATE [START] ----------------------------

def windowpending(Database="TestDatabase"):
    pendinglist = []
    mydb = myclient[Database]
    for collection in [mydb.list_collection_names()][0]:
        mycol = mydb[collection]
        def check(sub,part=None):
            query = {"_id": sub}

            user = mycol.find(query)
            Part = None
            for result in user:
                if part == None:
                    Part = result
                else:
                    Part = result[part]
            return Part

        subjectlist = ['Mathematics',
                    'Physics',
                    'Chemistry',
                    'Biology',
                    'Artificial Intelligence',
                    'History',
                    'Political Science',
                    'Geography',
                    'Economics',
                    'Hindi',
                    'English',
                    'Drawing']
        for subject in subjectlist:
            checked = check(subject,'status')
            resulthw = check(subject,'HW')
            resultcw = check(subject,'CW')
            if checked == False or resultcw != 'Complete':
                pendinglist.append((collection,subject,resulthw,resultcw))
            elif checked == True and (collection,subject,resulthw,resultcw) in pendinglist:
                if resultcw == 'Complete':
                    pendinglist.remove((collection,subject,resulthw,resultcw))

    datelist=[]
    sublist=[]
    hwlist=[]
    cwlist=[]
    for tup in pendinglist:
        datelist.append(list(tup)[0])
        sublist.append(list(tup)[1])
        hwlist.append(list(tup)[2])
        cwlist.append(list(tup)[3])
       

    pendingdata = {'Date':datelist,
        'Subject':sublist,
        'HW':hwlist,
        'CW':cwlist}

#load data into a DataFrame object:
    global pendingdf
    pendingdf = pd.DataFrame(pendingdata)

#---------------------------------------- GETTING ALL THE PENDING WORK BY SCANNING EACH DATE [END] ------------------------------

#-------------------------------------------- FUNCTION TO CHECK A RANDOM DATE'S WORK [START] ------------------------------------

def checkwindow():
    checklist=[]
    subjectlist = ['Mathematics',
                   'Physics',
                   'Chemistry',
                   'Biology',
                   'Artificial Intelligence',
                   'History',
                   'Political Science',
                   'Geography',
                   'Economics',
                   'Hindi',
                   'English',
                   'Drawing']
    for subj in subjectlist:
        result = check(sub=subj,col=mydb[answercol])
        checklist.append(result)
    checklist=list(filter((None).__ne__, checklist))
    Tstatus=[]
    Tsublist=[]
    Thwlist=[]
    Tcwlist=[]
    for dic in checklist:
        Tstatus.append(dic['status'])
        Tsublist.append(dic['_id'])
        Thwlist.append(dic['HW'])
        Tcwlist=(dic['CW'])

    checkdata = {
                'Subject':Tsublist,
                'HW':Thwlist,
                'CW':Tcwlist,
                'status':Tstatus}
    global checkdf
    checkdf = pd.DataFrame(checkdata)
    return checkdf
#-------------------------------------------- FUNCTION TO CHECK A RANDOM DATE'S WORK [END] --------------------------------------

#------------------------------------------------- CHECKING TODAY'S WORK [START] ------------------------------------------------

todaylist=[]
subjectlist = ['Mathematics',
               'Physics',
               'Chemistry',
               'Biology',
               'Artificial Intelligence',
               'History',
               'Political Science',
               'Geography',
               'Economics',
               'Hindi',
               'English',
               'Drawing']
for subj in subjectlist:
    mycol = mydb[today]
    result = check(subj,col=mycol)
    todaylist.append(result)
Tstatus=[]
Tsublist=[]
Thwlist=[]
Tcwlist=[]
for dic in todaylist:
    Tstatus.append(dic['status'])
    Tsublist.append(dic['_id'])
    Thwlist.append(dic['HW'])
    Tcwlist=(dic['CW'])

todaydata = {
            'Subject':Tsublist,
            'HW':Thwlist,
            'CW':Tcwlist,
            'status':Tstatus}

todaydf = pd.DataFrame(todaydata)

#------------------------------------------------- CHECKING TODAY'S WORK [END] --------------------------------------------------

#------------------------------------------------------- GUI STUFF [START] ------------------------------------------------------

main = Tk()
main.title('Select Option')


def clicktoday():
    global pendingTestApp
    global ButtonCheck
    global ButtonFix
    global ButtonToday
    global ButtonPending
    global frame
    global main
    global e
    global answercol
    answercol=e.get()    
    main.destroy()

    main=Tk()
    class TodayTestApp(Frame):
        """Basic test frame for the table"""
        def __init__(self, parent=None):
            self.parent = parent
            Frame.__init__(self)
            self.main = self.master
            self.main.geometry('600x400+200+100')
            self.main.title('Today')
            f = Frame(self.main)
            f.pack(fill=BOTH,expand=1)
            self.table = pt = Table(f, dataframe=todaydf,
                                    showtoolbar=False, showstatusbar=True)
            pt.show()
            #set some options
            options = {'colheadercolor':'white','floatprecision': 5}
            config.apply_options(options, pt)
            pt.show()
            pt.redraw()
            return
    
    frame = LabelFrame(main,text='Enter the date in yyyy/mm/dd format to check it',padx=10,pady=10)
    frame.pack(padx=10,pady=10,side='top')
    ButtonToday = Button(main, text = 'Today', command=clicktoday,fg = 'blue')
    ButtonFix = Button(main, text = 'Fix', command=fixstatus,fg = 'black')
    ButtonFix.pack(side='bottom')
    ButtonPending = Button(main, text = 'Pending', command=clickpending,fg = 'red')
    ButtonCheck = Button(frame, text = 'Check', command=clickcheck,fg = 'green')
    e = Entry(frame,width=50)
    e.pack(side='top')
    ButtonToday.pack(side='left')
    ButtonPending.pack(side='right')
    ButtonCheck.pack(side='bottom')
    main.title('Select Option')
    todayapp = TodayTestApp()
    todayapp.mainloop()
    main.mainloop()


def clickpending():
    global pendingTestApp
    global ButtonCheck
    global ButtonFix
    global ButtonToday
    global ButtonPending
    global frame
    global main
    global e
    global answercol
    answercol=e.get()
    main.destroy()

    main=Tk()
    class pendingTestApp(Frame):
        """Basic test frame for the table"""
        def __init__(self, parent=None):
            self.parent = parent
            Frame.__init__(self)
            self.main = self.master
            self.main.geometry('600x400+200+100')
            self.main.title('Pending')
            f = Frame(self.main)
            f.pack(fill=BOTH,expand=1)
            windowpending()
            self.table = pt = Table(f, dataframe=pendingdf,
                                    showtoolbar=False, showstatusbar=True)
            pt.show()
            #set some options
            options = {'colheadercolor':'white','floatprecision': 5}
            config.apply_options(options, pt)
            pt.show()
            pt.redraw()
            return
    
    frame = LabelFrame(main,text='Enter the date in yyyy/mm/dd format to check it',padx=10,pady=10)
    frame.pack(padx=10,pady=10,side='top')
    ButtonToday = Button(main, text = 'Today', command=clicktoday,fg = 'blue')
    ButtonFix = Button(main, text = 'Fix', command=fixstatus,fg = 'black')
    ButtonFix.pack(side='bottom')
    ButtonPending = Button(main, text = 'Pending', command=clickpending,fg = 'red')
    ButtonCheck = Button(frame, text = 'Check', command=clickcheck,fg = 'green')
    e = Entry(frame,width=50)
    e.pack(side='top')
    ButtonToday.pack(side='left')
    ButtonPending.pack(side='right')
    ButtonCheck.pack(side='bottom')
    main.title('Select Option')
    pendingapp = pendingTestApp()
    pendingapp.mainloop()
    main.mainloop()


def clickcheck():
    global checkTestApp
    global ButtonCheck
    global ButtonFix
    global ButtonToday
    global ButtonPending
    global frame
    global main
    global e
    global answercol
    answercol=e.get()
    if answercol not in collist:
        answercol=today
        tkinter.messagebox.showinfo("Error",  "Please enter an appropriate date.\n \n (Try checking if you entered in right format)\n                                          OR\n (Maybe you entered a date not saved in the Database)\n\n We will provide you with today's data for now.")
    main.destroy()

    main=Tk()
    class checkTestApp(Frame):
        """Basic test frame for the table"""
        def __init__(self, parent=None):
            self.parent = parent
            Frame.__init__(self)
            self.main = self.master
            self.main.geometry('600x400+200+100')
            self.main.title('Check')
            f = Frame(self.main)
            f.pack(fill=BOTH,expand=1)
            checkwindow()
            self.table = pt = Table(f, dataframe=checkdf,
                                    showtoolbar=False, showstatusbar=True)
            pt.show()
            #set some options
            options = {'colheadercolor':'white','floatprecision': 5}
            config.apply_options(options, pt)
            pt.show()
            pt.redraw()
            return
    
    frame = LabelFrame(main,text='Enter the date in yyyy/mm/dd format to check it',padx=10,pady=10)
    frame.pack(padx=10,pady=10,side='top')
    ButtonToday = Button(main, text = 'Today', command=clicktoday,fg = 'blue')
    ButtonFix = Button(main, text = 'Fix', command=fixstatus,fg = 'black')
    ButtonFix.pack(side='bottom')
    ButtonPending = Button(main, text = 'Pending', command=clickpending,fg = 'red')
    ButtonCheck = Button(frame, text = 'Check', command=clickcheck,fg = 'green')
    e = Entry(frame,width=50)
    e.pack(side='top')
    ButtonToday.pack(side='left')
    ButtonPending.pack(side='right')
    ButtonCheck.pack(side='bottom')
    main.title('Select Option')
    checkapp = checkTestApp()
    checkapp.mainloop()
    main.mainloop()


frame = LabelFrame(main,text='Enter the date in yyyy/mm/dd format to check it',padx=10,pady=10)
frame.pack(padx=10,pady=10,side='top')
ButtonToday = Button(main, text = 'Today', command=clicktoday,fg = 'blue')
ButtonFix = Button(main, text = 'Fix', command=fixstatus,fg = 'black')
ButtonFix.pack(side='bottom')
ButtonPending = Button(main, text = 'Pending', command=clickpending,fg = 'red')
ButtonCheck = Button(frame, text = 'Check', command=clickcheck,fg = 'green')
e = Entry(frame,width=50)
e.pack(side='top')
ButtonToday.pack(side='left')
ButtonPending.pack(side='right')
ButtonCheck.pack(side='bottom')

main.mainloop()

#------------------------------------------------------- GUI STUFF [END] --------------------------------------------------------
