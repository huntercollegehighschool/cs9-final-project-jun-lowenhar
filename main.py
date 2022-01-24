"""
Jun Lowenhar:
Goat Roundup (choose your own adventure):
"""

thing = 0

def again():
  import time
  time.sleep(5)
  print("Note: These are real goats with real attitude!")
  import time
  time.sleep(5)
  agains = input("Press enter to play again")
  if agains == "":
    welcome()
  else:
    again()

import os
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def tyvek():
  clearConsole()
  global tyveks
  tyveks = input("The grove looks full of ivy and bugs! Do you put on protective gear? (y or n) ")
  if tyveks != "y" and tyveks != "n":
    print("You must enter y or n.")
    import time
    time.sleep(1)
    tyvek()
  else:
    letssee()

def enter():
  if input("Press Enter to continue...") != "":
    clearConsole()
    enter()
  else:
    tyvek()

def finalbossfight():
  print("Three goats defiantly remain: Romeo, Brooklyn, and Skittles.")
  boss = input("Who will you deal with first: Romeo (r), Brooklyn (b), or Skittles (s)? ")
  if boss == "r":
    print("Romeo is frisky and he refuses to go into the tent.")
    spray = input("Will you use the dreaded... spray bottle?! (y or n) ")
    if spray == "y":
      sprays = int(input("How many times will you spray? Enter a number between 1 and 10 "))
      if sprays == 1:
        clearConsole()
        print("SUCCESS Romeo finally goes into the tent, and Brooklyn and Skittles follow! Let's call it a day.")
        again()
      else:
        clearConsole()
        print("FAIL Romeo jumps the fence and runs away! Concerned for the safety of the kid, the other goats follow. Did I mention that this grove is in Riverside Park? Congratulations, you now have set a herd of goats loose in Manhattan.")
        again()
    elif spray == "n":
      clearConsole()
      print("FAIL Romeo jumps the fence and runs away! Concerned for the safety of the kid, the other goats follow. Did I mention that this grove is in Riverside Park? Congratulations, you now have set a herd of goats loose in Manhattan.")
      again()
    else:
      print("You must enter y or n.")
      import time
      time.sleep(1)
      clearConsole()
      finalbossfight()
  elif boss == "b":
    print("Brooklyn is stubborn and she refuses to go into the tent.")
    spray = input("Will you use the dreaded... spray bottle?! (y or n) ")
    if spray == "y":
      sprays = int(input("How many times will you spray? Enter a number between 1 and 10 "))
      if sprays == 6:
        clearConsole()
        print("SUCCESS Brooklyn finally goes into the tent, and Romeo and Skittles follow! Let's call it a day.")
        again()
      else:
        clearConsole()
        print("FAIL Brooklyn will simply not budge. You are forced to give up and let the goats stay outside for the night.")
        again()
    elif spray == "n":
      clearConsole()
      print("FAIL Brooklyn will simply not budge. You are forced to give up and let the goats stay outside for the night.")
      again()
    else:
      print("You must enter y or n.")
      import time
      time.sleep(1)
      clearConsole()
      finalbossfight()
  elif boss == "s":
    print("Skittles is defiant and he refuses to go into the tent.")
    spray = input("Will you use the dreaded... spray bottle?! (y or n) ")
    if spray == "y":
      sprays = int(input("How many times will you spray? Enter a number between 1 and 10 "))
      if sprays == 8:
        clearConsole()
        print("SUCCESS Skittles finally goes into the tent, and Brooklyn and Romeo follow! Let's call it a day.")
        again()
      else:
        clearConsole()
        print("FAIL Skittles head-butts you into the tent and somehow locks the gate! You are trapped and Skittles can finally begin his plan of world domination. It is the beginning of the Age of Goat!")
        again()
    elif spray == "n":
      clearConsole()
      print("FAIL Skittles head-butts you into the tent and somehow locks the gate! You are trapped and Skittles can finally begin his plan of world domination. It is the beginning of the Age of Goat!")
      again()
    else:
      print("You must enter y or n.")
      import time
      time.sleep(1)
      clearConsole()
      finalbossfight()
  else:
    print("Not a valid response.")
    import time
    time.sleep(1)
    clearConsole()
    finalbossfight()

def tent():
  import time
  time.sleep(4)
  clearConsole
  fw = input("All the goats may be here, but you still have to get them into their tent. First, would you like to move their feed and water into the tent? (y or n) ")
  if fw != "y" and fw != "n":
    print("You must enter y or n.")
    tent()
  elif fw == "y":
    import random
    fight = [1, 2, 3]
    yon = random.choice(fight)
    if yon == 3:
      finalbossfight()
    else:
      clearConsole()
      print("SUCCESS All the goats are in the tent! What a responsible goat herder!")
      again()
  else:
    finalbossfight()
  

def back():
  global tyveks
  if tyveks == "n":
    print("You walk past the tent and into the brush. You begin to pick your way through, but the branches, poison ivy, and bugs are overwhelming. You must turn back.")
    global thing
    thing = thing + 1
    import time
    time.sleep(4)
    if thing == 3:
      clearConsole()
      print("FAIL Looks like you've gotten too many scratches and scars! You must give up for today. Always wear necessary protective gear!")
      again()
    else:
      clearConsole()
      tyvek()
  else:
    clearConsole()
    print("You walk past the tent and into the brush. You begin to pick your way through when you hear a mehh. A goat is near!")
    import time
    time.sleep(1)
    import random
    whothere1 = ["Skittles", "Chalupa"]
    whobethere = random.choice(whothere1)
    print("It's...", whobethere, "!")
    if whobethere == "Chalupa":
      print("Chalupa cautiously makes his way to you and nuzzles your side. As you walk him back towards the tent, one by one the rest of the goats come galloping out of the bushes and into line.")
      tent()
    else:
      print("Skittles the alpha stands defiantly there for a moment, then runs off. The other goats must be elsewhere. Return to the gate to look again.")
      letssee()

def top():
  clearConsole()
  print("You walk up the hill and follow the fence. Suddenly you see a hircine mouth bite at a branch up ahead. It's a goat!")
  import time
  time.sleep(1)
  import random
  whothere2 = ["Ms. Bo Peep", "Cheech"]
  whobethere2 = random.choice(whothere2)
  print("It's...", whobethere2, "!")
  if whobethere2 == "Ms. Bo Peep":
    print("Ms. Bo Peep saves her usual sass for later and gaily prances down the hill. The other goats follow in single file.")
    tent()
  else:
    print("Cheech's narrow muzzle stares you down from afar. With a mehh, he turns and walks back into the brush. Return to the gate to look again.")
    letssee()

def called():
  print("You call out as loud as you can. Halfway up the hill, leaves rustle, and out steps a goat!")
  import time
  time.sleep(1)
  import random
  whothere3 = ["Buckles", "Carmella"]
  whobethere3 = random.choice(whothere3)
  print("It's...", whobethere3, "!")
  if whobethere3 == "Buckles":
    print("Buckles, once abused and meek, happily picks his way down the hill to you. The other goats, sensing it's time to go inside, emerge from the bushes after him.")
    tent()
  else:
    print("Carmella, though typically pretty obedient, does enjoy her alone time. She mehhs as if to tell you she's still busy eating, then steps back out of sight. Return to the gate to look again.")
    letssee()

def call():
  clearConsole()
  calls = input("How will you call them: 'Ladies' (l), 'Kids' (k), or 'Goats' (g) ")
  if calls != "l" and calls != "k" and calls != "g":
    print("Not a valid response.")
    import time
    time.sleep(1)
    call()
  elif calls == "l":
    called()
  elif calls == "g":
    called()
  else:
    print("You call, but all you hear in response is a distant mehh. No goats come running. Try something else.")
    import time
    time.sleep(3)
    call()

def there():
  import time
  time.sleep(0.5)
  import random
  whothere = ["Cheech", "Romeo", "Carmella", "Mallomar", "Brooklyn", "Buckles", "Ms. Bo Peep", "Skittles", "Chalupa"]
  global whobethere
  whobethere = random.choice(whothere)
  print("It's...", whobethere, "!")
  nowwhat()
  
def nowwhat():
  method = input("A goat stands at the top of the hill, but how are you going to get them down: treats (t) or leading (l)? ")
  if method != "t" and method != "l":
    print("Not a valid response.")
    import time
    time.sleep(1)
    clearConsole()
    nowwhat()
  elif method == "t":
    treats()
  else:
    leading()
    
def treats():
  treat = input("You have a few options for treats. Will you use carrots (c), apples (a), or grain (g)? ")
  global whobethere
  if treat == "c":
    if whobethere == "Romeo":
      print("Romeo, the baby of the herd, bleats and runs down the hill for his favorite treat. The other goats,sensing the child straying from them, run after him.")
      tent()
    elif whobethere == "Carmella":
      print("Carmella can be quite fussy about snacks. She's not feeling carrots today. Look for another goat.")
      letssee()
    else:
      print(whobethere, "doesn't seem very hungry for carrots today. Look for another goat.")
      letssee()
  elif treat == "a":
    if whobethere == "Cheech":
      print("Cheech, enticed by the tart crunchiness of apple pieces, picks his way down the hill. As he opens his mouth for the first bite, the other goats gather.")
      tent()
    elif whobethere == "Romeo":
      print("Though the baby of the herd, Romeo doesn't really like apples. He runs off again to join the big goats somewhere. Look for another goat.")
      letssee()
    else:
      print(whobethere, "doesn't seem very hungry for apples today. Look for another goat.")
      letssee()
  elif treat == "g":
    if whobethere == "Mallomar":
      print("Mallomar, with the softest light brown coat, loves feed! He bleats and excitedly runs down the hill to get a nibble. The rest of the goats come to race him to it.")
      tent()
    elif whobethere == "Brooklyn":
      print("Brooklyn, the pitch-black goat with a huge attitude, tilts her snout sassily away from the grain. She sees right through your little plot, and she not having it! Look for another goat.")
      letssee()
    else:
      print(whobethere, "doesn't seem very hungry for grain today. Look for another goat.")
      letssee()
  else:
    print("Not a valid response.")
    import time
    time.sleep(1)
    clearConsole()
    treats()

def leading():
  led = input("There are a few ways to lead a goat. Do you want to clap (c), push (p), or pull (u)? ")
  global whobethere
  if led == "c":
    if whobethere == "Carmella":
      print("You make your way up to Carmella. You carefully walk bakwards, clapping slowly and steadily. Carmella follows your clapping hands, and the other goats fall in line, hearing the claps.")
      tent()
    elif whobethere == "Buckles":
      print("Though he's recovered from his abuse, loud noises still frighten Buckles sometimes. He runs away. Look for another goat.")
      letssee()
    else:
      print(whobethere, "ignores your claps and continues to eat. Look for another goat.")
      letssee()
  elif led == "p":
    if whobethere == "Brooklyn":
      print("Brooklyn has quite a good grip, but even even she eventually gives in to the pushing and budges. The other goats, sensing your determination, reluctantly make their way down the hill.")
      tent()
    elif whobethere == "Ms. Bo Peep":
      print("Ms. Bo Peep is small, but don't let that fool you. Her short, stubby nature forces you bend over to push her, and you loose your balance and fall over. She trots away, bleating as if laughing at you. Look for another goat.")
      letssee()
    else:
      print(whobethere, "has a very strong stance today and doesn't budge. Look for another goat.")
      letssee()
  elif led == "u":
    if whobethere == "Skittles":
      print("Despite being a quite standoffish goat, this time Skittles does not try to loosen your grip on his collar. Those big horns do look scary though. The other goats follow you and their leader.")
      tent()
    elif whobethere == "Chalupa":
      print("Chalupa is a sweet goat, but that means he doesn't respond very well to force. He bleats, frightened, and runs off.")
      import time
      time.sleep(3)
      clearConsole()
      print("FAIL You have upset Chalupa! If you did not previously know, Chalupa is my favorite baby boy and upsetting him is the worst crime here. Get away from him!")
      again()
    else:
      print(whobethere, "easily breaks free of your grasp and runs off. Look for another goat.")
      letssee()
  else:
    print("Not a valid response.")
    import time
    time.sleep(1)
    clearConsole()
    leading()

def nothere():
  how = input("How do you want to get them: do you want to look in the back (b), look at the top of the hill (h), or call them from here (c)? ")
  if how == "b":
    back()
  elif how == "h":
    top()
  elif how == "c":
    call()
  else:
    print("Not a valid response.")
    import time
    time.sleep(1)
    clearConsole()
    nothere()

def letssee():
  print("Let's see if any goats are around...")
  import time
  time.sleep(3)
  import random
  here = ["There's a goat there! Who could it be?", "There are no goats here yet. Let's look for them!"]
  hereorno = random.choice(here)
  print(hereorno)
  if hereorno == "There's a goat there! Who could it be?":
    there()
  else:
    nothere()

def welcome():
  clearConsole()
  print("Welcome to the Goat Grove. The nine lovely goats have had a great day of grazing, but soon it's time for them to go back inside. Can you get them all back in their tent?")
  import time
  time.sleep(2)
  enter()

welcome()