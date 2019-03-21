import requests


server = "http://rest.ensembl.org"
resource = "/sequence/id"
headers={ "Content-Type" : "application/json", "Accept" : "application/json"}
r = requests.post(server+resource, headers=headers, data='{ "ids" : ["ENST00000371021.4"] }')


data = r.json()
seq= data[0]['seq']


#CALCULATING THE RESULTS:
print('\n\nTHE RESULTS OF ' , data[0]['id'], ' sequence is: ')

#nº of bases in the sequence
count= len(seq)
print('\n   -The total number of bases is: ', count)

#counts
counts= {'T': seq.count('T'),
         'A': seq.count('A'),
         'C': seq.count('C'),
         'G': seq.count('G')}

#finding the most popular base and percenatge:
max = max(counts['T'], counts['A'], counts['C'], counts['G'])
for base in counts:
    if counts[base]==max:
        popular_base=base

perc_popular= (counts[popular_base]/count)*100

print('\n   -The most popular base in the sequence is', popular_base, 'and the percentage of it is: ',round(perc_popular, 2), '%')

#calculating the percentages of all bases:
for base in counts:
    perc= (counts[base]/count)*100
    print('\n   -The percentage of ', base, ' is ', round(perc, 2), '%')


