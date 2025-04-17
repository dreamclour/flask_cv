# longlonglonglong
# 读取文件并解析16进制数据
import sys
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
file_path='C:/Users/49860/Desktop/11.txt'
rgb_data = []
imagee=np.zeros((200,320))
bianma=np.zeros((1,64000))
def read_hex_from_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            # 按空格分割每一行的16进制字符串
            hex_values = line.strip().split()
            #print(np.size(hex_values))
            for i in range(1,np.size(hex_values),2):
              high_byte = int(hex_values[i],16)  # 高8位,应该是这样
              low_byte = int(hex_values[i-1],16)  # 低8位
              combined_16bit = (high_byte << 8) | low_byte

              r1 = combined_16bit >> 11
              r1 = r1 << 3
              g1 = (combined_16bit >> 5) & 0x3F
              g1 = g1 << 2
              b1 = (combined_16bit) & 0x1F
              b1 = b1 << 3

              # b2 = combined_16bit >> 11
              # b2 = b2 << 5
              # r2 = (combined_16bit >> 5) & 0x3F
              # r2 = r2 << 2
              # g2 = (combined_16bit) & 0x1F
              # g2 = g2 << 3
              #
              # g3 = combined_16bit >> 11
              # g3 = g3 << 5
              # b3 = (combined_16bit >> 5) & 0x3F
              # b3 = b3 << 2
              # r3 = (combined_16bit) & 0x1F
              # r3 = r3 << 3
              #
              # r_arg = (r1 + r2 + r3)/3
              # g_arg = (g1 + g2 + g3)/3
              # b_arg = (b1 + b2 + b3)/3

              r_arg = r1
              g_arg = g1
              b_arg = b1

              rgb_data.append((r_arg, g_arg, b_arg))
              #print(rgb_data)

              normalized_value = int((combined_16bit / 65535) * 255)  # 归一化到0-255

              bianma[0,int(i/2)]=normalized_value
            print(max(bianma[0]))
            rgb_array = np.array(rgb_data, dtype=np.uint8).reshape((200, 320, 3))
            image = Image.fromarray(rgb_array, mode='RGB')
            image.save('C:/Users/49860/Desktop/rgb_image2.png')
            imagee = np.reshape(bianma, (200, 320))
            #print(bianma)

            # gray_image = Image.fromarray(imagee, mode='L')  # 'L' 表示灰度模式
            # gray_image.save('C:/Users/49860/Desktop/gray_image.png')
            plt.imshow(imagee, cmap='gray')  # 'L' 表示灰度模式
            plt.show()
            #plt.savefig("C:/Users/49860/Desktop/minist.png")
    return 0

# 示例文件路径
read_hex_from_file(file_path)


















