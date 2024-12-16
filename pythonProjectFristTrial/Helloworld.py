import  random
from optparse import Values
from symtable import Class
from tkinter.font import names

x,y,z="banana","Maongo","orange"
print(x)
print(y)
print(z)
fuits=["banana","mango","Oranges"]
b,c,d=fuits
print(b)
print(c)
print(d)
j=k=l="Namoota"
print(j)
print(l)
print(k)
x="Python "
y="is "
z="awesome"
print(x,y,z)
print(x + y + z)
l=7
h="jaalala"
print(l, h)

D ="awesome"
def myfunc():
    global D
    D="fantastic is coming"
    print("Python is "+D)
myfunc()
print("Python is " + D)

print("0----")
print(" ||||")
print("* "*10)
for strs in "wakisa birhanu":
    print(strs)
print(len(D))
text ="The best thing in life is being Free"
print("bst" in text)
if "t0mo" in text:
    print("yes there is it")
#how slicing work on strin
f="Wel come to our party        "
print(len(f))
print(f[0:5])
print(f[2:])
print(f[2:8])
print(f[-21:])
print(f[0:5])
print(f.upper())
print(f.lower())
print(f.strip())

age =21
price=200
txt=f"I am Wakisa, I am {age} "
Cost=f"The value of it is {price*age} birr"
print(Cost)
print(txt)
print(random.randrange(1,10))
w=0
while w<5:
    print("not yet,w= "+str(w))
    w=w+1
print("w="+str(w))
friends =["wakisa","John","James","Ebisa"]
for friend in friends:
    print(friend)
def attemts(n):
    x=1
    while x<=n:
        print("attemt "+str(x))
        x+=1
attemts(5)

correct_password="jesusislord"
attemts =0
max_attemt=3
while attemts<=max_attemt:
    checked_password=input("Enter your password  ")
    if checked_password== correct_password:
        print("access guaranted")
        break
    else:
        attemts += 1
        print(f"incorrect password {max_attemt - attemts} attemt is  Left")
        if attemts == max_attemt:
            print("Your account is blocked")
            break
Values =[12,34,12.56]
sum =0
length=0
for value in Values:
    sum += value
    length += 1
print("Total sum ="+str(sum) + " Average ="+str(sum/length))

prod =1
for n in range(2,6):
    prod *=n
print("product is "+ str(prod))

def toCelcius(x):
    return (x-32)*5/9
for x in range(0,101,10):
 print(x,toCelcius(x))

for left in range(7):
    for right in range(left,7):
        print("[ "+ str(left)+ "|" +str(right) +"]" ,end=" ")
    print()

teams =["waqo","Ebisa","Jiru","James"]
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs "+ away_team)

def greet_team(friends):
    for friend in friends:
        print("Hi " +friend)

greet_team(["wakisa","Birhanu","bula"])

def factorial(n):
    if n<2:
        return 1
    return n*factorial(n-1)
F=factorial(5)
print("factorial is "+ str(F))

def areaTriangle(width,height):
    return (height*width)/2
area_a=areaTriangle(2,3)
area_b=areaTriangle(4,6)
sum = area_a + area_b
print("the sum of the Area "+str(sum))

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds- hours * 3600 )// 60
    remain_seconds = seconds - hours* 3600 - minutes*60
    return  hours , minutes ,remain_seconds
hours , minute, seconds = convert_seconds(5000)
print(hours, minute , seconds)

def lucky_number(name):
    number = len(name) * 9
    print("Hello "+ name +" your lucky number is "+ str(number))
lucky_number("Wakisa")
lucky_number("Ebisa")

def is_correcct_name(userName):
    if len(userName)<3:
        print("user name maust be greater than 3 char")
    elif len(userName)>10:
        print("Again user name must be less than 15 char")
    else:
        print("Yes it can be user name")
is_correcct_name("Wa")

class Apple:
    color = ""
    fluvor = ""

jonagond = Apple()
jonagond.color = "red"
jonagond.fluvor = "Good"
print(jonagond.color)
print(jonagond.fluvor)

Marville = Apple()
jonagond.color ="Blue"
jonagond.fluvor ="Favor"
print(jonagond.fluvor.upper())
print(jonagond.color.upper())

class Animal:
    name = ""
    def speak(self):
        print("Oink i am {} ".format(self.name))
cat = Animal()
cat.name ="Adurre"
cat.speak()

class Jangle:
    def __init__(self,color, fluvor):
            self.color = "Black"
            self.Flovur ="Exelent"
jango = Jangle("Black","Exelent")
print(jango.Flovur)
print(jango.color)

class piglet:
    years =0
    def pigYears(self):
        return self.years * 3
pig = piglet()
pig.years = 10
print("The pig years is "+str(pig.pigYears()))

class mango:
   def __init__(self,color,fluvor):
       self.color = color
       self.fluvor = fluvor
   def __str__(self):
       return "The mangoes color is {} and its fluvor is {} ".format(self.color,self.fluvor)
mango1 = mango("green","bitter")
print(mango1)
# In heritance
class Fruit:
    def __init__(self, hallu,dhandhama):
        self.hallu = hallu
        self.dhandhama = dhandhama

class Papaya(Fruit):
    pass
class Avocado(Fruit):
    pass

Papa = Papaya("red","Sweet")
Avo = Avocado("Green","Tart")

print(Papa.hallu)
print(Avo.dhandhama)

class Animal:
    sound = ""
    def __init__(self,name):
        self.name = name
    def speak(self):
        print("{sound} i am {name}!  {sound} ".format(name= self.name, sound = self.sound ))

class Pig(Animal):
    sound = "woui"

sheep = Pig("cow")
sheep.speak()

class Cow(Animal):
    sound = "Wooooo"

dale = Cow("milky cow")
dale.speak()



