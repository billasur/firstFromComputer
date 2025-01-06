#WAP to find BMI using height and weight
height = float(input("what is you height?(Metre)"))
weight = int(input("what is you weight(Kg)?"))
bmi = weight/(height*height)
print("Your BMI is",bmi)


#WAP to calculate simple Interest
p = int(input("principal amount: "))
r = int(input("Rate of interest: "))
t = int(input("Time for the loan: "))
SimpleInterest = int((p*r*t)/100)
print("Total S.I you will pay is" , SimpleInterest)



#WAP to calculate area of circle
import math
r = int(input("radius: "))
if(r<0):
    print("Invalid radius")
else:
    area = (math.pi*r*r)
print("Area of circle is",area)



#WAP to calculate acceleration using distance and time
d = int(input("distance is"))
t = int(input("time taken is"))
a = d/(t*t)
print("accerleration is:",a)


#WAP to calculate velocity using mass and force
m = int(input("mass; "))
f = int(input("force: "))
t = int(input("time: "))
v= f*t/m
print("velocity is:",v)


#WAP to calculate (*)pyramid
n = int(input("how many lines you want in your program"))
for i in range(n):
    print(' ' * (n - i - 1) + '*' * (2*i + 1))


#WAP to ninvert Km to miles
km = float(input("in Kilometer: "))
miles = km*1.6
print(f"{km} in miles is {miles} miles")


#WAP to find joules
mass = int(input("mass:")) # kg
velocity = int(input("velocity: ")) #m/s
ke = (1/2)*(mass)*(velocity)**2
print("Kinetic energy in joule is",ke)


#WAP to find distance between two points using euclers distance formula
x1,y1 = map(int,input("first point co-oridnates(x1 y1)").split())
x2,y2= map(int,input("second point co-oridnates(x2 y2)").split())
distance = ((y2-y1)**(2)+(x2-x1)**(2))**(1/2)
print("distance between those points is",distance)




#WAP to convert into dollars,quaters,cents and pennies
def convert_cents(total_cents):
    dollars, cents = divmod(total_cents, 100)
    quarters, cents = divmod(cents, 25)
    dimes, cents = divmod(cents, 10)
    nickels, pennies = divmod(cents, 5)
    return dollars, quarters, dimes, nickels, pennies

total_cents = int(input("Enter the total cents: "))
dollars, quarters, dimes, nickels, pennies = convert_cents(total_cents)
print(f"Dollars: {dollars}")
print(f"Quarters: {quarters}")
print(f"Dimes: {dimes}")
print(f"Nickels: {nickels}")
print(f"Pennies: {pennies}")









