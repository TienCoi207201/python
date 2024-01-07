import tkinter as tk
from tkinter import ttk
# import PIL.ImageTk
# import PIL.Image

root = tk.Tk()
root.geometry("700x400")
root.title("Đăng nhập")
# name_user_input = tk.StringVar()
# pass_user_input = tk.StringVar()

# def submit():
#     username = name_user_input.get()
#     password = pass_user_input.get()
#     print(username)
#     print(password)
# import tkinter as tk

# root = tk.Tk()

# # Tạo và đặt các widget vào cùng một hàng với khoảng cách dọc
# label1 = tk.Label(root, text="Label 1")
# label2 = tk.Label(root, text="Label 2")
# label3 = tk.Label(root, text="Label 3")

# label1.grid(row=0, column=0, pady=10)  # Khoảng cách dọc 10 pixel
# label2.grid(row=0, column=1, pady=20)  # Khoảng cách dọc 20 pixel
# label3.grid(row=0, column=2, pady=100)  # Khoảng cách dọc 30 pixel

# root.mainloop()

# from tkinter import *
# from tkinter import ttk
# root = Tk()
# root.geometry("1000x500")
# frm = ttk.Frame(root, padding=50)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# # ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# ttk.Combobox()
# root.mainloop()
def form_login():
    def on_selected_combobox(event):
        selected_item = combobox_var.get()
        result_label.config(text=f"You selected: {selected_item}")
    #Tạo biến và list quốc gia
    combobox_var = tk.StringVar()
    listNational = ['Nhật Bản', 'Hàn Quốc', 'Việt Nam']
#     # Tạo label và ô nhập dữ liệu
#     login_user = tk.Label(root, text = 'Tài khoản', font=('TimeNewRoman', 10, 'bold'))
#     pass_user = tk.Label(root, text = 'Mật khẩu', font=('TimeNewRoman', 10, 'bold'))
#     name_input = tk.Entry(root, textvariable= name_user_input, font=(' Times New Roman', 10))
#     pass_input = tk.Entry(root, textvariable= pass_user_input, font=(' Times New Roman', 10), show= '*')
#     btn_submit = tk.Button(root, text= 'Đăng nhập', command = submit)
#     result_label = tk.Label(root, text="")
#     result_label.grid(column=0, row=4)
#     login_user.grid(row=0, column=0)
#     pass_user.grid(row=1, column=0)
#     name_input.grid(row=0, column=1)
#     pass_input.grid(row=1, column=1)
#     btn_submit.grid(row=2, column=0)
# def test_anh():
#     path = Image.open('./183076132_1138687499938981_3255220776413760679_n.jpg')
#     photo = ImageTk.PhotoImage(path)
#     labe = tk.Label(image=photo)
#     labe.pack()
# test_anh()

#     # Tạo combobox
    droplist = ttk.Combobox(root, textvariable= combobox_var, values= listNational)
    print(combobox_var.get())
#     # droplist.current(2)
    droplist.bind("<<ComboboxSelected>>", on_selected_combobox)


    droplist.grid(row=3, column=1)
    result_label = tk.Label(root, text="")
    result_label.grid(column=0, row=1)

form_login()

root.mainloop()



