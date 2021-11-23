
import pygame
import time
import random
import sys






#init
pygame.init()
#score
score = 0
#fps control
setfps = pygame.time.Clock()

#size
f_size_x = 400
f_size_y = 400
#difficulty
difficulty = 10
#window
pygame.display.set_caption("Snake game by : Sleepy")
wn = pygame.display.set_mode((f_size_x, f_size_y))
#colors
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 128, 0)
purple = pygame.Color(128, 0, 128)
lime = pygame.Color(0, 255, 0)
yellow = pygame.Color(255, 255, 0)
blue = pygame.Color(0, 0, 255)
grey = pygame.Color(32, 32, 32)


#variables

def_height=10
def_width=10
width=0
height=0

snake_pos = [100, 50]
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]

food = [random.randrange(1, f_size_x//10)*10, random.randrange(1, f_size_y//10)*10]
rock = [[-100,-100]]

#foodbools
food_bool = True
rock_bool = True
gfood_bool = True
pfood_bool = True
rfood_bool = True
yfood_bool = True
random_bool = True
yellow_food = [-100,-100]
purple_food = [-100,-100]
green_food = [-100,-100]
red_food = [-100,-100]

fruit_array = [rock,yellow_food,purple_food,green_food,red_food] 
direction = 'RIGHT'
change_dir = direction
random_fruit=10
cur_time = 0
btn_press_time = 0
enter_bool = True
start_m= True
gameloop=False

#defs
def detectCollisions(x1,y1,w1,h1,x2,y2,w2,h2):
    if (x2+w2>=x1>=x2 and y2+h2>=y1>=y2):

        return True

    elif (x2+w2>=x1+w1>=x2 and y2+h2>=y1>=y2):

        return True

    elif (x2+w2>=x1>=x2 and y2+h2>=y1+h1>=y2):

        return True

    elif (x2+w2>=x1+w1>=x2 and y2+h2>=y1+h1>=y2):

        return True

def start_menu(clr):
    my_font = pygame.font.SysFont('comicsans',40)
    start_surface = my_font.render('SNAKE GAME', True,green)
    start_rect = start_surface.get_rect()
    start_rect.midbottom = (f_size_x/2, f_size_y/3)
    wn.fill(black)
    pressbtn(clr)
    wn.blit(start_surface,start_rect)
    pygame.display.flip()
    
def pressbtn(clr):
    my_lil_font = pygame.font.SysFont('comicsans',30)
    press_surface = my_lil_font.render('Press any button to play', True,clr)

    
    press_rect = press_surface.get_rect()
    press_rect.midbottom = (f_size_x/2, f_size_y/2)
    wn.blit(press_surface,press_rect)

def game_over():
    my_font = pygame.font.SysFont('comicsans',40)
    game_over_surface = my_font.render('GAME OVER', True,red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midbottom = (f_size_x/2, f_size_y/3)
    wn.fill(black)
    high_score(1, white, 'comicsans', 35)
    life_time( white, 'comicsans', 35)
    wn.blit(game_over_surface,game_over_rect)
    pygame.display.flip()
    time.sleep(4)
    pygame.quit()
    sys.exit()

def high_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font,size)
    score_surface = score_font.render('Score: '+str(score),True,color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midbottom = ( f_size_x/2,f_size_y/2)
    elif choice==0:
        score_rect.midbottom = (f_size_x/8, f_size_y/12)
    wn.blit(score_surface, score_rect)

def life_time( color, font, size):
    mins, secs = divmod(life_spam, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    life_font = pygame.font.SysFont(font,size)
    life_surface = life_font.render('Time: '+str(timer),True,color)
    life_rect = life_surface.get_rect()
    life_rect.midtop = ( f_size_x/2,f_size_y/2)
    wn.blit(life_surface, life_rect)
#start menu


while start_m:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            start_m = False
            gameloop = True
    cur_time = pygame.time.get_ticks()
    
    
    if (cur_time-btn_press_time)%1000==0:
        start_menu(green)
    elif (cur_time-btn_press_time)%500==0:
        start_menu(black)
#gameloop
while gameloop:
   

    #movment
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            
            

            if event.key == pygame.K_UP or event.key == pygame.K_w:
                change_dir = "UP"
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                change_dir = "DOWN"
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                change_dir = "RIGHT"
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                change_dir = "LEFT"

            #start
            if event.key == pygame.K_RETURN and enter_bool:
                btn_press_time = pygame.time.get_ticks()
                enter_bool = False
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        

   

    

    #checking if the snake not moving in the opposite direction instantaneously

    if change_dir == "UP" and direction != "DOWN":
        direction = "UP"

    if change_dir == "DOWN" and direction != "UP":
        direction = "DOWN"

    if change_dir == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"

    if change_dir == "LEFT" and direction != "RIGHT":
        direction = "LEFT"


    # snake moving mechanism
    
    if direction == 'RIGHT':
        snake_pos[0] += 10
    if direction == 'LEFT':
        snake_pos[0] -=10
    if direction == 'DOWN':
        snake_pos[1] +=10
    if direction == 'UP':
        snake_pos[1] -=10


    #set current time 

    cur_time = pygame.time.get_ticks()
    #print((cur_time - btn_press_time)//1000)
    life_spam=(cur_time - btn_press_time)//1000
    
    
    #random fruit generator based on time
    
    if (life_spam)%10==0 and random_bool  :
        random_fruit=random.randrange(0,5)
        random_bool= False
        #set the new position of the random foods
        if random_fruit ==0:
            if rock[0][0]!=-100:
                rock.append([-100,-100])
            rock_bool=False
            
        
        if random_fruit ==1:
            yfood_bool=False
        else:
            yellow_food=[-100,-100]
        if random_fruit ==2:
            pfood_bool=False
        else:
            purple_food=[-100,-100]
        if random_fruit ==3:
            gfood_bool=False
        else:
            green_food=[-100,-100]
        if random_fruit ==4:
            rfood_bool=False
        else:
            red_food=[-100,-100]
    elif (life_spam)%10!=0 :
        random_bool= True
        


    #snake moving
    snake_body.insert(0, list(snake_pos))
    if detectCollisions(snake_pos[0],snake_pos[1],def_height*0.9,def_height*0.9,food[0],food[1],10-(def_width*0.1),10-(def_height*0.1))==True:
        score += 1
        food_bool = False


        
    else:
        snake_body.pop()

    #snake friuts mechanism

    #rock

    for stone in rock:

        if detectCollisions(snake_pos[0],snake_pos[1],1,1,stone[0],stone[1],width-1,height-1)==True:
            game_over()
        
        #the food is spawned in the rock

        if detectCollisions(food[0],food[1],1,1,stone[0],stone[1],width-1,height-1)==True:
            food_bool = False


        if not rock_bool and random_fruit==0:
            width=random.randrange(10,50)
            height=random.randrange(10,50)
            stone[0] = random.randrange(
                1, (f_size_x//10)) * 10
            stone[1] = random.randrange(
                1, (f_size_y//10)) * 10
            

        if random_fruit==0:
            pygame.draw.rect(wn, white, pygame.Rect(
        (stone[0]), (stone[1]), 10,10))
    
    #purple fruit
    if detectCollisions(snake_pos[0],snake_pos[1],def_height*0.9,def_height*0.9,purple_food[0],purple_food[1],10-(def_width*0.1),10-(def_height*0.1))==True:
        purple_food = [-100,-100]

        if def_height >=20 and def_width >=20:
            def_height=def_height
        else:
            def_width=def_width*2
            def_height=def_height*2
        

    #yellow fruit
    if detectCollisions(snake_pos[0],snake_pos[1],def_height*0.9,def_height*0.9,yellow_food[0],yellow_food[1],10-(def_width*0.1),10-(def_height*0.1))==True:
        yellow_food = [-100,-100]

        if  def_height <=2.5 and def_width <=2.5:
            def_height=def_height
        else:
            def_width=def_width/2
            def_height=def_height/2
        
    
    #green fruit
    if detectCollisions(snake_pos[0],snake_pos[1],def_height*0.9,def_height*0.9,green_food[0],green_food[1],10-(def_width*0.1),10-(def_height*0.1))==True:
        difficulty+=5
        score += 2
        green_food = [-100,-100]

    
    #red fruit
    if detectCollisions(snake_pos[0],snake_pos[1],def_height*0.9,def_height*0.9,red_food[0],red_food[1],10-(def_width*0.1),10-(def_height*0.1))==True:
        red_food = [-100,-100]
        if difficulty >5:
            difficulty=6
        else:
            difficulty-=5
        score -= 5
        

        
        
       
   
 

   
    

  
    
   
    
  

    

    # spawning the foods
    if not food_bool :
        food = [random.randrange(
            1, (f_size_x//10)) * 10, random.randrange(1, (f_size_y//10)) * 10]
        
    

    
    if not yfood_bool and random_fruit==1:
        yellow_food = [random.randrange(
            1, (f_size_x//10)) * 10, random.randrange(1, (f_size_y//10)) * 10]
    
    if not pfood_bool and random_fruit==2:
        purple_food = [random.randrange(
            1, (f_size_x//10)) * 10, random.randrange(1, (f_size_y//10)) * 10]

    if not gfood_bool and random_fruit==3:
        green_food = [random.randrange(
            1, (f_size_x//10)) * 10, random.randrange(1, (f_size_y//10)) * 10]

    if not rfood_bool and random_fruit==4:
        red_food = [random.randrange(
            1, (f_size_x//10)) * 10, random.randrange(1, (f_size_y//10)) * 10]


    food_bool = True
    rock_bool = True
    gfood_bool = True
    rfood_bool = True
    pfood_bool = True
    yfood_bool = True

    

    #snake draw
   
    wn.fill(black)
    # drawing the fruits
   
    pygame.draw.rect(wn, white, pygame.Rect(
        food[0], food[1], 10,10))
    
    for piece in rock:
        
            pygame.draw.rect(wn, grey, pygame.Rect(
        (piece[0]), (piece[1]), width,height))

    if random_fruit==1:    
        pygame.draw.rect(wn, yellow, pygame.Rect(
            yellow_food[0], yellow_food[1], 10, 10))
    if random_fruit==2:    
        
        pygame.draw.rect(wn, purple, pygame.Rect(
            purple_food[0], purple_food[1], 10, 10))
    if random_fruit==3:    
        
        pygame.draw.rect(wn, lime, pygame.Rect(
            green_food[0], green_food[1], 10, 10))
    if random_fruit==4:    
        
        pygame.draw.rect(wn, red, pygame.Rect(
            red_food[0], red_food[1], 10, 10))


    for pos in snake_body:
        # Snake body
        # .draw.rect(play_surface, color, xy-coordinate)
        # xy-coordinate -> .Rect(x, y, size_x, size_y)
        pygame.draw.rect(wn, green, pygame.Rect(pos[0], pos[1], def_width, def_height))
  
    #snake going trought walls
    
    
    if snake_pos[0] == f_size_x :
        snake_pos[0] = -10
    elif snake_pos[0] == 0 and direction=='LEFT' or snake_pos[0]<-10:
        snake_pos[0] = f_size_x
    elif snake_pos[1] == f_size_y :
        snake_pos[1] = -10
    elif snake_pos[1] == 0 and direction=='UP' or snake_pos[1]<-10:
        snake_pos[1] = f_size_y
    

    #snake hitting himself
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()

    high_score(0, white, 'comicsans', 20)



    #updating screen
    pygame.display.update()     
    #refresh fps
    setfps.tick(difficulty)



