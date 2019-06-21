import numpy as np


def compute_med(s1, s2, ins_cost=1, del_cost=1, sub_cost=1):
	'''
	Compute the minimum edit distance (MED) between string 1 (s1) and
	string 2 (s2)
	'''
	target = s1 
	source = s2
	target_len = len(target)+1 # num cols
	source_len = len(source)+1 # num rows
	matr = np.zeros((source_len, target_len))
	matr[0,0] = 0 

	# initialize first row and first column
	for row in range(matr.shape[0]):
		matr[row,0] = row
	for col in range(matr.shape[1]): 
		matr[0,col] = col 

	# fill in the rest of the table
	for row in range(1,source_len): 
		for col in range(1,target_len):
			ins_dist = matr[row, col-1] + ins_cost
			del_dist = matr[row-1, col] + del_cost
			if source[row-1] == target[col-1]:
				sub_dist = matr[row-1, col-1]
			else:
				sub_dist = matr[row-1, col-1] + sub_cost
			dist = min([ins_dist, del_dist, sub_dist])
			matr[row,col] = dist

	print(matr)
	med = matr[source_len-1, target_len-1]
	return med 


def main():
	s1 = 'honda'
	s2 = 'hyundai'
	med = compute_med(s1, s2)
	print(med)


if __name__=="__main__":
	main()
