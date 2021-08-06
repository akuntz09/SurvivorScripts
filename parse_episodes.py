import glob
import matplotlib.pyplot as plt
import string

terms = ['idol', 'advantage']
counts = [[] for term in terms] 
seasons = range(1, 41)
for i in range(1, 41):
	episodes = glob.glob("episodes/"+str(i)+"-*.txt")
	termCounts = [0] * len(terms)
	for e in episodes:
		f = open(e, 'r')	
		read_data = f.read().lower().replace('<br>','').translate(str.maketrans('', '', string.punctuation))
		for j in range(len(terms)):
			termCounts[j] += read_data.count(terms[j])
		f.close()
	for k in range(len(terms)):
		counts[k].append(termCounts[k])
for i in range(len(counts)):
	plt.plot(seasons, counts[i], label = terms[i])
plt.xlabel("Season")
plt.ylabel("Count")
plt.legend()
plt.show()






