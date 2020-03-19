#yijun zhou 52533998


NONE=' '*3

def gravity(field:list):
    '''
    This funciton takes a field,
    returns a field with all jewels immediately fill empty space below them.
    '''
    new_field=[]
    for i in range(len(field)):
        line=[]
        number=0
        for j in range(len(field[0])):
            if field[i][j]!=NONE:
                line.append(field[i][j])
            elif field[i][j]==NONE:
                number+=1
        for n in range(number):
            line.insert(0,NONE)
        new_field.append(line)
    return new_field

def _new_game_field(row:int,column:int):
    '''
    This function takes row & column and returns a empty field with given information.
    '''
    field=[]
    for i in range(column):
        field.append([])
        for j in range(row+3):
            field[-1].append(NONE)
    return field

def take_faller(command:str):
    '''
    This function returns the faller of the command input as a list.
    '''
    faller=[]
    for i in command.split()[2:]:
        faller.append(FALLER(i))
    return faller
    

def take_column_number(command:str):
    '''
    This funtion returns the column number of the command input.
    '''
    return int(command.split()[1])

class FALLER:
    def __init__(self,variable):
        '''
        It takes the varible and makes the variable into appropriate format.
        '''
        self.variable='['+variable+']'
        self.status='fall'
        
    def f_command(self,field:list,colnumber:int,faller:list):
        '''
        This fuction takes the field, column number and faller.
        It returns a field that contain the faller.
        '''
        if not is_forze(field):
            return
        else:
            n=0
            while n<=3:
                for i in range(n):
                    field[colnumber-1][i]=faller[i]
                n+=1
            self.falling(field)

    def falling(self,field:list):
        '''
        This funtion takes a field that contains the faller.
        If the faller is not been forzen yet, it'll make the faller falls one step once it be called.
        If the faller is been forzen, it'll decide whether there are matching faller or game over.
        '''       
        if not is_forze(field):
            if is_land(field):
                return
            else:
                for i in range(len(field)):
                    for j in reversed(range(len(field[i]))):
                        if type(field[i][j])==FALLER:
                            field[i][j+1]=field[i][j]
                            field[i][j]=NONE
        if is_forze(field):
            matched(field)   
            matching(field)
            if is_match(field):
                print(is_match(field))
                pass
            else:
                if is_game_over(field):
                    return 0
        is_land(field)
            

    def rotate(self,field:list):
        '''
        This function takes field.
        It'll find the faller in it and rotate the faller in a particular way. 
        '''
        n=[]
        temp=[]
        for i in range(len(field)):
            for j in reversed(range(len(field[i]))):
                if type(field[i][j])==FALLER:
                    n.append(i)
                    n.append(j)
                    temp.append(field[i][j])
                    field[i][j]=field[i][j-1]
        try:
            field[n[0]][n[1]-2]=temp[0]
        except:
            pass

    def left(self,field:list):
        '''
        This function takes field.
        It'll find the faller in it and make it move to the left if there is space on the left side.
        '''
        for i in range(len(field)):
            for j in reversed(range(len(field[i]))):
                if type(field[i][j])==FALLER:
                    if i-1>=0:                           
                        if field[i-1][j]==NONE:
                            field[i-1][j]=field[i][j]
                            field[i][j]=NONE
                        else:
                            return
                    else:
                        pass                   

    def right(self,field:list):
        '''
        This function takes field.
        It'll find the faller in it and make it move to the right if there is space on the right side.
        '''
        for i in reversed(range(len(field))):
            for j in reversed(range(len(field[i]))):
                if type(field[i][j])==FALLER:
                    try:
                        if field[i+1][j]==NONE:
                            field[i+1][j]=field[i][j]
                            field[i][j]=NONE
                        else:
                            return
                    except:
                        pass
    def land(self):
        '''
        This function change the '[' into '|'.
        '''
        self.variable='|'+self.variable[1]+'|'
        self.status='land'        


def is_land(field:list):
    '''
    This function takes a field, find the faller in it and decide whetehr it should land.
    '''
    if forze(field):
        pass
    else:
        r=0
        c=[]
        for i in range(len(field)):
                for j in reversed(range(len(field[i]))):
                    if type(field[i][j])==FALLER:
                        r=i
                        c.append(j)     
        try:
            if field[r][c[0]+1]==NONE:
                return False
            else:
                for n in range(3):
                    field[r][c[n]].land()
                return True
        except:
            for n in range(3):
                field[r][c[n]].land()
            return True
    
def forze(field:list):
    '''
    check if the faller is forzen.
    '''
    result=True
    for i in range(len(field)):
            for j in reversed(range(len(field[i]))):
                if type(field[i][j])==FALLER:
                    result=False
    return result
                        
def is_forze(field:list):
    '''
    This function takes a field and decides whether the whole field is forzen.
    if not, it make the land faller forze.
    '''
    result=True
    for i in range(len(field)):
            for j in reversed(range(len(field[i]))):
                if type(field[i][j])==FALLER:
                    if field[i][j].status=='land':
                        field[i][j]=' '+field[i][j].variable[1]+' '
                    elif field[i][j].status=='fall':
                        result=False
                else:
                    pass              
    return result

def is_game_over(field:list)->bool:
    '''
    This function takes a field and decieds whether game over.
    '''
    result=0
    for i in range(len(field)):
        if field[i][2]==NONE:
            result+=0
        else:
            result+=1
    if result!=0:
        return True
    else:
        return False
    
def matching(field:list):
    '''
    This function conbine all the matching situations.
    '''
    _vertical_matching(field)
    _horizontal_matching(field)
    _diagonal_rd_matching(field)
    _diagonal_lr_matching(field)

def is_match(field:list):
    result=False
    for i in range(len(field)):
            for j in (range(len(field[i]))):
                if field[i][j][0]=='*':
                    result=True
    return result

def matched(field:list):
    '''
    This function takes a field and eliminate the matching elements.
    '''
    result=False
    for i in range(len(field)):
            for j in (range(len(field[i]))):
                if field[i][j][0]=='*':
                    field[i][j]=NONE
                    result=True
    if result==True:
        new_field=gravity(field)
        for i in range(len(field)):
            for j in (range(len(field[i]))):
                field[i][j]=new_field[i][j]
                    
    

def _vertical_matching(field:list):
    '''
    This function takes a field and check the vertical matching.
    '''
    for i in range(len(field)):
        match_number=0
        for j in range(len(field[0])-1):
            if field[i][j][1]==field[i][j+1][1] and field[i][j+1]!=NONE:
                match_number+=1
                if match_number>=2:
                    field[i][j+1]='*'+field[i][j+1][1]+'*'
                    field[i][j]='*'+field[i][j][1]+'*'
                    field[i][j-1]='*'+field[i][j-1][1]+'*'
            else:
                match_number=0
    

def _horizontal_matching(field):
    '''
    This function takes a field and check the horizontal matching.
    '''
    for j in range(len(field[0])):
        match_number=0
        for i in range(len(field)-1):
                if field[i][j][1]==field[i+1][j][1] and field[i+1][j]!=NONE:
                    match_number+=1
                    if match_number>=2:
                        field[i+1][j]='*'+field[i+1][j][1]+'*'
                        field[i][j]='*'+field[i][j][1]+'*'
                        field[i-1][j]='*'+field[i-1][j][1]+'*'
                else:
                    match_number=0              

def _diagonal_rd_matching(field):
    '''
    This function takes a field and check the diagonal matching that on right down direction.
    '''
    for i in range(len(field)-1):
        match_number=0
        for j in range(len(field[0])-1):
            try:
                if field[i][j][1]==field[i+1][j+1][1] and field[i+1][j+1]!=NONE:
                    match_number+=1
                    if match_number>=2:
                        field[i+1][j+1]='*'+field[i+1][j+1][1]+'*'
                        field[i][j]='*'+field[i][j][1]+'*'
                        field[i-1][j-1]='*'+field[i-1][j-1][1]+'*'
                        i+=1
                    else:
                        i+=1
                else:
                    match_number=0
            except:
                pass
                    
def _diagonal_lr_matching(field):
    '''
    This function takes a field and check the diagonal matching that on left rising direction.
    '''
    for i in reversed(range(1,len(field))):
        match_number=0
        for j in range(len(field[0])-1):
            try:
                if field[i][j][1]==field[i-1][j+1][1] and field[i-1][j+1]!=NONE:
                    match_number+=1
                    if match_number>=2:
                        field[i-1][j+1]='*'+field[i-1][j+1][1]+'*'
                        field[i][j]='*'+field[i][j][1]+'*'
                        field[i+1][j-1]='*'+field[i+1][j-1][1]+'*'
                        i-=1
                    else:
                        i-=1
                else:
                    match_number=0
            except:
                pass

