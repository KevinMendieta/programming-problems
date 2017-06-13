from sys import stdin

def main():
    cont = 0
    line = stdin.readline().strip()
    while line != '*':
        if line == "Hajj":
            print("Case "+str(cont+1)+": "+"Hajj-e-Akbar")
        else:
            print("Case "+str(cont+1)+": "+"Hajj-e-Asghar")
        cont += 1
        line = stdin.readline().strip()
main()
