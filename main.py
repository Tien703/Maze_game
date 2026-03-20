import pygame
import sys
from generator.Randomized_DFS import Randomized_DFS
from logic.Player import Player
from front_end.renderer import Renderer

def main():
    # Cấu hình maze
    W, H = 10,10  # Kích thước maze (nên là số lẻ)
    cell_size = 30
    
    # 1. Khởi tạo Maze Generator và tạo maze
    maze_gen = Randomized_DFS(W, H)
    grid, path = maze_gen.generate()
    
    # 2. Khởi tạo Player tại vị trí (1, 1)
    player = Player(1, 1)
    
    # 3. Điểm thoát tại (W-2, H-2)
    exit_pos = (W - 2, H - 2)
    grid[exit_pos[0]][exit_pos[1]] = 0 # Đảm bảo lối thoát là đường đi
    
    # 4. Khởi tạo Renderer
    renderer = Renderer(W, H, cell_size)
    
    # Chạy animation tạo maze (tùy chọn)
    renderer.animate_maze(path, delay=0.005)
    
    # Game Loop
    running = True
    won = False
    
    while running:
        # Xử lý sự kiện
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            
            if not won and event.type == pygame.KEYDOWN:
                direction = None
                if event.key == pygame.K_UP:
                    direction = 1
                elif event.key == pygame.K_DOWN:
                    direction = 2
                elif event.key == pygame.K_LEFT:
                    direction = 3
                elif event.key == pygame.K_RIGHT:
                    direction = 4
                
                if direction:
                    if player.valid_direction(grid, direction):
                        player.moves(direction)
                        
                        # Kiểm tra điều kiện thắng
                        if player.win_condition(exit_pos):
                            print("Chúc mừng! Bạn đã thắng!")
                            won = True

        # Vẽ lại màn hình
        renderer.show_static_maze(grid)
        renderer.show_exit(exit_pos[0], exit_pos[1])
        renderer.show_player(player.r, player.c)
        
        if won:
            # Hiển thị thông báo thắng đơn giản (có thể cải thiện sau)
            font = pygame.font.SysFont("Arial", 48)
            text = font.render("YOU WIN!", True, (255, 255, 0))
            text_rect = text.get_rect(center=(W * cell_size // 2, H * cell_size // 2))
            renderer.visualizer.screen.blit(text, text_rect)

        renderer.update()

if __name__ == "__main__":
    main()
