#1
a = input()
wynik = 0
for litera in a:
    #print(litera)
    if litera == " ":
        wynik += 1

print("To zdanie ma "+ str(wynik) +" spacje")
#2
import sys
a = 0
b = 0
print("Podaj pierwsza liczbe:")
liczba1 = sys.stdin.readline()
print("Podaj druga liczbe:")
liczba2 = sys.stdin.readline()
wynik = int(liczba1) * int(liczba2)
sys.stdout.write(str(wynik))
print("\n")
#3
# < > <= >= == !=
#4
import cmath
liczba3 = input()
if int(liczba3) < 0:
    print(abs(int(liczba3)))
#5
a = input()
b = input()
c = input()
if int(a) in (0,10) and int(a)>int(b) or int(b)>int(c):
    print("Spelnia warunek")
else:
    print("Nie spelnia warunku")

#6
for a in range(0,30,5):
    print (a)
