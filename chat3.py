lines = []
with open("3.txt", 'r', encoding = "utf-8-sig") as f :
	for line in f:
		lines.append(line.strip())

for line in lines:
	s= line.split(' ')
	time = s[0][:5] #结束值不包含
	name = s[0][5:] #开始值包含
	print(time)
	print(name)