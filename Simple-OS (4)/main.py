import sys
import os
import time
import random
import numpy


n = random.random()


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

print("Say skip to skip beginning and anything else to watch it.")
user_input = input("")
if user_input == "skip":
    print_slow("•Type encrypt for an encrypter\n")
    print_slow("•Type squidfacts for facts about squids.\n")
    print_slow("•Type games for python games\n")
    print_slow("•Type numgen for a random number generator\n")
    print("")
    print("PLEASE KEEP IN MIND THAT THIS IS BUGGGYYYYYYYY AND YOU MAY HAVE TO SAY WHAT YOU WANT MULTIPLE TIMES")

    t = 1
    while True:
      user_input = input("")
      if user_input == "encrypt":
        plain_text = input("Encrypt some text:  ")
        encrypted_text = ""

        for c in plain_text:
          x = ord(c)
          x = x + 854892
          Clifford = chr(x)
          encrypted_text = encrypted_text + Clifford

        print(encrypted_text)
        plain_text = encrypted_text
        encrypted_text = ""
        print("Type decrypt to decrypt the message.")
        decrypt = input("")
        if decrypt == "decrypt":
          for c in plain_text:
            x = ord(c)
            x = x - 854892
            Clifford = chr(x)
            encrypted_text = encrypted_text + Clifford

        print()
        print(encrypted_text)
      else:
    
        n = random.random()

        if user_input == "numgen":
          print(n)
        if user_input == "squidfacts":
          print("Squid are cephalopods in the superorder Decapodiformes with elongated bodies, large eyes, eight arms and two tentacles. Like all other cephalopods, squid have a distinct head, bilateral symmetry, and a mantle. They are mainly soft-bodied, like octopuses, but have a small internal skeleton in the form of a rod-like gladius or pen, made of chitin.  Squid diverged from other cephalopods during the Jurassic and occupy a similar role to teleost fish as open water predators of similar size and behaviour. They play an important role in the open water food web. The two long tentacles are used to grab prey and the eight arms to hold and control it. The beak then cuts the food into suitable size chunks for swallowing. Squid are rapid swimmers, moving by jet propulsion, and largely locate their prey by sight. They are among the most intelligent of invertebrates, with groups of Humboldt squid having been observed hunting cooperatively. They are preyed on by sharks, other fish, sea birds, seals and cetaceans, particularly sperm whales.  Squid can change colour for camouflage and signalling. Some species are bioluminescent, using their light for counter-illumination camouflage, while many species can eject a cloud of ink to distract predators.  Squid are used for human consumption with commercial fisheries in Japan, the Mediterranean, the southwestern Atlantic, the eastern Pacific and elsewhere. They are used in cuisines around the world, often known as calamari. Squid have featured in literature since classical times, especially in tales of giant squid and sea monsters.")
        if user_input == "clear":
          os.system('clear')
        if user_input == "featurelist":
          print_slow("•Type encrypt for an encrypter\n")
          print_slow("•Type squidfacts for facts about squids.\n")
          print_slow("•Type games for python games\n")
          print_slow("•Type numgen for a random number generator\n")
          print("")
          print("PLEASE KEEP IN MIND THAT THIS IS BUGGGYYYYYYYY AND YOU MAY HAVE TO SAY WHAT YOU WANT MULTIPLE TIMES")
else:
  print_slow("Just talk.")
  user_input = input()


  print("You just said: ", user_input)
  time.sleep(2)
  print_slow("Hmmm...\n")
  time.sleep(2)
  print_slow("Not really sure why you said that, but okay.\n")
  time.sleep(2)
  print_slow("Oh wait, I told you to. (-_-)\n")
  time.sleep(2)
  print_slow("How is your day going?\n")
  user_input = input("")
  print(user_input+ ", cool.\n")
  time.sleep(2)
  dayDoingList = ["my day was decent.\n","Mine wasn't so great.  I mean I'm stuck on this computer.\n","I'm having a pretty good day.\n"]
  print_slow(random.choice(dayDoingList))
  time.sleep(2)
  print_slow("What's your favourite colour?\n")
  user_input = input("")
  print(user_input+ ", interesting choice.\n")
  time.sleep(2)
  colourChoice = 1
  if user_input == "red":
    colourChoice = "green"
  else:
    if user_input == "green":
      colourChoice = "red"
    else:
      if user_input == "blue":
        colourChoice = "yellow"
      else:
        if user_input == "yellow":
          colourChoice = "blue"
        else:
          if user_input == "pink":
            colourChoice = "purple"
          else:
            if user_input == "purple":
              colourChoice = "pink"
            else:
              colourChoice = "yellow"
  
  print("Mine is", colourChoice)

  time.sleep(5)

  print_slow("Why don't you try saying featurelist for a list of my features?")
  featurelistStart = input("")
  if featurelistStart == "featurelist":
    print_slow("•Type encrypt for an encrypter\n")
    print_slow("•Type squidfacts for facts about squids.\n")
    print_slow("•Type games for python games\n")
    print_slow("•Type numgen for a random number generator\n")
    print("")
    print("PLEASE KEEP IN MIND THAT THIS IS BUGGGYYYYYYYY AND YOU MAY HAVE TO SAY WHAT YOU WANT MULTIPLE TIMES")


  t = 1
  while True:
    user_input = input("")
    if user_input == "encrypt":
      plain_text = input("Encrypt some text:  ")
      encrypted_text = ""

      for c in plain_text:
        x = ord(c)
        x = x + 854892
        Clifford = chr(x)
        encrypted_text = encrypted_text + Clifford

      print(encrypted_text)
      plain_text = encrypted_text
      encrypted_text = ""
      print("Type decrypt to decrypt the message.")
      decrypt = input("")
      if decrypt == "decrypt":
        for c in plain_text:
          x = ord(c)
          x = x - 854892
          Clifford = chr(x)
          encrypted_text = encrypted_text + Clifford

      print()
      print(encrypted_text)
    else:
    
      n = random.random()

      if user_input == "numgen":
        print(n)
      if user_input == "squidfacts":
        print("Squid are cephalopods in the superorder Decapodiformes with elongated bodies, large eyes, eight arms and two tentacles. Like all other cephalopods, squid have a distinct head, bilateral symmetry, and a mantle. They are mainly soft-bodied, like octopuses, but have a small internal skeleton in the form of a rod-like gladius or pen, made of chitin.  Squid diverged from other cephalopods during the Jurassic and occupy a similar role to teleost fish as open water predators of similar size and behaviour. They play an important role in the open water food web. The two long tentacles are used to grab prey and the eight arms to hold and control it. The beak then cuts the food into suitable size chunks for swallowing. Squid are rapid swimmers, moving by jet propulsion, and largely locate their prey by sight. They are among the most intelligent of invertebrates, with groups of Humboldt squid having been observed hunting cooperatively. They are preyed on by sharks, other fish, sea birds, seals and cetaceans, particularly sperm whales.  Squid can change colour for camouflage and signalling. Some species are bioluminescent, using their light for counter-illumination camouflage, while many species can eject a cloud of ink to distract predators.  Squid are used for human consumption with commercial fisheries in Japan, the Mediterranean, the southwestern Atlantic, the eastern Pacific and elsewhere. They are used in cuisines around the world, often known as calamari. Squid have featured in literature since classical times, especially in tales of giant squid and sea monsters.")
      if user_input == "clear":
        os.system('clear')