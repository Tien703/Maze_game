import pygame
from front_end.visualizer import Visualizer

class Renderer:
    """
    Class điều phối (Manager) cao cấp để quản lý quy trình hiển thị Maze.
    
    Attributes:
        visualizer (Visualizer): Đối tượng thực hiện việc vẽ chi tiết.
    """
    
    def __init__(self, rows, cols, cell_size=20):
        """
        Khởi tạo Renderer.

        Args:
            rows (int): Tổng số hàng của ma trận maze (bao gồm tường).
            cols (int): Tổng số cột của ma trận maze (bao gồm tường).
            cell_size (int, optional): Kích thước ô tính bằng pixel. Mặc định là 20.
        """
        self.visualizer = Visualizer(rows, cols, cell_size)

    def show_full_walls(self):
        """
        Giai đoạn 1: Hiển thị maze ở trạng thái ban đầu (đầy tường).
        
        Returns:
            None
        """
        self.visualizer.draw_full_walls()

    def animate_maze(self, path, delay=0.02):
        """
        Giai đoạn 2: Thực hiện animation xóa tường dựa trên đường đi của thuật toán.

        Args:
            path (list): Danh sách các tọa độ ô thuật toán đã duyệt qua.
            delay (float, optional): Tốc độ animation (giây giữa mỗi bước). Mặc định là 0.02.
            
        Returns:
            None
        """
        self.visualizer.animate_generation(path, delay)

    def show_player(self, r, c):
        """
        Giai đoạn 3: Vẽ người chơi lên maze sau khi hoàn thành.

        Args:
            r (int): Vị trí hàng của người chơi.
            c (int): Vị trí cột của người chơi.
            
        Returns:
            None
        """
        self.visualizer.draw_player(r, c)

    def show_exit(self, r, c):
        """
        Vẽ điểm thoát lên maze.

        Args:
            r (int): Vị trí hàng của điểm thoát.
            c (int): Vị trí cột của điểm thoát.
        """
        self.visualizer.draw_exit(r, c)

    def update(self):
        """
        Cập nhật hiển thị.
        """
        self.visualizer.update_display()

    def show_static_maze(self, grid):
        """
        Hiển thị maze tĩnh từ ma trận dữ liệu (không chạy animation).

        Args:
            grid (numpy.ndarray): Ma trận maze (0=đường, 1=tường).
            
        Returns:
            None
        """
        self.visualizer.draw_maze_static(grid)

    def keep_open(self):
        """
        Duy trì cửa sổ hiển thị cho đến khi người dùng đóng lại.
        
        Returns:
            None
        """
        self.visualizer.wait_for_close()
