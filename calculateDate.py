import sys

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

    if (date[6] == '2' and date[7] == '9' and isLeapYear(date) == False and date[4]+date[5] == '02'):
       return str(int(date) + 72000000)


    if (date[6] == '3' and date[7] == '0'):
        if (isLeapYear(date) == True and date[4]+date[5] == '02'):
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
    date = date.replace("\n","")
    new_date = str(int(date) + 100)
    if (new_date[10] == '6'):
        return changeHour(new_date)
    return new_date

def subMinute(date):
    a = '20160101000000'
    while (a != date):
        new_date = changeMinute(a)
        if (new_date == date):
            return a
        a = new_date

def subHour(date):
    a = '20160101000000'

    #This if/else clause is used for speedup, by starting out with a closer date
    if (date[4] == '0'):
        if (int(date[5]) < 4):
            a = a
        else:
            a = '20160'+str(int(date[5])-2)+'01000000'
    else:
        if (int(date[5]) < 11):
            a = '20160901000000'
        else:
            a ='20161'+str(int(date[5])-2)+'01000000'

    b = ''
    while (a != date):
        new_date = changeMinute(a)
        junk = new_date
        for i in range(0, 60):
            b = changeMinute(junk)
            junk = b
        if (b == date):
            return new_date
        a = new_date

def subDay(date):
    a = '20160101000000'

    #This if/else clause is used for speedup, by starting out with a closer date
    if (date[4] == '0'):
        if (int(date[5]) < 4):
            a = a
        else:
            a = '20160'+str(int(date[5])-2)+'01000000'
    else:
        if (int(date[5]) < 11):
            a = '20160901000000'
        else:
            a ='20161'+str(int(date[5])-2)+'01000000'

    b = ''
    while (a != date):
        
        new_date = changeMinute(a)
        junk = new_date
        for i in range(0, 1440):
            b = changeMinute(junk)
            junk = b
        
        if (b == date):
            return new_date
        a = new_date
    return b 
def subWeek(date):
    a = '20160101000000'

    #This if/else clause is used for speedup, by starting out with a closer date
    if (date[4] == '0'):
        if (int(date[5]) < 4):
            a = a
        else:
            a = '20160'+str(int(date[5])-2)+'01000000'
    else:
        if (int(date[5]) < 11):
            a = '20160901000000'
        else:
            a ='20161'+str(int(date[5])-2)+'01000000'

    b = ''
    while (a != date):
        new_date = changeMinute(a)
        junk = new_date
        for i in range(0, 10080):
            b = changeMinute(junk)
            junk = b
        if (b == date):
            return new_date
        a = new_date



if (len(sys.argv) == 3):
    if (sys.argv[1] == "-subDay"):
        print subDay(sys.argv[2])

#print subDay("20160103000000")
