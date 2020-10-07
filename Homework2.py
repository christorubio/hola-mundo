#Chris Rubio
#1530668

def find(da_te):
   
   monthList = {"January": 1,"February": 2,"March": 3,"April": 4,"May": 5,"June": 6,"July": 7,"August": 8,"September": 9,"October": 10,"Novenber": 11,"December": 12}
   try:
      year = da_te.split(",")[-1].strip() 
      month = da_te.split(",")[0].split()[0] 
      day = da_te.split(",")[0].split()[-1] 
      mes = monthList[month] 
      int(year)
      int(day)
      return str(mes)+"/"+day+"/"+year
   except:
      return ""

with open("inputDates.txt") as f: 
   for x in f.readlines():  
      if x.strip() != "-1": 
         res = find(x.strip()) 
         if res != "": 
            with open("parsedDates.txt","a+") as w:
               w.write(res+"\n") 
