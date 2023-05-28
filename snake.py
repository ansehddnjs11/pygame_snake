import pygame
import random
import time

# 1. 게임 초기화
pygame.init()

# 2. 게임 창 옵션 설정
size = [800, 600]
screen = pygame.display.set_mode(size)

title = 'Snake'
pygame.display.set_caption(title)

# 3. 게임 내 필요한 설정
clock = pygame.time.Clock()

snake_rgb = (0, 255, 0)
apple_rgb = (255, 0, 0)

sa_size = [20, 20]

class Snake():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.move = 20
        self.position = [(40,0), (20,0), (0,0)]
        
    def draw(self,x,y):
        pygame.draw.rect(screen,snake_rgb,(x,y,sa_size[0],sa_size[1]))
        
    def s_move(self):
        x, y = self.position[0]
        if direction == 'L':
            self.position = [(x - self.move, y)] + self.position[:-1]
        elif direction == 'R':
            self.position = [(x + self.move, y)] + self.position[:-1]
        elif direction == 'U':
            self.position = [(x, y - self.move)] + self.position[:-1]
        elif direction == 'D':
            self.position = [(x, y + self.move)] + self.position[:-1]
    
    def grow(self):
        self.position.append(self.position[-1])
        
class Apple():
    def __init__(self):
        self.x = 0
        self.y = 0
        
    def spawn(self):
        self.x = random.randrange(0, size[0] // 20 + 1) * 20
        self.y = random.randrange(0, size[1] // 20 + 1) * 20 
        
    def draw(self):
        pygame.draw.rect(screen,apple_rgb,(self.x,self.y,sa_size[0],sa_size[1]))
        
snake = Snake()
apple = Apple()
apple.spawn()

b_sx, b_sy = 5, 5

direction = ''

last_time = pygame.time.get_ticks()
move_interval = 100
# 4. 메인 이벤트
SB = 0
while SB == 0:
    # 4-1. FPS 설정
    clock.tick(60)
    
    # 4-2. 각종 입력 감지
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            SB = 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = 'L'
            elif event.key == pygame.K_RIGHT:
                direction = 'R'
            elif event.key == pygame.K_UP:
                direction = 'U'
            elif event.key == pygame.K_DOWN:
                direction = 'D'
    # 4-3 입력, 시간에 따른 변화
    snake_mid_x, snake_mid_y = snake.position[0][0] + sa_size[0] / 2, snake.position[0][1] + sa_size[1] / 2
    
    if current_time - last_time >= move_interval:
        if direction == 'L':
            snake.s_move()
        elif direction == 'R':
            snake.s_move()
        elif direction == 'U':
            snake.s_move()
        elif direction == 'D':
            snake.s_move()        
        last_time = current_time
        
    if snake_mid_x > apple.x - b_sx and snake_mid_x < apple.x + sa_size[0] + b_sx and snake_mid_y > apple.y - b_sy and snake_mid_y < apple.y + sa_size[1] + b_sy:
        snake.grow()
        apple.spawn()
        
    # 4-4 그리기
    print(snake_mid_x, snake.position)
    screen.fill((210,255,210)) 
    for i in range(len(snake.position)):
        snake.draw(snake.position[i][0],snake.position[i][1])
    apple.draw()
    # 4-5 업데이트
    pygame.display.flip()

# 5. 게임종료
pygame.quit()
