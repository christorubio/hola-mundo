#Chris Rubio
#1530668

password = input()
new_password = ''

for x in password:
  if x == 'i':
    new_password += '!'
  elif x == 'a':
    new_password += '@'
  elif x == 'm':
    new_password += 'M'
  elif x == 'B':
    new_password += '8'
  elif x == 'o':
    new_password += '.'
  else:
    new_password += x
    
new_password += 'q*s'

print(new_password)
