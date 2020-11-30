#Hackerrank 30 days challenge day 8
entries = int(input())
phonebook = {}
flag = True
for i in range(entries):
    #.split() is very useful in dealing with inputs
    namephone = input().split()
    #always remember to int() if necessary
    phonebook[namephone[0]] = int(namephone[1])
#while-try-except for accepting input until no input
#when user input nothing and hit EOF, EOFError occurs
while flag == True:
    try:
        query = input()
        if query in phonebook:
            print(f'{query}={phonebook[query]}')
        else:
            print('Not found')
    except EOFError:
        flag = False