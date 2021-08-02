#!/usr/bin/python3

def adjacency_matrix(ar):
	ret = []
	for ctr, i in enumerate(ar):
		ret += [[0]*len(ar)]
		for j in i.split()[1:]:
			if j!='->':
				ret[ctr][int(j)]=1
	return ret

def print_matrix(ar):
	print(' ',*[i for i in range(len(ar))], sep='  ')
	for ctr, i in enumerate(ar):
		print(ctr, i)
if __name__== '__main__':
    st =["0 -> 1 -> 3","1 -> 0 -> 2 -> 3 -> 5 -> 6","2 -> 1 -> 3 -> 4 -> 5","3 -> 0 -> 1 -> 2 -> 4","4 -> 2 -> 3 -> 6","5 -> 1 -> 2","6 -> 1 -> 4"]
    res = adjacency_matrix(st)
    print_matrix(res)
