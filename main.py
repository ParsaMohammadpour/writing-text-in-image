from PIL import Image, ImageDraw, ImageFont

image = Image.open('image.jpg')
image.show()

draw = ImageDraw.Draw(image)
text = 'Parsa Mohammadpour - {student_id}'

font = ImageFont.truetype('arial.ttf', 40)

width, height = image.width/2, image.height/2

draw.text((width, height), text, font=font, anchor="mm", fill=(255,0,0))

image.show()
image.save('Result.jpg')
