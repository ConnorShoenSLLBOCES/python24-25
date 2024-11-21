color = input ("What is your favorite color? ")
color.lower

anim = input ("What is your favorite animal: Dog, Cat, Pigeon, Frog, Rabbit, Panda, Monkey, Sloth, or Goat? ")
anim.lower

if anim == "dog":
    print ("Ah, so your favorite color is " + color + " and your favorite animals are dogs. Let's see what that says about you!")
    input ("Press enter to see your results!")
    print ("Based on your answers, you are a loser.")
elif anim == "cat":
    print ("Ah, so your favorite color is " + color + " and your favorite animals are cats. Let's see what that says about you!")
    input ("Press enter to see your results!")
    print ("Based on your answers, you're a mom.")
elif anim == "pigeon":
    print ("Ah, so your favorite color is " + color + " and your favorite animals is pigeon. Let's see what that says about you!")
    input ("Press enter to see your results!")
    print ("Based on your answers, you're alright")
elif anim == "frog":
    print ("Ah, so your favorite color is " + color + " and your favorite animals are frogs. Let's see what that says about you!")
    input ("Press enter to see your results!")
    print ("Based on your answers, you're extremly autistic.")
elif anim == "rabbit":
    print ("Ah, so your favorite color is " + color + " and your favorite animals are rabbits. Let's see what that says about you!")
    input ("Press enter to see your results!")
    print ("Based on your answers, you're okay.")
elif anim == "panda":
    print ("Ah, so your favorite color is " + color + " and your favorite animals are pandas. Let's see what that says about you!")
    input ("Press enter to see your results!")
    print ("Based on your answers, you're probably normal.")
elif anim == "monkey":
    print ("Ah, so your favorite color is " + color + " and your favorite animals are monkeys. Let's see what that says about you!")
    input ("Press enter to see your results!")
    print ("Based on your answers, you're cool.")
elif anim == "sloth":
    print ("Ah, so your favorite color is " + color + " and your favorite animals are sloths. Let's see what that says about you!")
    input ("Press enter to see your results!")
    print ("Based on your answers, you're slow.")
elif anim == "goat":
    print ("Ah, so your favorite color is " + color + " and your favorite animals are goats. Let's see what that says about you!")
    input ("Press enter to see your results!")
    print ("Based on your answers, you're a farmer or a white woman.")
else:
    print ("Invalid Answer.")