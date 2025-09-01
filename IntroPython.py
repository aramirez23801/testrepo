# Example 1
print("Hello")

# Example 2
solution = 20
print(solution)
print("solution")

# Example 3
solution = 20
solution = solution + 10
print(solution)

#Example 4
a = 20
b = -5
if a < 0 or b<0:
  print(a*b)
else: 
  print(a+b)

# You will obtain a different error type in each. Why are these errors taking place?
# Example 5
#a = 10
#printed(a)

# Example 6
#number 1 = 20

# Example 7
a = 10
b = 20
print("The sum of these two numbers is", a - b)

#Example 8
p = 30000
i = 0.04
n = 8/12
fv=p*i*n
print("You must return the received money plus", fv, "euro in terms of interests")

#Example 9
# Datos conocidos
FV = 50000  # valor futuro en euros
I = 0.06    # tasa de interés anual (6%)

# Pedir al usuario que ingrese los años
N = int(input("Ingrese el número de años (N): "))

# Fórmula para calcular el valor presente
P = FV/((1+I) **N)

# Mostrar el resultado
print("Debe invertir hoy", P,  "para obtener €50,000 en", N,  "años.")

# Exercise 1: Define 2 variables with the values 10 and 20. Show their product.
a=10
b=20
c=a*b
print("El valor de C es ",c)

# Exercise 2: Given a positive number, print its last digit.
x=float (input("Ingrese un valor: "))
solution=x%10
print("El el ultimo digito de X es: ", solution)
# Exercise 3: Check this formula to transform Fahrenheit degrees to Celsius:
# Celsius = ((Fahrenheit - 32) x 5 )/9
f=float (input("Type the amount of Fahrenheit degrees: "))
c=float(((f-32)*5)/9)
print("The amount of Celsius degrees for the Fahrenhit degress give is ",c)

# Exercise 1: Given a date with this format "11:59:02, June 7th", extract the minutes.
example = "11:59:02, June 7th"
sol = example[3:5]
print("The minute in this date is", sol)

# Exercise 2: Given 2 strings, show the number of characters (symbols, digits, etc included) in the longest string.
# Spaces should not be counted!
a = "this is the first example"
b = "nothing"
length_a = len(a) - a.count(" ")
length_b = len(b) - b.count(" ")
answer = max(length_a, length_b)
print("The longest string has",answer,"characters in total")

# Exercise 3: Given 3 flight codes with this aspect, check how many flights start in Madrid.
f1 = "MAD-BCN"
f2 = "MAD-LON"
f3 = "LIS-MAD"
total = f1+f2+f3
solution = total.count("MAD-")
print("There are", solution, "flights starting in Madrid")

#Gues the 3 most popular names in Spain
name=input("Guess: ")
name=name.lower().strip()
if name == "lucia":
  print("Congrats. You guessed the most popular name in Spain")
elif name == "hugo":
    print("Congrats. You guessed the second most popular name in Spain")
elif name == "daniel":
    print("Congrats. You guessed the third most popular name in Spain")
else:
   print("Try again")

 # Exercise 1: Given a numerical variable, print a message explaining if the value is negative, positive or zero.
X = int(input("Enter a value: "))
if X > 0:
   print("El valor es positivo")
elif X < 0:
   print("El valor es negativo")
else:
   print("El valor es cero")
# Exercise 2: Ask for a name to the user. Show "Congrats" if the first character is an "A".
name = input("Provide a name")
name = name.lower().strip()
first = name[0]
if first == "a":
	print("Congrats")
else:
	print("The first character given is not A")
# Exercise 3: Ask for a name to the user. Show "Congrats" if the first character is a vowel.
name = input("Give a name")
name = name.lower().strip()
first = name[0]
if first in ["a","e","i","o","u"]:
	print("Congrats")
else:
	print("The first character given is not a vowel")
    
 #While Loop
name = input("Choose one brand")
name=name.lower().strip()
options = ["dell", "lenovo"]
while name not in options:
    name = input("Choose a brand within the options. Try again ")
    name=name.lower().strip()
print("Thanks!")

#For Loops
revenues = [20, 40, 100, -23, 12, -5 ]
for option in revenues:
    if option < 0:
        print("Negative Revenue Identified")

# Exercise 1: Given a lot of client's balances in a Bank office, show a message every time that you identify a negative balance.
balances = [-120,2300,-40, 120, 1000, 80]
for number in balances:
	if number < 0:
		print("Negative balance identified!!")

# Exercise 2: Given a lot of ages in a list for a lot of clients (we can assume that all the values are positive), show how many clients are adults (greater than 18 in Spain).
clients = [24,12,34,54,80,15]
adult = 0 #Contador
for age in clients:
	if age >= 18:
		adult = adult + 1
print("There are",adult,"adults in this group")

# Exercise 3: Ask for names until the user says "Pablo".
name = input("Please, say a name")
name = name.lower().strip()
while name != "pablo":
	name = input("Please, say a name")
	name = name.lower().strip()
print("Ok. You typed Pablo")