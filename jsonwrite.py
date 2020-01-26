#This script converts the JSON for an HTRC collection's metadata into a an array that can then be dumped into individual json files that are named based on the htitem_id from the metadata

#import the necessary packages
import json
#import re

#identify and open the json file - this should be the file that you download from your collection page on HTRC
filename = 'HTRCFull.json'
with open(filename) as f:
    fulljson = json.load(f)

#Double check the number of items in the collection
all_text_dicts = fulljson['texts']
#print('The number of HTRC items in this collections is:')
#print(len(all_text_dicts))


#Create an array for each of the pieces of metadata and pass the elements from the JSON into a python array and split the title, date, and htitem_id elements
titles, mags, vols, authors, dates, years, rights, oclcs, lccns, isbns, catalog_urls, htitem_ids, htreference_ids = [], [], [], [], [], [], [], [], [], [], [], [], []
for text_dict in all_text_dicts:
    title = text_dict['title']
    new_title = title.split(". ", 1)
    mag = new_title[0]
    vol = new_title[1]
    author = text_dict['author']
    date = text_dict['date']
    full_date = date.split('-', 1)
    year = full_date[0]
    right = text_dict['rights']
    oclc = text_dict['oclc']
    lccn = text_dict['lccn']
    isbn = text_dict['isbn']
    catalog_url = text_dict['catalog_url']
    htitem_id = text_dict['htitem_id']
    new_id = htitem_id.split(".", 1)
    htreference_id = new_id[1]
    titles.append(title)
    mags.append(mag)
    vols.append(vol)
    authors.append(author)
    dates.append(date)
    years.append(year)
    rights.append(right)
    oclcs.append(oclc)
    lccns.append(lccn)
    isbns.append(isbn)
    catalog_urls.append(catalog_url)
    htitem_ids.append(htitem_id)
    htreference_ids.append(htreference_id)

#define the python dictionary

#print the first five items in each array to spot check
spot_check=input("Would you like a spot check of the first five objects? y/n\n")
if spot_check == 'y':
    print('the first sets of items are:\n',
        titles[:5],'\n',
        mags[:5],'\n',
        vols[:5],'\n',
        authors[:5],'\n',
        dates[:5],'\n',
        years[:5],'\n',
        rights[:5],'\n',
        oclcs[:5],'\n',
        lccns[:5],'\n',
        isbns[:5],'\n',
        catalog_urls[:5],'\n',
        htitem_ids[:5],'\n',
        htreference_ids[:5])
else:
    print("Ok.")

print(text_dict)
#dump to individual json files that are named based on the hathitrust ids
n=0
while n < len(all_text_dicts):
    text_dict[n] = {
        'title': titles[n],
        'mag': mags[n],
        'vol': vols[n],
        'author': authors[n],
        'date': dates[n],
        'year': years[n],
        'rights': rights[n],
        'oclc': oclcs[n],
        'lccn': lccns[n],
        'isbn': isbns[n],
        'catalog_url': catalog_urls[n],
        'htitem_id': htitem_ids[n],
        'htreference_id': htreference_ids[n]
    }
    with open(f'New_jsons/{htreference_ids[n]}.json', 'w', encoding='utf-8') as j:
        json.dump(text_dict[n], j, ensure_ascii=False, indent=4)
    n += 1
