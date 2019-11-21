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

## score finder ##

## union ##

## intersection ##

## not in ##


