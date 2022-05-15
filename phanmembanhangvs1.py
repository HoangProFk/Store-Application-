from tkinter import *
from tkinter import font
from PIL import Image,ImageTk
from tkinter import messagebox

#Hàm thoát
def thoat():
    quit()
#Hàm tính tiền
def tinhtoan():
    x1 = int(nhap_soluong.get())
    x2 = int(nhap_soluong2.get())
    x3 = int(nhap_soluong3.get())
    x4 = int(nhap_soluong4.get())
    tong_all = x1 * 13000 + x2 * 10000 + x3 * 15000 + x4 * 40000
    nhap_tien.config(text = tong_all)
#Hàm xuất hóa đơn
def xuathoadon():
    global tong_all
    messagebox.showinfo("Phần mềm quản lý bán hàng", "Tên Khách Hàng: " + nhapten.get() + "\n" + "Lương thực (kg) " + nhap_soluong.get() + "\n" +  "Nước Ngọt/Bia (lon) " + nhap_soluong2.get() + "\n" +  "Trái cây (kg) " + nhap_soluong3.get() + "\n" + "Bánh kẹo (Hộp) " + nhap_soluong4.get())
    


hoangdz = Tk()
hoangdz.resizable (False, False)
#hoangdz.iconbitmap("ic_local_grocery_store_128_28460.ico")

#load = Image.open("pro11.jpg")
#render = ImageTk.PhotoImage(load)
#img = Label(hoangdz, image = render)
#img.place(x = 0, y = 0)

hoangdz.geometry("800x400")
hoangdz.title("Phần mềm quản lý bán hàng")
hoangdz.configure(bg = "Skyblue1")

tenKH = Label (hoangdz, text = "Tên khách hàng" ,font = ("Arial", 14), fg = "Red")
tenKH.pack()
tenKH.place(x = 400, y = 150)
nhapten = Entry (hoangdz, width = 30, font = (14))
nhapten.pack()
nhapten.place(x = 310, y = 180)

cac_mat_hang = Label (hoangdz, text = "Các mặt hàng", font = ("Arial", 18),bg = "Pink", fg = "#FFFFFF")
cac_mat_hang.pack()
cac_mat_hang.place(x = 10, y = 10)

luong_thuc = Label (hoangdz, text = "Lương Thực (kg)", font = ("Arial", 14 ), fg = "black")
luong_thuc.pack()
luong_thuc.place(x = 10, y = 50)
nhap_soluong = Entry (hoangdz,  width = 5, font = 14)
nhap_soluong.pack()
nhap_soluong.place(x = 10, y = 80)

luong_thuc2 = Label (hoangdz, text = "Nước ngọt/Bia (lon)", font = ("Arial", 14 ), fg = "black")
luong_thuc2.pack()
luong_thuc2.place(x = 10, y = 130)
nhap_soluong2 = Entry (hoangdz, width = 5, font = 14)
nhap_soluong2.pack()
nhap_soluong2.place(x = 10, y = 160)

luong_thuc3 = Label (hoangdz, text = "Trái Cây (kg)", font = ("Arial", 14 ), fg = "black")
luong_thuc3.pack()
luong_thuc3.place(x = 10, y = 210)
nhap_soluong3 = Entry (hoangdz, width = 5, font = 14)
nhap_soluong3.pack()
nhap_soluong3.place(x = 10, y = 240)

luong_thuc4 = Label (hoangdz, text = "Bánh kẹo (hộp/túi)", font = ("Arial", 14 ), fg = "black")
luong_thuc4.pack()
luong_thuc4.place(x = 10, y = 290)
nhap_soluong4 = Entry (hoangdz, width = 5, font = 14)
nhap_soluong4.pack()
nhap_soluong4.place(x = 10, y = 320)

tong_tien = Label (hoangdz, text = "Tổng số tiền hàng(đ)", font = ("Arial", 14), fg = "Red")
tong_tien.pack()
tong_tien.place (x = 400, y = 70 )
nhap_tien = Label(hoangdz, text = "",font = ("Arial", 14), fg = "Red")
nhap_tien.pack()
nhap_tien.place(x = 450, y = 100)

gia1 = Label (hoangdz, text = "13000", font = ("Arial", 14), fg = "Red")
gia1.pack()
gia1.place (x = 80, y = 80 )
gia2 = Label (hoangdz, text = "10000", font = ("Arial", 14), fg = "Red")
gia2.pack()
gia2.place (x = 80, y = 160 )
gia3 = Label (hoangdz, text = "20000", font = ("Arial", 14), fg = "Red")
gia3.pack()
gia3.place (x = 80, y = 240 )
gia4 = Label (hoangdz, text = "40000", font = ("Arial", 14), fg = "Red")
gia4.pack()
gia4.place (x = 80, y = 320 )

button1 = Button (hoangdz, text = "Xuất hóa đơn", font = ("Arial", 14), bg = "Yellow", fg = "Black", command = xuathoadon)
button1.pack ()
button1.place (x = 400, y = 270)

button2 = Button (hoangdz, text = "Thoát", font = ("Arial", 14), bg = "Pink", command = thoat )
button2.pack()
button2.place(x = 730, y = 360)

button3 = Button (hoangdz, text = "Tính", font = ("Arial", 14), bg = "Pink", command = tinhtoan)
button3.pack()
button3.place(x = 310, y = 60)


hoangdz.mainloop()