import math
from PIL import Image
import sys

n = -1
op = -1
showTable = False
tableMode = -1
valid_n = False
valid_op = False
valid_showTable = False
valid_tableMode = False
showTable_int = 0
checkpoints = [True, False, False, False, False, False, False, False, False, False]

try:
    n = int(input("input modulus: "))
except:
    while valid_n == False:
        try:
            n = int(input("invalid input, expecting an integer: "))
        except: pass
        else: valid_n = True
else:
    valid_n = True

if n > 512:
    input("the modulus is above 512; values for the table won't be displayed in console")
else:
    try:
        showTable_int = int(input("Would you like for the resulting table to be displayed? (0 - no, 1 - yes): "))
    except:
        while valid_showTable == False:
            try:
                showTable_int = int(input("invalid input, expecting 0 or 1: "))
            except: pass
            else: 
                if showTable_int == 1 or showTable_int == 0: valid_showTable = True
    else: pass
if showTable_int == 1: showTable = True

try:
    op = int(input("input operation (0 - sum, 1 - difference, 2 - product, 3 - quotient, 4 - power, 5 - root*, 6 - combinatorial): "))
except:
    while valid_op == False:
        try:
            op = int(input("invalid input, expecting an integer from 0 to 6: "))
        except:
            pass
        else: 
            if op == 0 or op == 1 or op == 2 or op == 3 or op == 4 or op == 5 or op == 6:
                valid_op = True
else:
    while valid_op == False:
        if op >= 0 and op <= 6:
            valid_op = True
        else:
            try:
                op = int(input("invalid input, expecting an integer from 0 to 6: "))
            except:
                pass
            else: 
                if op == 0 or op == 1 or op == 2 or op == 3 or op == 4 or op == 5 or op == 6:
                    valid_op = True


print()
img = Image.new("RGBA", (n, n))
i = 0
k = 0

output = "" 

def colorPhase(a):
    b = a*7
    # print(f"b = {b}")
    if b >= 0 and b <= 1: return (int(b*255),0,0)
    elif b > 1 and b <= 2: return (255, int((b-1)*255),0)
    elif b > 2 and b <= 3: return (int(255*(1-(b-2))), 255, 0)
    elif b > 3 and b <= 4: return (0,255, int((b-3)*255))
    elif b > 4 and b <= 5: return (0, int(255*(1-(b-4))), 255)
    elif b > 5 and b <= 6: return (int((b-5)*255), 0, 255)
    elif b > 6 and b <= 7: return (255, int((b-6)*255), 255)


# print("_"*10)

while k < n:
    while i < n:
        if op == 0:
            cell = (i+k)%n
            if showTable == True:
                output = output + str(cell) + " "*(len(str(n)) - len(str(cell)) + 1)
            img.putpixel((i, k), (colorPhase(cell/n)))
        elif op == 1:
            cell = (i-k)%n
            if showTable == True:
                output = output + str(cell) + " "*(len(str(n)) - len(str(cell)) + 1)
            img.putpixel((i, k), colorPhase(cell/n))
        elif op == 2:
            cell = (i*k)%n
            if showTable == True:
                output = output + str(cell) + " "*(len(str(n)) - len(str(cell)) + 1)
            img.putpixel((i, k), (colorPhase(cell/n)))
        elif op == 3:
            if k == 0:
                output = output + "First row is all divisions by zero, therefore ignored\n0" + " "*(len(str(n)) - 1)
                k = 1
            else:
                cell = math.floor(i/k)%n
                if showTable == True:
                    output = output + str(cell) + " "*(len(str(n)) - len(str(cell)) + 1)
                img.putpixel((i, k), colorPhase(cell/n))
        elif op == 4:
            cell = (i**k)%n
            if showTable == True:
                output = output + str(cell) + " "*(len(str(n)) - len(str(cell)) + 1)
            img.putpixel((i, k), (colorPhase(cell/n)))
        elif op == 5:
            if k == 0:
                output = output + "First row is all divisions by zero, therefore ignored\n0" + " "*(len(str(n)) - 1)
                k = 1
            else:
                cell = math.floor(i**(1/k))%n
                if showTable == True:
                    output = output + str(cell) + " "*(len(str(n)) - len(str(cell)) + 1)
                img.putpixel((i, k), colorPhase(cell/n))
        elif op == 6:
            try: cell = (math.factorial(i)/(math.factorial(k)*math.factorial(i-k)))%n
            except: 
                img.putpixel((i, k), (0,0,0,0))
                output = output + " "*(len(str(n)) - len(str(cell)) + 1)
            else:
                if showTable == True:
                    output = output + str(cell) + " "*(len(str(n)) - len(str(cell)) + 1)
                img.putpixel((i, k), (colorPhase(cell/n)))
        i += 1
    k += 1
    i = 0
    output = output + "\n"
    if k/n > 0.1 and checkpoints[1] == False:
        print("10%")
        checkpoints[1] = True
    elif k/n > 0.2 and checkpoints[2] == False:
        print("20%")
        checkpoints[2] = True
    elif k/n > 0.3 and checkpoints[3] == False:
        print("30%")
        checkpoints[3] = True
    elif k/n > 0.4 and checkpoints[4] == False:
        print("40%")
        checkpoints[4] = True
    elif k/n > 0.5 and checkpoints[5] == False:
        print("50%")
        checkpoints[5] = True
    elif k/n > 0.6 and checkpoints[6] == False:
        print("60%")
        checkpoints[6] = True
    elif k/n > 0.7 and checkpoints[7] == False:
        print("70%")
        checkpoints[7] = True
    elif k/n > 0.8 and checkpoints[8] == False:
        print("80%")
        checkpoints[8] = True
    elif k/n > 0.9 and checkpoints[9] == False:
        print("90%")
        checkpoints[9] = True



img.save(f"n={n}, op={op}.png")
if showTable == True:
    print("\n")
    print("="*(47 + len(str(n))))
    print(f"\n   Resulting sum table for a set Z modulus {n}:\n")
    print("="*(47 + len(str(n))) + "\n")
    input(output)
else:
    print("\n")
    print("="*80)
    print(f"\n   Resulting sum table for a set Z modulus {n} has been saved as ''n={n}, op={op}.png''\n")
    print("="*80)