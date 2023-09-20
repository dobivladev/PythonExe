import math

user_input = float(input("Enter lengt:"))

a = user_input

# Square

P = 4 * a
S = a * a
# Circle

C = 2 * math.pi * a

# Lice i obikolka trig
St = (math.sqrt(3) / 2) * a
Pt = 3 * a

print("Square: P = " + str(P) + " ,S = " + str(S))
print("Circle: P = " + str(C))
print("Square: P = " + str(Pt) + " S = " + str(St))
