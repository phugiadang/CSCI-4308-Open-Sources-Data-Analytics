import sys, csv

date = '20160101'
if (len(sys.argv) == 2):
    date = sys.argv[1]

list_of_candidates=["kasich","bush","trump","clinton","sanders","cruz","carson","rubio"]


for name in list_of_candidates:

    #ex. open carson20160306.tsv
    count = 0
    with open("/VOLUME/GDELT/"+name+date+".tsv") as tsv_file:
        for line in csv.reader(tsv_file, dialect="excel-tab"):
            count +=1
        print "%s: %d" % (name, count)
