import qrcode
data = input("Please enter the data : ")
img = qrcode.make(data)
img.save("QR.png")