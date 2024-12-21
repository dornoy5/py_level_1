command= input("enter the command: ")
start=False
stop=False
quit=False
help=False

while not quit:
    if command.lower() == 'start':
        if not start:
            start=True
            stop=False
            print('Game started')
        else: print("game is already started")
    elif command.lower() == 'stop':
        if not stop and not start:
            stop=False
            start=False
            print('game cant stop if it didnt start yet')
        elif not stop:
            stop=True
            start=False
            print('Game stopped')
        else: print("game is already stoped")
    elif command.lower() == 'quit':
        print('Game quit')
        quit=True
        break
    elif command.lower() == 'help':
        print('Available commands: start, stop, quit')
    else:
        print('Invalid command. Please try again, Available commands: start, stop, quit, help')
    command=input()


