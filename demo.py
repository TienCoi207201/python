# # a = int(input('Nhập số a:'))
# # b = int(input('Nhập số b:'))
# # # print(a+b, a-b, a*b, a/b)

# # if(a == 0):
# #     if(b == 0):
# #         print("phương trình vô số nghiệm")
# #     else:
# #         print("phương trình vô nghiệm")
# # else:
# #     print("phương trình có một nghiệm", -b/a)

# import tkinter as tk

# def register():
#     username = username_entry.get()
#     email = email_entry.get()
#     password = password_entry.get()

#     # Xử lý thông tin đăng ký ở đây (có thể in ra để kiểm tra)
#     print(f"Đăng ký thành công!\nTên người dùng: {username}\nEmail: {email}\nMật khẩu: {password}")

# root = tk.Tk()
# root.title("Form Đăng Ký")

# # Tạo frame chứa các phần tử giao diện
# form_frame = tk.Frame(root, padx=20, pady=20)
# form_frame.pack()

# # Tạo các Label và Entry để nhập thông tin
# username_label = tk.Label(form_frame, text="Tên người dùng:")
# username_label.grid(row=0, column=0, pady=5, sticky="w")
# username_entry = tk.Entry(form_frame, width=30)
# username_entry.grid(row=0, column=1, padx=10)

# email_label = tk.Label(form_frame, text="Email:")
# email_label.grid(row=1, column=0, pady=5, sticky="w")
# email_entry = tk.Entry(form_frame, width=30)
# email_entry.grid(row=1, column=1, padx=10)

# password_label = tk.Label(form_frame, text="Mật khẩu:")
# password_label.grid(row=2, column=0, pady=5, sticky="w")
# password_entry = tk.Entry(form_frame, show="*", width=30)  # show="*" để ẩn mật khẩu khi nhập
# password_entry.grid(row=2, column=1, padx=10)

# # Tạo nút đăng ký
# register_button = tk.Button(root, text="Đăng Ký", command=register, width=20, bg="blue", fg="white", pady=8)
# register_button.pack(pady=10)

# root.mainloop()

# Định nghĩa lớp "Ngôi nhà"
# class House:
#     def __init__(self, address, owner, rooms, area):
#         self.address = address  # Địa chỉ của ngôi nhà
#         self.owner = owner      # Chủ sở hữu
#         self.rooms = rooms      # Số phòng
#         self.area = area        # Diện tích

#     def describe(self):
#         return f"Ngôi nhà tại {self.address} có diện tích {self.area} mét vuông, có {self.rooms} phòng và chủ sở hữu là {self.owner}."

# # Tạo đối tượng từ lớp "Ngôi nhà"
# my_house = House("123 Đường ABC", "John Doe", 4, 200)

# # In ra thông tin về ngôi nhà
# print(my_house.describe())


import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import *

window = tk.Tk()
window.title = "Đăng nhập"
window.geometry("1000x1000")

def wind2():
    window2 = tk.Tk()
    window2.geometry("900x900")
    window2.title = "Cửa sổ mới"
#Combobox
list = Combobox(window, font=("TimeNewRoman", 16))
# droplist = tk.OptionMenu(window, 'Môn học',*list)
list['value'] = ('Siêu nhân lập trình web', 'Siêu nhân làm game', 'Khám phá Robotics')
list.current(1)
list.place(x=300,y=300)

#RadioButton
radio = Radiobutton(window, text="Nam").place(x=300, y= 350)
radio = Radiobutton(window, text="Nữ").place(x= 380, y=350)

#Checkbox
check = Checkbutton(window, text="Đồng ý với điều khoản").place(x= 300, y= 380)


def showinfo():
    messagebox.showinfo('Thông báo', 'Đây là message box')
#Label(nhãn) and entry(ô nhập)
label1 = tk.Label(window, text="Tên người dùng", font="TimeNewRoman", justify="center").place(x=100, y=150)
entry1 = tk.Entry(window, width=40).place(x=300, y=150)
label2 = tk.Label(window, text="Mật khẩu", font="TimeNewRoman").place(x=100, y=200)
entry2 = tk.Entry(window, show="*", width=40).place(x=300, y=200)

# def getUserInput():
#     value = entry1.get()
#     messagebox.showinfo("Thông báo", value)

btn = tk.Button(text="Đăng nhập", command=wind2).place(x=300, y=250)



window.mainloop()


