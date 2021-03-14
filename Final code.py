import pygame
import time
pygame.init()
from pygame.locals import ( 
    K_z,
    K_x,  
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
#HERO
x = 860
y = 750
#NPC_intro
w = 1450
z = 230
#NPC_farmer
k = 1440
l = 540
#NPC_beekeeper
s = 1025
o = 180
#NPC_fisherman
m = 875
n = 605

q = 1

 
RIGHT = pygame.image.load(r'D:\\python\\python_arts\\Hero_right.png') 
LEFT = pygame.image.load(r'D:\\python\\python_arts\\Hero_left.png') 
DOWN = pygame.image.load(r'D:\\python\\python_arts\\hero_dow.png')
UP = pygame.image.load(r'D:\python\python_arts\Hero_up.png')
hero_fish = pygame.image.load(r'D:\python\python_arts\\Hero_right_fish.png')
fishing = False
happy = False

bottles = pygame.image.load(r'D:\\python\\python_arts\\Garbage_bottles.png') 
sakura = pygame.image.load(r'D:\python\python_arts\\Sakura1.png')
fenceClosed = pygame.image.load(r'D:\\python\\python_arts\\Fence_closed.png')
fenceOpened = pygame.image.load(r'D:\\python\\python_arts\\Fence_open2.png')

tomatoes = list(range(7))
br=1
while br<=6: 
    tomatoes[br] = pygame.image.load(r'D:\\python\\python_arts\\Tomatoes.png')
    br += 1

g_count = 0
left = False
right = True
down = False
up = False
open = False

first_load=False
fish_cooked = False
fishing_rod = False

water_plants = False

map_loader= 5
last_map=0
Fdialogue = False
map1 = pygame.image.load(r'D:\\python\\python_arts\\map_1.png')
map2 = pygame.image.load(r'D:\\python\\python_arts\\map_2.png')
map3 = pygame.image.load(r'D:\\python\\python_arts\\map_3.png')
map4 = pygame.image.load(r'D:\\python\\python_arts\\map_4.png')
map5 = pygame.image.load(r'D:\\python\\python_arts\\map_5.png')
map6 = pygame.image.load(r'D:\\python\\python_arts\\map_6.png')
map7 = pygame.image.load(r'D:\\python\\python_arts\\map_7.png')
map8 = pygame.image.load(r'D:\\python\\python_arts\\map_8.png')
map9 = pygame.image.load(r'D:\\python\\python_arts\\map_9.png')

i=1

garbage = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
while i<=5:
    garbage[i] = pygame.image.load(r'D:\\python\\python_arts\\Garbage_bottles.png')
    i += 1
while i<=10:
    garbage[i] = pygame.image.load(r'D:\\python\\python_arts\\Garbage_papers.png')
    i += 1
while i<=15:
    garbage[i] = pygame.image.load(r'D:\\python\\python_arts\\Garbage_glass_bottles.png')
    i += 1
gar_x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
gar_y = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
garTrue = [0,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True]

for tr in garTrue:
    tr = True


inventory = False
txt=True
speed = 15
speed_return = speed
RED = (245, 66, 66)
white = (255, 255, 255)
black = (0, 0, 0)
NPC_intro = pygame.image.load(r'D:\python\python_arts\\NPC_intro.png')
NPC_farmer2 = pygame.image.load(r'D:\python\python_arts\\Farmer_back.png')
NPC_farmer = pygame.image.load(r'D:\python\python_arts\\Farmer.png')
NPC_beekeeper = pygame.image.load(r'D:\python\python_arts\\Beekeeper.png')
NPC_fisherman = pygame.image.load(r'D:\python\python_arts\\Fisherman.png')
Hero_watering = pygame.image.load(r'D:\python\python_arts\\Hero_down_water.png')
screen = pygame.display.set_mode((1920,1080))
campfire = pygame.image.load(r'D:\python\python_arts\\campfire.png')

font = pygame.font.Font('freesansbold.ttf', 17)
text4 = font.render('Inventory full!', True, black)
text4Rect = text4.get_rect()
text4Rect = (0,20)


clock = pygame.time.Clock()
 
font2 = pygame.font.Font(None, 25)
 
frame_count = 0
frame_rate = 60
start_time = 10
fish = False

#LINE
text2 = font.render('Hello friend!'
' Nice to meet you at this time of the day!'
' I need your help. The hole village is full of garbage. '
' Please help me clean it!',True,black)

text2Rect = text2.get_rect()
text2Rect = (850,0)
text = font.render('Press Escape to exit', True, black) 
textRect = text.get_rect()
textRect = (40,40)

text4 = font.render('Press Escape to exit', True, black) 
text4Rect = text4.get_rect()
text4Rect = (40,40)

clock = pygame.time.Clock()
FPS = 200

def Touch(x,y,left,right,down):
    if left:
        screen.blit(LEFT,(x,y))
    if right:
        screen.blit(RIGHT,(x,y))
    if down:
        screen.blit(DOWN,(x,y))
    if up:
        screen.blit(UP,(x,y))

def Inventory_full(inventory,text,textRect,black,font):
    if inventory == True:
        text4 = font.render('Inventory full!', True, black)
        text4Rect = text4.get_rect()
        text4Rect = (0,20)
        screen.blit(text4,text4Rect)

def Garbage(garTrue,garbage,gar_x,gar_y):
    if garTrue[q]==True:
        screen.blit(garbage[q],(gar_x[q],gar_y[q]))

'''def render_multi_line(textF2, x, y, fsize):
        lines = text.splitlines(textF2, x , y)
        for i, l in enumerate(lines):
            screen.blit(font.render(l, 0, black), (x, y + fsize*i))'''



while True:
    clock.tick(FPS)
    total_seconds = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
        left = True
        right = False
        down = False
        up = False
    if keys[pygame.K_RIGHT]:
        x += speed
        left = False
        right = True
        down = False
        up = False
    if keys[pygame.K_UP]:
        y -= speed
        left = False
        right = False
        down = False
        up = True
    if keys[pygame.K_DOWN]:
        y += speed
        left = False
        right = False
        down = True
        up = False

    #MAP9###################################################################################################################################################
    if map_loader==9:
        screen.blit(map9,(0,0))
        if first_load:
            if last_map==6:
                y=1100-y
            else: x=2000-x
        first_load=False

        gar_y[12] = 220
        gar_x[12] = 750
        q = 12
        a = 570
        b = 750
        c = 60
        d = 220
        Garbage(garTrue,garbage,gar_x,gar_y)
        if x > a and x < b and y > c and y < d:
            if inventory == False and garTrue[q] == True:
                garTrue[q]=False
                inventory=True
                g_count += 1
        Inventory_full(inventory,text,textRect,black,font)
        screen.blit(NPC_fisherman,(m,n))
        Touch(x,y,left,right,down)
        #NPC_fisherman
        if x > 740 and x < 1180 and y < 830 and y > 620:
            textFi = font.render('Hold Z to talk with the fisherman', True, black)
            textFiRect = textFi.get_rect()
            textFiRect = (1400,20)
            screen.blit(textFi,textFiRect)
            if keys[pygame.K_z]:
                textFi2 = font.render("Man I've been here all day, all alone. Would you mind joining me? If you want, go ahead and fish with this fishing rod. ", True, black)
                textFi2Rect = textFi2.get_rect()
                textFi2Rect = (0,0)
                screen.blit(textFi2,textFi2Rect)
                fishing_rod = True 
            if fishing_rod == True and x >= 1150:
                textFi3 = font.render("Hold x to fish", True, black)
                textFi3Rect = textFi3.get_rect()
                textFi3Rect = (30,40)
                screen.blit(textFi3,textFi3Rect) 
                if keys[pygame.K_x]:
                    screen.blit(hero_fish,(x-85,y-60))
                    total_seconds = start_time - (frame_count // frame_rate)
                    if total_seconds < 0:
                        total_seconds = 0
                    if total_seconds == 0:
                        fish = True
        minutes = total_seconds // 60
        seconds = total_seconds % 60
    
        output_string = "Time left: {0:02}:{1:02}".format(minutes, seconds)
    
        
        text2 = font2.render(output_string, True, black)

        frame_count += 1
        if total_seconds > 0:
            screen.blit(text2, [0,100])


        if x < -5 and y > 525:
            x =- 5
        if y > 890:
            y = 890
        if x < 25 and y < 175:
            x = 25
        if y>815 and y<635 and x>735:
            if right:
                x = 735
            if up:
                y = 635
            if down:
                y = 815
        if x>950 and x <= 1160 and y < 621:
                y=621
        if x >= 1161 and y >= 621 and y < 860:
            x=1160
        if x > 950 and x <= 1160 and y >= 800:
            y = 800
        if x > 920 and y < 610:
            x=920
        if x > 920 and y > 840:
            x = 920
        if y <- 10:
            map_loader = 6
            first_load = True
        if x <- 10:
            map_loader = 8
            first_load = True
        last_map = 9
            
        
    #MAP8###################################################################################################################################################
    if map_loader == 8:
        screen.blit(map8,(0,0))
        if first_load:
            if last_map == 5:
                y = 1100-y
            if last_map == 7:
                x =- 10
            if last_map == 9: 
                x = 1900
        first_load = False
        if y >= 265 or y <= 80:
            screen.blit(tomatoes[4],(450,265))
        if y >= 665 or y<= 480:
            screen.blit(tomatoes[2],(350,665))
        gar_y[7] = 275
        gar_x[7] = 170
        q = 7
        a = 275
        b = 425
        c = 125
        d = 230
        Garbage(garTrue,garbage,gar_x,gar_y)
        if x > a and x < b and y > c and y < d:
            if inventory == False and garTrue[q] == True:
                garTrue[q]=False
                inventory=True  
                g_count += 1
        Inventory_full(inventory,text,textRect,black,font)
        gar_y[13] = 80
        gar_x[13] = 1595
        q = 13
        a = 1505
        b = 1765
        c = 0
        d = 110
        Garbage(garTrue,garbage,gar_x,gar_y)
        if x > a and x < b and y > c and y < d:
            if inventory == False and garTrue[q] == True:
                garTrue[q]=False
                inventory=True
                g_count += 1
        Inventory_full(inventory,text,textRect,black,font)
        gar_y[4] = 530
        gar_x[4] = 800
        q = 4
        a = 710
        b = 905
        c = 335
        d = 515
        Garbage(garTrue,garbage,gar_x,gar_y)
        if x > a and x < b and y > c and y < d:
            if inventory == False and garTrue[q] == True:
                garTrue[q]=False
                inventory=True
                g_count += 1
        Inventory_full(inventory,text,textRect,black,font)
        Touch(x,y,left,right,down)
        if y > 480 and y < 665:
            screen.blit(tomatoes[1],(350,665))
        if y > 80 and y < 265:
            screen.blit(tomatoes[3],(450,265))
        
        if x < 10 and y < 155:
            x=10
        if x < -35 and y > 545:
            x =- 35
        if y > 515 and x > 1795:
            x = 1795
        if x > 1810 and y < 155:
            x = 1810
        if y >= 815:
            y = 815
        if y > 185 and y < 320 and x > 365 and x < 1505:
            if right:
                x = 365
            if left:
                x=1505
            if up:
                y=320
            if down:
                y=185
        if Fdialogue and y >= 185 and y < 320 and x > 365 and x < 1505:
            textW = font.render("Hold x to water the tomatoes", True, black)
            textWRect = textW.get_rect()
            textWRect = (30,40)
            screen.blit(textW,textWRect)
            if down:
                if keys[pygame.K_x]:
                    screen.blit(Hero_watering,(x-10,y))
                    water_plants = True
        if y > 590 and y < 725 and x > 290 and x < 1390:
            if right:
                x = 290
            if left:
                x=1390
            if up:
                y=725
            if down:
                y=590
        if y < 5 and x < 530:
            y = 5
        if y < 5 and x > 1145:
            y = 5
        if y <- 10:
            map_loader = 5
            first_load = True
        if x<-10:
            map_loader = 7
            first_load = True

        if x>1920:
            map_loader = 9
            first_load = True
        last_map=8 
    
    #MAP7###################################################################################################################################################
    if map_loader == 7:
        screen.blit(map7,(0,0))
        screen.blit(campfire,(1435,35))
        if first_load:
            if last_map == 8:
                x=1900
            if last_map == 4:
                y = 1100-y
        first_load = False
        if x>1920:
            map_loader = 8
            first_load = True
        Touch(x,y,left,right,down)
        if y >- 205 and x < 790:
            x = 790
        if x > 0 and y > 450:
            y = 450
        if y < 230 and y >- 225 and x > 1150 and x < 1360:
            if right:
                x = 1150
            if up:
                y = 230
            if left:
                x = 1360 
        if x > 1805 and y < 40:
            x = 1805
        if x > 1490 and x < 1920 and y < 230 and y > 35:
            if up:
                y = 230
            if down:
                y = 35
            if right:
                x = 1490
        if x > 1150 and x < 1910 and y <- 65:
            y=-65
        if x > 1860 and x <- 200 and y < 35 and y <- 200:
            if right:
                x = 1860
        if y <- 90:
            map_loader = 4
            first_load = True
        #Campfire fish
        if x >= 1380 and y >= -65 and fish == True:
            text7 = font.render('Hold x to cook fish', True, black)
            text7Rect = text7.get_rect()
            text7Rect = (0, 40)
            screen.blit(text7,text7Rect)
            if keys[pygame.K_x]:
                fish_cooked = True

        screen.blit(fenceOpened,(816,535))
        #NPC_FARMER_INTERRACTION
        screen.blit(NPC_farmer,(k,l))
        if x > 1360 and x < 1570 and y >= 405:
            textF = font.render('Hold Z to talk to the farmer', True, black)
            textFRect = textF.get_rect()
            textFRect = (0,20)
            screen.blit(textF,textFRect)
            if keys[pygame.K_z]:
                textF2 = font.render("Huh!Hello.... do we now each other.Hmmmm...... You don't seem to be very talkative.Anyways, my name is Stan, Stan the farmer.", True, black)
                textF2Rect = textF2.get_rect()
                textF2Rect = (0,900) 

                textF3 = font.render("You probbably now that the village theese days is pretty dirty.You look like a nice person. Can you do me a favor?Please clean up my garden and water the tomatoes.", True, black)
                textF3Rect = textF3.get_rect()
                textF3Rect = (0,950)
                
                screen.blit(textF3,textF3Rect)
                screen.blit(textF2,textF2Rect)
                screen.blit(NPC_farmer2,(k,l))
                Fdialogue = True

        last_map = 7

        



    #MAP6###################################################################################################################################################
    if map_loader == 6:
        screen.blit(map6,(0,0))
        if first_load:
            if last_map == 5:
                x = 2000-x
            if last_map == 9:
                y = 900-y 
            if last_map == 3:
                y = 10
        first_load = False
        gar_y[11] = 670
        gar_x[11] = 750
        q = 11
        a = 555
        b = 750
        c = 520
        d = 670
        Garbage(garTrue,garbage,gar_x,gar_y)
        if x > a and x < b and y > c and y < d:
            if inventory == False and garTrue[q] == True:
                garTrue[q]=False
                inventory=True
                g_count += 1
        Inventory_full(inventory,text,textRect,black,font)
        gar_y[5] = 135
        gar_x[5] = 245
        q = 5
        a = 135
        b = 345
        c = 90
        d = 240
        Garbage(garTrue,garbage,gar_x,gar_y)
        if x > a and x < b and y > c and y < d:
            if inventory == False and garTrue[q] == True:
                garTrue[q]=False
                inventory=True
                g_count += 1
        Inventory_full(inventory,text,textRect,black,font)

        gar_y[8] = 680
        gar_x[8] = 100
        q = 8   
        a = 25
        b = 210
        c = 610
        d = 730
        Garbage(garTrue,garbage,gar_x,gar_y)
        if x > a and x < b and y > c and y < d:
            if inventory == False and garTrue[q] == True:
                garTrue[q]=False
                inventory=True
                g_count += 1
        Inventory_full(inventory,text,textRect,black,font)



        Touch(x,y,left,right,down)
        if y >- 195 and x > 960:
            x = 960
        if  y <- 20 and x > -40 and x < 165:
            if left:
                x = 165
            if up:
                y =- 20
        if y < 355 and y > 25 and x > 410 and x < 980:
            if right:
                x = 410
            if up:
                y = 355
            if down:
                y = 25
        if y < 235 and x  <0:
            x = 0
        if y > 565 and x <- 5:
            x = -5
        if y<0:
            map_loader = 3
            first_load = True
        if x <- 10:
            map_loader = 5
            first_load = True
        if y>1080:
            map_loader = 9
            first_load = True
        last_map = 6
        
    #MAP5###################################################################################################################################################
    if map_loader == 5:
        screen.blit(map5,(0,0))
        gar_y[1] = 450
        gar_x[1] = 1600
        q = 1
        a = 1490
        b = 1715
        c = 300
        d = 400
        Garbage(garTrue,garbage,gar_x,gar_y)
        if x > a and x < b and y > c and y < d:
            if inventory == False and garTrue[q] == True:
                garTrue[q]=False
                inventory=True
                g_count += 1
        Inventory_full(inventory,text,textRect,black,font)
        if first_load:
            if last_map == 4 or last_map == 6:
                x = 1920-x
            else: y = 1040-y
            if last_map == 4:
                y = y+50
            first_load = False
        if y<250:
            y=250
        if y > 560 and y < 800 and x > 1430 and x < 1685:
            if right:
                x = 1430
            if down:
                y = 560
            if up:
                y = 800
            if left:
                x = 1685
        if y > 450 and x < 0:
            x = 0
        if x < 635 and y > 900:
            y = 900
        if x > 975 and y > 900:
            y = 900
        if y > 600 and x > 1805:
            x = 1805      
        if y >= 560 and y <= 800 and x >= 1430 and x <= 1685:
            text = font.render("Hold x to throw a trash", True, black)
            textRect=(0,0)
            screen.blit(text,textRect)
            if keys[pygame.K_x]:
                inventory = False
        if x >= 1460 and x <= 1540 and y < 395:
            text = font.render('Hold Z to talk with the guide', True, black)
            textRect = text.get_rect()
            textRect = (1460,180)
            screen.blit(text,textRect)
        if x <= 1580 and x >= 1460 and y >= 250 and y <= 520:
            if keys[pygame.K_z]:
                screen.blit(text2, text2Rect)
            elif water_plants == True and happy == True and g_count==10:
                text6 = font.render('Thank you for helping me and the whole villige, your journey ends here...', True, black)
                text6Rect =  text.get_rect()
                text6Rect = (0,80) 
                screen.blit(text6,text6Rect)      
        screen.blit(NPC_intro,(w,z))
        if x <- 10:
            map_loader = 4
            first_load = True
        if x>1980:
            map_loader = 6
            first_load = True
        if y>1080:
            map_loader = 8
            first_load = True
        Touch(x,y,left,right,down)
        last_map = 5


    #MAP 4###################################################################################################################################################
    if map_loader == 4:
        if first_load:
            if last_map == 5:
                x = 1750-x
                y = y-50
            if last_map == 7:
                y = 1070
            if last_map == 1:
                y = 0
        first_load = False
        screen.blit(map4,(0,0))
        gar_y[2] = 635
        gar_x[2] = 520
        Garbage(garTrue,garbage,gar_x,gar_y)
        q = 2
        a = 490
        b = 595
        c = 545
        d = 680 
        if x > a and x < b and y > c and y < d:
            if inventory == False and garTrue[q] == True:
                garTrue[q]=False
                inventory=True
                g_count += 1
        Inventory_full(inventory,text,textRect,black,font)

        gar_y[6] = 890
        gar_x[6] = 890
        Garbage(garTrue,garbage,gar_x,gar_y)
        q = 6
        a = 890
        b = 1050
        c = 800
        d = 890 
        if x > a and x < b and y > c and y < d:
            if inventory == False and garTrue[q] == True:
                garTrue[q]=False
                inventory=True
                g_count += 1
        Inventory_full(inventory,text,textRect,black,font)
        if y<-10:
            map_loader = 1
            first_load = True
        if x > 1900:
            map_loader = 5
            first_load = True
        if y >= 1130:
            map_loader = 7
            first_load = True
        if x < 460:
            x = 460   
        if y < 215 and x > 1050:
            if right:
                x = 1050
            if down:
                y = -180
            if up:
                y = 215
            if left:
                x = 10
        if y > 410 and x > 1080:
            if right:
                x = 1080
            if down:
                y = 410 

        if y < 515 and y > 380 and x > 595 and x < 925:
            if right:
                x = 595
            if left:
                x = 925
            if up:
                y = 515
            if down:
                y = 380       
        Touch(x,y,left,right,down)
        screen.blit(fenceClosed,(1181,500))
        if y < 400:
            screen.blit(sakura,(608,0))
        last_map = 4
    #MAP3##################################################################################################################################################
    if map_loader == 3:
        screen.blit(map3,(0,0))
        if first_load:
            if last_map == 2:
                x = 1920 - x
            if last_map == 6:
                y = 1070
        first_load = False

        if x<-10:
            map_loader = 2
            first_load = True
        if y>1080:
            map_loader = 6
            first_load = True
        last_map = 3 
        Touch(x,y,left,right,down)  
    #MAP2##################################################################################################################################################
    if map_loader == 2:
        if first_load:
            if last_map == 1:
                x = 2000-x
            if last_map == 3:
                x = 1900
        first_load = False
        screen.blit(map2,(0,0))
        if y > 530:
            y = 530
        if y < 185:
            y=185
        if x<0:
            map_loader = 1
            first_load = True
        if x>1900:
            map_loader = 3
            first_load = True
        last_map = 2
        Touch(x,y,left,right,down)
    #Map1###################################################################################################################################################
    if map_loader==1:
        screen.blit(map1,(0,0))
        if first_load:
            if last_map == 4:
                y=1070
            else: x = 1750-x
        first_load = False
        if x>1900:
            map_loader=2
            first_load = True
        if x < 1920 and y < 245:
            y = 245
        if y>0 and x<260:
            x = 260
        if x < 465 and x > 260 and y > 515 and y < 920:
            if down:
                y = 515
            if left:
                x = 465
        if y > 515 and x > 1100:
            if down:
                y = 515
            if right:
                x = 1100
        screen.blit(NPC_beekeeper,(s,o))
        if x > 875 and x < 1175 and y <= 245:
            textB = font.render('Hold Z to talk with the beekeeper', True, black)
            textBRect = text.get_rect()
            textBRect = (1460,180)
            screen.blit(textB,textBRect)
            if keys[pygame.K_z]:
                if fish_cooked == False:
                    textB2 = font.render('Hey, nice to meet you! I heard that you are the brave man who wants to clean the village.', True, black)
                    textB2Rect = text.get_rect()
                    screen.blit(textB2,textB2Rect)
                    textB2Rect = (1000,40)
                    textB3 = font.render("I support your activity! Keep it up! I'm so hungry right now, maybe we can talk another time?", True, black)
                    textB3Rect = text.get_rect()
                    screen.blit(textB3,textB3Rect)
                    textB3Rect = (1000,80)
                elif fish_cooked == True:
                    textB5 = font.render('Thank you so much, cowboy! It looks delicious!', True, black)
                    textB5Rect = textB5.get_rect()
                    screen.blit(textB5,textB5Rect)
                    textB5Rect = (0,100) 
                    happy = True
                #else:
        Touch(x,y,left,right,down)
        if y>1080:
            map_loader=4
            first_load = True
        last_map = 1

        
    
    print(x,y,fishing_rod, fish_cooked)
    pygame.display.update() 
    
    
    

