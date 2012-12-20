#Interaction Method
#By Max Novak
#4/24/10
#This class will control all interactions the user can have with the world of ConnQuest
from random import randrange
from Placement import *


class Interaction:

    def __init__(self, invent, location):
        """Sets up the inventory"""
        self.invent=invent
        self.location=location
        self.drop=Placement(location)
    
    def use(self, object):
        """Allows the user to use items they have picked up"""
        if self.invent[object]==1:
            if object=="nerfgun":
                if self.invent["bullets"]==1:
                    print "You load the nerfgun."
                    self.invent["loaded nerfgun"]+=1
                    self.invent["bullets"]+=1
                    self.invent["nerfgun"]+=1
                    return 1
                elif self.invent["bullets"]==0:
                    print "You realize that the nerfgun is empty and essentially useless."
                    return 0
                else:
                    print "You have already loaded the nerfgun."
                    return 0
            if object=="bullets":
                if self.invent['nerfgun']==0:
                    print "You don't have anything to use the bullets with."
                    return 0
                elif self.invent["nerfgun"]==1:
                    print "You load the nerfgun."
                    self.invent["loaded nerfgun"]+=1
                    self.invent["bullets"]+=1
                    self.invent["nerfgun"]+=1
                    return 1
                else:
                    print "You have already loaded the nerfgun."
                    return 0
            if object=="key":
                print "You can' seem to find anything that this key will unlock."
                print "This is the red key..."
                return 0
            else:
                print "You use the " +object+"."
                return 0
        if self.invent[object]==0:
            if object=="panal":
                if self.invent["lamp"]==1:
                    print "You hear some sounds coming from the roof."
                    print "You should go and check it out."
                    self.location["door2"]+=1
                    return 1
        else:
            print "Do what with what?"
            return 0
    def inventory(self):
        """Will display the users inventory"""
        for item in self.invent.keys():
            if self.invent[item] == 1:
                print item


    def take(self, object):
        ##add rooms for objects, not just accessable anywhere
        """Allows the user to take items from their environment"""
        if self.invent.has_key(object):
            if self.invent[object]==0:
                test=self.drop.place(object)
                if test==True:
                    self.invent[object]+=1
                    print "You take "+object+"."
                    if object=="painting":
                        print "You try to take it off the wall, but as soon as you get closer"
                        print "you are so repulsed by the painting that it forces you to back away"
                        return 0
                    if object=="lamp":
                        print "You decide to turn it on, since a lamp that is off is kinda useless."
                        return 0
                    else:
                        return 1
                else:
                    print "There is nothing like that here."
                    return 0
            
            if object=="mail":
                print "You check your mail box, doesn't look like the mail staff"
                print "was willing to fight through the zombies to get to Cro today."
                return 0
            else:
                print "You already have that."
                return 0
        
            
        else:
            print "There isn't anything like that here."
            return 0
        
    def open(self, object):
        """used to open doors and allow access to new rooms"""
        if self.location["NS"]==1 and self.location["EW"]==1 and self.location["UD"]==0:
            if object=="door":
                print "You open the door and zombies come puring in and eat your BRAINZ!!!!"
                print "OH NO!!!"
                print ""
                print ""
                print "ha ha"
                print "Just kidding, why would there be zombies in the basement?"
                self.location["door"]+=1
                return 1
        else:
            print "You don't see any closed doors around here."
            return 0

    def kill(self, object):
        if object=="zombie":
            if self.invent["loaded nerfgun"]==1:
                if self.location["NS"]==2 and self.location["EW"]==-2 and self.location["UD"]==-1:
                    print "You slowly sneak up on the zombie, nerfgun at the ready.  You cock it"
                    print "and prepare to fire.  As you reach for the trigger it turns around and"
                    print "notices you.  You freeze as it charges you. At the last second you"
                    print "gain control of your hand again and closing your eyes you pull the"
                    print "trigger."
                    print ""
                    print "You open your eyes and the zombie lays dead on the floor, a perfect"
                    print "headshot.  Way to go you."
                    self.location["zombie"]+=1
                    return 1
                else:
                    print "There are no zombie here."
                    print "You are safe for now."
                    return 0
            else:
                print "You don't have anything to kill a zombie with."
                print "You need a projectile device, some ammunition, and to load the darn thing."
                return 0
        else:
            print "Sorry, I can't let you kill that."
            return 0

    def read(self, object):
        if object=="book":
            if self.invent["book"]==1:
                print "The title of the book is 'The Zombie Survival Guide', by Max Brooks."
                print "You skim through the book to see if any of it will be helpful."
                print "You find a chapter all about the most efficient ways to kill zombies."
                print "Your knowledge of the world has expanded."
                return 1

        elif object=="flyer":
            if self.invent["flyer"]==1:
                print "ConnQuest was designed and coded by Maxwell Alexander Novak,"
                print "with guidance from Paul Novak and Bridget Baird."
                print "Game Testers include:"
                print "Dann Goldman"
                print "Caroline Mills"
                print "Copyright 2010"
                return 1

        else:
            print "That is not readable, sorry."
            return 0
            
    def eat(self,object):
        if object=="fries":
            if self.invent["fries"]==1:
                print "You eat the curly fries. Yum!"
                print "You feel more energized."
                self.invent["fries"]+=1
                return 1
            else:
                print "You don't have that on your person."
                return 0
        elif object=="pie":
            print "You pull a slice of pie out your pocket dimension and eat it."
            pie=randrange(0,6)
            if pie == 0:
                print "It is apple."
            if pie == 1:
                print "It is blueberry."
            if pie == 2:
                print "It is chocolate cream."
            if pie == 3:
                print "It is strawberry."
            if pie == 4:
                print "It is banana cream."
            if pie == 5:
                print "It is peacan."
            print "YUM!"
            return 0
        else:
            print "Sorry, that isn't edible or you are allergic to it "
            print "or something like that."
            return 0
    
def main(): 
    invent={"pie":0 }
    inter=Interaction(invent)
    inter.take("pie")
    inter.inventory("pie")
    inter.use("pie")



if __name__=="__main__":
    main()
