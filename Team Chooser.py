import random

def main():
    print('\n\tTEAM CHOOSER\n')
    players=input('Enter player names: ').split()
    team_names=input('Enter team names: ').split()
    if len(team_names)>len(players):
        print('Even distribution of players not possible.')
        exit()
    i=0
    teams={x:[] for x in team_names}
    while len(players)>0:
        choice=random.choice(players)
        teams[team_names[i]].append(choice)
        players.remove(choice)
        i+=1
        if i==len(team_names):
            i=0
    for team,members in teams.items():
        if len(members)==1:
            print(f'{team} : {members[0]}')
        elif len(members)==2:
            print(f'{team} : {members[0]} and {members[1]}')
        else:
            print(f'{team} : {members[0]}',*members[1:-1],sep=',',end=f' and {members[-1]}\n')

if __name__ == '__main__':
    main()