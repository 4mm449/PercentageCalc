import datetime #importing date module
import random #importing random module for random numbers
#Function to print ticket ID
def ticketid():
    ticketid = random.randint(10000, 600000)
    print("Ticket ID:", ticketid)
#Start of output
grades = ["A*", "A", "B", "C", "D", "F", "U"] #list of grades to be used later on
print("Valid grades: ",grades[0:])

#algorithm to calculate percentage
Marks = input("Enter marks attained: ")  #enter marks attained
TotalMarks = input("Enter total marks: ")  #enter total number of marks
TotalPercentage = float(Marks)/float(TotalMarks) * 100  #formula to calculate total percentage
print("Total Percentage:", TotalPercentage,"%")  #output total percentage in full
print("Total Percentage (Rounded Down):", int(TotalPercentage),"%")  #output total percentage in full

#if total percentage is greater than 50, pass, if not, fail, if equal 50, just pass
def failorpass():
    if TotalPercentage > 50:
        print("You have Passed")
    elif TotalPercentage == 50:
        print("You have Just Passed")
    else:
        print("You have Failed")
failorpass()


#grades calculator
def gradescalc():
    global TotalPercentage
    if TotalPercentage >= 90 and TotalPercentage < 100:
        TotalPercentage = grades[0]
        print("Your Grade:", TotalPercentage)
        print("Excellent")

    elif TotalPercentage >= 80 and TotalPercentage < 90:
        TotalPercentage = grades[1]
        print("Your Grade:", TotalPercentage)
        print("Good")

    elif TotalPercentage >= 70 and TotalPercentage < 80:
        TotalPercentage = grades[2]
        print("Your Grade:", TotalPercentage)
        print("Average")

    elif TotalPercentage >= 60 and TotalPercentage < 70:
        TotalPercentage = grades[3]
        print("Your Grade:", TotalPercentage)
        print("Acceptable")

    elif TotalPercentage >= 50 and TotalPercentage < 60:
        TotalPercentage = grades[4]
        print("Your Grade:", TotalPercentage)
        print("Need to improve")

    elif TotalPercentage >= 25 and TotalPercentage < 50:
        TotalPercentage = grades[5]
        print("Your Grade:", TotalPercentage)
        print("Work Harder")

    elif TotalPercentage < 25:
        TotalPercentage = grades[6]
        print("Your Grade:", TotalPercentage)
        print("Work Harder")
gradescalc()


date = datetime.datetime.now()
print("Results provided on (YYYY-MM-DD HH:MM:SS.MS): ",date)

ticketid()

