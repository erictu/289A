import numpy as np
import itertools
		
		
		
		
for k in [5,7,10,12,15]:
#for k in [5]:
	cluster_dicts = []
	range_labels = []
	range_id = []
	for i in range(1, 11):
		cluster_dict = {}
		for j in range(200):
			num = str(j)
			zeros = '0' * (5 - len(num)) 
			with open('Cluster_Stability_Output/chr21Stable/chr21_Predictions_K' + str(k) + '_' + str(i) + '/part-' + zeros + num) as f:
				for line in f:
					line = line.replace('(', '').replace(')', '').replace('\n', '').replace(' ', '')
					line = line.split(',')
					label = int(line[1])
					range_id.append(line[0])
					cluster_dict[line[0]] = label
					range_labels.append(label)
		cluster_dicts.append(cluster_dict)	
	#print set(range_labels)
	#print len(set(range_id))
	cost = 0.0
	combos = itertools.permutations(range(0, 10), 2)
	#print combos
	for c in combos:
		#print c
		best = 1000000000000000.0
		d1 = cluster_dicts[c[0]]
		d2 = cluster_dicts[c[1]]
		#print len(d1)
		#print len(d2)
		s1 = set(d1.keys())
		s2 = set(d2.keys())
		#print len(s1)
		#print len(s2)
		#print len(s1)
		#print len(s2)
		n_points = s1 & s2
		#print len(n_points)
		if len(n_points) == 0:
			continue
		#print len(n_points)
		for i in range(k):
			label_map = {}
			offset = i
			for j in range(k):
				label_map[j] = j + offset
				if label_map[j] > k - 1:
					label_map[j] = label_map[j] - k
			#print label_map
			total = 0.0
			for n in n_points:
				if d1[n] != label_map[d2[n]]:
					total += 1
			if total < best:
				best = total
		cost += best / float(len(n_points))
	instability = (1.0 / 100) * cost
	print k
	print instability

