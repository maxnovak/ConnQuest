#Movement method
#By Max Novak
#4/19/10
#This class will control all movements around the game world

class Direction():

    def __init__(self, location):
        """sets up the location variable"""
        self.location=location 

    def printLocation(self):
        """will display the current location"""
        print self.location 
    
    def north(self):
        """the parameters for northern movement"""
        if self.location["EW"]!=1 and self.location["UD"]!=1:
            if self.location["NS"]<2:
                self.location["NS"]+=1
            else:
                print "Can't go that way."
        else:
            print "Can't go that way."

    def south(self):
        """the parameters for southern movement"""
        if self.location["EW"]!=1 and self.location["UD"]!=1:
            if self.location["NS"]>0:
                self.location["NS"]+=-1
            else:
                print "Can't go that way."
        else:
            print "Can't go that way."

    def east(self):
        """the parameters for eastern movement"""
        if self.location["UD"]==-1:
            if self.location["NS"]==0:
                if self.location["EW"]>-2 and self.location["EW"]<=0:
                    self.location["EW"]+=-1
                else:
                    print "Can't go that way."
            if self.location["NS"]==1:
                if self.location["EW"]<=1 and self.location["EW"]>-2:
                    self.location["EW"]+=-1
            if self.location["NS"]==2:
                print "Can't go that way."
        if self.location["UD"]==0:
            if self.location["NS"]==1:
                if self.location["EW"]==1:
                    self.location["EW"]+=-1
                else:
                    print "Can't go that way."
            else:
                print "Can't go that way."
        if self.location["UD"]==1:
            print "Can't go that way."

    def west(self):
        """the parameters for western movement"""
        if self.location["UD"]==-1:
            if self.location["NS"]==0:
                if self.location["EW"]>=-2 and self.location["EW"]<0:
                    self.location["EW"]+=1
                else:
                    print "Can't go that way."
            if self.location["NS"]==1:
                if self.location["EW"]>=-2 and self.location["EW"]<1:
                    self.location["EW"]+=1
            if self.location["NS"]==2:
                print "Can't go that way."
        if self.location["UD"]==0:
            if self.location["NS"]==1:
                if self.location["EW"]==0:
                    self.location["EW"]+=1
                else:
                    print "Can't go that way."
            else:
                print "Can't go that way."
        if self.location["UD"]==1:
            print "Can't go that way."

    def up(self):
        """the parameters for moving up"""
        if self.location["NS"]==1 and self.location["EW"]==1 and self.location["UD"]==-1:
            self.location["UD"]+=1
        if self.location["NS"]==1 and self.location["EW"]==0 and self.location["UD"]==0:
            self.location["UD"]+=1
        else:
            print "Can't go that way."
            
    def down(self):
        """the parameters for moving down"""
        if self.location["NS"]==1 and self.location["EW"]==1 and self.location["UD"]==0:
            self.location["UD"]+=-1
        if self.location["NS"]==1 and self.location["EW"]==0 and self.location["UD"]==1:
            self.location["UD"]+=-1
        else:
            print "Can't go that way."
    
def main():
    location={"NS":0,"EW":0,"UD":0}
    space=Direction(location)
    while True:
        word=raw_input("direction: ")
        if word == "north":
            space.north()
        if word == "south":
            space.south()
        if word == "east":
            space.east()
        if word == "west":
            space.west()
        if word == "up":
            space.up()
        if word == "down":
            space.down()
        space.printLocation()


if __name__=="__main__":
    main()
