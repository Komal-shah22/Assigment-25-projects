import qrcode as qr
image = qr.make("https://github.com/Komal-shah22")
image.save("github.png")