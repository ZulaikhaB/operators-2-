print("enter marks in 4 subjects :")
A = int(input("enter marks of the first subject:"))
U = int(input("enter marks of the second subject:"))
Z = int(input("enter marks of the third subject:"))
B = int(input("enter marks of the forth subject:"))
H = A + U + Z + B
F = H / 5 
if F >= 90:
    print("grade A")
elif F >= 80 and F <= 89 :
    print ("grade B")
elif F >= 70 and F<= 79 :
    print ("grade C")
elif F >= 60 and F <= 69 :
    print ("grade D")
else :
    print ("invalid")


