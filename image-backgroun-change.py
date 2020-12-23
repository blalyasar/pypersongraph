from PIL import Image
img = Image.open("person_white.jpg")
img = img.convert("RGB")

datas = img.getdata()

# gold:255,215,0
# green:0,128,0
# pink :255,192,203
# purple : 128,0,128
# red: 255,0,0
# yellow:255,255,0
# black : 00
# blue : 0,0,255
new_image_data = []
for item in datas:
    # change all white (also shades of whites) pixels to yellow
    if item[0] in list(range(1,256)):
        new_image_data.append(( 255,255,255))
    else:
        new_image_data.append(item)
        
# update image data
img.putdata(new_image_data)

# save new image
img.save("person_white1.jpg")

# show image in preview
img.show()
