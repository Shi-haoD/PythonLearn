from sys import argv

scricpt, input_file = argv


def print_all(f):
	print(f.read())


def rewind(f):
	f.seek(0)


def print_a_line(line_count, f):
	print(line_count, "this is ", f.readline())


current_file = open(input_file)

print("First let's rewind , kind of like a tape:倒退回去\n")
print_all(current_file)
print("now let's rewind ,kind of like a tape ")
rewind(current_file)
print("let's print three lines:")
curren_line = 1
print_a_line(curren_line, current_file)
curren_line = curren_line + 1
print_a_line(curren_line, current_file)
curren_line = curren_line + 1
print_a_line(curren_line, current_file)
