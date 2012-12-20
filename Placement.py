#Placement method
#By Max Novak
#5/5/10
#This class will control the location of all of the items one can pick up in the game world.

class Placement:

    def __init__(self,location):
        self.location=location

    def place(self, item):
        """sets up the location that all items that get picked up are at."""
        if self.location["NS"]==0 and self.location["EW"]==0 and self.location["UD"]==0:
            if item=="flyer" or item=="fries":
                return True
        if self.location["NS"]==2 and self.location["EW"]==0 and self.location["UD"]==0:
            if item=="nerfgun":
                return True
        if self.location["NS"]==1 and self.location["EW"]==1 and self.location["UD"]==-1:
            if item=="bullets":
                return True
        if self.location["NS"]==2 and self.location["EW"]==0 and self.location["UD"]==-1:
            if item=="key":
                return True
        if self.location["NS"]==2 and self.location["EW"]==-2 and self.location["UD"]==-1:
            if item=="lamp":
                return True
        if self.location["NS"]==1 and self.location["EW"]==0 and self.location["UD"]==1:
            if item=="book":
                return True
        if self.location["NS"]==0 and self.location["EW"]==0 and self.location["UD"]==-1:
            if item =="painting":
                return False
        else:
            return False
        
