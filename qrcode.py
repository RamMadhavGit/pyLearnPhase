import pyqrcode
s = "Hello"
url = pyqrcode.create(s)
url.png("hy.png", scale=8)