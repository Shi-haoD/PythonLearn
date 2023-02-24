from sys import argv

# scrpit, filename = argv
# 读操作
filename="111.txt"
txt = open(filename,encoding="utf-8")

print(f'你的文件名是{filename}:')
print(txt.read())
#
# print('再一次输入文件名:')
# file_agin = input('>')
# txt_agin = open(file_agin)
# print(txt_agin.read())
