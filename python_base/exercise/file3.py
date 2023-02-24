from sys import argv
from os.path import exists #

from_file = "111.txt"
tofile = "222.txt"
print(f"copying from {from_file} to {tofile}")
#从 1 复制到2
#we could do these two on one line , how?
in_file = open(from_file,encoding="utf-8")
indata = in_file.read()

print(f"the input file is{len(indata)}bytes long(输入的文件时in_file文件的长度)")

print(f"daes the output file exits? {exists(tofile)}()退出了吗")
print("ready , hit return to continue , ctrl-c to abort()点击返回继续")
input()
out_file = open(tofile,'w',encoding="utf-8")
out_file.write(indata)

print("alright,all done.")

out_file.close()
in_file.close()
