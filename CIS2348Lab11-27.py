#Chris Rubio
#1530668

def printRoster():
   keys = list(players.keys())

   keys.sort()

   
   print("ROSTER")
   for key in keys:
       print("Jersey number: %d, Rating: %d" %(key,players[key]))

players = {}

for i in range(5):   
   j_num = int(input("Enter player %d's jersey number:\n" %(i+1)))
  
   players[j_num] = int(input("Enter player %d's rating:\n" %(i+1)))
  
   print("")
  


printRoster()

while True:
   
   print("\nMENU\na - Add player\nd - Remove player\nu - Update player rating\nr - Output players above a rating\no - Output roster\nq - Quit\n")
     
   option = input("Choose an option:\n")
  
     
   if option == 'o':
       printRoster()
        
   elif option == 'a':       
       j_num = int(input("Enter a new player's jersey number:\n"))
            
       rating = int(input("Enter the player's rating:\n"))
             
       players[j_num] = rating
     
   elif option == 'd':       
       j_num = int(input("Enter a player's jersey number:\n"))
             
       if j_num in list(players.keys()):          
           del players[j_num]
  
   # if user option is 'u'
   elif option == 'u':       
       j_num = int(input("Enter a player's jersey number:\n"))
      
       rating = int(input("Enter a new rating for player:\n"))
            
       players[j_num] = rating
      
   elif option == 'r':       
       rating = int(input("Enter a rating:\n"))
             
       keys = list(players.keys())
     
       keys.sort()
       
       print("\nABOVE %d" %(rating))
      
       count = 0
       for key in keys:          
           if(players[key]>rating):
               print("Jersey number: %d, Rating: %d" %(key,players[key]))
                            
               count +=1
             
       if(count == 0):
           print("No players found above %d rating" %(rating))
      
     
   if option == "q":
       break
