# polymorphism can also be applied to the classes like

class bird:
    def sound(self):
        print(f"Birds make sounds!")
    
class sparrow(bird):
    def sound(self):
        print(f"Sparrows Chirp!")

class parrot(bird):
    def sound(self):
        print(f"parrot makes some unique sound!")

    
bird1  = sparrow()
bird2  = parrot()
bird1.sound()
bird2.sound()

# so here we can see the polymorphism being in action like sound is used for the different purposes  