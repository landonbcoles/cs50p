months = [
       "January", 
       "February", 
       "March", 
       "April", 
       "May", 
       "June",
       "July", 
       "August", 
       "September", 
       "October", 
       "November", 
       "December"
]

def findMonth(m):
        for i, name in enumerate(months):
            if name == m:
                m = i + 1   
                return(m)
            
        return -1

while True:
    date = input("Date: ").strip()
    if date.find("/") == -1:
        date = date.replace(",", "")
        month, day, year = date.split(" ")
        month.title()

        if findMonth(month) == -1:
             pass

        if int(day) > 31 or int(day) < 1:
             pass

        if int(year) < 1:
             pass

        print(str(year) + "-" + str(findMonth(month)) + "-" + str(day))
        break
    else: 
        m, d, y = date.split("/")

        if int(m) > 12 or int(m) < 1:
             pass

        if int(d) > 31 or int(d) < 1:
             pass

        if int(y) < 1:
             pass

        print(str(y) + "-" + str(m) + "-" + str(d))
        break

