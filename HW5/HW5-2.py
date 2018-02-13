
class GainsevilleAddress:
    ___addressStart = 1
    ___addressEnd = 99999
    ___streetNumber = 999
    ___zipStart = 00
    ___zipEnd = 19
    ___directionalIndicator = ["N", "NW", "NE", "SW", "S", "W", "E"]
    ___streetIndicator = ["ST", "ND", "RD", "TH"]
    ___roadType = ["RD", "AVE", "DR", "TERR", "ST", "CIR"]
    ___cityName = "Gainesville"
    ___state = "FL"

    def getAddress(self):
        address = "1105 NW 3rd AVE, Gainesville, FL, 32618"
        addressList = address.split()
        self.checkAddress(addressList)

    def checkAddress(self, address):
            print(address)
            if self.checkStreetNumber(address[0]) is not True:
                print("invalid street Number")
                return

            if self.checkDirectionalIndicator(address[1]) is not True:
                print("invalid directional indicator")
                return

            if self.checkStreetName(address[2]) is not True:
                print("invalid street name")
                return

            if self.checkRoadType(address[3]) is not True:
                print("invalid road name")
                return

            if self.checkStateAndZip(address) is not True:
                print("invalid state and zip")
            else:
                print("valid address")

    def checkStreetNumber(self,streetNumber):
        if int(streetNumber) > self.___addressStart and int(streetNumber) < self.___addressEnd:
            return True
        else:
            return False

    def checkDirectionalIndicator(self, directionalIndicator):
        for di in self.___directionalIndicator:
            if directionalIndicator.upper() == di:
                return True
        return False

    def checkStreetName(self, streetName):
        snumber = ""
        sName = ""
        for i in streetName:
            if i.isdigit():
                snumber += i
            else:
                sName += i

        if int(snumber) < self.___addressStart or int(snumber) > self.___streetNumber:
            return False

        for i in self.___streetIndicator:
            if i == sName.upper():
                return True
        return False

    def checkRoadType(self, roadType):
        roadType = roadType.replace("," , "")
        for i in self.___roadType:
            if roadType.upper() == i:
                return True
        return False

    def checkStateAndZip(self, str):
        #print (len(str))
        newlist = ""
        for a in range(len(str)):
            if(a > 3):
                temp = str[a].replace("," , "")
                newlist += temp+" "
        newlist = newlist.split()
        lastTwoDigit = newlist[2][3] + newlist[2][4]
        if newlist[0] != self.___cityName or newlist[1] != self.___state:
            return False
        if int(lastTwoDigit) > self.___zipEnd or int(lastTwoDigit) < self.___zipStart:
            return False
        return True

address = GainsevilleAddress();

address.getAddress();
