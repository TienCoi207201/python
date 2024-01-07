import pygame
pygame.init()

# Tạo cửa sổ
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Di chuyển khối")

# Tạo đối tượng (hình chữ nhật) và vận tốc
object_rect = pygame.Rect(100, 100, 50, 50)
velocity = [3, 2]  

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            

    # Cập nhật vị trí của đối tượng
    object_rect.x += velocity[0]
    print("x:",object_rect.x)
    print("y:",object_rect.y)
    object_rect.y += velocity[1]

    # Kiểm tra va chạm với biên
    if object_rect.left < 0 or object_rect.right > width:
        velocity[0] = -velocity[0]  # Đảo hướng khi chạm biên trái hoặc phải
    if object_rect.top < 0 or object_rect.bottom > height:
        velocity[1] = -velocity[1]  # Đảo hướng khi chạm biên trên hoặc dưới

    # Xóa màn hình và vẽ lại đối tượng
    screen.fill((0, 0, 0)) 
    pygame.draw.rect(screen, (255, 0, 0), object_rect)  # Vẽ hình chữ nhật đối tượng màu đỏ

    pygame.display.flip()
    pygame.time.Clock().tick(120) 

pygame.quit()

# import pygame
# import sys

# pygame.init()

# # Các cài đặt cửa sổ game
# window_width = 800
# window_height = 600
# window = pygame.display.set_mode((window_width, window_height))
# pygame.display.set_caption('Resizing an Image')

# # Màu sắc
# white = (255, 255, 255)

# # Load hình ảnh của nhân vật
# character_image = pygame.image.load('character-archetype-the-hero-removebg-preview.png')

# new_width = character_image.get_width() // 2
# new_height = character_image.get_height() // 2
# resized_character_image = pygame.transform.scale(character_image, (new_width, new_height))

# # Vị trí của ảnh
# character_rect = resized_character_image.get_rect()
# character_rect.center = (window_width // 2, window_height // 2)

# clock = pygame.time.Clock()
# speed = 5

# running = True
# while running:
#     window.fill(white)

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     key = pygame.key.get_pressed()

#     if key[pygame.K_LEFT]:
#         character_rect.x -= speed
#     if key[pygame.K_RIGHT]:
#         character_rect.x += speed
#     if key[pygame.K_UP]:
#         character_rect.y -= speed
#     if key[pygame.K_DOWN]:
#         character_rect.y += speed

#     window.blit(resized_character_image, character_rect)

#     pygame.display.flip()
#     clock.tick(60)

# pygame.quit()
# sys.exit()
