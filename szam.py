import random

def elso():
    szam = random.randint(1,50)
    if szam % 5 == 0:
        print("“A szám öttel osztható!”,")
    elif szam % 3 == 0:
        print("“A szám öttel osztható!”,")
    elif szam % 3 & szam % 5 == 0:
        print("“A szám öttel és hárommal is osztható!”,")