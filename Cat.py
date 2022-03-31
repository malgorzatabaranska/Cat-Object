#Napisz klasę reprezentującą kota, każdy kot ma
#imie
#swoje ulubione zabawki
#zabawki których nie znosi
#ponadto potafi:
#przywitać się i przedstawić
#powiedziec jakie są jego ulubione/ nielubiane zabawki i ile ich jest
#polubić napotkaną zabawke
#obrazić się na jakąś 
#obrazić się na jakąś zabwke, którą dotąd lubił
#kot do nowych zabawek podchodzi z ufnoscia . Na liście lubianych i nielubianych żaden element sie nie powtarza



class Cat(object): 

    def __init__(self, name, mood =0, fun = 0, hungry = 0):
        self.name= name
        self.mood = mood
        self.fun = fun
        self.hungry = hungry

    def __str__(self):
        rep1 = self.name

        return rep1, 

    def pass_time(self):
        self.mood += 5
        self.hungry +=5

    def introduce(self):
        print("Cześć jestem", self.name)
        self.pass_time()

    def play(self):
        print("Mruuu")
        self.pass_time()
        self.fun -= 5
        if self.mood <= 0:
            self.mood == 0

    def eat(self):
        print(
            """
            1 - sucha karma
            2 - mokra karma
            3 - kwałek mięsa
            4 - mleko
            """
        )
        quest = input("Czym nakarmić kota?: ")
        if quest == "1":
            self.hungry -= 2
            self.mood += 4
        elif quest == "2":
            self.hungry -= 4
            self.mood += 2
        elif quest == "3":
            self.hungry -= 5
            self.mood += 1
        elif quest == "4":
            self.hungry -= 1
            self.mood += 5

        if self.hungry <= 0:
            self.hungry = 0

        print("mruuu.... pycha")


    def humor(self):
        if self.mood == 0:
            m = "wniebowzięty"
        elif  0 < self.mood < 5:
            m = "w dobrym humorze"
        elif 5 < self.mood < 10 :
            m = "Jest mi smuto"
        else:
            m = "wściekły!!!"

        return m
        

    def ask_for_toys(self, like, basket):
        if len(like) == 0:
            print("Nie znoszę wszystkich zabawek!")
        elif len(basket) == 0:
            print("Uwielbiam wszystkie swoje zabawki")
        else:
            print("W tym momencie lubie zabawki: ", like , "oraz nie lubię zabawek: ", basket )
    
    def talk(self):
        print("Jestem teraz ", self.humor())



class Toys():
    basket = ["piłeczka", "kłębek wełny", "gumowy kurczak"]
    like = []

    def __init__(self):
        self.like = []

    def __str__(self):
        rep1 = self.like

        return rep1

    def love(self):
        import random
        for toys in random.sample(Toys.basket, random.randint(1 ,len(Toys.basket))):
            try:
                Toys.like.append(toys)
                Toys.basket.remove(toys)
            except ValueError: 
                print("Uwielbiam wszystkie swoje zabawki")
    
    def add_toy(self):
        new_toy_name = input("Jaką zabawke chcesz oddać? : ")
        if new_toy_name != "":
            Toys.like.append(new_toy_name)
        else: 
            print("Trudno będę sie bawił tym co mam")
        
    def replace(self):
        import random
        for x in random.sample(Toys.like, random.randint(1, len(Toys.like))):
            try:
                Toys.basket.append(x)
                Toys.like.remove(x)
            except ValueError: 
                print("Nie lubię wszystkich zabawek!")
        
        

def  main():
    cat_name = input("Jak chcesz nazwać swojego kota: ?")
    pupil = Cat(cat_name)
    pupil_toys = Toys()
    basket = Toys.basket
    like = Toys.like

    pupil.introduce()

    choice = None
    while choice != 0 :
        print \
        ("""
        0 - zakończ
        1 - zapytaj, które zabawki lubi
        2 - zapytaj, których zabawek nie lubi
        3 - dodaj nową zabawkę do koszyka
        4 - pobaw się z kotem
        5 - nakarm kota
        6 - zapytaj kota w jakim jest nastroju 
        """)

        choice = input("Wybierasz: ")

        if choice == "0":
            print("Do widzenia.")
        elif choice == "1": 
            pupil_toys.love()
            pupil.ask_for_toys(like, basket)  
            pupil_toys.replace()
            pupil.pass_time()
        elif choice == "2":
            pupil_toys.love()
            pupil.ask_for_toys(like, basket)
            pupil_toys.replace()
            pupil.pass_time()
        elif choice == "3":
            pupil_toys.add_toy()
            pupil_toys.love()
            pupil_toys.replace()
        elif choice == "4":
            pupil.play()
        elif choice == "5":
            pupil.eat()
        elif choice == "6":
            pupil.talk()

main()

