from sys import argv

filename = "111.txt"
#读写操作
print(f"我们要读写的文件是{filename}")
print("你如果不想这样可以CTRL-C (^c).")
print("if you do want that , hit return(如果你想要这个 回车).")

input("?")

print("opening the file.....(打开文件)")
target = open(filename,'r+')

print("truncating thr file . goodbye(截断这个文件 再见)")
target.truncate()

print("now i'm going to ask you for three lines(现在我要问你三行)")

line1 = input("line1")
line2 = input("line2")
line3 = input("line3")

print("i'm going to write  these to the file(我去写道文件中).")
target.write(line1+'\n'+line2+'\n'+line3+'\n')

print( "and finally ,we close it(最后,我们现在把他关闭)")
str = open(filename)

target.close()

print(str.read())