#Chris Rubio
#1530668


print('Birthday Calculator')
print('Current day')
#current day variables
month = int(input('Month: '))
day = int(input('Day: '))
year = int(input('Year: '))
print('Birthday')
#bday variables
bday_month = int(input('Month: '))
bday_day = int(input('Day: '))
bday_year = int(input('Year: '))
#age variable
age = year - bday_year
#if else to calculate age
if month < bday_month:
    age = age - 1
elif month == bday_month:
    if day < bday_day:
        age = age - 1
#if dates match
if month == bday_month and day == bday_day:
    print('Happy Birthday!')
print('You are', age, 'years old.')
