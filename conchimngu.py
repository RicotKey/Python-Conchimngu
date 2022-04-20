#Thư viện
import pygame
from random import randint #Ran int 
#Khởi tạo hàm pygame
pygame.init()
#Tạo biến backgroup
WIDTH,HEIGHT = 400,600
#Tạo màn hình
screen=pygame.display.set_mode((WIDTH,600))
#Đặt tên chương trình
pygame.display.set_caption('CON CHIM NGU')
#Màu
YELLOW=(245, 243, 191)
VIOLET=(136, 134, 240)
BLUE_SKY=(3, 186, 252)
BLUE=(0,0,255)
RED=(255,0,0)
BLACK=(0,0,0)
#Tạo font
font=pygame.font.SysFont('sans',20)
font_1=pygame.font.SysFont('sans',50)
#Biến chạy
running = True
TUBE_GAP= 150 #Biến khoảng trống
score = 0
#Tạo chữ
Programer=font.render('RicotKey',True,VIOLET)
#Giảm fbs
clock =pygame.time.Clock()
#Tạo ống
TUBE_WIDTH = 50#Chiều rộng ống mặc định
tube1_x=650#Vị trí ống 1
tube1_height=randint(100,300)#Chiều cao ống 1
tube2_x=800#Vị trí ống 2
tube2_height=randint(100,300)#Chiều cao ống 2
tube3_x=950#Vị trí ống 3
tube3_height=randint(100,300)#Chiều cao ống 3
TUBE_VELOCITY =3#Tốc độ di chuyển của ống
#Biến đi qua ống 
tube_pass = False
#Tạo chim
BIRD_X= 50
bird_y=200
BIRD_WIDTH= 35
BIRD_HEIGHT= 35
#Tạo trọng lực
#Biến chơi lại
pausing= False 
BIRD_FALL_VELOCITY=0
GRAVITY=0.5
#Load background
background_image=pygame.image.load("background2.png")
background_image=pygame.transform.scale(background_image,(WIDTH,HEIGHT))
#Load ảnh chim
bird_image=pygame.image.load("bird.png")
bird_image=pygame.transform.scale(bird_image,(BIRD_WIDTH,BIRD_HEIGHT))
#Load ảnh đất
sand_image=pygame.image.load("sand.png")
sand_image=pygame.transform.scale(sand_image,(WIDTH,600))

#Lặp chạy game
while running:
	#Vẽ 60 hình 1s
	clock.tick(60)
	#Màu nền
	screen.fill(YELLOW)
	screen.blit(background_image,(0,0))
	#Load tube
	tube_inv_image=pygame.image.load("tube1_1.png")
	tube_image=pygame.image.load("tube1.png")
	#Tube trên 1
	tube_image=pygame.transform.scale(tube_image,(TUBE_WIDTH,tube1_height))
	tube1=screen.blit(tube_image,(tube1_x,0))
	#Tube trên 2
	tube_image=pygame.transform.scale(tube_image,(TUBE_WIDTH,tube2_height))
	tube2=screen.blit(tube_image,(tube2_x,0))
	#Tube trên 3
	tube_image=pygame.transform.scale(tube_image,(TUBE_WIDTH,tube3_height))
	tube3=screen.blit(tube_image,(tube3_x,0))
	#Tube dưới 1
	tube_inv_image=pygame.transform.scale(tube_inv_image,(TUBE_WIDTH,HEIGHT-(TUBE_GAP+tube1_height)))
	tube1_inv=screen.blit(tube_inv_image,(tube1_x,tube1_height+TUBE_GAP))
	#Tube dưới 2
	tube_inv_image=pygame.transform.scale(tube_inv_image,(TUBE_WIDTH,HEIGHT-(TUBE_GAP+tube2_height)))
	tube2_inv=screen.blit(tube_inv_image,(tube2_x,tube2_height+TUBE_GAP))
	#Tube dưới 3
	tube_inv_image=pygame.transform.scale(tube_inv_image,(TUBE_WIDTH,HEIGHT-(TUBE_GAP+tube3_height)))
	tube3_inv=screen.blit(tube_inv_image,(tube3_x,tube3_height+TUBE_GAP))
	#Cho ống di chuyển
	tube1_x -= TUBE_VELOCITY
	tube2_x -= TUBE_VELOCITY
	tube3_x -= TUBE_VELOCITY
	
	#Tạo ống liên tục 
	if tube1_x < -TUBE_WIDTH:
		tube1_x =400
		tube1_height = randint(100,300)
		tube_pass = False#Đưa vé
	if tube2_x < -TUBE_WIDTH:
		tube2_x =400
		tube_pass = False#Đưa vé
		tube2_height = randint(100,300)
	if tube3_x < -TUBE_WIDTH:
		tube3_x =400
		tube3_height = randint(100,300)	
		tube_pass = False#Đưa vé 
	#Tạo chim
	chim=screen.blit(bird_image,(BIRD_X,bird_y))
	#Vẽ sand
	sand=screen.blit(sand_image,(0,550))
	#Vẽ sky
	sky=pygame.draw.rect(screen,BLUE_SKY,(0,0,400,5))
	#Chim rơi
	bird_y += BIRD_FALL_VELOCITY
	BIRD_FALL_VELOCITY += GRAVITY
	#Hiển thị điểm
	score_txt = font_1.render(str(score),True,BLACK)
	screen.blit(score_txt,(190,190))
	#Tên 
	screen.blit(Programer,(10,10))
	#Tính điểm 
	if tube1_x + TUBE_WIDTH <= BIRD_X + BIRD_WIDTH and tube_pass == False:
		score += 1
		tube_pass = True#Trả vé
	if tube2_x + TUBE_WIDTH <= BIRD_X + BIRD_WIDTH and tube_pass == False:
		score += 1
		tube_pass = True#Trả vé
	if tube3_x + TUBE_WIDTH <= BIRD_X + BIRD_WIDTH and tube_pass == False:
		score += 1
		tube_pass = True#Trả vé
	#Chim chết
	for tube in [tube1,tube2,tube3,tube3_inv,tube2_inv,tube1_inv,sky,sand]:
		if chim.colliderect(tube):
			pausing=True
			play=True

			#Dừng màn hình
			TUBE_VELOCITY=0
			BIRD_FALL_VELOCITY=0
			#Game over
			gameover_txt = font_1.render('GAME OVER',True,BLACK)
			screen.blit(gameover_txt,(85,240))
			#Restart
			restart_txt = font.render('Press BACKSPACE to Restart',True,BLACK)
			screen.blit(restart_txt,(100,320))
 #Sự kiện
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		#Bấm dúng cách
		if event.type == pygame.KEYDOWN: 
			if event.key == pygame.K_SPACE:
				#Trở lại ban đầu
				if pausing:
					pausing = False
					TUBE_VELOCITY=3
					score=0
					bird_y=200
					tube1_x=650
					tube2_x=800
					tube3_x=950
				#Chim bay lên
				BIRD_FALL_VELOCITY = 0
				BIRD_FALL_VELOCITY -=8
	#Vẽ lên màn hình
	pygame.display.flip()
#Xóa bộ nhớ
pygame.quit()