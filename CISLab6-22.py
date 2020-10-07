#Chris Rubio
#1530668

x1 = int(input())
y1 = int(input())
z1 = int(input())
 
x2 = int(input())
y2 = int(input())
z2 = int(input())
 
def func1(x, y):
    return x1*x + y1*y - z1
def func2(x, y):
    return x2*x + y2*y - z2
finalx = 100
finaly = 100
for x in range(-10, 11):
    for y in range(-10,11):
        if func1(x,y) == func2(x,y) and func1(x,y) == 0:
            finalx = x
            finaly = y
if finalx != 100:
    print(finalx, finaly)
else:
    print('No solution')
