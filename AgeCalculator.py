
#
#  AgeCalculator.py
#  Age Calculation by years, months, weeks & days.
#
#  Created by Gorugantham, Ramu Raghu Vams on 10/23/22.
#
#  Preface:
#  get current date & birth date
#  should Adjust Age = current month, day < birth month, day == true if true its 1 else 0
#  ageInYears = current date year - birth date year - should adjust age
#

from datetime import date
import datetime
import math

#formulae
avgNoOfDaysInAYear = 365.25
noOfMonthsInAYear = 12
avgNoOfDaysInAMonth = 30.417
noOfDaysInAWeek = 7

def ageInDays(currentDate, birthDate):
    return (currentDate - birthDate).days

def ageInWeeks(currentDate, birthDate):
    totalNoOfDays = ageInDays(currentDate, birthDate)
    (frac, weeks) = math.modf(totalNoOfDays / noOfDaysInAWeek)
    days = round(frac * noOfDaysInAWeek)
    if int(days) == 0:
        return str(int(weeks)) + " weeks"
    else:
        return str(int(weeks)) + " weeks & " + str(int(days)) + " days"

def ageInYears(currentDate, birthDate):
    adjustedAge = (currentDate.month, currentDate.day) < (birthDate.month, birthDate.day)
    return currentDate.year - birthDate.year - adjustedAge

def ageInYearsMonthsAndDays(currentDate, birthDate):
    totalNoOfDays = ageInDays(currentDate, birthDate)
    yearsComponent = totalNoOfDays / avgNoOfDaysInAYear
    (frac, years) = math.modf(yearsComponent)
    monthsComponent = frac * noOfMonthsInAYear
    (frac, months) = math.modf(monthsComponent)
    daysComponent = frac * 30.417
    (frac, days) = math.modf(daysComponent)
    return str(int(years)) + " years, " + str(int(months)) + " months & " + str(int(days)) + " days"

def getAge(currentDate, birthDate):
    print("\n\nAge of the person born on", birthDate.strftime("%d %B, %Y"),":\n", ageInYearsMonthsAndDays(currentDate, birthDate))
    print(" or", ageInWeeks(currentDate, birthDate))
    print(" or", ageInDays(currentDate, birthDate), " days\n\n" )

def getBirthDate():
    birthDateString = input("Enter date of birth as yyyy-mm-dd\n\n")
    birthDate = datetime.datetime.strptime(birthDateString, '%Y-%m-%d').date()
    return birthDate

def askForUserInput():
    userSelection = input("1. Calculate age as of today\n2. Calculate age as of a future date\n\n")
    if userSelection.isdigit():
        if int(userSelection) == 1:
            birthDate = getBirthDate()
            currentDate = date.today()
            getAge(currentDate, birthDate)
        elif int(userSelection) == 2:
            birthDate = getBirthDate()
            birthDateString = input("\n\nEnter a date of future date as yyyy-mm-dd\n\n")
            futureDate = datetime.datetime.strptime(birthDateString, '%Y-%m-%d').date()
            getAge(futureDate, birthDate)
        else:
            print("invalid input. Please try again.\nPlease select from one of the below options:")
            askForUserInput()
    else:
        print("invalid input. Please try again.\nPlease select from one of the below options:")
        askForUserInput()

def main():
    print("Welcome to Python Age Calculator. \n\nPlease select from one of the below options:")
    askForUserInput()

if __name__ == '__main__':
    main()
