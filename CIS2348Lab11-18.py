#Chris Rubio
#1530668

values = input()

numbers = [int(i) for i in values.split() if int(i) > 0]
numbers.sort() 

for i in numbers:
  print (i, end=' ')
