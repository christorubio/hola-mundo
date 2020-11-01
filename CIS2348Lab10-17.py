#Chris Rubio
#1530668

class ItemToPurchase:
  def __init__(self):
    self.item_name = 'none'
    self.item_quantity = 0 
    self.item_price = 0.0

  def print_item_cost(self):
    print(self.item_name +" "+ str(self.item_quantity) + " @ $" + str(self.item_price) + " = $" + str(self.item_quantity * self.item_price))

if __name__ == "__main__":
  print("Item 1")
  firstitem = ItemToPurchase()
  firstitem.item_name = input("Enter the item name:\n")
  firstitem.item_price = int(input("Enter the item price:\n"))
  firstitem.item_quantity = int(input("Enter the item quantity:\n"))

  print("\nItem 2")
  seconditem = ItemToPurchase()
  seconditem.item_name = input("Enter the item name:\n")
  seconditem.item_price = int(input("Enter the item price:\n"))
  seconditem.item_quantity = int(input("Enter the item quantity:\n"))

  total = (firstitem.item_price * firstitem.item_quantity) +  (seconditem.item_price * seconditem.item_quantity)

  print("\nTOTAL COST")
  firstitem.print_item_cost()
  seconditem.print_item_cost()

  print("\nTotal: $" + str(total))
