import pandas as pd 
from mlxtend.preprocessing import OnehotTransactions
from mlxtend.frequent_patterns import apriori, association_rules

with open('file') as infile:
	outline = ''
	data = list()
	counter = -1
	for line in infile:
			line = line[0:-1]
			if (line != '**SOF**'):
				if (line != '**EOF**'):
					data[counter].append(line)
			else:
				data.append(list())
				counter += 1

oht = OnehotTransactions()
oht_fit = oht.fit(data).transform(data)
df = pd.DataFrame(oht_fit, columns=oht.columns_)
df = apriori(df, min_support=0.03, use_colnames=True)
print(association_rules(df, metric='confidence', min_threshold=0.03))