import pygame
import time
import sys

class Visualizer:
    """
    Class xử lý các thao tác vẽ cấp thấp bằng Pygame cho Maze.
    
    Attributes:
        rows (int): Số hàng của maze (bao gồm cả tường).
        cols (int): Số cột của maze (bao gồm cả tường).
        cell_size (int): Kích thước của mỗi ô (pixel).
        screen (pygame.Surface): Cửa sổ hiển thị của Pygame.
    """
    
    # ─── COLOR PALETTE ──────────────────────────────────────────
    COLOR_BG        = (15, 15, 25)      # Màu nền
    COLOR_WALL      = (40, 40, 60)      # Màu tường
    COLOR_PATH      = (200, 200, 220)   # Màu đường đi
    COLOR_VISITED   = (80, 140, 200)    # Màu ô đang được duyệt (xanh dương)
    COLOR_DONE      = (200, 200, 220)   # Màu ô đã vẽ xong (trắng xám)
    COLOR_PLAYER    = (255, 100, 100)   # Màu người chơi (đỏ)
    COLOR_EXIT      = (100, 255, 100)   # Màu điểm thoát (xanh lá)

    def __init__(self, rows, cols, cell_size=20):
        """
        Khởi tạo Visualizer và tạo cửa sổ Pygame.

        Args:
            rows (int): Số hàng thực tế của ma trận maze.
            cols (int): Số cột thực tế của ma trận maze.
            cell_size (int, optional): Kích thước pixel của mỗi ô. Mặc định là 20.
        """
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        
        pygame.init()
        self.screen_width =1000
        self.screen_height = 1000
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Maze Game")
        self.clock = pygame.time.Clock()

    def draw_full_walls(self):
        """
        Vẽ toàn bộ maze với màu tường (trạng thái bắt đầu).
        
        Returns:
            None
        """
        self.screen.fill(self.COLOR_WALL)
        pygame.display.flip()

    def draw_cell(self, r, c, color):
        """
        Vẽ một ô đơn lẻ tại tọa độ (r, c).

        Args:
            r (int): Chỉ số hàng của ô.
            c (int): Chỉ số cột của ô.
            color (tuple): Màu RGB của ô.
            
        Returns:
            None
        """
        pygame.draw.rect(
            self.screen,
            color,
            (c * self.cell_size, r * self.cell_size, self.cell_size, self.cell_size)
        )

    def animate_generation(self, path, delay=0.01):
        """
        Tạo animation xóa tường dựa trên danh sách các ô đã đi qua.
        Hàm này sử dụng một stack nội bộ để tái hiện quá trình Backtracking.

        Args:
            path (list): Danh sách các tuple (r, c) là thứ tự các ô thuật toán DFS đã ghé thăm.
            delay (float, optional): Thời gian chờ giữa các bước (giây). Mặc định là 0.01.
            
        Returns:
            None
        """
        self.draw_full_walls()
        if not path:
            return

        # Khởi tạo điểm bắt đầu
        start_r, start_c = path[0]
        self.draw_cell(start_r, start_c, self.COLOR_VISITED)
        pygame.display.flip()
        time.sleep(delay)

        track = [path[0]] # Stack để theo dõi đường đi hiện tại (để tìm cha của ô kế tiếp)

        for next_node in path[1:]:
            nr, nc = next_node
            
            # Tìm kiếm trong stack để xác định ô nào là ô cha của next_node
            # (ô có khoảng cách là 2 ô - vì ở giữa là 1 bức tường)
            while track:
                cr, cc = track[-1]
                if (abs(cr - nr) == 2 and cc == nc) or (abs(cc - nc) == 2 and cr == nr):
                    # Tìm thấy ô cha: Xóa bức tường nằm giữa ô cha và ô con
                    wr, wc = (cr + nr) // 2, (cc + nc) // 2
                    
                    # Cập nhật màu sắc: Ô cha cũ thành DONE, ô tường và ô con thành VISITED
                    self.draw_cell(cr, cc, self.COLOR_DONE)
                    self.draw_cell(wr, wc, self.COLOR_DONE)
                    self.draw_cell(nr, nc, self.COLOR_VISITED)
                    
                    track.append(next_node)
                    break
                else:
                    # Nếu ô top không phải cha, tức là đang backtrack
                    self.draw_cell(cr, cc, self.COLOR_DONE)
                    track.pop()

            pygame.display.flip()
            
            # Xử lý sự kiện Pygame để tránh bị treo cửa sổ
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            time.sleep(delay)

        # Đổi màu các ô cuối cùng trong stack thành màu DONE
        for r, c in track:
            self.draw_cell(r, c, self.COLOR_DONE)
        pygame.display.flip()

    def draw_player(self, r, c):
        """
        Vẽ người chơi (hình tròn màu đỏ) tại tọa độ (r, c).

        Args:
            r (int): Chỉ số hàng.
            c (int): Chỉ số cột.
            
        Returns:
            None
        """
        padding = self.cell_size // 4
        pygame.draw.circle(
            self.screen,
            self.COLOR_PLAYER,
            (c * self.cell_size + self.cell_size // 2, 
             r * self.cell_size + self.cell_size // 2),
            self.cell_size // 2 - padding
        )

    def draw_exit(self, r, c):
        """
        Vẽ điểm thoát (hình vuông màu xanh lá) tại tọa độ (r, c).

        Args:
            r (int): Chỉ số hàng.
            c (int): Chỉ số cột.
            
        Returns:
            None
        """
        padding = self.cell_size // 4
        pygame.draw.rect(
            self.screen,
            self.COLOR_EXIT,
            (c * self.cell_size + padding, r * self.cell_size + padding, 
             self.cell_size - 2 * padding, self.cell_size - 2 * padding)
        )

    def draw_maze_static(self, grid):
        """
        Vẽ nhanh toàn bộ maze từ một ma trận có sẵn (không animation).

        Args:
            grid (numpy.ndarray): Ma trận 2D chứa giá trị 0 (đường) và 1 (tường).
            
        Returns:
            None
        """
        for r in range(self.rows):
            for c in range(self.cols):
                color = self.COLOR_DONE if grid[r][c] == 0 else self.COLOR_WALL
                self.draw_cell(r, c, color)

    def update_display(self):
        """
        Cập nhật màn hình và giới hạn tốc độ khung hình.
        """
        pygame.display.flip()
        self.clock.tick(60)


    def wait_for_close(self):
        """
        Giữ cửa sổ Pygame mở và xử lý sự kiện đóng cửa sổ.
        
        Returns:
            None
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.clock.tick(10)
