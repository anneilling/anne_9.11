bot=0
player=0
viik=0
mangija=0
def start():
    """
    Teeme valik kellega mängime
    Tagastame m mutuja int formaadis

    :rtype: int
    """
    print("---Kivi, käärid, paber---.")
    print()
    game=0
    while game not in [1,2,3]:
        try:
            game=int(input("Kas soovid mängida sõbraga (1),\n robotiga (2)\n või robot+robot (3)? => ") ) 
        except TypeError:
                print("Viga")
    return game

def sober(b:list)
if game==1:
    """sobraga mäng
    Näitame ekraanile võitja nime
    :param list b: järjend esimese roboti jaoks
    :rtype: int
    """
    while True:
        print("Soovid jätka (vajuta ``backspace``) või lopetada (vajuta ``enter``)?")
        print()
        try:
             if read_key()=="backspace":
                print()
                print("Jätkame mängu.")
                print()
                pass
        except:
                ValueError
        try:
            if read_key()=="enter":
                print()
                print("Aitäh!")
                print()
                print(f"Viik {viik} , Mängija võitu {player} , Roboti võitu {bot}.")
                break
        except:
                ValueError
        c=0
        while c not in [1,2,3] :
            try:
                c=int(input("Kivi (1), käärid (2), paber (3) =>. "))
            except TypeError:
                print("Viga")
            print()
            if c == 1:
                print("Teie valik on kivi.")
                print()
            elif c == 2:
                print("Teie valik on käärid.")
                print()
            elif c == 3:
                print("Teie valik on paber.")
                print()
            b = randint(1,3)
            print()
            if b == 1:
                print("Robot valis kivi.")
                print()
            elif b == 2:
                print("Robot valis käärid.")
                print()
            elif b == 3:
                 print("Robot valis paber.")
                 print()
            
            if b==c:
               print("Viik")
               print()
               viik+=1
            elif b==1 and c==2 or b==2 and c==3 or b==3 and c==1:
               player+=1
               print("Võitis mängija 1")
               print()
            elif b==1 and c==3 or b==2 and c==1 or b==3 and c==2:
               bot+=1
               print()
               print("Võitis robot")

def robot(g:list)
if game==2:
    """roobotiga mäng
    Näitame ekraanile võitja nime
    :param list g: järjend esimese mängija jaoks
    :rtype: int
    """
    while True:
        print("Soovid jätka (vajuta ``backspace``) või lopetada (vajuta ``enter``)?")
        print()
        try:
             if read_key()=="backspace":
                print()
                print("Jätkame mängu.")
                print()
                pass
        except:
                ValueError
        try:
            if read_key()=="enter":
                print()
                print("Aitäh!")
                print()
                print(f"Viik {viik} , Mängija 1 võitu {player} , Mängija 2 võitu {mangija}.")
                break
        except:
                ValueError
        c=0
        while c not in [1,2,3] :
            try:
                c=int(input("Kivi (1), käärid (2), paber (3) => "))
            except TypeError:
                print("Viga!")
            print()
            if c == 1:
                print("Teie valik on kivi.")
                print()
            elif c == 2:
                print("Teie valik on käärid.")
                print()
            elif c == 3:
                print("Teie valik on paber.")
                print()
        b=0
        while b not in [1,2,3] :
            try:
                b=int(input("Kivi (1), käärid (2), paber (3) => ") )
            except TypeError:
                print("Viga!")
            print()
            if b == 1:
                print("Mängija 2 valis kivi.")
                print()
            elif b == 2:
                print("Mängija 2 valis käärid.")
                print()
            elif b == 3:
                 print("Mängija 2 valis paber.")
                 print()
        if b==c:
            print("Viik")
            print()
            viik+=1
        elif b==1 and c==2 or b==2 and c==3 or b==3 and c==1:
            player+=1
            print("Võitis mängija 1")
        elif b==1 and c==3 or b==2 and c==1 or b==3 and c==2:
            mangija+=1
            print()
            print("Võitis mängija 2")


def bot_vs_bot(b:list,g:list):
    if game==3
    """roobotite mäng
    Näitame ekraanile võitja nime
    :param list b: järjend esimese roboti jaoks
    :param list g: järjend teise roboti jaoks
    :rtype: int
    """
    while True:
        print("Soovid jätka (vajuta ``backspace``) või lopetada (vajuta ``enter``)?")
        print()
        try:
             if read_key()=="backspace":
                print()
                print("Jätkame.")
                print()
                pass
        except:
                ValueError
        try:
            if read_key()=="enter":
                print()
                print("Aitah!")
                print()
                print()
                print(f"Viik {viik} , Robot 1 võitu {player} , Robot 2 võitu {bot}.")
                break
        except:
                ValueError
        b = randint(1,3)
        g = randint(1,3)
        print()
        if b == 1:
            print("Robot 1 valis kivi.")
            print()
        elif b == 2:
            print("Robot 1 valis käärid.")
            print()
        elif b == 3:
            print("Robot 1 valis paber.")
            print()
        if g== 1:
            print("Robot 2 valis kivi.")
            print()
        elif g == 2:
            print("Robot 2 valis käärid.")
            print()
        elif g == 3:
            print("Robot 2 valis paber.")
            print()
        if b==g:
            print("Viik")
            viik+=1
        elif b==1 and g==2 or b==2 and g==3 or b==3 and g==1:
            player+=1
            print("Võitis robot 1")
        elif b==1 and g==3 or b==2 and g==1 or b==3 and g==2:
            bot+=1
            print("Võitis robot 2")
