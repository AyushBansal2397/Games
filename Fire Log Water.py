import random

def main():
    while True:
        print('''\nFire(-~<{) , Logs(|||) and Water(~~~)
            
    Fire burns Logs
    Logs makes a bridge over Water
    Water puts out Fire
''')
        c=input('Enter your Choice(f,l or w): ')
        sym={'f':'-~<{','l':'|||','w':'~~~'}
        rules_win={'-~<{':'|||','|||':'~~~','~~~':'-~<{'}
        try:
            inp=sym[c.lower()]
        except:
            print('Wrong Choice!!!')
            continue
        out=random.choice(list(sym.values()))
        print(f'\n{inp} vs {out}')
        if inp==out:
            print('Draw :|')
        elif rules_win[inp]==out:
            print('YOU WON :)')
        else:
            print('You Loose :(')
        try:
            if not int(input('\nWanna Play More?(Enter 1) : ')):
                print('Till next time ;)')
                exit()
        except:
            print('Till next time ;)\n')
            exit()

if __name__ == '__main__':
    main()