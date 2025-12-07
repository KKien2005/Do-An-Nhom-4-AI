# 🎒 Knapsack Optimization using Simulated Annealing

Ứng dụng mô phỏng thuật toán **Simulated Annealing** để giải quyết **bài toán Knapsack** (tối ưu hoá chọn vật phẩm theo cân nặng và giá trị).

---

## 🚀 Tính năng
✔ Chọn và tải file dữ liệu vật phẩm (`.csv`)  
✔ Thiết lập tham số thuật toán (Temp, Cooling, Iterations)  
✔ Hiển thị kết quả tối ưu: Tổng giá trị, trọng lượng, vật phẩm chọn  
✔ Giao diện trực quan bằng **Tkinter + ttkbootstrap**

---

## 🛠 Công nghệ sử dụng
- Python 3.x  
- Tkinter + ttkbootstrap (UI)
- Simulated Annealing (thuật toán tối ưu)

---

## 📂 Cấu trúc dự án
│── main.py # File chạy chính
│── ui.py # Giao diện ứng dụng
│── knapsack_algorithm.py # Thuật toán SA
│── data_100_unique.csv # File dữ liệu mẫu

---

## ▶️ Hướng dẫn chạy ứng dụng
-Cài đặt thư viện cần thiết
Mở Terminal tại thư mục dự án và chạy:
pip install ttkbootstrap 
- Chỉnh lại folder chứa dự liệu tại file UI.py dòng 113
- Sau đó chạy python main.py
- Trên giao diện ứng dụng

Chọn file dữ liệu CSV

Nhập thông số thuật toán

Nhấn Run Algorithm

Xem kết quả tối ưu hiển thị bên dưới

