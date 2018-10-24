import sys
import csv
import codecs
#C:\Users\shin\Documents\excel\accounts.csv

class CSVtoExcel:
    __pathToCSVFile = ""

    def getPath(self):
        targetPath ="."
        if len(sys.argv) == 2: # check if there is an argument for path
            self.__pathToCSVFile = str(sys.argv[1])
            print("path : " + self.__pathToCSVFile)
            return True
        else:
            print("*******************************************************************************\n")
            print("*** Please enter a path to the .csv file you would like to covert into .exl ***\n")
            print("*******************************************************************************\n")
            return False

    def readCSV(self):
        with open(self.__pathToCSVFile, mode='rb') as fobj:
            readFile = csv.reader((line.replace('\0','') for line in fobj))
            readFile = list(readFile)
            print(readFile)

CSVtoXL = CSVtoExcel()

if(CSVtoXL.getPath()):
    CSVtoXL.readCSV()


