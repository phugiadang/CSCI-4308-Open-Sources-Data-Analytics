months1 = ["04", "06", "09", "11"]

def isLeapYear(date):
    year = int(date[0]+date[1]+date[2]+date[3])
    if (year % 4 == 0):
        return True
    return False


def changeYear(date):
    month = int(date[4]+date[5])
    if (month == 13):
        return str(int(date) + 8800000000)   
    return date


def changeMonth(date):
    
    if (date[6] == '2' and date[7] == '9' and isLeapYear(date) == False):
       return str(int(date) + 72000000)  


    if (date[6] == '3' and date[7] == '0'):
        if (isLeapYear(date) == True):
            return str(int(date) + 71000000)
        


    if (date[6] == '3' and int(date[7]) >= 1):
        month = date[4] + date[5]
        if month in months1:
            return changeYear(str(int(date) + 70000000))
        if (int(date[7]) == 2):
            return changeYear(str(int(date) + 69000000))
                     
    return date


def changeDay(date):
 
    if (date[6] == '2' and date[7] == '9'):
        return changeMonth(date)
        

    if ((date[6] == '3') and (int(date[7]) >= 0)):
        return changeMonth(date)
    
    return date#str(int(date) + 1000000)


def changeHour1(date):
    new_date = str(int(date) + 760000)
    return changeDay(new_date)


def changeHour(date):
    #new_date = str(int(date) + 10000)
    new_date = str(int(date) + 4000)
    if ((new_date[8] == '2') and (new_date[9] == '4')):
        return changeHour1(new_date)
    #new_end_date = str(int(new_end_date) + 760000)
    return new_date


def changeMinute(date):
    new_date = str(int(date) + 100)
    if (new_date[10] == '6'):
        return changeHour(new_date)
    return new_date
 

