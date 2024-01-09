from decimal import Decimal
from decimal import getcontext
import sys
def pi(precision):
    getcontext().prec=precision
    return sum(1/Decimal(16)**k * 
        (Decimal(4)/(8*k+1) -
         Decimal(2)/(8*k+4) -
         Decimal(1)/(8*k+5) -
         Decimal(1)/(8*k+6)) for k in range(precision))
pin = pi(int(sys.argv[1])*10)
search = int(sys.argv[2])
x = []
for i in str(pin):
    if i == ".":
        continue
    else:
        print("\r"+str(i),end="")
        x.append(i)
z = 13
d = 0
b = 0
color = "\033[36m"
print("")
try:
    while (True):
        for c in x:
            print(f"\r{color}"+str(z+d), end="")
            if (len(str(z+d)) < len(str(x))):
                db = ""
                for i in range(len(str(z+d))):
                    db += str(int(x[b+i]))
                if(str(int(z)+int(d)) == db):
                    print("\r\033[0m"+str(int(z)+int(d))+" => "+db+" \033[32m are matching numbers")
                if(str(db) == str(search)):
                    print("\r\033[28m"+str(int(z)+int(d))+" => "+db+" \033[0m is what you were searching for")
            level = ""
            for f in range(len(str(search))):
                level += str(int(x[b+f]))
            v = 0
            if(str(level) == str(search)):
                for e in str(search):
                    v += 1
                print("\r\033[4mIn regular Positioning "+str(d)+" through "+str(d+v)+" => "+level+" \033[0m is what you were searching for")
            d += 1
            b += len(db)
except Exception as e:
    print("\r\033[0m"+str(e))
