
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

def main():
    currentDate = date.today()
    birthDate = date(1994,7,23)    #date(yyyy,m,d)
    futureDate = date(2032,7,1)

    print("\n\nAge of the person born on", birthDate.strftime("%d %B, %Y"),":\n", ageInYearsMonthsAndDays(futureDate, birthDate))
    print(" or", ageInWeeks(futureDate, birthDate))
    print(" or", ageInDays(futureDate, birthDate), " days\n\n" )

if __name__ == '__main__':
    main()
