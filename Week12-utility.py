#
# Hannah Taylor
#CSCI 102 - Scetion B
#Week 11 - Part B 
def PrintOutput(a):
    print('OUTPUT ' + str(a))
    
def LoadFile(a):
    f=open(a,'r+')
    contents=f.read()
    f.close()
    contents=contents.split()
    return contents

def UpdateString(a,b,c):
    string=a
    string_list=[]
    updated_string=''
    for char in string:
        string_list+= char
    string_list[c]=b
    updated_string=updated_string.join(string_list)
    PrintOutput(updated_string)

def FindWordCount(a,b):
    count=0
    i=0
    while i < (len(a)):
        if a[i] == b:
            count+=1
        i+=1
    return count

def ScoreFinder(players,scores,a):
    a=a.capitalize()
    if a in players:
        player_index=players.index(a)
        players_score=scores[(int(player_index))]
        PrintOutput(( str(a) + ' got a score of ' + str(players_score)))
    else:
        PrintOutput('player not found') 


def Union(a,b):
    union=[]
    union=a+b
    return str(union)

def Intersection(a,b):
    intersection=[]
    i=0
    while i < (len(a)):
        if a[i] in b:
            intersection.append(str(a[i]))
        i += 1
    return intersection 

def NotIn(a,b):
    Not_In=[]
    i=0
    while i < (len(a)):
        if a[i] not in b:
            Not_In.append(str(a[i]))
        i += 1
    return Not_In 
