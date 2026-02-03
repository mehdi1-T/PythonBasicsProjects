import qrcode

# get URL from the user
url = input("Enter URL adress: ")

# store URL into an image
img = qrcode.make(url)
img.save("qrcode.png", "PNG")