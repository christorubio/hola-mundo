#Chris Rubio
#1530668

#service menu
services = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12, '-': 0}

print("Davy's auto shop services")
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12')
print("")
print("Select first service:")
first = input()
print("Select second service:")
second = input()
print("")
print("Davy's auto shop invoice")
print("")
if(first == '-'):
  print('Service 1: No service')
else:
  print('Service 1: %s, $%d' % (first, services.get(first)))
if(second == '-'):
  print('Service 2: No service')
else:
  print('Service 2: %s, $%d' % (second, services.get(second)))
total = services.get(first) + services.get(second)
print()
print('Total: $%d' % (total))
