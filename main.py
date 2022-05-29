error = False
import sys
import time
import random
try:
    import os
    from os import system
    system("title " + "Nitro Sniper")
except:
    pass
try:
    import colorama
except Exception:
    print("Missing Colorama Module")
    error = True
import os
if error == True:
    while True:
        autofix = input("Missing Module(s), Wanna Try Auto Fix The Problem (y/n): ")
        if autofix == "y" or autofix == "n":
            break
        else:
            print("Enter A Valid Choice")
    if autofix == "y":
        try:
            os.system("pip install colorama")
        except Exception:
            print("Error While Downloading Module")
            input("")
            exit()
        print("Problem Should Be Fixed Now, Please Restart The Program")
        input("")
        exit()
    if autofix == "n":
        print("Press Enter To Close Program")
        input("")
        exit()
colorama.init(autoreset=True)
def print00025(text):
    for c in text:
        sys.stdout.write(colorama.Fore.CYAN + c)
        sys.stdout.flush()
        time.sleep(0.0025)
    sys.stdout.write("\n")
def print0040(text):
    for c in text:
        sys.stdout.write(colorama.Fore.CYAN + c)
        sys.stdout.flush()
        time.sleep(0.040)
    sys.stdout.write("\n")
def print0040f(text):
    for c in text:
        sys.stdout.write(colorama.Fore.RED + c)
        sys.stdout.flush()
        time.sleep(0.00000005)
    sys.stdout.write("\n")
def print0040e(text):
    for c in text:
        sys.stdout.write(colorama.Fore.GREEN + c)
        sys.stdout.flush()
        time.sleep(0.00000005)
    sys.stdout.write("\n")
print00025("""
    _   ___ __                  
   / | / (_) /__________        
  /  |/ / / __/ ___/ __ \       
 / /|  / / /_/ /  / /_/ /       
/_/_|_/_/\__/_/_  \____/        
  / ___/____  (_)___  ___  _____
  \__ \/ __ \/ / __ \/ _ \/ ___/
 ___/ / / / / / /_/ /  __/ /    
/____/_/ /_/_/ .___/\___/_/     
            /_/                 
    MADE BY blob#0005""")

print0040("Loading Api...")
print0040("Starting Proxys...")
print0040("Started Api And Proxys")
print0040("Starting Gen In 3 Seconds...")
time.sleep(3)
done = 0
ee = random.randint(15, 40)
for e in range(int(ee)):
    choices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    n1 = random.choice(choices)
    n2 = random.choice(choices)
    n3 = random.choice(choices)
    n4 = random.choice(choices)
    n5 = random.choice(choices)
    n6 = random.choice(choices)
    n7 = random.choice(choices)
    n8 = random.choice(choices)
    n9 = random.choice(choices)
    n10 = random.choice(choices)
    n11 = random.choice(choices)
    n12 = random.choice(choices)
    n13 = random.choice(choices)
    n14 = random.choice(choices)
    n15 = random.choice(choices)
    n16 = random.choice(choices)
    code = f"{n1}{n2}{n3}{n4}{n5}{n6}{n7}{n8}{n9}{n10}{n11}{n12}{n13}{n14}{n15}{n16}"
    done = int(done) + 1
    print0040f(f"[{str(done)}] Generated Invalid Code: https://discord.gift/" + code)
n1 = random.choice(choices)
n2 = random.choice(choices)
n3 = random.choice(choices)
n4 = random.choice(choices)
n5 = random.choice(choices)
n6 = random.choice(choices)
n7 = random.choice(choices)
n8 = random.choice(choices)
n9 = random.choice(choices)
n10 = random.choice(choices)
n11 = random.choice(choices)
n12 = random.choice(choices)
n13 = random.choice(choices)
n14 = random.choice(choices)
n15 = random.choice(choices)
n16 = random.choice(choices)
code = f"{n1}{n2}{n3}{n4}{n5}{n6}{n7}{n8}{n9}{n10}{n11}{n12}{n13}{n14}{n15}{n16}"
done = int(done) + 1
print0040e(f"[{str(done)}] Generated Valid Code: https://discord.gift/" + code)
time.sleep(2)
print0040e("Succsesfully Redeemed Nitro To Account")
time.sleep(2)
print0040e("CYA")
time.sleep(5)
exit()
