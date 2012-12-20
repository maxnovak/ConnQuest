#Look method
#By Max Novak
#4/24/10
#This class will give the user information about the environment

class Location:

    def __init__(self, location, inventory):
        """sets up the location of the user and the objects in the rooms"""
        self.location=location
        self.inventory=inventory

    def Look(self):#The if statements will determine if the user has taken objects or opened doors etc. and display the world for them.
        """Will display a room discription for the user"""
        """Certain items will only appear dependent upon if the user has them in the inventory or not"""
        if self.location["NS"]==0 and self.location["EW"]==0 and self.location["UD"]==0:
            print ""
            print "You are standing at the entrance to Oasis. It seems like"
            print "a ghost town, no one is around."
            print "There is a walkway leading to the north."
            print "Outside are hordes of zombies."
            if self.inventory["fries"]==0:
                print "There are some fries on the table."
            if self.inventory["flyer"]==1:
                print ""
            elif self.inventory["fries"]>=1:
                print "You notice a flyer that was under the fries."
                
        elif self.location["NS"]==1 and self.location["EW"]==0 and self.location["UD"]==0:
            print ""
            print "You are standing in the foyer at Cro."
            print "The mail room is to the north, the '62 room is to the west,"
            print "and the entrance to Cro is to the east. The door has been"
            print "locked because of the zombies outside, which keeps you"
            print "safe from their insatiable hunger."
            print "There are some stairs leading up to the second floor."
            print "Oasis is back to the south."

        elif self.location["NS"]==2 and self.location["EW"]==0 and self.location["UD"]==0:
            print ""
            print "You are standing in the mailroom."
            print "Yay, mail!"
            print "The foyer is to the south."
            if self.inventory["nerfgun"]==0:
                print "There is a nerfgun on the counter."
                
        elif self.location["NS"]==1 and self.location["EW"]==1 and self.location["UD"]==0:
            print ""
            print "You are in the '62 room."
            print "The foyer is back to the east."
            if self.location["door"]==0:
                print "You notice a door that is slightly ajar."
            elif self.location["door"]==1:
                print "There is a path leading down to the basement."
                
        elif self.location["NS"]==1 and self.location["EW"]==0 and self.location["UD"]==1:
            print ""
            if self.location["door2"]>=1:
                print "You notice a door that wasn't here before, and it looks unlocked."
                print "You open the door and run onto the roof of Cro.  The zombies are climbing"
                print "Up the walls and it looks like they will soon be able to get inside."
                print "You hear a sound coming from the distance and look up. There is a helicopter"
                print "flying over towards the roof.  When they are over head they begin to pick off"
                print "the nearest zombies, while lowering a ladder to you.  You grab on and climb up."
                print "Once you are inside the helicopter begins to leave the infested campus and you"
                print "look back thinking about a day when you will return and clear the campus of "
                print "zombies for good. So that students may once again attend Connecticut College."
                print "But for now your quest is at an end."
                return False
            else:
                print "You are on the second floor in Cro's nest."
                print "Sadly there is nothing going on in Cro's nest today, but that"
                print "might be related to the zombie outbreak."
                print "The Foyer is back down the stairs."
                if self.inventory["book"]==0:
                    print "You notice a torn up book on the floor."
                
                
        elif self.location["NS"]==1 and self.location["EW"]==1 and self.location["UD"]==-1:
            print ""
            print "You are in the basement of Cro. Most people don't even know that Cro has"
            print "a basement, and you found it."
            print "Go you!"
            print "There is a set of stairs heading back up."
            print "There is a doorway leading to the east."
            if self.inventory["bullets"]==0:
                print "There are some nerf bullets laying on the floor."

        elif self.location["NS"]==1 and self.location["EW"]==0 and self.location["UD"]==-1:
            print ""
            print "Wow who knew the basement was such a maze, if you enter here you might"
            print "not get back out alive. So be sure to make a map."
            print "There are hall ways leading in all directions. (North, south, east, and"
            print "west that is)"

        elif self.location["NS"]==0 and self.location["EW"]==0 and self.location["UD"]==-1:
            print ""
            print "You enter a pretty dreary looking room.  It has white plaster walls"
            print "and the uliest painting you have ever seen on the wall, it might be worth"
            print "a lot of money though..."
            print "There are doorways leading to the north and east."

        elif self.location["NS"]==2 and self.location["EW"]==0 and self.location["UD"]==-1:
            print ""
            print "A dead end."
            print "The hallway is back to the south."
            if self.inventory["key"]==0:
                print "Hey, look there is a key on the floor."
                print "You should pick that up."
                print "There is a doorway back to the south."

        elif self.location["NS"]==2 and self.location["EW"]==-1 and self.location["UD"]==-1:
            if self.inventory["lamp"]==0:
                print ""
                print "Wow, this room is really dark, your likely to be eaten by a zombie"
                print "if you don't leave soon."
                print "There is a doorway back to the south."
            if self.inventory["lamp"]==1:
                print ""
                print "Your lamp lights up the room and you can see lots of interesting stuff."
                print "You look around and see a lot of electrical panals."
                print "One of them says roof access."
                
        elif self.location["NS"]==1 and self.location["EW"]==-1 and self.location["UD"]==-1:
            print ""
            print "White room, white walls, white floor.  This is a boring room, lets find"
            print "somewhere cooler."
            print "There be exits to the north, south, east, and west of here."

        elif self.location["NS"]==0 and self.location["EW"]==-1 and self.location["UD"]==-1:
            print ""
            print "In the white room with no curtains in the basement of Cro is where you stand now."
            print "There are exits to the north, east, and west of here."

        elif self.location["NS"]==0 and self.location["EW"]==-2 and self.location["UD"]==-1:
            print ""
            print "Hey, there is a chest here, now if only you had the blue key..."
            print "The doorways lead to the west and north."

        elif self.location["NS"]==1 and self.location["EW"]==-2 and self.location["UD"]==-1:
            print ""
            print "Another plain old room..."
            print "There is a door leading to the north that says 'Kitchen' on it."
            print "There are also hallways leading to the west and south."

        elif self.location["NS"]==2 and self.location["EW"]==-2 and self.location["UD"]==-1:
            if self.location["zombie"]==0:
                print ""
                print "There is a zombie in the corner raiding the frige.  Luckily he hasn't"
                print "seen you yet, you should slowly back out unless you want to try to kill him."

            else:
                print ""
                print "There is a zombie corpse laying on the ground.  It is starting to smell."
                if self.inventory["lamp"]==0:
                    print "You notice a lamp on the table."
                print "There is an exit back to the south."


            

            


        

def main():
    location={"NS":2,"EW":0,"UD":0, "door":1}
    inventory={"nerfgun":0,"book":0,"bullets":0,"flyer":0,"fries":0}
    room=Location(location)
    room.Look(inventory)
    

if __name__=="__main__":
    main()
