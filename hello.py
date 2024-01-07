print("Thành Nam Coffee xin chào quý khách !")
# for i in range(1,3):
#     print()
a = 'Bạc xỉu nóng/đá\t'
b = 'Trà sữa nhài xanh'
c = 'Hồng trà bốn mùa'
d = 'Trà sữa socola\t'
e = 'Capuchino\t'
f = 'Latte\t\t'

print("\t\t\t\tThành Nam coffee")
print()
print("--------------------------------------Menu-------------------------------------")
for i in range(1,2):
    print()

print("STT\tTên đồ uống\t\t\t\t  Giá")
print("1. \tBạc xỉu nóng/đá \t\t\t 45.000 VNĐ")
print("2. \tTrà sữa nhài xanh \t\t\t 40.000 VNĐ")
print("3. \tHồng trà bốn mùa  \t\t\t 35.000 VNĐ")
print("4. \tTrà sữa socola \t\t\t\t 35.000 VNĐ")
print("5. \tCapuchino \t\t\t\t 50.000 VNĐ")
print("6. \tLatte Machiato \t\t\t\t 60.000 VNĐ")
print()
print("Lưu ý:")
print("Quý khách mua tiếp sẽ nhập 1 phím bất kì, không mua tiếp sẽ nhập N.")
print("Đối với hóa đơn trên 500k sẽ bị phụ thêm vat 10%.")
print()

tien = 0
list1 = [ ' ']
list2 = [ ' ']
list3 = [ ' ']
soluong =""
shopping = True
while (shopping):
        name = int(input('Mời quý khách chọn đồ uống: '))
        n = int(input('Số lượng đồ uống cần chọn: ')) 
        if name == 1:
            tien += n*45
            list1.append(a)
            list2.append('\t\t45.000 VNĐ')
            list3.append(n)
        elif name == 2:
            tien += n*40
            list1.append(b)
            list2.append('\t\t40.000 VNĐ') 
            list3.append(n)
        elif name == 3:
            tien += n*35
            list1.append(c)
            list2.append('\t\t35.000 VNĐ') 
            list3.append(n)
        elif name == 4:
            tien += n*35
            list1.append(d)
            list2.append('\t\t35.000 VNĐ')
            list3.append(n)
        elif name == 5:
            tien += n*50
            list1.append(e)
            list2.append('\t\t50.000 VNĐ')
            list3.append(n)
        elif name == 6:
            tien += n*60
            list1.append(f)
            list2.append('\t\t60.000 VNĐ') 
            list3.append(n)
        muaTiep = input("Bạn có muốn mua tiếp (Y/N): ")
        if muaTiep == "N":
            shopping = False
print()   
print("\t\t\t\tThành Nam coffee")
print()
print("--------------------------------------Bill-------------------------------------")
for i in range(1,2):
    print()


print("STT\tTên đồ uống\t\tSố lượng\t\tGiá")
vat = 0
if tien > 500:
    vat = tien // 10

m = len(list1)
for i in range(1,m):
    print(i,list1[i],list3[i],list2[i], sep= '\t')

print()    
print('Thuế của quý khách là vat: ','%.4f' %vat,'VNĐ')
tong = tien + vat
print('Số tiền quý khách cần thanh toán là:','%.4f' %tong, 'VNĐ')
if tong >= 1000:
    print("Quý khách được tặng voucher 10% vào lần mua tiếp theo")
elif tong >= 2000:
    print("Quý khách được tặng voucher 20% vào lần mua tiếp theo")
elif tong >= 3000:
    print("Quý khách được tặng voucher 30% vào lần mua tiếp theo")

print()
print("---------------------Thành Nam Coffee cảm ơn quý khách-------------------------")
print('\n')
print('Liên hệ với chúng tôi : 0979254083 -','S4.01 Vinhomes Smart City -','gmail: nambeo1909tn@gmail.com')
