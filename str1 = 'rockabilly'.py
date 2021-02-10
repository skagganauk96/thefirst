str1 = 'rockabilly'
str2 = 'rocknrolla'

result = []
str2_chars = list(str2) 

for c in str1:
	if c not in str2_chars:
		continue
	
	c_index = str2_chars.index(c)
	str2_chars.pop(c_index)
	result.append(c)


print(result)

for res in result:
	print(res)