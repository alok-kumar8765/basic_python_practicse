from PIL import Image
win=Image.open('my_computer_image.png')
type(win)
#print(win)
#win.show() #Show the image
#print(win.size)
#print(win.filename)
#print(win.format_description)

#cropping image
crp=win.crop((0,0,100,100))
#print(crp.show())

pencils=Image.open('pencils.jpg')
#pencils.show()
print(pencils.size)
'''
#now lets try to crop this image
x=0
y=0
w=1950/3
h=1300/10
crp=pencils.crop((x,y,w,h))
print(crp.show())
'''
#lets try to crop from bottom
x=0
y=1100
w=1950/3
h=1300
crp=pencils.crop((x,y,w,h))
crp.show()