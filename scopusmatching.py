from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import csv
import pickle

editorshiplist=[]
matches=[]

with open('editorships.csv', 'r') as editorshipscsv:
    editorshipsdata=csv.reader(editorshipscsv, delimiter=',')
    for row in editorshipsdata:
        #print(row)
        editorshiplist.append(row[0])
    #print(editorshiplist)


with open('scopus.csv', 'r') as scopuscsv:
    scopusdata = csv.reader(scopuscsv, delimiter=',')
    for row in scopusdata:
        row.append(process.extract(row[1], editorshiplist, limit=2))
        print(row)
        pickle.dump(row, open('results.pkl', 'wb'))