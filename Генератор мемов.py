from PIL import Image, ImageDraw, ImageFont

print("Генератор мемов запущен!")

memes = ["cat_in_restaurant.png", "cat_with_glasses.png"]
text_type = int(input("Введите 1, если нужен только нижний текст, и 2, если и верхний, и нижний: "))


top_text = ""
bottom_text = ""
if text_type == 1:
    bottom_text = input("Введите нижний текст: ")
elif text_type == 2:
    top_text = input("Введите верхний текст: ")
    bottom_text = input("Введите нижний текст: ")
else:
    print("Введен неправильный режим. Перезапустите программу")
    quit()

print(top_text, bottom_text)

image = Image.open("cat_with_glasses.png")
width, height = image.size

draw = ImageDraw.Draw(image)

font = ImageFont.truetype('arial.ttf', size=70)

text = draw.textbbox((0, 0), top_text, font)
draw.text(((width - text[2]) / 2, 10), top_text, font=font, fill="black")

draw.text(((width - text[2]) / 2, (height - text[3] - 10)), bottom_text, font=font, fill="black")

image.save("new_meme.jpg")
#Конец!
