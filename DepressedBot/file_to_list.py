def file_to_list(textfile):
	result = []
	with open(textfile,'r') as file:
		for line in file:
			line=line.split()
			result.append(' '.join(line))
	return result

my_file = file_to_list('sad_words')
my_file =list(set(my_file))
print(my_file)