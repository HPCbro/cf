print("Creator  -  Delete_L")

a = 100000000



import random , string

list = [5228402 , 5447317 , 2308880 , 5232841 , 5188148 , 4390270]




num = float(input('Input How Many Card to Generate: '))
f=open("card_b.txt","w", encoding='utf-8')
z = 0
zn = input("""1 or 2
    + - your first 7 digits
    - - system first 7 digits
        """)
if zn == "+":
    z = z + 1
if zn == "-":
    z = z + 2
if z == 1:
    fg = input("enter your 7 digits")
    for n in range(int(num)):
        m = random.randint(1, 9) 
        y = random.randint(21, 27)
        s = random.randint(100, 999)
        a = a + 1
        p = a
        c = (str(fg) + p + " " + "0" + str(m) + "/" + str(y) + " " + str(s))
        f.write(c)
        f.write("\n")
if z == 2:  
    for n in range(int(num)):
        m = random.randint(1, 9) 
        y = random.randint(21, 27)
        s = random.randint(100, 999)
        a = a + 1
        p = a
        l = (random.choice(list)) 
        c = (str(l) + str(p) + " " + "0" + str(m) + "/" + str(y) + " " + str(s))
        f.write(c)
        f.write("\n")
f.close()
print("numbers are saved to the file 'card_b.txt'")