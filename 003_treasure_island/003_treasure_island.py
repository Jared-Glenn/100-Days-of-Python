print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("There's treasure on that island over there.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

path1 = None
path2 = None
path3 = None
path4 = None

print("After rowing ashore, you find yourself on a beach. Nearby footprints move to the left, following a path inland. You also see a movement in the bushes to your right. They shake like something saw you and started running away.")
path1 = input("Do you follow the footprints INLAND or CHASE the creature in the bushes?").lower()

if path1 == "inland":
    print("The path is dense with foliage and you struggle to stay with the footprints, but, in the end it spits you out into a field of rolling hills.")
    print("You see a cabin built of palm logs with smoke rising from a hole in the roof. In the other direction, you see a sparkling lagoon, filled with blue water and leaping fish.")
    path2 = input("Do you visit the LAGOON or the CABIN?").lower()
else:
    print("Worried about what already might be watching you, you burst after the watcher. Crashing into the underbrush, you suddenly realize that there might be more than one watcher!")
    print("You see the shaking underbrush continue along two different paths, something red just visible between the branches. One of the watchers seems to be moving toward a pillar of smoke rising above the trees. The other seems to have followed a darker path, full of crags and crevases.")
    path2 = input("Do you run toward the SMOKE or the DARK path?").lower()
    if path2 == "smoke":
        print("You burst out of the jungle, finding yourself looking down on a field of rolling hills. Up ahead, you can see a cabin made of palm logs with smoke rising from a hole in the roof.")
        path2 = "cabin"

if path2 == "dark":
    print("You see something red slip into a crevass and hurry after it. The light fades quickly, but a quickly lit torch soon fills the cavern with light. There's an oddly misty quality to the air here, like you can't see very far. Ahead, the cavern splits into three passages.")
    print("One passage, to the left, feels oddly wet, the stone slick beneath your feet, but, at least, it smells of fresh, clean water. To the right, you can see thin prints in the muddy soil, like the watcher you were following was walking on stilts. The middle passage smells foul and looks dark.")
    path3 = input("Do you go to the LEFT, MIDDLE, or RIGHT?").lower()
    if path3 == "left":
        print("You remember hearing somewhere that, when lost, its best to follow one's nose, so that's what you do. The cavern eventually leads into the light of a beautiful oasis. Just ahead, you see a sparkling lagoon, filled with blue water and leaping fish.")
        path3 = "lagoon"
    if path3 == "middle":
        print("Almost as a joke, you decide to continue into the dark and dank cave. Nothing but terrible smelling air greets you. No signs of life. No light. And, in the end, no way out. You try to backtrack, but must have gotten turned around. You stop and rest to regain your bearings, but they never return. You live longer than the torch, but not by much. In the end, your quest ended not in the brilliance of riches, but in the eternal darkness of stone.")
    if path3 == "right":
        print("You walk into the right tunnel, looking closely at the prints in the mud. Thin, like someone was stabbing the earth itself. You feel something stick to your face and look up. Your heart seems to drop out of your chest as you realize it is a spider web - and not a thin one. Whatever spun this web wasn't looking to catch flies. You try to push it away, but to no avail. You feel yourself suddenly trapped. A skittering sound echoes up the cavern and you see the red you were following creep out of the darkness. A massive, red-marked spider. It moves quickly, paralyzing you with a single bite. From there, though, the process is slow, and you do not die for several days as you are slowly fed on, the newest meal for the guardians of Treasure Island.")



if path2 == "cabin":
    method2 = input("Do you want to approach the cabin QUIETLY or go in with GUNS blazing?").lower()
    if method2 == "gun" or method2 == "guns":
        print("You run down the hill at full speed and kick in the door. There, you find a tall figure, dressed in a red coat and carrying a sword. A pirate! He seems to be examining a treasure chest, hurriedly trying to get it open.")
    if method2 == "quietly" or method2 == "quiet":
        print("You sneak down toward the cabin, trying to not be noticed by anyone who might be inside. Reaching the door of the cabin, you find it unlocked. Cracking the door, you can see a tall figure, dressed in a red coat and carrying a sword. A pirate! He seems to be examining a treasure chest, hurriedly trying to get it open.")
        method2 = input("Do you try to get the DROP on him, offer to HELP him, or WAIT to see what happens?").lower()
        if method2 == "drop":
            print("You kick in the door, grabbing your weapons.")

    if method2 == "guns" or method2 == "gun" or method2 == "drop":
        print("The pirate turns around in confusion and fear, but you've already fired on him and a moment later you're alone with the chest. You notice the stench of death in this room and not just from the pirate. Perhaps there is a wicked curse on the chest and you should flee now!")
        path3 = input("Do you ABANDON your quest and leave the island, go back OUTSIDE to explore some more, or OPEN the chest?").lower()
        if path3 == "outside":
            print("Determining that something is off, you return outside and can see a sparkling lagoon, filled with blue water and leaping fish in the distance. Behind you, the path back to the beach and your ship.")
            path3 == input("Do you try to examine the LAGOON or RETURN to your ship?").lower()
            if path3 == "return":
                path3 = "abandon"
        
        if path3 == "open":
            print("You bend over and carefully begin examining the chest. It takes some time, but in the end you get the lid open ... but the box is empty! Or nearly so. A smell fills your nostrils as you catch your breath with surprise. Poison! You stumble out of the house, desperate for clean air, but your throat closes and you never get another chance to taste it. A trap, after all. Blood was the price of treasure today, and indeed you paid it in full ....")

    if method2 == "help":
        print("Cautiously, you open the door and announce yourself to the pirate. He turns around, surprised, but is willing to hear you out once you offer to help him open the chest. A 50-50 split seems more than fair and you both agree to it. He steps aside and gives you room to offer your assistance.")
        print("You bend over and carefully begin examining the chest. Together, you manage to get the lid open ... but the box is empty! Or nearly so. A smell fills your nostrils as you catch your breath with surprise. Poison! You and the pirate stare at each other in shock and then try to stumble out of the house, desperate for clean air, but it's too late for both of you. Your throat closes and you never get another chance to taste the outside air. A trap, after all. Blood was the price of treasure today, and indeed you paid it in full ....")
    
    if method2 == "wait":
        print("The pirate is horribly slow at opening the chest, but in the end he gets it open. You watch with rapt attention, hoping to see what it is that he found, but his shocked gasp reveals that the box was actually empty! Well, nearly so. Suddenly, he is gasping in pain and shock. Poison! He stumbles toward the door and bursts into the open air. He never gets to taste that air again, though. You back away, seeing the life leave his body and catching the faintest whiff of the poison on the breeze, you decide not to enter the cabin.")
        print("Returning to your ship suddenly doesn't seem like such a bad plan, considering this death trap, but then you see a beautiful lagoon in the distance, full of crystal blue water and jumping fish.")
        path3 = input("Do you RETURN to your ship or continue to explore at the LAGOON?").lower()
        if path3 == "return":
            path3 = "abandon"
    
    if path3 == "abandon":
        print("You make your way back to your boat. It wasn't worth it. There was more blood on that chest than just the pirate's and you have a hunch that if you had stayed, it would have claimed yours as well. Now, though, you're safe and returning to your ship. Treasure - real treasure - awaits!")


if path2 == "lagoon" or path3 == "lagoon":
    print("The lagoon is more beautiful than anything you've ever seen with happy looking fish swimming and leaping about, flitting over the white rocks at the base of the lagoon. Looking around, you notice something on the shore. A dead pirate! He seems to have been shot in the head in a piratical disagreement of some sort. But then you also notice something in the water. A treasure chest! It is only about ten feet under water and looks light enough to carry, even if it might take a few trips.")
    path4 = input("Do you SWIM in after the treasure chest or examine the dead PIRATE?").lower()

if path4 == "pirate":
    print("You approach the fallen pirate. There's a tragic air to his posture, like he wasn't expecting the attack that killed him. He has a single flintlock pistol on him and a silver coin. You wonder if you ought to pay your last respects somehow. You know pirates like to buried at sea, but you wonder if a pirate's last wishes are worth ruining the beauty of this lagoon.")
    path4 = input("Do you THROW the dead pirate into the lagoon or leave him where he is and SWIM down to the treasure chest?").lower()

if path4 == "swim":
    print("You lower yourself into the pond and begin to swim toward the chest, feeling the fish surge around you, clearly enjoying your presence. You suddenly feel a nip in your shoulder and turn your head to see blood in the water. One of the fish attacked you! Surprised, you look around and realize that other fish are closing in. You have a brief moment to realize that you're surrounded by the treasure's guardians before they attack. In the minutes before you are stripped clean, you look down at the white stones and recognise them for what they are - the bones of treasure hunters just like you. Now you, like many before, will serve as a hidden warning to future treasure hunters. You hope the next visitor notices.")
    
if path4 == "throw":
    print("You decide to honor the pirate's final wishes and throw him into the lagoon. For a moment, it feels very peaceful, but only for a moment. Suddenly, a fish approaches the body and rips a piece of flesh off. Within moments, the entire pond of fish have joined the feeding frenzy and not a single fish remains elsewhere in the pond. You realize that these are the guardians of the treasure and recognise your chance to retrieve the treasure chest!")
    print("You dive into the water, swimming with all your might until you reach the chest. With a mighty pull, you tug it along until you yank it onto the shore.")
    print("Hours later, you look on the opened chest from the bow of your ship. This will make life much easier for you and a lot more sturdy for your ship. Your shipmates look at you in awe, but you just laugh. For a treasure hunter like you, victory was NEVER in question!")

print("Thank you for playing!")