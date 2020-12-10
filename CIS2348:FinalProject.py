#Chris Rubio
#1530668
#Final Project

#Import what will be used
import csv
import operator
import datetime

##PART1
#Initializing the list for the csv data
ManufacturerList = []
ServiceDatesList = []
PriceList = []

#opening the csv files and listing the indexes
with open('ManufacturerList.csv') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    for row in csv_reader:
        ManufacturerList.append(dict(ID=row[0], Product=row[1], Item=row[2], Damaged=row[3]))

with open('ServiceDatesList.csv') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    for row in csv_reader:
        ServiceDatesList.append(dict(ID=row[0], Date=row[1]))

with open('PriceList.csv') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    for row in csv_reader:
        PriceList.append(dict(ID=row[0], Price=row[1]))

#defining the writecsv func.
def writecsv(listDictionary, file):
    with open(file, mode='w', newline='') as file:
        csv_writer = csv.writer(file, delimiter=',')
        for item in listDictionary:
            csv_writer.writerow([item[key] for key in item])

#writing the FullInventory csv
FullInventory = ManufacturerList.copy()
for i in FullInventory:
    i['Price'] = 0
    i['Date'] = ''
for i in range(len(FullInventory)):
    FullInventory[i]['Price'] = PriceList[i]['Price']
    FullInventory[i]['Date'] = ServiceDatesList[i]['Date']

FullInventory.sort(key=operator.itemgetter('Product'))
writecsv(FullInventory, 'FullInventory.csv')

#Initializing lists for the csv files
LaptopType = []
TowerType = []
PhoneType = []

#separating each type by the keyword
for item in FullInventory.copy():
    first_type = item.copy()
    if first_type['Item'] == 'phone':
        first_type.pop('Item')
        PhoneType.append(first_type)
        writecsv(PhoneType, 'PhoneType.csv')

for item in FullInventory.copy():
    second_type = item.copy()
    if second_type['Item'] == 'tower':
        second_type.pop('Item')
        TowerType.append(second_type)
        writecsv(TowerType, 'TowerType.csv')

for item in FullInventory.copy():
    third_type = item.copy()
    if third_type['Item'] == 'laptop':
        third_type.pop('Item')
        LaptopType.append(third_type)
        writecsv(LaptopType, 'LaptopType.csv')

#sorting by ID
PhoneType.sort(key=operator.itemgetter('ID'))
TowerType.sort(key=operator.itemgetter('ID'))
LaptopType.sort(key=operator.itemgetter('ID'))

#Pastservicedate csvfile
PastServiceDate = []
for item in FullInventory.copy():
  da_te = item.copy()
  if datetime.datetime.strptime(da_te['Date'], "%m/%d/%Y") < datetime.datetime.today():
    da_te.pop('Damaged')
    PastServiceDate.append(da_te)
#sorting
PastServiceDate.sort(key=operator.itemgetter('Date'))
writecsv(PastServiceDate, 'PastServiceDate.csv')

#Damaged csv file
DamagedProducts = []
for item in FullInventory.copy():
    dam_age = item.copy()
    if dam_age['Damaged'] == 'damaged':
        dam_age.pop('Damaged')
        DamagedProducts.append(dam_age)
        writecsv(DamagedProducts, 'DamagedProducts.csv')
DamagedProducts.sort(key=operator.itemgetter('Price'))

###PART 2
##User query interaction
#establish dictionary
data = {'apple': 'apple', 'Apple': 'Apple', 'Lenovo':'Lenovo', 'lenovo':'lenovo'}
itemtypee = {'tower':'tower', 'Tower':'Tower', 'phone':'phone', 'Phone':'Phone', 'laptop':'laptop', 'Laptop':'Laptop'}
#Ask the user for the key using input():
while True:
  manuf = input('Enter the product or q to quit: ')
  if manuf == 'q':
    quit()
  typee = input('Enter the type: ')

  #If keyword in dictionary it'll print
  if manuf in data:
      print('Your item is:', data[manuf], itemtypee[typee])
  else:
      print('No such item in inventory')


