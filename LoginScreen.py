import tkinter as tk #importing tkinter
from tkinter import *
import hashlib

class LoginScreen: #The login screen
    def __init__(self):
        self.window = tk.Tk()
        self.window.title = "Login"
        self.window.geometry("400x300+300+120")

        self.topFrame = tk.Frame(self.window)
        self.midFrame = tk.Frame(self.window)
        self.bottomFrame = tk.Frame(self.window)

        self.admEntry = tk.Entry(self.topFrame)
        self.admButton = tk.Button(self.topFrame, text="Login as Admin", command=self.authAdmin)
        self.admPass = tk.Entry(self.topFrame, show="*")

        self.admEntry.pack(side="left")
        self.admPass.pack(side="left")
        self.admButton.pack(side="left")

        self.docEntry = tk.Entry(self.midFrame)
        self.docPass = tk.Entry(self.midFrame, show="*")
        self.docButton = tk.Button(self.midFrame, text="Login as a doctor", command=self.authDoctor)

        self.docEntry.pack(side="left")
        self.docPass.pack(side="left")
        self.docButton.pack(side="left")
 

        self.patButton = tk.Button(self.bottomFrame, text="Patient View", command=self.callPatientWindow)

        self.patButton.pack()

        self.topFrame.pack()
        self.midFrame.pack()
        self.bottomFrame.pack()

        tk.mainloop()


    def authAdmin(self):
        user = self.admEntry.get() #getting the entry for first name and password
        passw = self.admPass.get()
        check = False
        
        if user != "" or passw != "":
            with open("admin.txt", "r") as file: #Opening the file as read only
                lines = file.readlines() #reading each line
                for line in lines:
                    splitline = line.split(",") #splitting up the entries
                    if splitline[1] == user and splitline[3] == passw: #if the users line up and the passwords line up
                        check = True  #check is true
            
                if check == True:
                    self.callAdminWindow() #If true load to admin screen
                else:
                    passbad = tk.Label(text = "Username or password is incorrect") #Displaying wrong password
                    passbad.pack()
            file.close()
        else:
            passblank = tk.Label(text="username and password cannot be blank") #Displaying if the user has left the boxes empty
            passblank.pack()
    
    def authDoctor(self):
        user = self.docEntry.get()
        passw = self.docPass.get()
        hashpassword = hashlib.md5(passw.encode()) #hashing the password
        hashedpassword = hashpassword.hexdigest()
        check = False

        if user != "" or passw != "":
            with open("doctor.txt", "r") as file: #Opening the file as read only
                lines = file.readlines() #reading each line
                for line in lines:
                    splitline = line.split(",") #splitting up the entries
                    if splitline[1] == user and splitline[3] == hashedpassword: #if the users line up and the passwords line up
                        check = True  #check is true
            
                if check == True:
                    self.callDoctorWindow() #If true load to admin screen
                else:
                    passbad = tk.Label(text = "Username or password is incorrect") #Displaying wrong password
                    passbad.pack()
            file.close()
        else:
            passblank = tk.Label(text="username and password cannot be blank")
            passblank.pack()


    def callAdminWindow(self): #deletes current window and calls adminwindow class to create a new window
        self.window.destroy()
        admin = AdminWindow()
    
    def callDoctorWindow(self): #calls the doctor window class
        self.window.destroy()
        doctor = DoctorWindow()

    def callPatientWindow(self): #calls the patient window class
        self.window.destroy()
        patient = PatientWindow()

class AdminWindow:#Admin view window
    def __init__(self):
        self.adminwindow = tk.Tk()
        self.adminwindow.title = "admin"
        self.label = tk.Label(text="ghsdigfb")
        self.adminwindow.geometry("600x500")

        self.oneFrame = tk.Frame(self.adminwindow)
        self.twoFrame = tk.Frame(self.adminwindow)
        self.threeFrame = tk.Frame(self.adminwindow)

        self.doctButton = tk.Button(text="Manage Doctors", command=self.callManageDWindow)
        self.patButton = tk.Button(text="Manage Patients", command=self.callManagePWindow)
        self.manButton = tk.Button(text="Generate management report", command=self.callManScreen)
        self.adminEn = tk.Label(self.oneFrame, text="Admin Username: ")
        self.adminE = tk.Entry(self.oneFrame)
        self.Passlabel = tk.Button(self.twoFrame, text="Change password", command=self.changePassword)
        self.PassEntry = tk.Entry(self.twoFrame, show="*")
        self.Passlabel.pack(side="left")
        self.adminEn.pack(side="left")
        self.adminE.pack(side="left")
        self.PassEntry.pack(side="left")

        self.AddressLabel = tk.Button(self.threeFrame, text="Change Address", command=self.changeAddress)
        self.AddressEntry = tk.Entry(self.threeFrame)
        self.AddressLabel.pack(side="left")
        self.AddressEntry.pack(side="left")

        self.backButton = tk.Button(text="Back", command=self.callLoginScreen)
        
        self.doctButton.pack()
        self.patButton.pack()
        self.manButton.pack()
        self.oneFrame.pack()
        self.twoFrame.pack()
        self.threeFrame.pack()
        self.backButton.pack()

    def changePassword(self):
        Password = self.PassEntry.get() 
        name = self.adminE.get()
        passcheck = self.authPass()
        if passcheck == True:
            Array = "" #Empty string
            file = open('admin.txt', 'r') #opening the file in read only
            throughlines = file.readlines() #reading each line one at a time
            for i in throughlines:
                trial = i.split(",") #splitting between entries
                if trial[1] != name: #If the ID isn't the same as the entered one
                    Array += i #write the line to the string
                else: #if the ID's match
                    newline = (trial[0]+","+name+","+trial[2]+","+Password+","+trial[4]+",\n") #writing in the new data
                    Array += newline
            file.close() #closing file
            file = open('admin.txt', 'w')#opening the file in write only
            file.write(Array) #writing over the data in the array
            file.close()

    def changeAddress(self):
        Address = self.AddressEntry.get() 
        name = self.adminE.get()
        
        Array = "" #Empty string
        file = open('admin.txt', 'r') #opening the file in read only
        throughlines = file.readlines() #reading each line one at a time
        for i in throughlines:
            trial = i.split(",") #splitting between entries
            if trial[1] != name: #If the ID isn't the same as the entered one
                Array += i #write the line to the string
            else: #if the ID's match
                newline = (trial[0]+","+name+","+trial[2]+","+trial[3]+","+Address+",\n") #writing in the new data
                Array += newline
        file.close() #closing file
        file = open('admin.txt', 'w')#opening the file in write only
        file.write(Array) #writing over the data in the array
        file.close()

    def authPass(self): 
        password = self.PassEntry.get() #Getting the password entry
        auth = False
        symbols = ["!", "@", "(", "(", "*"] #A list of available symbols to use
        if len(password) > 8 or len(password) < 17: #keeping the password 9-16 characters
            Cap = False
            Low = False
            Sym = False 
            num = False
            for i in password:
                try:
                    number = int(i) #if the character can be int() without raising an error it's a number
                    num = True
                except ValueError: #if there's an error
                    if i.isalpha(): #if it's alphabetical
                        if i == i.upper(): #checking if it's upper case
                            Cap = True
                        if i == i.lower(): #checking if it's lower case
                            Low = True
                    else: #if not alphabetical the check for symbols
                        if i in symbols:
                            Sym = True #loop through the array of symbols
            if Cap == True and Low == True and Sym == True and num == True:
                auth = True
            else: 
                autherror = tk.Label(text="Make sure there is at least on capital and lowercase letter, a number and a symbol")
                autherror.pack()
        else:
            length = tk.Label(text="Password not long enough")
            length.pack()
        return auth    



    def callManagePWindow(self): #Calling the manage patient window
        self.adminwindow.destroy()
        ManageP = ManagePWindow()

    def callManageDWindow(self): #Calling the manage doctor window
        self.adminwindow.destroy()
        ManageD = ManageDWindow()
    
    def callLoginScreen(self):
        self.adminwindow.destroy()
        LScreen = LoginScreen()

    def callManScreen(self):
        self.adminwindow.destroy()
        mScreen = manReport()

class manReport:
    def __init__(self):
        self.Manwindow = tk.Tk()
        self.Manwindow.title = "Doctor View"
        self.Manwindow.geometry("400x300+300+120")

        self.Manage = tk.Button(self.Manwindow, text="Generate management report", command=self.actualGen)
        self.Manage.pack()

    def CountDocs(self):
        count = 0
        file = open("doctor.txt", 'r') #Opening the file in read only
        line = file.readlines() #Reading through each line
        for l in line:
            splitlines = l.split(",") #splitting up each part of the database
            if len(splitlines) > 2: #if the line has more than just the number
                count+=1
        file.close()
        return count
    
    def countPats(self):
        list = ""
        Name = ""
        file = open('doctor.txt', 'r') #opens doctor file
        fileline = file.readlines()
        for line in fileline:
            count = 0
            splits = line.split(",") #iterates through each line and splits up entries
            if splits[1] != "\n": #if doctor hasn't been deleted
                Name = splits[1]+" "+splits[2] #writes the doctors name
                if splits[4] != "\n":
                    patients = splits[4] #List of patients
                    moresplit = patients.split(";") 
                    count = len(moresplit) -1
                list += Name+":"+str(count)+"\n" #making list
        return list

    def countApps(self):
        listD = "" 
        file = open('doctor.txt', 'r') #opens doctor file
        fline = file.readlines()
        for line in fline: #splits through lines
            count = 0
            lines = line.split(",")
            if lines[1] != "\n": #if the doctor hasn't been deleted
                docId = lines[0]
                docName = lines[1]+" "+lines[2] #getting doctor name and id
                appFile = open('appointment.txt', 'r') #opening appointment file
                appline = appFile.readlines()
                for l in appline:
                    newline = l.split(",")#splitting through
                    if str(newline[3]) == str(docId):#If the doctor ID is the same
                        count += 1 #adjust the counter
                listD += docName+ ": "+str(count)+"\n" #add the amount to the list
        return listD

    def actualGen(self):
        Doctors = self.CountDocs() #calls the three other functions
        Patients = self.countPats()
        Appointments = self.countApps()

        DocLabel = tk.Label(self.Manwindow, text="Number of Doctors: "+ str(Doctors)) #printing out each one
        NumofPat = tk.Label(self.Manwindow, text="Number of patients per doctor")
        PatLabel = tk.Label(self.Manwindow, text=Patients)
        NumofApps = tk.Label(self.Manwindow, text="Number of appointments per doctor")
        AppLabel = tk.Label(self.Manwindow, text=Appointments)

        DocLabel.pack()
        NumofPat.pack()
        PatLabel.pack()
        NumofApps.pack()
        AppLabel.pack()



class DoctorWindow:
    def __init__(self):
        self.Docwindow = tk.Tk()
        self.Docwindow.title = "Doctor View"
        self.Docwindow.geometry("400x300+300+120")

        self.oneFrame = tk.Frame(self.Docwindow)
        self.twoFrame = tk.Frame(self.Docwindow)
        self.threeFrame = tk.Frame(self.Docwindow)

        self.PatientName = tk.Label(self.oneFrame, text="First and Last name//Doctor ID")
        self.PatientEntry = tk.Entry(self.oneFrame)
        self.PatientLast = tk.Entry(self.oneFrame)

        self.PatientName.pack(side="left")
        self.PatientEntry.pack(side="left")
        self.PatientLast.pack(side="left")

        self.viewOne = tk.Button(self.twoFrame, text="View specific record", command=self.Viewpatient)
        self.viewappoint = tk.Button(self.twoFrame, text="Upcoming appointments", command=self.ViewDAppointments)

        self.viewOne.pack(side="left")
        self.viewappoint.pack(side="left")

        self.oneFrame.pack()
        self.twoFrame.pack()
        self.threeFrame.pack()

    def Viewpatient(self):
        firstName = self.PatientEntry.get() #taking the patients first and last name
        lastName = self.PatientLast.get()

        file = open('patient.txt', 'r') #opening patient file
        fileLine = file.readlines()
        PatientFile = ""
        for line in fileLine:
            splitLine = line.split(",") #splitting each entry
            if splitLine[2] == firstName and splitLine[3] == lastName and splitLine[11] != "Yes":
                for i in splitLine:
                    if i != splitLine[4]: #not printing password
                        
                        PatientFile += i + " " #printing out patient informations
        view = tk.Label(self.threeFrame, text=PatientFile)
        view.pack()
        file.close()

    def ViewDAppointments(self):
        allApoint = ""
        DocID = self.PatientEntry.get() #getting patient entry
        file = open('appointment.txt', 'r') #opening appointment file
        lines = file.readlines()
        for line in lines:
            IndLine = line.split(",")
            if int(IndLine[3]) == int(DocID): #if the entry is the doctor id
                allApoint += line + "\n" #adding to the string
        Apponit = tk.Label(self.threeFrame, text=allApoint) #printing the string
        Apponit.pack()


class ManageDWindow:
    def __init__(self):

        self.Managedwindow = tk.Tk()
        self.Managedwindow.title = "Manage Doctors"
        self.label = tk.Label(text="ghsdigfb")
        self.Managedwindow.geometry("600x500")

        self.oneFrame = tk.Frame(self.Managedwindow)
        self.twoFrame = tk.Frame(self.Managedwindow)
        self.threeFrame = tk.Frame(self.Managedwindow)
        self.fourFrame = tk.Frame(self.Managedwindow)
        self.fiveFrame = tk.Frame(self.Managedwindow)
        self.sixFrame = tk.Frame(self.Managedwindow)
        self.sevenFrame = tk.Frame(self.Managedwindow)

        self.ManageLabel = tk.Label(self.oneFrame, text="Manage Doctors")

        self.ManageLabel.pack()

        self.IDLabel = tk.Label(self.twoFrame, text="Doctor ID: ")
        self.IDEntry = tk.Entry(self.twoFrame)

        self.IDLabel.pack(side="left")
        self.IDEntry.pack(side="left")

        self.firstLabel = tk.Label(self.threeFrame, text = "Doctor's first name: ")
        self.firstEntry = tk.Entry(self.threeFrame)

        self.firstLabel.pack(side="left")
        self.firstEntry.pack(side="left")

        self.lastLabel = tk.Label(self.fourFrame, text = "Doctor's last name: ")
        self.lastEntry= tk.Entry(self.fourFrame)

        self.lastLabel.pack(side="left")
        self.lastEntry.pack(side="left")

        self.passLabel = tk.Label(self.fiveFrame, text = "Doctor's Password (only for updates or changes): ")
        self.passEntry = tk.Entry(self.fiveFrame, show="*")

        self.passLabel.pack(side="left")
        self.passEntry.pack(side="left")

        self.manDButton = tk.Button(self.sixFrame, text="Register new doctor", command=self.addDoctor)
        self.countDButton = tk.Button(self.sixFrame, text="Number of Doctors", command=self.countDoctors)
        self.searchDButton = tk.Button(self.sixFrame, text="Search for a Doctor", command=self.searchDoctors)
       
        self.manDButton.pack(side="left")
        self.countDButton.pack(side="left")
        self.searchDButton.pack(side="left")
        

        self.updateDButton = tk.Button(self.sevenFrame, text="Update", command=self.updateDoctor)
        self.deleteDButton = tk.Button(self.sevenFrame, text="Delete", command=self.deleteDoctor)
        self.backButton = tk.Button(self.sevenFrame, text="Back", command=self.callAdminWindow)
        

        self.updateDButton.pack(side="left")
        self.deleteDButton.pack(side="left")
        self.backButton.pack(side="left")

        self.oneFrame.pack()
        self.twoFrame.pack()
        self.threeFrame.pack()
        self.fourFrame.pack()
        self.fiveFrame.pack()
        self.sixFrame.pack()
        self.sevenFrame.pack()

        tk.mainloop()
    
    def callAdminWindow(self):
        self.Managedwindow.destroy()
        adminWindow = AdminWindow()

    
    def addDoctor(self): #Code to add a doctor
        doctor = []
        file = open('doctor.txt', 'r') #opening doctor file
        numberlines = len(file.readlines()) + 1 #reading the current amount of lines then adding one
        file.close()
        firstName = self.firstEntry.get() #getting first and last name, and password
        lastName = self.lastEntry.get()
        password = self.passEntry.get()
        hashpassword = hashlib.md5(password.encode()) #hashing the password
        hashedpassword = hashpassword.hexdigest() #making it readable into hex
        check = self.authPass() #calling the function to make sure the password is strong enough
        if check == True: #if it passes that check
            doctor.append({'doctor_id': numberlines, 'first_name': firstName, 'last_name': lastName, 'doctor_pass': hashedpassword}) 
            self.appendFile(doctor) #running the append function
        else:
            wrongPass = tk.Label(text="Unsuitable password") #printing if the password is unsuitable
            wrongPass.pack(side="left")

    def appendFile(self,doctor): #Function to append the file with a new entry
        file = open('doctor.txt', 'a') #Opens file in append mode
    
        for i in doctor: #For loop to loop through each doctor in the file
            string = "{doctor_id},{first_name},{last_name},{doctor_pass},\n".format(**i) #Formatting the input

            file.write(string) #Writing to the file
        file.close()
    
    def updateDoctor(self):
        ID = self.IDEntry.get() #getting each entry needed
        first = self.firstEntry.get()
        last = self.lastEntry.get()
        passw = self.passEntry.get()
        hashpassword = hashlib.md5(passw.encode()) #hashing the password
        hashedpassword = hashpassword.hexdigest() #making it readable into hex
        passcheck = self.authPass()
        if passcheck == True:
            Array = "" #Empty string
            file = open('doctor.txt', 'r') #opening the file in read only
            throughlines = file.readlines() #reading each line one at a time
            for i in throughlines:
                trial = i.split(",") #splitting between entries
                if trial[0] != ID: #If the ID isn't the same as the entered one
                    Array += i #write the line to the string
                else: #if the ID's match
                    newline = (ID+","+first+","+last+","+hashedpassword+",\n") #writing in the new data
                    Array += newline
            file.close() #closing file
            file = open('doctor.txt', 'w')#opening the file in write only
            file.write(Array) #writing over the data in the array
            file.close()
    
    def deleteDoctor(self):
        ID = self.IDEntry.get() #getting id 
        Array = "" #Empty string
        file = open('doctor.txt', 'r') #opening file in readonly
        throughlines = file.readlines()
        for i in throughlines: #looping through lines
            trial = i.split(",") #splitting up each entry
            if trial[0] != ID: #if the ID doesn't match
                Array += i #print into the array
            else:
                newline = (ID+",\n")# overwriting the line that needs to be deleted
                Array += newline
        file.close() 
        file = open('doctor.txt', 'w') #write to text file
        file.write(Array)

    def countDoctors(self): #Function to count the doctors in the list
        count = 0
        file = open("doctor.txt", 'r') #Opening the file in read only
        line = file.readlines() #Reading through each line
        for l in line:
            splitlines = l.split(",") #splitting up each part of the database
            if len(splitlines) > 2: #if the line has more than just the number
                count+=1
        countlabel = tk.Label(text = "Number of current doctors: " + str(count)) #Printing the number of doctors to the screen
        countlabel.pack()
        file.close()

    def searchDoctors(self): #Function to search a doctor by ID number
        found = False #So far the entry hasn't been found
        deleted = False #To check for any deleted entries
        doctor=""
        count = 0
        search = self.IDEntry.get() #Getting the ID number
        if search != "":
            with open("doctor.txt", "r") as file: #Opening the file as read only
                lines = file.readlines() #reading each line
                for line in lines:
                    look = line.split(",") #splitting between entries
                    if look[0] == search and look[1] != "\n": #If the ID number is there and it isn't a blank entry
                        found = True
                        break #breaking out of the for loop
                    elif look[0] == search and look[1] == "\n": #If the ID is there but it's an empty entry
                        deleted = True
                if found == True: #If the entry has been found
                    
                    for j in look:
                         #making sure the password won't be printed out along with the rest of the data
                        if j != look[3]:
                
                            doctor += j + " "
                            
                        
                    doctorsearch = tk.Label(text=doctor) #printing the entry
                    doctorsearch.pack()
                elif deleted == True: #If the data was empty showing the user has been deleted
                    searchNotFound = tk.Label(text="This user has been deleted")
                    searchNotFound.pack()
                else:
                    searchNotFound = tk.Label(text="Doctor not found")
                    searchNotFound.pack()
            file.close()

    def authPass(self): 
        password = self.passEntry.get() #Getting the password entry
        auth = False
        symbols = ["!", "@", "(", "(", "*"] #A list of available symbols to use
        if len(password) > 8 or len(password) < 17: #keeping the password 9-16 characters
            Cap = False
            Low = False
            Sym = False 
            num = False
            for i in password:
                try:
                    number = int(i) #if the character can be int() without raising an error it's a number
                    num = True
                except ValueError: #if there's an error
                    if i.isalpha(): #if it's alphabetical
                        if i == i.upper(): #checking if it's upper case
                            Cap = True
                        if i == i.lower(): #checking if it's lower case
                            Low = True
                    else: #if not alphabetical the check for symbols
                        if i in symbols:
                            Sym = True #loop through the array of symbols
            if Cap == True and Low == True and Sym == True and num == True:
                auth = True
            else: 
                autherror = tk.Label(text="Make sure there is at least on capital and lowercase letter, a number and a symbol")
                autherror.pack()
        else:
            length = tk.Label(text="Password not long enough")
            length.pack()
        return auth    

class PatientWindow:
    def __init__(self):
        self.patientwindow = tk.Tk()
        self.patientwindow.title = "Patient view"
        self.patientwindow.geometry("600x500")

        self.oneFrame = tk.Frame(self.patientwindow)
        self.twoFrame = tk.Frame(self.patientwindow)
        self.threeFrame = tk.Frame(self.patientwindow)
        self.fourFrame = tk.Frame(self.patientwindow)
        self.fiveFrame = tk.Frame(self.patientwindow)
        self.sixFrame = tk.Frame(self.patientwindow)
        self.sevenFrame = tk.Frame(self.patientwindow)
        self.eightFrame = tk.Frame(self.patientwindow)
        self.nineFrame = tk.Frame(self.patientwindow)
        self.tenFrame = tk.Frame(self.patientwindow)
        self.elevenFrame = tk.Frame(self.patientwindow)
        self.twelveFrame = tk.Frame(self.patientwindow)

        self.LoginLabel = tk.Label(self.oneFrame, text="Current Patients Login")
        self.LoginLabel.pack()

        self.FirstLabel = tk.Label(self.twoFrame, text="Firstname          ")
        self.LastLabel = tk.Label(self.twoFrame, text="             Lastname             ")
        self.PassLabel = tk.Label(self.twoFrame, text="          Password")

        self.FirstLabel.pack(side="left")
        self.LastLabel.pack(side="left")
        self.PassLabel.pack(side="left")

        self.FirstEntry = tk.Entry(self.threeFrame)
        self.LastEntry = tk.Entry(self.threeFrame)
        self.PassEntry = tk.Entry(self.threeFrame, show="*")

        self.FirstEntry.pack(side="left")
        self.LastEntry.pack(side="left")
        self.PassEntry.pack(side="left")

        self.loginButton = tk.Button(self.fourFrame, text="Login", command=self.authPatients)
        self.loginButton.pack()

        self.separation = tk.Label(self.fiveFrame, text="===================================================================================")
        self.separation.pack()

        self.RegisterLabel = tk.Label(self.sixFrame, text="Request to Enroll")
        self.RegisterLabel.pack()

        self.FirstRLabel = tk.Label(self.sevenFrame, text="Firstname           ")
        self.LastRLabel = tk.Label(self.sevenFrame, text="           Lastname           ")
        self.PassRLabel = tk.Label(self.sevenFrame, text="           Password     ")
        self.DOBRLabel = tk.Label(self.sevenFrame, text="        Date of Birth (dd/mm/yyyy)")

        self.FirstRLabel.pack(side="left")
        self.LastRLabel.pack(side="left")
        self.PassRLabel.pack(side="left")
        self.DOBRLabel.pack(side="left")

        self.FirstREntry = tk.Entry(self.eightFrame)
        self.LastREntry = tk.Entry(self.eightFrame)
        self.PassREntry = tk.Entry(self.eightFrame, show="*")
        self.DOBREntry = tk.Entry(self.eightFrame)

        self.FirstREntry.pack(side="left")
        self.LastREntry.pack(side="left")
        self.PassREntry.pack(side="left")
        self.DOBREntry.pack(side="left")

        self.phoneLabel = tk.Label(self.nineFrame, text="Phone number")
        self.AddressLabel = tk.Label(self.nineFrame, text="         Address (separated by ;)")

        self.phoneLabel.pack(side="left")
        self.AddressLabel.pack(side="left")

        self.phoneEntry = tk.Entry(self.tenFrame)
        self.addressEntry = tk.Entry(self.tenFrame)

        self.phoneEntry.pack(side="left")
        self.addressEntry.pack(side="left")

        self.registerButton = tk.Button(self.elevenFrame, text="Request", command=self.addPatient)
        self.registerButton.pack()

        self.backButton = tk.Button(self.twelveFrame, text="Back", command=self.callLoginScreen)
        self.backButton.pack()

        self.oneFrame.pack()
        self.twoFrame.pack()
        self.threeFrame.pack()
        self.fourFrame.pack()
        self.fiveFrame.pack()
        self.sixFrame.pack()
        self.sevenFrame.pack()
        self.eightFrame.pack()
        self.nineFrame.pack()
        self.tenFrame.pack()     
        self.elevenFrame.pack() 
        self.twelveFrame.pack()                 

    def callLoginScreen(self):
        self.patientwindow.destroy()
        lScreen = LoginScreen()

    def addPatient(self): #adding a patient
        patient = []
        file = open('patient.txt', 'r') #opening patient file
        numberlines = len(file.readlines()) + 1 #reading the current amount of lines then adding one
        file.close()
        firstName = self.FirstREntry.get() #getting data
        lastName = self.LastREntry.get()
        password = self.PassREntry.get()
        DOB = self.DOBREntry.get()
        phone = self.phoneEntry.get()
        address = self.addressEntry.get()
        doctorid = 0 #doctor id as 0 until assigned one by an admin
        pending = 'pending' #pending until approved by admin
        symptoms = 'N/A' #added by doctors
        diagnoses = 'N/A' #added by doctors
        Treated = 'No'

        hashpassword = hashlib.md5(password.encode()) #hashing the password
        hashedpassword = hashpassword.hexdigest() #making it readable into hex
        check = self.authPass() #calling the function to make sure the password is strong enough
        if check == True: #if it passes that check
            patient.append({'patient_id': numberlines, 'doctor_id': doctorid, 'first_name': firstName, 'last_name': lastName, 'patient_pass': hashedpassword, 'DOB': DOB, 'Phone_number': phone, 'Address': address,'symptoms':symptoms, 'diagnoses':diagnoses, 'request': pending, 'treated': Treated}) 
            self.appendFile(patient) #running the append function
        else:
            wrongPass = tk.Label(text="Unsuitable password") #printing if the password is unsuitable
            wrongPass.pack(side="left")
    
    def appendFile(self,patient): #Function to append the file with a new entry
        file = open('patient.txt', 'a') #Opens file in append mode
    
        for i in patient: #For loop to loop through each doctor in the file
            string = "{patient_id},{doctor_id},{first_name},{last_name},{patient_pass},{DOB},{Phone_number},{Address},{symptoms},{diagnoses},{request},{treated},\n".format(**i) #Formatting the input

            file.write(string) #Writing to the file
        file.close()

    def authPass(self): 
        password = self.PassREntry.get() #Getting the password entry
        auth = False
        symbols = ["!", "@", "(", "(", "*"] #A list of available symbols to use
        if len(password) > 8 or len(password) < 17: #keeping the password 9-16 characters
            Cap = False
            Low = False
            Sym = False 
            num = False
            for i in password:
                try:
                    number = int(i) #if the character can be int() without raising an error it's a number
                    num = True
                except ValueError: #if there's an error
                    if i.isalpha(): #if it's alphabetical
                        if i == i.upper(): #checking if it's upper case
                            Cap = True
                        if i == i.lower(): #checking if it's lower case
                            Low = True
                    else: #if not alphabetical the check for symbols
                        if i in symbols:
                            Sym = True #loop through the array of symbols
            if Cap == True and Low == True and Sym == True and num == True:
                auth = True
            else: 
                autherror = tk.Label(text="Make sure there is at least on capital and lowercase letter, a number and a symbol")
                autherror.pack()
        else:
            length = tk.Label(text="Password not long enough")
            length.pack()
        return auth  

    def callRegisterwindow(self): 
        self.UploadAppoint() #calling the function
        self.patientwindow.destroy() #destroying window
        register = RegisterdPWindow() #calling the next class

    def UploadAppoint(self):
        appoint = []
        file = open('appointment.txt', 'r') #opening appointment file
        numberlines = len(file.readlines()) +1 #counting how many lines there are
        file.close()
        firstName = self.FirstEntry.get()
        lastName = self.LastEntry.get()
        appoint.append({'appoint_id':numberlines, 'first_name':firstName, 'last_name':lastName }) #assigning variable to update file with
        self.appendOther(appoint)
        file.close()

    def appendOther(self, appoint):
        file = open('appointment.txt', 'a') #appending the appointment
        for i in appoint:
            string = "{appoint_id}, {first_name}, {last_name},\n".format(**i) #information from function above
            file.write(string)
        file.close()
    
    def authPatients(self):
        user = self.FirstEntry.get() #getting the entry for first name and password
        lastuser = self.LastEntry.get()
        passw = self.PassEntry.get()
        check = False
        hashpassword = hashlib.md5(passw.encode()) #hashing the password
        hashedpassword = hashpassword.hexdigest() #making it readable into hex
        
        if user != "" or passw != "" or lastuser != "":
            with open("patient.txt", "r") as file: #Opening the file as read only
                lines = file.readlines() #reading each line
                for line in lines:
                    splitline = line.split(",") #splitting up the entries
                    if splitline[2] == user and splitline[4] == hashedpassword and splitline[3] == lastuser and splitline[10] == "approved": #if the users line up and the passwords line up
                        check = True  #check is true
                    elif splitline[10] == 'pending':
                        pendingcheck = tk.Label(text="Your request hasn't been approved, wait for a phone call")
                if check == True:
                    self.callRegisterwindow() #If true load to admin screen
                else:
                    passbad = tk.Label(text = "Username or password is incorrect") #Displaying wrong password
                    passbad.pack()
            file.close()
        else:
            passblank = tk.Label(text="username and password cannot be blank")
            passblank.pack()


class RegisterdPWindow:
    def __init__(self):
        self.registeredWindow = tk.Tk()
        self.registeredWindow.title = "Registered patient"
        self.registeredWindow.geometry = ("400x300+300+120")

        self.oneFrame = tk.Frame(self.registeredWindow)
        self.twoFrame = tk.Frame(self.registeredWindow)
        self.threeFrame = tk.Frame(self.registeredWindow)
        self.fourFrame = tk.Frame(self.registeredWindow)
        self.fiveFrame = tk.Frame(self.registeredWindow)
        self.sixFrame = tk.Frame(self.registeredWindow)
        self.sevenFrame = tk.Frame(self.registeredWindow)
        self.eightFrame = tk.Frame(self.registeredWindow)
        self.nineFrame = tk.Frame(self.registeredWindow)

        self.title = tk.Label(text="Book an appointment")
        self.title.pack()

        self.dayv = StringVar(self.registeredWindow)
        self.dayoptions = self.day()
        self.dayv.set(self.dayoptions[0])
        self.days = OptionMenu(self.twoFrame, self.dayv, *self.dayoptions)
        self.days.pack(side="left")

        self.monthv = StringVar(self.registeredWindow)
        self.monthoptions = self.month()
        self.monthv.set(self.monthoptions[0])
        self.months = OptionMenu(self.twoFrame, self.monthv, *self.monthoptions)
        self.months.pack(side="left")

        self.yearv = StringVar(self.registeredWindow)
        self.yearoptions = self.year()
        self.yearv.set(self.yearoptions[0])
        self.years = OptionMenu(self.twoFrame, self.yearv, *self.yearoptions)
        self.years.pack(side="left")

        self.timev = StringVar(self.registeredWindow)
        self.timeoptions = self.time()
        self.timev.set(self.timeoptions[0])
        self.times = OptionMenu(self.threeFrame, self.timev, *self.timeoptions)
        self.times.pack(side="left")

        self.apply = tk.Button(self.threeFrame, text="Apply", command=self.addAppointment)
        self.apply.pack(side="left")

        self.spacer = tk.Label(self.fourFrame, text="=================================================================")
        self.spacer.pack()

        self.check = tk.Button(self.fiveFrame, text="check", command=self.viewDoctor)
        self.check.pack(side="left")
        self.viewappoint = tk.Button(self.sixFrame, text="View pending and approved appointments", command=self.viewAppointments)
        self.viewappoint.pack(side="left")

        self.end = tk.Label(self.sevenFrame, text="Pending")
        self.end.pack()

        self.appr = tk.Label(self.eightFrame, text="Approved: ")
        self.appr.pack()

        self.backagain = tk.Button(self.nineFrame, text="Back", command=self.callPatientWindow)
        self.backagain.pack()

        self.oneFrame.pack()
        self.twoFrame.pack()
        self.threeFrame.pack()
        self.fourFrame.pack()
        self.fiveFrame.pack()
        self.sixFrame.pack()
        self.sevenFrame.pack()
        self.eightFrame.pack()
        self.nineFrame.pack()

    def callPatientWindow(self): #calling the next class
        self.window.destroy()
        patient = PatientWindow()

    def day(self):
        days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
        return days   #formatting the drop down menu for days

    def month(self):
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        return months #formatting the drop down menu for months
    
    def year(self):
        years = [2024,2025]
        return years #formatting the drop down menu for years
    
    def time(self):
        times = ["9:00","9:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30","14:00","14:30","15:00","15:30","16:00"]
        return times #formatting the drop down menu for times
    
    def viewAppointments(self):
        approved = ""
        pending = ""
        file = open('appointment.txt', 'r') #reading through appointment files
        throughlines = file.readlines()
        otherline = (throughlines[-1]).split(",") #splitting up the last line in the file only
        firstName = otherline[1]
        lastName = otherline[2]
        for line in throughlines: #for looping through all the lines
            newline = line.split(",")
            if newline[3] != "\n":
                if newline[1] == firstName and newline[2] == lastName:
                    if newline[9] != "past": #making sure the appointment hasn't happened
                        if newline[8] == "pending": #If appointment hasn't been approved yet
                            pending += line + "\n"
                        elif newline[8] == "Approved": #If appointment has been approved
                            approved += line + "\n"
        pendinglabel = tk.Label(self.sevenFrame, text=pending) #writing out the separate strings
        approvedlabel = tk.Label(self.eightFrame, text=approved)
        pendinglabel.pack()
        approvedlabel.pack()
        

    
    def viewDoctor(self):
        file = open('appointment.txt', 'r') #opening the appointment file
        filecheck = file.readlines()
        patientneeded = filecheck[-1] # finding the last line
        patientSplit = patientneeded.split(",") #splitting it up
        firstName = patientSplit[1]
        lastName = patientSplit[2]
        file.close()

        file = open('patient.txt', 'r') #opening the patient file
        patientlines = file.readlines()
        for line in patientlines: #looping through each line
            splitLines = line.split(",")
            firstCheck = " "+splitLines[2]
            lastCheck = " "+splitLines[3]
            if firstCheck == firstName and lastCheck == lastName: #if the name lines up get the doctor id
                doctID = splitLines[1]
        file.close()

        file = open('doctor.txt', 'r') #opening doctor file and looping through
        doctorlines = file.readlines()
        for line in doctorlines:
            doctorLine = line.split(",")
            if doctorLine[0] == doctID:
                genius = ("Your doctor is: "+doctorLine[1]+" "+doctorLine[2]) #formatting saying which doctor
                doctorLabel = tk.Label(self.fiveFrame, text=genius)
                doctorLabel.pack()
        file.close()

    def addAppointment(self): #adding an appointment
        appointment = []
        file = open('appointment.txt', 'r') #opening appointment file
        filecheck = (file.readlines()) #reading the current amount of lines then adding one
        patientneeded = filecheck[-1]
        Patientsplit = patientneeded.split(",")
        id = str(Patientsplit[0])
        firstName = Patientsplit[1]
        lastName = Patientsplit[2]
        file.close()
        dayChoice = str(self.dayv.get())
        monthChoice = self.monthv.get()
        yearChoice = str(self.yearv.get())
        timeChoice = self.timev.get()

        doctorid = "0" #doctor id as 0 until assigned one by an admin
        pending = 'pending' #pending until approved by admin
        self.deleteUpdate(id)
        Array = "" #Empty string
        file = open('appointment.txt', 'a') #opening the file in read only
        
        newline = (id+","+firstName+","+lastName+","+doctorid+","+dayChoice+","+monthChoice+","+yearChoice+","+timeChoice+",pending,future,\n") #writing in the new data
        file.write(newline)
        file.close() #closing file

    def deleteUpdate(self, id):
        Array = "" #Empty string
        file = open('appointment.txt', 'r') #opening file in readonly
        throughlines = file.readlines()
        for i in throughlines: #looping through lines
            trial = i.split(",") #splitting up each entry
            if trial[0] != id: #if the ID doesn't match
                Array += i #print into the array
            else:
                newline = ("")# overwriting the line that needs to be deleted
                Array += newline
        file.close() 
        file = open('appointment.txt', 'w') #write to text file
        file.write(Array)
        file.close()
               

class ManagePWindow:
    def __init__(self):

        self.Managepwindow = tk.Tk()
        self.Managepwindow.title = "Manage Patients"
        self.Managepwindow.geometry("600x500")

        self.oneFrame = tk.Frame(self.Managepwindow)
        self.twoFrame = tk.Frame(self.Managepwindow)
        self.threeFrame = tk.Frame(self.Managepwindow)
        self.fourFrame = tk.Frame(self.Managepwindow)
        self.fiveFrame = tk.Frame(self.Managepwindow)
        self.sixFrame = tk.Frame(self.Managepwindow)
        self.sevenFrame = tk.Frame(self.Managepwindow)
        self.eightFrame = tk.Frame(self.Managepwindow)
        self.nineFrame = tk.Frame(self.Managepwindow)
        self.tenFrame = tk.Frame(self.Managepwindow)
        self.elevenFrame = tk.Frame(self.Managepwindow)

        self.ManageLabel = tk.Label(self.oneFrame, text="Manage Patients")
        self.ManageLabel.pack()

        self.variable = StringVar(self.Managepwindow)
        self.options = self.SearchRequests()
        self.variable.set(self.options[0])
        self.w = OptionMenu(self.twoFrame, self.variable, *self.options)
        self.w.pack(side="left")

        self.docVariable = StringVar(self.Managepwindow)
        self.Docoptions = self.searchDoctors()
        self.docVariable.set(self.Docoptions[0])
        self.d = OptionMenu(self.twoFrame, self.docVariable, *self.Docoptions)
        self.d.pack(side="left")
        
        
        self.registerButton = tk.Button(self.twoFrame, text="Register Patient", command=self.registerPatient)
        self.registerButton.pack()

        self.searchVariable = StringVar(self.Managepwindow)
        self.searchoptions = self.SearchAppointments()
        self.searchVariable.set(self.searchoptions[0])
        self.s = OptionMenu(self.threeFrame, self.searchVariable, *self.searchoptions)
        self.s.pack(side="left")

        self.approveButton = tk.Button(self.threeFrame, text="Approve", command=self.appointmentAccept)
        self.denyButton = tk.Button(self.threeFrame, text="Deny", command=self.appointmentDeny)
        self.approveButton.pack(side="left")
        self.denyButton.pack(side="left")

        self.idLabel = tk.Label(self.fourFrame, text="PatientID")
        self.patientID = tk.Entry(self.fourFrame)
        self.Discharge = tk.Button(self.fiveFrame, text="Discharge Patient", command=self.dischargePatient)
        self.idLabel.pack(side="left")
        self.patientID.pack(side="left")
        self.Discharge.pack()

        self.treatPatient = tk.Button(self.sixFrame, text="View treated patients", command=self.viewTreat)
        self.treatPatient.pack()

        self.PatientFile = tk.Button(self.sevenFrame, text="Load data to a file", command=self.PatientFile)
        self.PatientFile.pack()
        
        self.backButton = tk.Button(self.elevenFrame, text="Back", command=self.callAdminWindow)
        self.backButton.pack()

        self.oneFrame.pack()
        self.twoFrame.pack()
        self.threeFrame.pack()
        self.fourFrame.pack()
        self.fiveFrame.pack()
        self.sixFrame.pack()
        self.sevenFrame.pack()
        self.eightFrame.pack()
        self.nineFrame.pack()
        self.tenFrame.pack()
        self.elevenFrame.pack()

        tk.mainloop()
    
    def callAdminWindow(self): #calling the previous window
        self.Managepwindow.destroy()
        adminwindow = AdminWindow()

    def PatientFile(self):
        patientID = self.patientID.get()
        file = open('patient.txt', 'r') #opening the patient file
        lines = file.readlines()
        for line in lines: #reading through lines and splitting them up
            entries = line.split(",")
            if entries[0] == patientID: #assigning all the entries needed
                docID = entries[1]
                firstName = entries[2]
                lastName = entries[3]
                dob = entries[5]
                phone = entries[6]
                address = entries[7]
                symptoms = entries[8]
                diagnoses = entries[9]
        file.close()
        file = open('Patientdata.txt', 'w')
        file.write("Patient ID: "+patientID+"\n Doctor ID: "+docID+"\n First Name: "+firstName+"\n Last Name: "+lastName+"\n Date of Birth: "+dob+"\n Phone number: "+phone+"\n Address: "+address+"\n Symptoms: "+symptoms+"\n Diagnoses: "+diagnoses)
        file.close()

    def viewTreat(self):

        Treated = ""
        file = open('patient.txt', 'r') #opening patient file
        theLine = file.readlines()
        for line in theLine:
            eachEntry = line.split(",")
            if eachEntry[11] == "Yes": #if treated = yes then print treated
                if eachEntry != line[4]:
                    Treated += line +"\n"
        
        treatlist = tk.Label(self.sevenFrame, text=Treated)
        treatlist.pack()

    def dischargePatient(self):
        patID = self.patientID.get()

        Array = "" #Empty string
        file = open('patient.txt', 'r') #opening the file in read only
        throughlines = file.readlines() #reading each line one at a time
        for i in throughlines:
            find = i.split(",") #splitting between entries
            if find[0] != patID: #If the first and last names aren't the same as the entered one
                Array += i #write the line to the string
            else: #if the names match
                newline = (find[0]+","+find[1]+","+find[2]+","+find[3]+","+find[4]+","+find[5]+","+find[6]+","+find[7]+","+find[8]+","+find[9]+",approved,Yes,\n") #writing in the new data
                Array += newline
        file.close() #closing file
        file = open('patient.txt', 'w')#opening the file in write only
        file.write(Array) #writing over the data in the array
        file.close()


    def SearchRequests(self):
        requests = ['Pending Requests']
        Fullname = ""
        file = open('patient.txt', 'r') # open patient file
        lines = file.readlines()
        for line in lines:
            obj = line.split(",")
            if obj[10] == 'pending': #if approval is pending add to string to print out
                Fullname = (obj[2]+","+obj[3])
                requests.append(Fullname)
        return requests

    def SearchAppointments(self):
        search = ["Requested appointments"]
        Names = ""
        file = open('appointment.txt', 'r') #open appointment file
        lines = file.readlines()
        for line in lines:
            obj = line.split(",")
        
            if obj[8] == 'pending': #if approval is pending add to list
                Names = (obj[1]+";"+obj[2]+";"+obj[4]+";"+obj[5]+";"+obj[6]+";"+obj[7]+";")
                search.append(Names)
        return search

    def searchDoctors(self):
        Doctors = ['Assigned doctors']
        Fullname = ""
        file = open('doctor.txt', 'r') #open doctor file
        lines = file.readlines()
        for line in lines:
            obj = line.split(",")
            if obj[1] != "\n":
                Fullname = (obj[1]+","+obj[2]) #if doctor hasn't been deleted print out
                Doctors.append(Fullname)
        return Doctors    

    def registerPatient(self):
        PatientName = self.variable.get() 
        if PatientName != "Pending Requests": #if the entry isn't the cover one
            split = PatientName.split(",") #splitting between entries
            firstName = split[0]
            lastName = split[1]
            fullname = (split[0]+" "+split[1]) #full name for doctor records

            doctorName = self.docVariable.get()
            if doctorName != "Assigned doctors": #if the entry isn't the cover one
                Dsplit = doctorName.split(",")
                Dfirst = Dsplit[0]
                Dlast = Dsplit[1]
                DoctorArray = "" #Empty string
                DoctorFile = open('doctor.txt', 'r') #opening doctor file in read only
                lines = DoctorFile.readlines() # reading the lines
                for line in lines:
                    doctor = line.split(",")
                    if doctor[1] == Dfirst and doctor[2] == Dlast: #if the first and lastname match
                        Did = doctor[0]
                        newline = (Did+","+Dfirst+","+Dlast+","+doctor[3]+","+fullname+";,\n") 
                        DoctorArray +=newline

                    else:
                        DoctorArray += line
                
                DoctorFile.close()
                DoctorFile = open('doctor.txt', 'w')
                DoctorFile.write(DoctorArray)
                DoctorFile.close()


                DoctorFile.close()

                Array = "" #Empty string
                file = open('patient.txt', 'r') #opening the file in read only
                throughlines = file.readlines() #reading each line one at a time
                for i in throughlines:
                    find = i.split(",") #splitting between entries
                    if find[2] != firstName or find[3] != lastName: #If the first and last names aren't the same as the entered one
                        Array += i #write the line to the string
                    else: #if the names match
                        newline = (find[0]+","+Did+","+firstName+","+lastName+","+find[4]+","+find[5]+","+find[6]+","+find[7]+","+find[8]+","+find[9]+",approved,No,\n") #writing in the new data
                        Array += newline
                file.close() #closing file
                file = open('patient.txt', 'w')#opening the file in write only
                file.write(Array) #writing over the data in the array
                file.close()

    def appointmentAccept(self):
        AppointmentName = self.searchVariable.get()
        if AppointmentName != "Requested Appoinments":
            
            all = AppointmentName.split(";") #assign everything needed
            firstName = (all[0])
            lastName = (all[1])
            day = all[2]
            month = all[3]
            year = all[4]
            time = all[5]
            file = open('patient.txt', 'r')
            lines = file.readlines()
            for line in lines:
                Entries = line.split(",") 
                first = " "+Entries[2]
                last = " "+Entries[3]
                if first == firstName and last == lastName: #if its the right patient assign doctor id
                    docID = Entries[1]
                    
                    

            file.close()
            Array = ""
            file = open('appointment.txt', 'r') #open appointment file
            throughlines = file.readlines()
            for line in throughlines:
                splitUp = line.split(",") # if all the data matches then add to string with doc id updated
                if splitUp[1] == firstName and splitUp[2] == lastName and splitUp[4] == day and splitUp[5]==month and splitUp[6] == year and splitUp[7] == time:
                    newline = (splitUp[0]+","+splitUp[1]+","+splitUp[2]+","+docID+","+splitUp[4]+","+splitUp[5]+","+splitUp[6]+","+splitUp[7]+",Approved,"+splitUp[8]+",\n")
                    Array += newline
                else:
                    newline = line #if not just add to string
                    Array += newline
                file.close()
                file=open('appointment.txt','w')
                file.write(Array)
                file.close()
    
    def appointmentDeny(self): #same as previous function but denied instead of approved, doctor is still assigned
        AppointmentName = self.searchVariable.get()
        if AppointmentName != "Requested Appoinments":
            
            all = AppointmentName.split(";")
            firstName = (all[0])
            lastName = (all[1])
            day = all[2]
            month = all[3]
            year = all[4]
            time = all[5]
            file = open('patient.txt', 'r')
            lines = file.readlines()
            for line in lines:
                Entries = line.split(",")
                first = " "+Entries[2]
                last = " "+Entries[3]
                if first == firstName and last == lastName:
                    docID = Entries[1]

            file.close()
            Array = ""
            file = open('appointment.txt', 'r')
            throughlines = file.readlines()
            for line in throughlines:
                splitUp = line.split(",")
                if splitUp[1] == firstName and splitUp[2] == lastName and splitUp[4] == day and splitUp[5]==month and splitUp[6] == year and splitUp[7] == time:
                    newline = (splitUp[0]+","+splitUp[1]+","+splitUp[2]+","+docID+","+splitUp[4]+","+splitUp[5]+","+splitUp[6]+","+splitUp[7]+",Denied,"+splitUp[8]+",\n")
                    Array += newline
                else:
                    newline = line
                    Array += newline
                file.close()
                file=open('appointment.txt','w')
                file.write(Array)
                file.close()
                

        


gui = LoginScreen()    