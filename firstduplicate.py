def firstDuplicate(a):
	first_duplicate = -1
	dict_num = {a[0]: 1}
	dict_append = {}

	for count in range(1,len(a)):

		if a[count] in dict_num:
			dict_num[a[count]] += 1
		else:
			dict_append = {a[count]: 1}
			dict_num.update(dict_append)

		if dict_num[a[count]] == 2:
			first_duplicate = a[count]
			break
		elif count == len(a) - 1:
			continue

	return first_duplicate
