#Connquest 3.0
#By Max Novak

from Direction import *
from Location import *
from Interaction import *
from random import randrange
import string

def main():
    location={"NS":0,"EW":0,"UD":0,"door":0,"zombie":0, "door2":0}#sets up variables
    invent={"nerfgun":0, "book":0, "bullets":0, "flyer":0, "fries":0, "key":0, "lamp":0, "loaded nerfgun":0, "panal":0}
    basenoise=0
    score=0
    space=Direction(location)#sets up the classes being used
    inter=Interaction(invent, location)
    direct={"north":space.north, "n":space.north, "south":space.south, "s":space.south,
            "east":space.east, "e":space.east, "west":space.west,
            "west":space.west, "up":space.up, "u":space.up,
            "down":space.down, "d":space.down}#sets up the dictionaries that are being used as checks for valid commands
    interact={"inventory":inter.inventory, "help":"", "use":inter.use, "take":inter.take, "open":inter.open, "kill":inter.kill, "read":inter.read, "eat":inter.eat}
    print "Welcome to ConnQuest, an text based andventure game." # Intro text
    print "The way the game works is through simple one word commands for "
    print "direction, like north, south, east, west, up, or down."
    print "To interact with an object you use simple commands like "
    print "'use sword' or 'eat pie' etc. if you can't figure out how to"
    print "do something try rephrasing it or type help to get a list of "
    print "avalable commands.  Hope you have a good time."
    print "Good luck..."
    print ""
    print ""
    while True:
        inter=Interaction(invent, location)
        room=Location(location, invent)#establishes the room the user is in
        phase=room.Look()
        if phase==False:
            break
        noise=randrange(basenoise,10)#adds a random function that will add in comments about the surroundings, which change over time
        if noise==5: 
            print "The zombies are clawing at the windows and groaning hungrily for your brains!"
            if basenoise<=9:
                basenoise+=1
            if basenoise>=5 and basenoise<=9:
                print "The noises seem to be getting louder."
            if basenoise==9 and firsttime==0:
                print "The amount of zombies seems to have increased by tenfold from earlier."
                print "They must have finished off everyone else on campus."
                firsttime+=1

        command=raw_input("Command: ")#commands entered here
        if command=="":
            print "I don't understand that."
        else:
            command=string.lower(command)#convert to lowercase for ease
            command=string.split(command)#splits the command into words
            if direct.has_key(command[0])==True:#checks to see if it is a valid command
                direct[command[0]]()
            elif interact.has_key(command[0])==True:
                if command[0]=="inventory":
                    interact[command[0]]()
                if command[0]=="help":
                    print interact.keys()
                else:
                    score+=interact[command[0]](command[1])
            else:
                print "I don't understand that."
        #space.printLocation()
    print "Congradulations, you have survived ConnQuest."
    print "Your score is:", score,"."
main()
