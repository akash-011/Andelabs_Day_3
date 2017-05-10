def find_max_min(num_list):
	high = max(num_list)
	low = min(num_list)
	final = [low,high]
	if low == high:
		x = len(num_list)
		return [int(d) for d in str(x)]
	else:
		return final


print find_max_min([4,4,44,4])