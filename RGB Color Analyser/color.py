color = input("Enter a (R,G,B): ")

color = list(int(x.strip()) for x in color.split(','))
R, G, B = color

for i in color:
    i = hex(i)

luma = (R * 0.2126) + (G * 0.7152) + (B * 0.0722)

if luma < 128:
    print("The color is Dark")
elif luma >=128:
    print("The color is light")
else:
    print("invlid input")