from datetime import date

def ageCalculator(currentDate, birthDate):
    age = currentDate.year - birthDate.year
    if (currentDate.month, currentDate.day) < (birthDate.month, birthDate.day):
        age = age - 1
    print(age)

def main():
    currentDate = date.today()
    birthDate = date(1989,5,7)    #date(yyyy,m,d)
    futureDate = date(2032,7,1)

    print("Age as of date - ", currentDate)
    ageCalculator(currentDate, birthDate)

    print("Age as of date - ", futureDate)
    ageCalculator(futureDate, birthDate)

if __name__ == '__main__':
    main()


#  Age Calculation.
#
#  get current date
#  get birth date
#  should Adjust Age = current month, day < birth month, day == true if true its 1 else 0
#  age = current date year - birth date year - should adjust age

#
#
#
