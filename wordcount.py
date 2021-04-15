#!/usr/bin/python

from collections import Counter
from csv import reader
import re

with open('pax_all_agreements_data.csv', 'r') as read_obj:
    csv_reader=reader(read_obj)
    
    # skip header
    next(csv_reader)
    words = Counter()
    for row in csv_reader:
        # see if gewom is 1 (GeWom is field 75)
        if row[75] == '1':
            # show agt: field 7
            agt = row[7].lower()
            agt = agt.encode('ascii', errors='ignore').decode()

            # clean special chars
            table = str.maketrans(dict.fromkeys("(),."))            
            agt = agt.translate(table)

            # clean articles and non relevant words
            stopwords = ['a', 'an', 'and', 'the', 'of', 'on', 'de', 'in', 'for', 'between', 'agreement']
            final_words = [word for word in re.split("\W+", agt) if word.lower() not in stopwords]

            # remove words with less than 3 chars
            final_words = [word for word in final_words if len(word)>2]
            words += Counter(final_words)

# write to file
with open("final_words.txt", "w+t") as f:
    for k,v in words.most_common():
        f.write("{},{}\n".format(k,v))
