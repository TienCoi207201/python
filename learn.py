# import math
# import sys
# import json
# import turtle as t
# from random import random

# #Tạo list lưu thông tin người dùng
# users = []

# def quanly():
#     return 1

# def ptbacnhat():
#     a = int(input("Nhập số thứ nhất: "))
#     b = int(input("Nhập số thứ hai: "))
#     if a == 0:
#         if b == 0:
#             if c == 0:
#                 print("Phương trình có vô số nghiệm")
#             else:
#                 print("Phương trình vô nghiệm")
#         else:
#             print("Phương trình có nghiệm: ", -c / b)
#     else:
#         print("Phương trình có nghiệm", -b / a)

# def ptbac2():
#         a = int(input("Nhập số thứ nhất: "))
#         b = int(input("Nhập số thứ hai: "))
#         c = int(input("Nhập số thứ ba: "))
#         if a == 0:
#             if b == 0:
#                 if c == 0:
#                     print ("Phương trình vô số nghiệm!")
#                 else:
#                     if c == 0:
#                         print("Phương trình có 1 nghiệm x = 0")
#                     else:
#                         print("Phương trình có nghiệm: ", -c / b)
#         delta = b * b - 4 * a * c
#         if (delta > 0):
#             x1 = (float)((-b + math.sqrt(delta)) / (2 * a))
#             x2 = (float)((-b - math.sqrt(delta)) / (2 * a))
#             print ("Phương trình có 2 nghiệm là: x1 = ", x1, " và x2 = ", x2)
#         elif (delta == 0):
#             x1 = float(-b / (2 * a))
#             print("Phương trình có nghiệm kép: x1 = x2 = ", x1)
#         else:
#             print("Phương trình vô nghiệm!")

# def tinhtongmang():
#         #Tạo ra 1 list để lưu các phần tử
#         a = []
#         n = int(input("Nhập số phần tử mảng: "))
#         tong = 0
#         print("Nhập giá trị các phần tử mảng")
#         for i in range(0, n):
#             number = int(input())
#             a.append(number)
#         print("Mảng vừa nhập là:", a)
#         for i in a:
#             tong += i
#         print("Tổng các phần tử trong mảng là:", tong)

# user_id_counter = 1
# def thi():
#         print("---------------------------------------------------------------------")
#         print("Ở đây sẽ có 10 câu hỏi, và mỗi câu hỏi sẽ tương ứng với 1 điểm, nhiệm vụ\n\ncủa chúng ta là giải các câu hỏi đó^^")
#         print("---------------------------------------------------------------------")
#         point = 0
#         b = ['Kết quả của 4 + 8 là: ','Kết quả của 9 + 3 là: ',
#              'Kết quả của 9 - 4 là: ','Kết quả của 10 - 9 là: ',
#              'Kết quả của 4 * 6 là: ','Kết quả của 9 * 9 là: ',
#              'Kết quả của 9 / 3 là: ','Kết quả của 6 / 2 là: ',
#              'Kết quả của 5 * 5 - 10 là:','Kết quả của 10 - 8 / 2 là: ']
#         name = input("Nhập tên của bạn: ")
#         for i in range(0, len(b)):
#             print(b[i])
#             rs = int(input())
#             if i == 0:
#                 if rs == 12:
#                     print("Chính xác ^^")
#                     point += 1
#                 else:
#                     print("Sai mất tiu rùi :((")
#             elif i == 1:
#                 if rs == 12:
#                     print("Chính xác ^^")
#                     point += 1
#                 else:
#                     print("Sai mất tiu rùi :((")
#             elif i == 2:
#                 if rs == 5:
#                     print("Chính xác ^^")
#                     point += 1
#                 else:
#                     print("Sai mất tiu rùi :((")
#             elif i == 3:
#                 if rs == 1:
#                     print("Chính xác ^^")
#                     point += 1
#                 else:
#                     print("Sai mất tiu rùi :((")
#             elif i == 4:
#                 if rs == 24:
#                     print("Chính xác ^^")
#                     point += 1
#                 else:
#                     print("Sai mất tiu rùi :((")
#             elif i == 5:
#                 if rs == 81:
#                     print("Chính xác ^^")
#                     point += 1
#                 else:
#                     print("Sai mất tiu rùi :((")
#             elif i == 6:
#                 if rs == 3:
#                     print("Chính xác ^^")
#                     point += 1
#                 else:
#                     print("Sai mất tiu rùi :((")
#             elif i == 7:
#                 if rs == 3:
#                     print("Chính xác ^^")
#                     point += 1
#                 else:
#                     print("Sai mất tiu rùi :((")
#             elif i == 8:
#                 if rs == 15:
#                     print("Chính xác ^^")
#                     point += 1
#                 else:
#                     print("Sai mất tiu rùi :((")
#             elif i == 9:
#                 if rs == 6:
#                     print("Chính xác ^^")
#                     point += 1
#                 else:
#                     print("Sai mất tiu rùi :((")
#         def add_new_user(name, point):
#             global user_id_counter
#             new_user = {
#                 'id': user_id_counter,
#                 'name': name,
#                 'point': point
#             }
#             users.append(new_user)
#             user_id_counter += 1
#         add_new_user(name, point)
#         print(users)
#         print(name,"\tĐiểm: ",point)
#         if len(users) > 1:
#             sort_list = sorted(users, key = lambda x: x["point"], reverse= True)
#             print("Danh sách giảm dần", sort_list)
#             with open('myfile.txt', 'w') as file:
#                 for item in sort_list:
#                     file.write(json.dumps(item) + '\n')
#             # print(type(convert))

# select = True
# while (select):
#     print('---------------Toán học--------------')
#     print('-------------------------------------')
#     print("Vui lòng ấn phím 1 nếu bạn muốn chọn chức năng Tính toán\n")
#     print("Ấn phím 2 nếu bạn muốn chọn chức năng Giải các bài tập toán\n")
#     print("Ấn phím 3 nếu bạn muốn thoát chương trình\n")
#     print("Nếu ấn phím bất kỳ ngoài số nguyên ra chương trình sẽ lỗi")
#     print("-------------------------------------")
#     print('1\t Tính toán')
#     print('2\t Giải toán')
#     print('3\t Quản lý danh sách thi')
#     print('3\t Exit')
#     selected = int(input('Hãy chọn chương trình bạn muốn: '))
#     while not (selected >= 1 and selected <= 3):
#         selected = int(input("Vui lòng nhập lại: "))
#     if selected == 1:
#         print("----------------------------------------------------------")
#         print("Mỗi số thứ tự sẽ tương ứng với 1 phép tính, bạn hãy chọn bất kỳ \n\n1 số từ 1 đến 7 để chọn phép tính bạn muốn\n")
#         print("Nếu ấn phím bất kỳ ngoài số nguyên chương trình sẽ lỗi")
#         print("----------------------------------------------------------")
#         print("STT\t Bài toán\t")
#         print("1\t Phép cộng")
#         print("2\t Phép trừ")
#         print("3\t Phép nhân")
#         print("4\t Phép chia")
#         print("5\t Giải phương trình bậc 1: ax + b = 0")
#         print("6\t Giải phương trình bậc 2: ax2 + bx + c = 0")
#         print("7\t Tính tổng các phần tử trong mảng")
#         choosemath = int(input("Hãy chọn phép tính bạn muốn: "))
#         if choosemath == 1:
#             a = int(input("Nhập số thứ nhất:"))
#             b = int(input("Nhập số thứ hai:")) 
#             print("Kết quả là: ", a + b)

#         elif choosemath == 2:
#             a = int(input("Nhập số thứ nhất:"))
#             b = int(input("Nhập số thứ hai:"))
#             print("Kết quả là: ", a - b)

#         elif choosemath == 3:
#             a = int(input("Nhập số thứ nhất:"))
#             b = int(input("Nhập số thứ hai:"))
#             print("Kết quả là: ", a * b)

#         elif choosemath == 4:
#             a = int(input("Nhập số thứ nhất:"))
#             b = int(input("Nhập số thứ hai:"))
#             print("Kết quả là: ", a / b)

#         elif choosemath == 5:
#             ptbacnhat()

#         elif choosemath == 6:
#             ptbac2()
#         elif choosemath == 7:
#             tinhtongmang()
#     elif selected == 2:
#         thi()
#     elif selected == 3:
#         quanly()
#     elif selected == 4:
#         sys.exit()
#     tieptuc = input("Bạn có muốn tiếp tục không (Y/N):?")
#     if( tieptuc == "n" or tieptuc == "N" ):
#         select = False

import math

a = int(input("Nhập vào số a:"))
b = int(input("Nhập vào số b:"))
# c = int(input("Nhập vào số c:"))
if( a == 0):
    if( b == 0 ):
        print("Phương trình có vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    print("Phương trình có 1 nghiệm là:",-b/a)