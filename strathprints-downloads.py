from __future__ import print_function
import csv

author_names = ['Blair, Steven MacPherson']

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

try:
    import scipy.stats as stats
except ImportError:
    stats = None

def author_stats(author_name):
    print(author_name)

    my_score = 0
    for k,v in author.iteritems():
        if author_name in k:
            my_score = v
            print('total paper downloads:', my_score)
    
    for i,(k,v) in enumerate(sorted(author.items(), key=lambda kv: (kv[1], kv[0]))):
        if k == author_name:
            print('rank:', len(author) - i, 'out of', len(author))
            break
    if stats:
        print('in top {:.0f}%, university-wide'.format(100.0 - stats.percentileofscore(all_scores, my_score)))
    print('')

# open direct link to CSV data
response = urlopen("http://strathprints.strath.ac.uk/cgi/stats/get?range=_ALL_&irs2report=main&datatype=downloads&top=authors&view=Table&title_phrase=top_authors&limit=all&export=CSV").read()
response = response.replace('=', '')

reader = csv.DictReader(response.splitlines())
author = {}

# build dict of author score, summing duplicate author names
for row in reader:
    if row['description'] in author:
        author[row['description']] = author[row['description']] + int(row['count'])
    else:
        author[row['description']] = int(row['count'])

# overall counts
print(len(author), 'authors')
all_scores = sorted([x for x in author.itervalues()])
print(sum(all_scores), 'total downloads')
print('')

for a in author_names:
    author_stats(a)