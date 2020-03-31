# Závěrečná práce


## Úvod
Moje závěrečná práce se jmenuje “Cross game”. Tento název jsem ji dal kvůli tomu, že ve hře máte za úkol klikáním na kříže (odtud cross), vyčistit hrací plochu tak, že po kliknutí se na každé světové straně od kliknutí změní jeden blok tak, že pokud byl bílý, tak bude černý a naopak. Podrobněji v bodě 4. Kód a vysvětlení

## Spouštění
K vytvoření této hry jsem použil program python ve verzi 2.7 takže bude potřeba i ike spuštění. V konzoli si můžete zkontrolovat, jestli máe nainstalovaný python tím, že napíšete python. (já zde píšu python3 jelikož mám nainstalovaných více verzí, pokud máte také více verzi, můžete použít můj způsob)
	Zde můžete vidět verzi pythonu, která je nyní 3.x.x . Pro ukončení napíšete exit().
	Pokud nemáte nainstalovaný python na počítači, můžete ho stáhnout z oficiální stránky pythonu. Stáhněte si však verzi 3.x.x, jinak by program nemusel správně fungovat nebo by nemusel fungovat vůbec.
	Nyní, když máte nainstalovaný python 3.x.x, můžeme spustit program tím, že napíšete python zaverecka.py. Ovšem musíme bát ve složce kde je náš program uložený, v mém přípdadě je to složka python/graphWin. Do této složky se dostanu tak, že napíšu cd python/graphWin.
Pokud byste si chteli vytvořit spustitelný program, musíte si stáhnout python knihovnu auto-py-to-exe a pip. Pro nainsalování auto-py-to-exe potřebujete pip, ten nainstalujete následovně. Do kozole napíšete python get-pip.py
	Nyní, když máte nainstalovaný pip, můžete si stáhnout auto-py-to-exe tak, že napíšete pip install auto-py-to-exe.
	Teď už stačí jen napsat auto-py-to-exe a otevře se vám program pro konvertování pzthon souboru do spustitelného souboru. Do script location dáte složku s programem a dáte convert.

## Rozhraní
Při spuštění hry se vám zobrací úvodní okno s tlačítkem začít hru a s klávesovými zkratkami. 
  Tady nezbývá než kliknout na tlačítko start. Možná se můžete ptát, proč zde nemohu použít klávesové zkratky? 
  Z jednoho prostého důvodu, který bude vysvětlen v následujícím bodě.
	Po kliknutí na tlačítko start se zobrazí úrovně. Počet úrovní je proměnný v závislosti na velikosti okna. 
  Nyní si můžete vybrat úroveň a hrát. Úkolem je zbavit se všech černých čtverců. Doporučuji spustit první dva levely, kde se to dá snadno pochopit. Jakmile se zbavíte všech černých čtverců, tak se zobrazí text, že jste vyhráli a po kliknutí kamkoliv v okně vás to vrátí na výběr úrovně.
Úroveň je rozděleda do čtverců obdobně jako výber úrovně, tzn. že je promenný počet políček.

## Kód a vysvětlení
Začal bych s globálními proměnnými. Je jich zde několik. Těmi proměnnými jsou výška a šířka okna, dále velikost bloků v úrovni a výběru úrovně. Obě tyto velikosti jsou zadány v šírce x a výšce y.

### Hlavní menu
Hlavní rozdíl mezi hlavním menu a úrovní nebo výběrem úrovní je způsob fungování. Zde program prostě čeká, dokud nekliknete. 
A pokud se vám zrovna podaří tefit se do stlačítka start, tak vás to posune i dál.
	Zde jsem si vytvořil na to funkci, která kontroluje, kam jsem kliknul.
```python
if (mX > p1.getX() and mX < p2.getX() and mY > p1.getY() and mY < p2.getY()):
  return True
```
Kde mX je souřadnice kliknutí myši na ose X a mY je to samé, ale na ose Y. Dále p1 je levý horní bod čtverce a p2 je pravý dolní roh čtverce a funkcí getX() dostanu z bodu X a analogicky getY() dostane z bodu Y. V této funkci porovnávám, zda-li jsem kliknul do čtverce a pakod ano, vrátí to hodnotu true.
Menu = GraphWin("Menu", winX, winY)
    
```python
start = Rectangle(Point(winX/2-50,winY/2-50),Point(winX/2+50,winY/2))
start.draw(Menu)
desc1 = Text(Point(start.getCenter().getX(),start.getCenter().getY()+50),"while in game or level browser press 'e' to go back and 'q' to exit")
desc1.draw(Menu)
Text(start.getCenter(),"Start").draw(Menu)
```
Zde na obrázku vidíte kreslení objektů a vytváření oken. Okna jsou zde celkem tři. Jedno pro menu, úroveň a výběr úrovní. Vytvořím si okno Menu tak, že si do proměnné menu pomocí funkce GraphWin() vytvořím okno s následujícími parametry: název, velikost x a velikost y. Dále si vytvořím “tlačítko” start, což je vlastně čtverec, který vytvořím pomocí funkce Rectangle a vložím tam následující argumenty: bod1 a bod2. Zde jsem zvolil doby tak, aby bylo tlačítko start vždy uprostřed, tudíž jsem vzal šířku a výšku a vydělil je dvěma. Pak už stačí toto tlačítko jen vykreslit tak, že za objekt tečkou přidělím funkci draw() a do ní napíšu do jakého okna se má vykreslit, v tomto případě Menu. Aby to naše tlačítko obsahovalo nějaký text, musím ho tam přidat pomocí funkce Text() kde do argumentů píšu pozici, kde bude střed textového řetězce a samotný text.

### Výběr úrovní
Před vstupem do výběru úrovní se zkontroluje, jestli jsem tuto hru již hrál dříve a zda jsem již splnil nějaké úrovně. Zkontroluje to tak, že se podívá do souboru lvl.txt . Pokud soubor neexistuje, tak se vytvoří.
```python
try:
    f = open("lvl.txt","r")
    content = f.read()
    val = content.split(",")
    f.close()
except:
    f = open("lvl.txt","w+")
    f.close()
```
No a když ano, tak se z něj načtou všechny splněné úrovně.
```python
for el in val:
    if el == '':
        continue
    if int(el) > len(lvl):
        over += el + ","
        continue
        lvl[int(el)] = 1
```
Zde se načtou všechny úrovně do proměnné lvl, která slouží pro vykreslování správné barvy úrovní v závislosti na to, zda-li jste již danou úroveň splnili či nikoliv. První podmínka slouží pro odchytávání chyb, druhá slouží k zapisování úrovní, které nelze vykreslit, ale jsou splněné. Pokud jakákoliv z těchto podmínek nastane, tak se žádná hodnota nezapíše do proměnné lvl a pokračuje se další hodnotou.
	Před vykreslením všech úrovní, se ještě přidá do proměnné lvl právě splněná úroveň, ze které jste přišli. Ale aby byla úroveň splněná, musíte dosáhnout vítezství, jinak se nic nestane a vráttíte se do výběru úrovní bezezměny.
```python
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
```
  Jakmile jsou všechny tyto věci hotové, může se vykreslit samotné okno.
Funguje to stejným způsobem jako v menu, ale teď jsem na to vytvořil funkce. Funkci dám hodnoty x a y, kde x a y jsou souřadnice levého horního rohu. Taky zde kontroluji splněné úrovně, takže pokud je splněná, bude vybarvená šedě, ovšem pokud není, bude bílá.
	Teď, když máme vykreslenou úroveň můžeme začít něco dělat.
```python
while True:
    key = Levels.checkKey()
    mouse = Levels.checkMouse()
    if key == "q" or key == "Q":
        Levels.close()
        break
    if key == "e" or key == "E":
        Levels.close()
        menu()
        break
    if mouse != None:
        Levels.close()
        game(clickPos(mouse))
        break
```
Zde se kontroluje, jestli jsem něco udělal, tzn. jestli jsem kliknul nebo zmáčknul klávesu. Pokud ano, tak se zkontroluje, jestli to někam pasuje, jestli jsem zmáčkl q/Q opustím hru, jestli e/E vrátím se do menu, pokud jsem klikl, tzn, že hodnota kliku není prázdná, zavřu výběr úrovní a otevřu úroveň, na kterou jsem klikl. Zkontroluji to následovně.
Z kliku si vezmu x a y a budu počítat, kolikrát se vleze velikost bloku úrovně do něj na ose x a to samé na ose y. Kolikrát je na ose y tolikrát přičtu k x hodnotu počtu úrovní na řádku. Například pokud mám 25 úrovní v okně (5x5), tak jem klikl přesně doprostřed, tzn. že x i y jsou 3, ale abych dostal 13, což je střed, musím dvakrát přičíst pět.

### Úroveň
Na začátku všeho si vytvořím dvourozměrné hrací pole a do všech políček se nastaví hodnota 1. Pak můžeme celou úroveň vykreslit.
```python
field = [[1]*int(winY/blockSize) for i in range(int(winX/blockSize))]
```
Vykresluje se to v podstatě stejným způsobem jako ve výběru úrovní, akorát se zde kontroluje, jestli je hodnota políčka 0 nebo 1. Pokud je jedna, políčko bude bílé a pokud nula, políčko bude černé. Po vykreslení se hodnota změní.
```python
if field[x][y]:
    r = Rectangle(Point(x*blockSize,y*blockSize),Point(x*blockSize+blockSize,y*blockSize+blockSize))
    r.setFill("white")
    r.setOutline("gray")
    r.draw(Game)
    field[x][y] = 0
else:
    r = Rectangle(Point(x*blockSize,y*blockSize),Point(x*blockSize+blockSize,y*blockSize+blockSize))
    r.setFill("black")
    r.setOutline("gray")
    r.draw(Game)
    field[x][y] = 1
```
  Generování úrovní probíhá následovně. Ano, jsou pokaždé jiné až na první dvě, ketré jsou předdefinované.
```python
if level > 2:
    for i in range(level + 1):
        clickPos(Point(random.randint(15,winX-15),random.randint(15,winY-15)))
```
Generování úrovní probíhá tak, že se simulují kliknutí na hrací plochu, a tím se vytvoří požadovaná úroveň. Platí že kolikátá úroveň, tolik kliknutí plus jedna.
Pokud se vám podaří odstranit veškeré černé čtverečky, nastane vítezství.
```python
def victory():
    for row in field:
        for el in row:
            if el:
                return False
    Text(Point(winX/2,winY/2),"You won").draw(Game)
    Game.getMouse()
    return level
```
Kontroluje se to tak, že se projede celý seznam políček, a pokud se tam nachází černý čtvereček, tak se vrátí hodnota false. pokud tam ale žádný neí, vypíše se, že jste vyhráli, počká až kliknete, aby jste si to mohli přečíst a navrátí hodnotu úrovně.
Pokud je tedy navrácená hodnota jakékoliv číslo, tak se plní podmínka a tím pádem i úroveň. Zavře se úroveň a otevře se výběr úrovní.
```python
lv = victory()
if lv:
    Game.close()
    levels(lv)
    break
```

## Odkazy
grafická knihovna dokumentace - [zde](https://mcsp.wartburg.edu/zelle/python/graphics/graphics/graphref.html)

stránka pro stažení python - [zde](https://www.python.org/downloads/windows/)
