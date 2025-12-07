from ui import InventoryManagementApp  # Nhập lớp InventoryManagementApp từ file ui.py
import ttkbootstrap as ttkb  # Nhập thư viện ttkbootstrap, một thư viện giao diện người dùng đẹp và hiện đại, cải tiến từ tkinter

if __name__ == "__main__":  # Kiểm tra xem đoạn mã có đang được chạy trực tiếp hay không
    # Tạo cửa sổ chính của ứng dụng sử dụng ttkbootstrap với chủ đề "minty" (màu xanh lá đẹp mắt)
    root = ttkb.Window(themename="minty")  # Tạo một cửa sổ ứng dụng với chủ đề "minty"
    root.geometry("1200x800")  # Thiết lập kích thước cửa sổ
    root.configure(bg="#f0f4f8")  # Màu nền xám xanh nhạt
    
    # Tạo đối tượng InventoryManagementApp và gắn vào cửa sổ root
    app = InventoryManagementApp(root)
    
    # Bắt đầu vòng lặp chính của giao diện người dùng
    root.mainloop()  # Chạy vòng lặp chính của ttkbootstrap (giao diện người dùng)
