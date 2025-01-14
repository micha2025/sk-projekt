import os    

def main():

    while True:
        print('''
Menu:
1. Lista           
2. Wylacz hosta 
3. wyjdz
''')
        x = input()
        match x:
            case "1":
                i = 0
                print('\n')
                with open("lista") as file:
                    for line in file:
                        print(i, line)
                        i += 1
            case "2":
                print("wpisz numer:")
                try:
                    y = input()
                    y = int(y)
                except ValueError:
                    print("to nie numer")
                    continue
                lista = []
                with open("lista") as file1:
                    for line in file1:
                        lista.append(line.split()[0])
                if lista[y]:
                    with open("wylacz", "a") as f:
                        if os.path.getsize("wylacz") != 0:
                            f.write('\n')
                        f.write(lista[y].split(" ")[0])
                    lista.pop(y)
                    holder = ""
                    temp = 0
                    for el in lista:
                        holder += el
                        temp += 1
                        if temp == len(lista):
                            break
                        holder += '\n'
                    with open("lista", "w") as file2:
                        file2.write(holder)
                else:
                    "nie ma takiego hosta"
            case "3":
                break
            case _:
                print("niepoprawny input")

if __name__ == '__main__':
    main()