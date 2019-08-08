import random

def main():
    while True:
        print('''\nRock(O) , Paper([]) and Scissor(>8)
            
    Rock blunts scissors
    Paper covers rock
    Scissors cut paper
''')
        c=input('Enter your Choice(r,p or s): ')
        sym={'s':'>8','p':'[]','r':'oOo'}
        rules_win={'>8':'[]','[]':'oOo','oOo':'>8'}
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