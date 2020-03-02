from graphics import *
import random

# velikost okna
winY = 500
winX = 1000

# velikost bloků
blockSize = 25
levelsSize = 50

# vytvoření seznamu úrovní
lvl = [0]
for i in range(int(winX/levelsSize*winY/levelsSize)+1):
    lvl.append(0)

# pomocná proměnná pro ukládání levelů, které jsou mimo rozsah aktuálbího okna
over = ""

# ze souboru se načtou uložené úrovně, pokud soubor neexistuje tak se vytvoří
try:
    # otevření souboru
    f = open("lvl.txt","r")
    #přečtení obsahu
    content = f.read()
    # rozdělení obsahu souboru na "," (čárce)
    val = content.split(",")
    # print(val)
    # zavření souboru
    f.close()
    # pro každou hodnotu souboru se splní jedena úroveň
    for el in val:
        # odchycení posledního prázného řetězce ''
        if el == '':
            continue
        # odchycení úrovní, které jsou vyšší, než aktuálně zobrazené
        if int(el) > len(lvl):
            over += el + ","
            continue
        # nastavení úrovně na splněnou
        lvl[int(el)] = 1
except:
    # pokud soubor nebyl nalezen, tak se vytvoří a zavře
    f = open("lvl.txt","w+")
    f.close()



'''
    [ ]  přidat řešení jednotlivých úrovní??? řešení by se mohlo otevřít v novém okně
'''

'''
MM     MM    EEEEEE    NN    NN    UU    UU
MMM   MMM    EE        NNN   NN    UU    UU
MM MMM MM    EEEEEE    NN NN NN    UU    UU
MM     MM    EE        NN   NNN    UU    UU
MM     MM    EEEEEE    NN    NN    UUUUUUUU
'''
# startovní menu
def menu():

    # funkce, která zjišťuje, jestli jsem stisknul slačítko start (hodí se pouze na jednostlivé "tlačítka")
    def clickObj(obj):
        # nekonečná smyčka
        while True:
            # zkouším zda jsem kliknul či nikoliv (nemůžu neustále čekat pouze na jeden input, kdybych náhodou
            # chtěl použít klávesnici)
            try:
                # zjistím pozici kliknutí, dostanu Point(x,y)
                mPos = Menu.checkMouse()
                # separuji x a y z kliknutí
                mX = mPos.getX()
                mY = mPos.getY()
                
                try:
                    # pokud je objekt pravoúhelník, vyhodí to zde error a pokračuje to na 'except'
                    # pokud objekt je kruh, zjistím jeho poloměr a střed
                    oR = obj.getRadius()
                    oC = obj.getCenter()

                    # užitím pytagorovy věty zjistím vzdálenost kliku od středu kruhu,
                    # čímž docílím toho, že na rohy nebudu moci kliknout jako by tomu
                    # bylo u pravoúhelníku
                    x = abs(mX - oC.getX())
                    y = abs(mY - oC.getY())
                    length = math.sqrt(x*x + y*y)

                    # print(str(x) + " " + str(y) + " " + str(length) + " " + str(oR)) #debuging

                    # zjistím, jestli kliknutí bylo uskutečněno v kruhu (okraj se nepočítá)
                    # pokud ano navrátím hodnotu True
                    if length < oR:
                        # print("inside circle")
                        return True
                    else:
                        # print("outside circle")
                        return False

                except:
                    # tohle je pravoúhelník nebo jiný objekt (pokud možno pravoúhelník)

                    # zjistím si souřednice protilehlých rohů pravoúhelníku
                    # levý horní a pravý dolní
                    p1 = obj.getP1()
                    p2 = obj.getP2()

                    # zjistím, jestli byl klik uskutečněný mezi těmito rohy
                    # pokud ano navrátím hodnotu True
                    if (mX > p1.getX() and mX < p2.getX() and mY > p1.getY() and mY < p2.getY()):
                        # print("inside rect")
                        return True
                    else:
                        # print("outside rect")
                        return False
            except:
                # pokud nenastala žádná akce, dostanu se až sem, kde proběhne 'pass', který
                # funguje jako 'continue', takže se pokračuje dále
                pass
        
    # vytvořím okno Menu s názvem Menu a velikostí
    Menu = GraphWin("Menu", winX, winY)
    

    # do proměné 'start' si vytvořím objekt Rectangle, kterému zadám počáteční rohy a vykreslím do okna 'Menu' pomocí .draw(Menu)
    start = Rectangle(Point(winX/2-50,winY/2-50),Point(winX/2+50,winY/2))
    start.draw(Menu)
    # popisek
    desc1 = Text(Point(start.getCenter().getX(),start.getCenter().getY()+50),"while in game or level browser press 'e' to go back and 'q' to exit")
    desc1.draw(Menu)
    # vytvořím text, který bude uprostřed 'start'
    Text(start.getCenter(),"Start").draw(Menu)

    # čekám, dokud uživatel neklikne na 'start'
    while True:
        # pokud klikne, zavře se stávající okno, přeruší se cyklus a otevře se nové okno s výběrem levelů
        if clickObj(start):
            Menu.close()
            levels(0)
            break
'''
LL        EEEEEE    VV      VV   EEEEEE   LL       
LL        EE         VV    VV    EE       LL       
LL        EEEEEE      VV  VV     EEEEEE   LL       
LL        EE           VVVV      EE       LL       
LLLLLLL   EEEEEE        VV       EEEEEE   LLLLLLL  
'''
# výběr levelů
def levels(lv):

    # nastavení levelu na splněný
    # pokud hráč kliknul na určitou úroveň a vyřešil ji, tak zde bude hodnota úrovně
    # pokud ne, bude zde hodnota 0, která je pro tento účel
    # zároveň zde bude nula, když se přistupuje z menu
    lvl[lv] = 1

    # string pro ukládání vyřešených úrovní
    txt = over
    # projede se list s úrovněmi, a pokud je nějaká vyřešená, tak se číslo této úrovně zapíše do listu
    for i in range(len(lvl)):
        if lvl[i] == 1:
            txt += str(i) + ","

    # otevře se soubor s úrovněmi a zapíšou se tam a následně se soubor zavře
    f = open("lvl.txt", "w")
    f.write(txt)
    f.close()

    #nastavím větší velikost pro bloky
    # funkce na zjištění, do jakého "kvadrantu" uživatel kliknul
    def clickPos(mouse):
        # z parametru funkce, kde je Point získám x a y
        x = mouse.getX()
        y = mouse.getY()

        # vytvořím si proměnné pro počítáni kvadrantů
        blockX = -1
        blockY = -1

        # samotné počítání kvadrantů
        num = 0
        # dokud se nedostanu na hodnotu x nebo y, přičítám postupně
        # pixely kvadrantu a přidávám 1 do počítadla kvadrantů
        while num < x:
            num += levelsSize
            blockX += 1
        num = 0
        while num < y:
            num += levelsSize
            blockY += 1
        # print(str(blockX) + " " + str(blockY))

        # vrátím součet kvadrantů, s tím že y je vynásobené velikostí kvadrantu
        # pro zajištění správného zvolení levelu
        return int(blockX + blockY*(winX/levelsSize) + 1)
    
    # vykreslení všech levelů s číslem levelu
    def drawL(x,y):
        if lvl[int(x+y*winX/levelsSize)+1] == 1:
            r = Rectangle(Point(x*levelsSize,y*levelsSize),Point(x*levelsSize+levelsSize,y*levelsSize+levelsSize))
            r.setFill("gray")
            r.draw(Levels)
            Text(r.getCenter(),str(x+1+y*int(winX/levelsSize))).draw(Levels)
        else:
            r = Rectangle(Point(x*levelsSize,y*levelsSize),Point(x*levelsSize+levelsSize,y*levelsSize+levelsSize))
            r.setFill("white")
            r.draw(Levels)
            Text(r.getCenter(),str(x+1+y*int(winX/levelsSize))).draw(Levels)
            

    # vytvoření okna pro levely
    Levels = GraphWin("Select level", winX, winY)

    # vnořený loop pro vykreslení všech levelů
    for i in range(int(winX/levelsSize)):
        for j in range(int(winY/levelsSize)):
            drawL(i,j)
    
    # kontrolování pro jednotlivé interakce a volení levelů
    while True:
        # ukládám si stav klávesnice a myši
        key = Levels.checkKey()
        mouse = Levels.checkMouse()

        # pokud stiknu klávesu q nebo Q ukončí se hra
        if key == "q" or key == "Q":
            Levels.close()
            break
        # pokud stiknu klávesu e nebo E zobrazí se menu
        if key == "e" or key == "E":
            Levels.close()
            menu()
            break

        # pokud uživatel klikne a hodnota nebude none, vybere se korespondující level
        if mouse != None:
            Levels.close()
            game(clickPos(mouse))
            break



'''
GGGGGGGGG    AAAAAAA    MM     MM    EEEEEE
GG           AA   AA    MMM   MMM    EE
GG   GGGG    AAAAAAA    MM MMM MM    EEEEEE
GG     GG    AA   AA    MM     MM    EE
GGGGGGGGG    AA   AA    MM     MM    EEEEEE
'''

# hra samotná
def game(level):

    # array s informacemi o jednotlivých políčkách
    field = [[1]*int(winY/blockSize) for i in range(int(winX/blockSize))]

    # vykreslení hrací plochy podle dat v array 'field'
    def drawR(x,y):

        if field[x][y]:
            # pokud je v hodnota 1, vykreslí se bílé políčko a hodnota se změní na 0
            r = Rectangle(Point(x*blockSize,y*blockSize),Point(x*blockSize+blockSize,y*blockSize+blockSize))
            r.setFill("white")
            r.setOutline("gray")
            r.draw(Game)
            # t = Text(r.getCenter(),str(int(x+y*winY/blockSize)))
            # t.setTextColor("black")
            # t.draw(Game)
            field[x][y] = 0
        else:
            # pokud je v hodnota 0, vykreslí se černá políčko a hodnota se změní na 1
            r = Rectangle(Point(x*blockSize,y*blockSize),Point(x*blockSize+blockSize,y*blockSize+blockSize))
            r.setFill("black")
            r.setOutline("gray")
            r.draw(Game)
            # t = Text(r.getCenter(),str(int(x+y*winY/blockSize)))
            # t.setTextColor("white")
            # t.draw(Game)
            field[x][y] = 1

    # již popsáno výše
    def clickPos(mouse):
        x = mouse.getX()
        y = mouse.getY()

        blockX = -1
        blockY = -1

        num = 0
        while num < x:
            num += blockSize
            blockX += 1
        num = 0
        while num < y:
            num += blockSize
            blockY += 1

        # print(blockX*blockY)

        # po kliknutí se změní bravy bloků okolo
        # pokud se klikne na krajní blok, tak se změní barva pouze vnitřích bloků
        drawR(blockX,blockY)
        if blockX-1 >= 0: drawR(blockX-1,blockY)
        if blockY+1 < winY/blockSize: drawR(blockX,blockY+1)
        if blockY-1 >= 0: drawR(blockX,blockY-1)
        if blockX+1 < winX/blockSize: drawR(blockX+1,blockY)

    # kontroluje se, zda jsou všechny bloky bíle a pokud ano, nastane výhra
    def victory():
        # projedou se všechny řady seznamu
        for row in field:
            # v každé řadě se projede každé políčko
            for el in row:
                # pokud je políčko černé, má hodnotu 1 navrátí se False
                if el:
                    return False
        # pokud žádné políčko nemělo hodnotu 1, dostane se to až sem a tím nastane výhra
        # vypíše se text s výhrou
        
        Text(Point(winX/2,winY/2),"You won").draw(Game)
        # počká se, až uživatel klikne
        Game.getMouse()
        # navrátí se hodnota True
        return level

    # vytvoří se herní okno
    Game = GraphWin("Game - " + str(level), winX, winY)
    # vykreslí se všechna políčka
    for i in range(0,int(winX/blockSize)):
        for j in range(0,int(winY/blockSize)):
            drawR(i,j)

    # rozhodová ní o výběru úrovně
    # pokud má funkce parametr 0, vykreslí se první úroveň, pokud 1 druhý, atd.
    if level == 1:
        # úroveň se nastaví umělým kliknutím na pole
        clickPos(Point(winX/2,winY/2))
    if level == 2:
        clickPos(Point(winX/3,winY/3))
        clickPos(Point(winX/3*2,winY/3*2))
    
    # náhodné generování levelů od úrovně 3 a výše
    if level > 2:
        for i in range(level + 1):
            # print(Point(random.randint(15,winX-15),random.randint(15,winY-15)))
            clickPos(Point(random.randint(15,winX-15),random.randint(15,winY-15)))

    # nekonečná smyčka
    while True:
        # uložím si stav klávesy a myši
        key = Game.checkKey()
        mouse = Game.checkMouse()
        
        # pokud je stav klávesnice 'q', ukončí se hra a vyskočí se ze smyčky
        # if key == "q" or key == "Q":
        #     Game.close()
        #     break
        # pokud je stav klávesnice 'e', ukončí se hra, otevřou se úrovně a vyskočí se ze smyčky
        if key == "e" or key == "E":
            Game.close()
            levels(0)
            break
        
        # pokud stav myši není prázdný, to znamená, že není 'None', provede se klik
        if mouse != None:
            clickPos(mouse)

        # pokud funkce victory() vráti True, nastane výhra, zavře se okno
        # otevře se okno s úrovněmi a vyskočí se ze smyčky
        lv = victory()
        if lv:
            Game.close()
            levels(lv)
            break

# zapnutí menu
menu()
