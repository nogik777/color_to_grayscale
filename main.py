from PIL import Image


image = Image.open('test.jpg')
baw = image.convert('L')
baw.save('Gray.jpg')



