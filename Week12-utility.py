# Tucker Vana
# CSCI 102 - Section E

## print output ##
def PrintOutput(string):
    """formats output"""
    print('OUTPUT',string)

## load file ##
def LoadFile(file_name):
    f = open(file_name,'r')
    lines = f.read()
    print(lines)
    return lines

## update string ##
def UpdateString(string_1,string_2,index):
    string_1 = string_1[:index]+string_2+string_1[index+1:]
    return string_1

## find word count ##
def FindWordCount(lst, string):
    count = 0
    for i in lst:
        if string in lst:
            count += 1
        return count
    
## score finder ##
def ScoreFinder(names,scores,player):
    score = -1
    for i in range(len(names)):
        if (names[i].lower() == player.lower()):
            score = scores[i]
            break
    if (scores ==-1):
        print('Player not found')
    else:
        print(player,'got a score of',score)
            

## union ##
def Union(list_1,list_2):
    list_3=[]
    for i in list_1:
        if i not in list_3:
            list_3.append(i)
        for i in list_2:
            if i not in list_3:
                list_3.append(i)
        return list_3

## intersection ##

## not in ##


