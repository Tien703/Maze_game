from generator.Randomized_DFS import Randomized_DFS
from front_end.renderer import Renderer
import time

def main():
    # 1. Khởi tạo thuật toán tạo maze (ví dụ kích thước 15x15)
    # Lưu ý: W, H thực tế sẽ là (15*2+1) = 31
    width, height = 15, 15
    gen = Randomized_DFS(width, height)
    
    print("Đang tạo maze...")
    grid, path = gen.generate()
    
    # 2. Khởi tạo Renderer với số hàng và cột thực tế của maze
    # gen.H và gen.W là kích thước ma trận bao gồm cả tường
    renderer = Renderer(gen.H, gen.W, cell_size=20)
    
    # Bước 1: Hiện maze đầy tường
    renderer.show_full_walls()
    time.sleep(1) # Đợi 1 giây trước khi bắt đầu
    
    # Bước 2: Chạy animation xóa tường dựa trên path của thuật toán
    print("Đang chạy animation xóa tường...")
    renderer.animate_maze(path, delay=0.01)
    
    # Bước 3: Vẽ player tại vị trí bắt đầu (ô đầu tiên trong path)
    print("Vẽ player...")
    start_r, start_c = path[0]
    renderer.show_player(start_r, start_c)
    
    print("Hoàn thành! Đóng cửa sổ để kết thúc.")
    # Giữ cửa sổ mở cho đến khi bạn đóng nó
    renderer.keep_open()

if __name__ == "__main__":
    main()
