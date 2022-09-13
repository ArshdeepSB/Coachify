import os

class members:
    def __init__(self, username, password, phoneNumber, address, classesAttended, unpaidClasses):
      self.username = username
      self.password = password
      self.phoneNumber = phoneNumber
      self.address = address
      self.classesAttended = classesAttended
      self.debt = unpaidClasses * 10
      self.reminders = ""
      self.discount = False
      self.missedPaid = unpaidClasses
      self.schedule = []
      self.totalPayed = 0

    def __str__(self):
      if self.discount:
        return self.username + ", Number of Classes Attended: " + str(
            self.classesAttended) + ", " + self.phoneNumber + " Money Paid: " + str(self.debt <= -9) + ", " + self.address
      else: 
        return self.username + " Number of Classes Attended: " + str(
            self.classesAttended) + ", " + self.phoneNumber + " Money Paid: " + str(self.debt <= -10) + ", " + self.address 

    def getUsername(self):
        return self.username

    def getClassesAttended(self):
        return self.classesAttended

    def getDebt(self):
        return self.debt

    def getReminders(self):
        return self.reminders

    def addReminder(self, reminder):
        self.reminders = self.reminders + reminder + "\n"

    def addDebt(self, debt):
        self.debt = self.debt + debt
        #also updateReminder about the debt

    def addClass(self):
        self.classesAttended += 1

    def addDiscount(self, discount):
        self.discount = True


class treasurer:
    def __init__(self, username, password, rent, practice):
        self.coachExpense = 0
        self.username = username
        self.password = password
        self.hallExpense = rent
        self.practice = practice
        self.income = 0
        self.reminder = ""

    def addExpense(self):
        self.updateHallExpense(400)
        self.updateCoachExpense(200)
        return 600
      
    def addIncome(self, studentPay, otherIncome):
        return studentPay + otherIncome

    def profit(self, aCoach, pay, studentIncome, otherIncome):
        return self.addIncome(studentIncome, otherIncome) - self.addExpense()
      
    def updateCoachExpense(self, money): 
      self.coachExpense += money

    def updateHallExpense(self, money): 
      self.hallExpense += money

    def addReminder(self, reminder):
      self.reminder = self.reminder + reminder + "\n"



class coach:
    def __init__(self, username, password, daysAvailable, classesAttended):
        self.username = username
        self.password = password
        self.daysAvailable = daysAvailable
        self.classesAttended = classesAttended
        self.payroll = 0

    def addClass(self):
        self.classesAttended += self.classesAttended

    def changeAvailability(self, new):
        self.daysAvailable = new

def sort(list):
  temp = []
  while len(list) > 0:
      largest = -1
      index = 0
      for i in range(len(list)):
          if list[i].missedPaid > largest:
              largest = list[i].missedPaid
              index = i
      temp.append(list.pop(index))
  return temp

def sort_attended(list):
  temp = []
  while len(list) > 0:
    largest = -1
    index = 0
    for i in range(len(list)):
      if list[i].classesAttended > largest:
        largest = list[i].classesAttended
        index = i
    temp.append(list.pop(index))
  return temp

def discount_yes(list):
  i = 0
  temp = sort_attended(list)
  while i < len(list) and i < 10:
    list[i].discount = True
    i += 1

def main():
  endit = True
  notLoggedIn = True
  notLoggedIn2 = True
  notLoggedIn3 = True
  Jett = members("Jett", "password", "647-298-2382", "L21-3A4", 9, 0)
  Reyna = members("Reyna", "password","647-232-2142", "V73-FD8", 14, 0)
  Yoru = members("Yoru", "Urtrashkid", "647-242-6856","F9S-283", 3, 0)
  Raze = members("Raze", "Satchel", "647-278-2352", "DSF-S7V", 4, 0)
  Sova = members("Sova", "shak_dart", "647-858-3753", "DF0-CS0", 13, 0)
  mem_list = [Jett, Reyna, Yoru, Raze, Sova]

  teamCoach = coach("candice", "poggers", ["Monday", "Wednesday", "Friday"],
                    0)

  theTreasurer = treasurer("elon", "tesla", 0, 0)

  #Input Screen
  while (endit):
    user = input("Enter coach, student, or treasurer, exit:\n")
    while user.lower() != "coach" and user.lower(
    ) != "student" and user.lower() != "treasurer" and user.lower() != "exit":
        user = input("Enter coach, student, or treasurer:\n")

  
    #Student
    if user.lower() == "student":
      option = int(input("Enter a number of option below:\n1. Create Account\n2. Login\n"))
      if option == 1:
        createAccount(mem_list)
      elif option == 2:
        while (notLoggedIn):
          username = input("Enter a username: ").strip()
          password = input("Enter a password: ")
          for i in mem_list:
            if i.username == username and i.password == password:
              login(i, teamCoach, mem_list)
              notLoggedIn = False
          if notLoggedIn == True:
            print(
                  "Couldn't Find Your Account Try Again or Create Account"
              )

    # COACH
    elif user.lower() == "coach":
      while (notLoggedIn2):
          username = input("Enter a username: ").strip()
          password = input("Enter a password: ")
          if username == teamCoach.username and password == teamCoach.password:
            notLoggedIn2 = False 
            loginCoach(teamCoach, mem_list) 
          if notLoggedIn2 == True:
              print(
                  "Couldn't Find Your Account Try Again or Create Account"
                )
    #Treasurer            
    elif user.lower() == "treasurer": 
      while (notLoggedIn3):
          username = input("Enter a username: ").strip()
          password = input("Enter a password: ")
          if username == theTreasurer.username and password == theTreasurer.password:
            notLoggedIn3 = False 
            loginTreasurer(teamCoach, theTreasurer, mem_list) 
          if notLoggedIn3 == True:
              print(
                  "Couldn't Find Your Account Try Again or Create Account"
                )
            
    else:
            print("Quiting System")
            endit = False
    input("Enter to continue")
    notLoggedIn = True
    notLoggedIn2 = True
    notLoggedIn3 = True
    os.system('clear')

def loginTreasurer(teamCoach, theTreasurer, mem_list): 
  if theTreasurer.coachExpense > 0:
    theTreasurer.addReminder("Need to pay coach expenses ASAP!")
  if theTreasurer.hallExpense > 0:
    theTreasurer.addReminder("Need to pay hall expenses ASAP!")
  notFinished = True
  while(notFinished): 
    option = int(input("Enter a number of option below:\n1. Start New Month\n2. Pay Expense\n3. Print log\n4. Printing All People Who Paid In Adavence\n5.Income Statement\n"))
    # Total Amount of unpaid coach expenses and hall expenses
    if option == 1: 
      theTreasurer.updateCoachExpense(200) 
      theTreasurer.updateHallExpense(400) 
    elif option == 2: 
      theTreasurer.coachExpense = 0
      theTreasurer.hallExpense = 0
    elif option == 3: 
      treasurerList = [theTreasurer.coachExpense, theTreasurer.hallExpense]
      print(treasurerList)
      print(theTreasurer.reminder)
    elif option == 4:
      temp = []
      for i in mem_list:
        if i.debt < 0:
          temp.append(i.username)
      print(temp)
    elif option == 5:
      totalIncome = 0
      for students in mem_list:
        totalIncome += students.totalPayed
      print("Income Statement Report")
      exp = int(input("Enter other expenses: $"))
      totalExp = theTreasurer.addExpense() + exp
      print("Expenses = $", totalExp)
      inc = int(input("Enter other income amount: $"))
      totalInc = theTreasurer.addIncome(totalIncome, inc)
      print("Revenue = $", totalInc)
      print("Profit = $", totalInc - totalExp)
      
    else:
      notFinished = False

def membersList():
  print("memberList")


def memberStatistics():
  print("memberStatistics")


def notifications():
  print("notifications")


def login(member, teamCoach, mem_list):
  print("inside Login\n")
  # making reminders 
  if member.missedPaid > 0: 
    member.addReminder("You have missed one or more days and can be possibly excluded from the group")
  if member.missedPaid > 1:
    member.addReminder("You have recieved a penalty for missing more than one day: $20")
    member.addDebt(20)
    
  #printing reminders
  print(member.reminders)
  
  endit2 = True
  while (endit2):
    #Input Screen
    option = int(input("Enter a number of option below:\n1. Book\nPress any other number to logout\n"))
    if option == 1:
      print("the coach is available on")
      for days in teamCoach.daysAvailable:
          print(days + " ")
      print("\n")
      while (True):
          notinbooking = False
          bookingDay = input(
              "Enter which day of the week you would like to attend: "
          )
          for days in bookingDay.split():
              if days not in teamCoach.daysAvailable:
                  notinbooking = True
          if notinbooking == False:
              member.daysAvailable = bookingDay.split()
              prepay = input("Enter amount you want to prepay: $")
              prepay = int(prepay)
              member.debt = member.debt - prepay
              member.addReminder("You have booked a session for " + bookingDay)
              break
    else:
        print("LoggedOut")
        endit2 = False

def loginCoach(coach, mem_list):
    print("inside Login")
    endit = True
    while (endit):
        #Input Screen
        val = input("Enter a number of option below:\n1. Change Availability\n2. Enter Class Info\n3. Enter Day Unable to Attend\n4. Print List Sorted by Highest Missed Payments\n5. Add Student\n6. Remove Student\n")
        option = int(val)
        if option == 1:
            available = input("Enter the days you are available: ")
            available = available.split()
            for i in range(len(available)):
                while available[i] != "Monday" and available[
                        i] != "Tuesday" and available[
                            i] != "Wednesday" and available[
                                i] != "Thursday" and available[i] != "Friday":
                    available[i] = input("Enter the days you are available: ")
            coach.changeAvailability(available)
        elif option == 2:
            coach.addClass()
            attendance = input(
                "Enter the students who attended separated by spaces: ")
            paid = input("Enter the students who paid separated by spaces: ")
          
            attendance = attendance.split()
            attendance = list(dict.fromkeys(attendance))
            paid = paid.split()
            paid = list(dict.fromkeys(paid))

            for student in attendance:
                if not student in paid:
                    for member in mem_list:
                        if member.username == student:
                            if member.discount == False:
                                member.debt = member.debt + 30
                            else:
                                member.debt = member.debt + 29
                                member.discount = False
                            member.missedPaid += 1
                else:
                    for member in mem_list:
                        if member.username == student:
                            member.addClass()
                            disc = input("ApplyDiscount? (y/n): ").strip()
                            if disc.lower() == "y":
                              if member.discount:
                                member.totalPayed += 9
                              else:
                                member.totalPayed += 10
                            else:
                              member.totalPayed += 10
        elif option == 3:
            dayNotComing = input("Enter the day your not coming: ")
            for students in mem_list: 
              if coach.daysAvailable.index(dayNotComing) == len(coach.daysAvailable): 
                students.addReminder("The next meeting will be on " + coach.daysAvailable[0])
              else:
                students.addReminder("The next meeting will be on " + coach.daysAvailable[coach.daysAvailable.index(dayNotComing) + 1])
        elif option == 4: 
          print("This is the sorted list with the highest missed days:\n")
          mem_list = sort(mem_list)
          for i in mem_list: 
            print(i)
        # Adding or removing the members
        elif option == 5:
          createAccount(mem_list)
        elif option == 6:
          user = input("Enter the username you would like to remove: ")
          for i in range(len(mem_list)):
            if mem_list[i].username == user:
              mem_list = mem_list[:i] + mem_list[i+1:]
              break
        else:
            print("LoggedOut")
            endit = False
        # coach needs to see schedule of students 
          
def createAccount(mem_list):
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    phone = input("Enter Phone Number ex.(xxx-xxx-xxxx): ")
    address = input("Enter Postal Code ex(xxx-xxx): ")
    username = members(username, password, address, phone, 0, 0)
    mem_list.append(username)
  
main()
