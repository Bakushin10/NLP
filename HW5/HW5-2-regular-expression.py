#
#   2/16/2018
#   HW 5.2 address
#   Shin Nagai
#
#
#

import re

class GainsevilleAddress:

    def getAddress(self):
        address = input('enter address : ')
        address = address.upper();
        #print(address)
        isValid = re.findall(r'(\d{1,5}\s+(NW|NE|N|SW|SE|S|W|E)\s+\d{1,3}(ST|ND|RD|TH)\s+(RD|AVE|DR|TERR|ST|CIR)(,)\s(GAINESVILLE, FL)\s(326)[0-1][0-9])',address)
        if isValid != []:
            print("valid address : ")
            for i in isValid:
                print (i)
        else:
            print("invalid address")


addr = GainsevilleAddress();

addr.getAddress();
