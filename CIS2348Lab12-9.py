#Christopher Rubio
#1530668

parts = input().split()
name = parts[0]
while name != '-1':
    try:
        age = int(parts[1]) + 1
    except ValueError as ve:
        age = 0
    
    print('{} {}'.format(name, age))
    parts = input().split()
    name = parts[0]
