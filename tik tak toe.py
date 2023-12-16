import pygame
import button
import os
import copy
pygame.init()
#some constant values
WHITE=(255,255,255)
black=(0,0,0)
WIDTH,HEIGHT=800,800
FPS=60
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("tik tak toe by oussama sahraoui")
font = pygame.font.Font(os.path.join('assets','arialceb.ttf'),32)
text = font.render('click one of the squares to play', True,black)
replay_text = font.render('press x to play again', True,black)

textRect = text.get_rect()
textRect.center = (400,700)
textRect2 = text.get_rect()
textRect2.center =(400,750)
buttons=[]
img=img=pygame.image.load(os.path.join('assets','white.png')).convert_alpha()
circle=pygame.image.load(os.path.join('assets','circle.png'))
x=pygame.image.load(os.path.join('assets','x.png'))
background=pygame.image.load(os.path.join('assets','black.png'))

y1=200
y2=330
y3=460
x1=225
x2=355
x3=485


buttons.append(button.Button(x1,y1,img,1))
buttons.append(button.Button(x2,y1,img,1))
buttons.append(button.Button(x3,y1,img,1))

buttons.append(button.Button(x1,y2,img,1))
buttons.append(button.Button(x2,y2,img,1))
buttons.append(button.Button(x3,y2,img,1))

buttons.append(button.Button(x1,y3,img,1))
buttons.append(button.Button(x2,y3,img,1))
buttons.append(button.Button(x3,y3,img,1))


board_values=[0]*9
playing=True
turn="MAX"
def Terminal(s):
    
    for var in [1, 2]:
        if ((s[0] == var and s[1] == var and s[2] == var) or
            (s[3] == var and s[4] == var and s[5] == var) or
            (s[6] == var and s[7] == var and s[8] == var) or
            (s[0] == var and s[3] == var and s[6] == var) or
            (s[1] == var and s[4] == var and s[7] == var) or
            (s[2] == var and s[5] == var and s[8] == var) or
            (s[0] == var and s[4] == var and s[8] == var) or
            (s[6] == var and s[4] == var and s[2] == var)):
            return True, Value(s)

    
    if all(cell != 0 for cell in s):
        return True, 0

    return False, None

def Value(s):
    var = 1
    if ((s[0] == var and s[1] == var and s[2] == var) or
        (s[3] == var and s[4] == var and s[5] == var) or
        (s[6] == var and s[7] == var and s[8] == var) or
        (s[0] == var and s[3] == var and s[6] == var) or
        (s[1] == var and s[4] == var and s[7] == var) or
        (s[2] == var and s[5] == var and s[8] == var) or
        (s[0] == var and s[4] == var and s[8] == var) or
        (s[6] == var and s[4] == var and s[2] == var)):
        return 1
    var = 2
    if ((s[0] == var and s[1] == var and s[2] == var) or
        (s[3] == var and s[4] == var and s[5] == var) or
        (s[6] == var and s[7] == var and s[8] == var) or
        (s[0] == var and s[3] == var and s[6] == var) or
        (s[1] == var and s[4] == var and s[7] == var) or
        (s[2] == var and s[5] == var and s[8] == var) or
        (s[0] == var and s[4] == var and s[8] == var) or
        (s[6] == var and s[4] == var and s[2] == var)):
        return -1
    else:
        return 0


def Actions(s):
    actions=[]
    for i in range(len(s)):
        if s[i]==0:
            actions.append(i)
    return actions
def Result(s, action):
    new_state = s.copy()
    new_state[action] = 1 if Player(s) == "MAX" else 2
    return new_state
def Player(s):
    x_count = s.count(1)
    o_count = s.count(2)
    if x_count == o_count:
        return "MAX"
    else:
        return "MIN"

def MiniMax(s):
    if Terminal(s)[0]:
        return Terminal(s)[1]

    if Player(s) == "MAX":
        value = float('-inf')
    else:
        value = float('inf')

    for a in Actions(s):
        result = MiniMax(Result(s, a))
        if Player(s) == "MAX":
            value = max(value, result)
        else:
            value = min(value, result)

    return value


def board_is_full():
    global playing
    global text
    for i in board_values:
        if i==0:
            return False
    if Value(board_values)==-1:
        text = font.render("the board is full, but the bot wins!", True,black)
        playing=False
        return True
    elif Value(board_values)==0:
        text = font.render("the board is full, it's a draw!", True,black)
        playing=False
        return True
    elif Value(board_values)==1:
        text = font.render("the board is full, but the player wins!", True,black)
        return True
        playing=False
    
    
def AI():
    global board_values
    global turn
    if turn=="MIN":
        a=[]
        ans=[]
        if not 0 in board_values:
            return
        for i in range(len(board_values)):
            b=copy.deepcopy(board_values)
            b[i]=2
            if board_values[i]!=0:
                ans.append(float("inf"))
                continue
            ans.append(MiniMax(b))
        
        board_values[ans.index(min(ans))]=2
        
        turn="MAX"
        
            
def draw_window():
    global playing
    global text
    global turn
    AI()
    WIN.fill(WHITE)
    board_is_full()
    if Value(board_values)==1:
        playing=False
        text = font.render("the player wins!", True,black)
    elif Value(board_values)==-1:
        playing=False
        text = font.render("the bot wins!", True,black)
    
    WIN.blit(background,(225,200))
    

    for i in range(9):
        if buttons[i].draw(WIN) and board_values[i]==0 and playing==True:
            turn="MIN"
            board_values[i]=1
        else:
            if buttons[i].draw(WIN):
                pass

        
        
    
    
    
    if board_values[0]==1:
        WIN.blit(x,(x1,y1))
    elif board_values[0]==2:
        WIN.blit(circle,(x1,y1))
    if board_values[1]==1:
        WIN.blit(x,(x2,y1))
    elif board_values[1]==2:
        WIN.blit(circle,(x2,y1))
    if board_values[2]==1:
        WIN.blit(x,(x3,y1))
    elif board_values[2]==2:
        WIN.blit(circle,(x3,y1))
    
    
    if board_values[3]==1:
        WIN.blit(x,(x1,y2))
    elif board_values[3]==2:
        WIN.blit(circle,(x1,y2))
    if board_values[4]==1:
        WIN.blit(x,(x2,y2))
    elif board_values[4]==2:
        WIN.blit(circle,(x2,y2))
    if board_values[5]==1:
        WIN.blit(x,(x3,y2))
    elif board_values[5]==2:
        WIN.blit(circle,(x3,y2))
        
    
    if board_values[6]==1:
        WIN.blit(x,(x1,y3))
    elif board_values[6]==2:
        WIN.blit(circle,(x1,y3))
    if board_values[7]==1:
        WIN.blit(x,(x2,y3))
    elif board_values[7]==2:
        WIN.blit(circle,(x2,y3))
    if board_values[8]==1:
        WIN.blit(x,(x3,y3))
    elif board_values[8]==2:
        WIN.blit(circle,(x3,y3))
    
    
    
    
    if playing==False:
        WIN.blit(replay_text, textRect2)
    WIN.blit(text, textRect)
    pygame.display.update()



def main():
    global playing
    global board_values
    global text
    pygame.display.update()
    clock= pygame.time.Clock()
    run=True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    playing=True
                    board_values=[0]*9
                    text = font.render('good luck :)', True,black)
        draw_window()
if __name__=="__main__":
    main()
