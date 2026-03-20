import pygame
import sys
import numpy as np

# ─── CÀI ĐẶT ────────────────────────────────────────────────
CELL_SIZE = 20          # pixel mỗi ô
FPS = 60
ANIMATION_SPEED = 5     # số ô vẽ mỗi frame khi bật animation

# Màu sắc
COLOR_BG        = (15, 15, 25)      # nền tối
COLOR_WALL      = (40, 40, 60)      # tường
COLOR_PATH      = (200, 200, 220)   # đường đi (grid = 0)
COLOR_VISITED   = (80, 140, 200)    # ô đang được vẽ animation
COLOR_DONE      = (200, 200, 220)   # ô đã vẽ xong
COLOR_TEXT      = (255, 255, 255)
COLOR_BTN       = (60, 60, 90)
COLOR_BTN_HOVER = (90, 90, 130)


def draw_maze_full(surface, grid, cell_size, offset_x, offset_y):
    """Vẽ toàn bộ maze ngay lập tức (không animation)"""
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            color = COLOR_PATH if grid[r][c] == 0 else COLOR_WALL
            #color = COLOR_WALL
            pygame.draw.rect(surface, color,
                (offset_x + c * cell_size,
                 offset_y + r * cell_size,
                 cell_size, cell_size))


def draw_maze_animated(surface, grid, path, step, cell_size, offset_x, offset_y):
    """Vẽ maze đến bước step trong path (có animation)"""
    rows, cols = grid.shape

    # Vẽ nền tường trước
    for r in range(rows):
        for c in range(cols):
            color = COLOR_PATH if grid[r][c] == 0 else COLOR_WALL
            pygame.draw.rect(surface, color,
                (offset_x + c * cell_size,
                 offset_y + r * cell_size,
                 cell_size, cell_size))

    # Vẽ các ô đã đi qua trong path
    for i in range(min(step, len(path))):
        r, c = path[i]
        color = COLOR_VISITED if i == min(step, len(path)) - 1 else COLOR_DONE
        pygame.draw.rect(surface, color,
            (offset_x + c * cell_size,
             offset_y + r * cell_size,
             cell_size, cell_size))

        # Vẽ wall giữa 2 ô liên tiếp
        if i > 0:
            pr, pc = path[i - 1]
            wr = (r + pr) // 2
            wc = (c + pc) // 2
            pygame.draw.rect(surface, COLOR_DONE,
                (offset_x + wc * cell_size,
                 offset_y + wr * cell_size,
                 cell_size, cell_size))


def draw_button(surface, rect, text, hovered, font):
    color = COLOR_BTN_HOVER if hovered else COLOR_BTN
    pygame.draw.rect(surface, color, rect, border_radius=8)
    pygame.draw.rect(surface, (100, 100, 150), rect, 2, border_radius=8)
    label = font.render(text, True, COLOR_TEXT)
    lx = rect.x + (rect.width - label.get_width()) // 2
    ly = rect.y + (rect.height - label.get_height()) // 2
    surface.blit(label, (lx, ly))


def visualize(grid, path):
    """
    Hàm chính để hiển thị maze.

    Args:
        grid: numpy array (W x H), 0 = đường, 1 = tường
        path: list of tuples [(row, col), ...] — thứ tự các ô đã đi
    """
    pygame.init()
    font      = pygame.font.SysFont("consolas", 14)
    font_big  = pygame.font.SysFont("consolas", 16, bold=True)

    rows, cols = grid.shape
    maze_w = cols * CELL_SIZE
    maze_h = rows * CELL_SIZE

    # Padding và UI
    PAD = 20
    BTN_H = 36
    BTN_W = 160
    UI_BOTTOM = BTN_H + PAD * 2

    WIN_W = maze_w + PAD * 2
    WIN_H = maze_h + PAD * 2 + UI_BOTTOM

    screen = pygame.display.set_mode((WIN_W, WIN_H))
    pygame.display.set_caption("Maze Visualizer")
    clock = pygame.time.Clock()

    offset_x = PAD
    offset_y = PAD

    # Trạng thái
    animation_on  = True
    anim_step     = 0
    anim_done     = False

    # Nút bấm
    btn_toggle = pygame.Rect(PAD, maze_h + PAD * 2, BTN_W, BTN_H)
    btn_reset  = pygame.Rect(PAD + BTN_W + 10, maze_h + PAD * 2, BTN_W, BTN_H)
    generator = Randomized_DFS(10,10)
    grid, path = generator.generate()

    while True:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        draw_maze_full(screen, grid,CELL_SIZE, offset_x, offset_y)

        



        pygame.display.flip()
        clock.tick(FPS)


# ─── CHẠY THỬ ────────────────────────────────────────────────
if __name__ == "__main__":
    # Import maze generator của bạn
    import sys
    import os
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    from generator.Randomized_DFS import Randomized_DFS

    gen = Randomized_DFS(15, 15)
    grid, path = gen.generate()   # ← generate() cần return cả grid lẫn path

    visualize(grid, path)