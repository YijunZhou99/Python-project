#yijun zhou 52533998

import game_logic

NONE=' '


def main():
    '''
    This is the main funtion for the game.
    '''
    FIELD_ROWS = int(input())
    FIELD_COLUMNS = int(input())
    begin=input()
    start_field=begin_situation(FIELD_ROWS,FIELD_COLUMNS,begin)
    print_game_field(start_field)
    while True:
        command=input()
        if start_game(start_field,command)==None:
            break

def start_game(field:list,command:str):
    '''
    This function takes input continually and impeaches the command until game over.
    '''
    c=game_logic.FALLER(NONE)
    if command.startswith('F'):
        faller=game_logic.take_faller(command)
        colnumber=game_logic.take_column_number(command)
        c.f_command(field,colnumber,faller)
    elif command=='':
        n=c.falling(field)
        if n==0:
            print_game_field(field)
            print('GAME OVER')
            return 
    elif command=='R':
        c.rotate(field)
    elif command=='>':
        c.right(field)
    elif command=='<':
        c.left(field)
    elif command=='Q':
        return 
    print_game_field(field)
    return 1
        
def print_game_field(field:list):
    '''
    This function takes field and print it out with particular format. 
    '''
    for i in range(3,len(field[0])):
        print('|',end='')
        for j in range(len(field)):
            if type(field[j][i])==game_logic.FALLER:
                print(field[j][i].variable,end='')
            else:
                print(field[j][i],end='')
        print('|')
    print(' '+'---'*len(field)+' ')

def begin_situation(row:int,column:int,begin:str):
    '''
    This fucntion takes the comamnd which is either 'EMPTY' or 'CONTENTS' and
    the row & column. It decides which command is given and return the field.
    '''
    if begin=='EMPTY':
        start_field=empty(row,column)
    elif begin=='CONTENTS':
        start_field=contents(row,column)
    return start_field

def empty(row:int,column:int):
    '''
    This fuction will return a empty field by using given row & column.
    '''
    start_field=game_logic._new_game_field(row,column)
    return start_field

def contents(row:int,column:int):
    '''
    This fuction will return a field by using given row & column.
    And with given input information in the field.
    '''
    field=game_logic._new_game_field(row,column)
    inputs=[]
    for i in range(row):
        content=input()
        inputs.append(list(content))
    for col in range(column):
        for r in range(3,row+3):
            field[col][r]=' '+inputs[r-3][col]+' '
    start_field=game_logic.gravity(field)
    game_logic.matching(start_field)
    return start_field
    
if __name__ == '__main__':
    main()
