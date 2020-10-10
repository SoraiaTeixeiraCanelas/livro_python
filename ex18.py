#esta linha é funciona como os scripts eo argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2:{arg2}")

#*args nao serve para nada, em vez disso fazemos:
def print_two_again(arg1, arg2): #definção de função print_two_again com dois argumentos arg1, arg2
    print(f"arg1: {arg1}, arg2: {arg2}")

#esta só lega 1 argumento
def print_one(arg1):
    print(f"arg1: {arg1}")

#esta não leva argumentos
def print_none():
    print("I got nothin'.")

print_two("Soraia","Teixeira Canelas")
print_two_again("Soraia","Teixeira Canelas")
print_one("first!")
print_none()
