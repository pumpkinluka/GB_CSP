def grandma(player_name):
    print(f"You tumble through the door and end up in an apartment, with antiques scattering the area and intricately patterned couches. It seems like a grandma owns this place, unsuprisingly.\nIn the corner of your eye, you see a glimmer of saliva. On top of the counter, is GRANDMA'S DENTURES. You HAVE to steal them in order to progress.\nYou begin creeping towards the counter, when you hear a voice echoing from the nearby hallway.\n")
    print(f"Grandma: WHO'S IN MY HOUSE???\nOh no. It's the owner of this place, Grandma!\n")
    print(f"Goal: steal grandma's dentures from the counter\n")
    print(f"Grandma is coming, quick! You can: Quickly try and grab the dentures (Grab), hide beneath the sofa (Hide), or pretend to be a pet (Pet)")

    while True:                
        granny_choice1 = input("What do you do?: ").strip().lower()

        if granny_choice1 == "grab":
            print("You squrry across the floor, and make a leap of fate towards the counter!...\nYou miss.\nBadly.\nYou bounce off the counter, knocking off the dentures along with you. This would be perfect, but before you can react, Grandma appears in the kitchen doorway. She examines you and her dentures on the floor, taking it all in. Suddenly, she snaps.")
            print("Grandma: OH NO YOU DON'T, YOU PEST!!!")
            print("She grabs you and throw you out the window, ending your quest for good.")
            return False
        elif granny_choice1 == "hide":
            print("You flatten yourself against the floor and squeeze beneath the sofa, trying to become one with the colonies of dust bunnies down there. Grandma shuffles into the room.")
            print("Grandma: Now what was that noise?")
            print("The rotted cracker in front of you is calling your name, but you resist the temptation. For now at least.")
            break
        elif granny_choice1 == "pet":
            print("You remember all your previous training and lock in. You sit innocently in the middle of the room, looking adorable as always.")
            print("Grandma: I didn't know I had a pet... Well I forget a lot of things. Aw, what a precious little animal!")
            print("She picks you up and starts scratching your head, which feels AMAZING. You almost forget your mission, before coming back to reality an realizing your goal. You bathe in the affection before she sets you down and disappears down the hallway.")
            break
        else:
            print("QUICK DO SOMETHING!!")
        
        
    print("Grandma soon comes back, muttering about missing belongings.")
    print("Grandma: First my glasses...then my knitting needles...and now strange noises haunt this house!")
    print("You peek around the corner and spot the dentures still on the counter. Grandma is heading to the kitchen, about to grab them.\nYou CANNOT let that happen, or you will never make it out.")

    print("Hurry! You can: use the pepper spray on the coffee table (Spray), wait (Wait), or make a run for the dentures (Run).")

    while True:
        granny_choice2 = input("You have to decide something ASAP: ").strip().lower()

        if granny_choice2 == "spray":
            print("You grab the nearby pepper spray from the coffee table and run up to Grandma like you're on a stealth mission.\nSomehow, your grubby ferret hands manage to jump and spray Grandma with pepper spray in perfect coordination and timing. You have been training for this moment your whole life.\nYou dart to the counter while Grandma is crashing out over the pepper spray in her eyes, your life depending on precision.")
            break
        elif granny_choice2 == "wait":
            print("You decide to wait for the PERFECT moment. So you wait...and wait...and...wait. You're half asleep before you see Grandma right across from you. Her eyes narrow.")
            print("Grandma: Wait... you don't belong here. GET OUT OF MY HOUSE!!")
            print(f"{player_name}: Apartment, not house... Why are you chasing me.")
            print("You run away and attempt to squeeze beneath the fridge, but your tail is a dead giveaway! Grandma has caught you!")
            return False
        elif granny_choice2 == "run":
            print("You sprint towards the counter, scrambling up as quickly as possible. Your paws skid across the countertop. You grab the dentures as Grandma turns around and gasps so loud that her fine china probably broke.")
            print("Grandma: MY TEETH! GIVE THOSE BACK")
            print("With no teeth, Grandma just sounds like she's blabbering like a baby. ANYWAYS. You clamp the dentures tightly in your mouth and bolt towards the door.")
            break
        else:
            print(f"Hurry up and give me an answer, {player_name}")

    while True:
        granny_choice3 = input("Escape? (Y/N):").upper().strip()
        if granny_choice3 == "Y":
            print("Grandma: WHERE DO YOU THINK YOU'RE GOING, YOU FUZZY LITTLE PUNK!")
            print("You sprint through the living room. You slide beneath a chair. You bounce off a pillow. You are literally doing a roblox obby irl.\nGrandma almost catches your tail by a fraction of an inch, but you squeeze through the door just in time with the dentures in your mouth!")
            print("ITEM COLLECTED: GRANDMA'S DENTURES")
            has_dentures = True
            break
        elif granny_choice3 == "N":
            print("Well, I respect your decision, I guess. Anyways, Grandma grabs you from behind and throws you out the window, and you never escape!")
            return False
        else:
            print("ARE YOU SERIOUS ABOUT THIS OR NOT???")