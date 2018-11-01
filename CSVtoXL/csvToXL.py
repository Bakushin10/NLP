import sys
import csv
import glob
import codecs
#C:\Users\shin\Documents\excel\accounts.csv
#C:\Users\shin\Documents\excel\empList.csv

class CSVtoExcel:
    __pathToCSVFile = ""

    def getPath(self):
        targetPath ="."
        if len(sys.argv) == 2: # check if there is an argument for path
            self.__pathToCSVFile = str(sys.argv[1])
            print("path : " + self.__pathToCSVFile)
            return True
        else:
            return False

    def readCSV(self):
        with codecs.open(self.__pathToCSVFile,"r",encoding='utf-8', errors='ignore') as file:
            csvread= csv.reader(file,delimiter='\t')
            print(csvread)
            for i in csvread:
                print(i)

###
### main
###
CSVtoXL = CSVtoExcel()

if(CSVtoXL.getPath()):
    CSVtoXL.readCSV()
else:
    print("*******************************************************************************\n")
    print("*** Please enter a path to the .csv file you would like to covert into .exl ***\n")
    print("*******************************************************************************\n")
