import re

#
# question 2 using regular expression
#

#address = "301 SE 445th Ave, Gainesville, FL 32601"#"1105 NW 3rd AVE, Gainesville, FL 32618"

#directionalIndicator = re.compile(r'(ST|ND|RD|TH|st|nd|rd|th)')
class GainsevilleAddress:

    def getAddress(self):
        address = input('enter address : ')
        address = address.upper();
        #print(address)
        isValid = re.findall(r'(\d{1,5}\s+(NW|NE|N|SW|SE|S|W|E)\s+\d{1,3}(ST|ND|RD|TH)\s+(RD|AVE|DR|TERR|ST|CIR)(.)\s(GAINESVILLE, FL)\s\d{3}[0-1][0-9])',address)
        if isValid != []:
            print("valid address : ")
            for i in isValid:
                print (i)
        else:
            print("invalid address")


addr = GainsevilleAddress();

addr.getAddress();
