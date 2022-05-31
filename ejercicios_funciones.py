from os import system
import sys
def exercise():
    num_1 = int(input("Digite el primer numero\n"))
    system("cls")
    num_2 = float(input("Digite el segundo numero\n"))
    system("cls")
    if (num_1 > num_2):
        return 1
    elif (num_1 < num_2):
        return -1
    elif(num_1 == num_2):
        return 0

print(exercise())