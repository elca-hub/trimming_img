from PIL import Image
import math

user_width = input('width: ')
user_height = input('height: ')

user_width = int(user_width)
user_height = int(user_height)

img = Image.open('./target.jpg')

trimming_num_width = math.floor(img.width / user_width) # 横幅で何枚切り抜けるか
trimming_num_height = math.floor(img.height / user_height) # 縦幅で何枚切り抜けるか

start_position_width = math.floor((img.width - user_width * trimming_num_width) / 2)
start_position_height = math.floor((img.height - user_height * trimming_num_height) / 2)

for x in range(trimming_num_width):
  for y in range(trimming_num_height):
    file_path = './output/output_{}_{}.jpg'.format(x, y)
    img.crop((user_width * x + start_position_width, user_height * y + start_position_height, user_width * (x + 1) + start_position_width, user_height * (y + 1) + start_position_height)).save(file_path)
