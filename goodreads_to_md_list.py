#!/usr/bin/python3

import requests
import xml.etree.ElementTree as ET

# URL that needs to be GET
url = "https://www.goodreads.com/review/list?v=2"

# params that should go with the URL
parameters = {
    "id" : "37688006-aleksandar-todorovi",
    "shelf" : "read",
    "sort" : "date_read",
    "order" : "a",
    "per_page" : 200,
    "key" : "<API_KEY_GOES_HERE>"
}

# make a GET request
r = requests.get(url, params=parameters)

# parse XMl
root = ET.fromstring(r.text)

# XML Structure:
# <GoodreadsResponse>
#   <reviews>
#     <review>
#       <book>
#         <isbn13>XXXXXXXXXXXX</isbn13
#         <title_without_series>title</title_without_series>
#         <authors>
#           <author>
#             <name>Jon Doe</name>
#           </author>
#         </authors>
#       </book>
#       <rating>
#         <stars>5</stars>
#       </rating>
#     </review>
#   </reviews>
# </GoodreadsResponse>
f = open('00_books.md', 'w')

f.write("# Books\n\n> After all any book is just a list of thoughts of another guy, who might be wrong.\n\nThis file is the exported version of my [Goodreads `read` shelf](https://www.goodreads.com/review/list/37688006-aleksandar-todorovi?shelf=read), synced using my [`goodreads_to_md_list.py`](https://github.com/aleksandar-todorovic/automation-scripts#goodreads_to_md_listpy) script. Having a Git backup prevents me from feeling that I might be vendor-locked-in, even though it's just a freaking list of books that I could probably re-create.\n\nThe books below are in order of me marking them as read on Goodreads, from oldest to newest. The stars are my subjective opinion of the book on the scale from one to five.\n\nFormat: ``* `author_name` book_title (rating) [[isbn13](link_to_goodreads)]``\n\n## Books I have read\n\n")

for review in root.find('reviews'):
    book = review.find('book')
    title = book.find('title_without_series').text
    authors = book.find('authors')
    author = authors.find('author')
    name = author.find('name').text
    stars_int = review.find('rating').text
    stars_str = ""
    i = 0
    while i < 5:
        if i < int(stars_int):
            stars_str = stars_str + "★"
        elif i == int(stars_int) or i > int(stars_int):
            stars_str = stars_str + "☆"
        i = i + 1
    isbn = book.find('isbn13').text
    link = book.find('link').text
    f.write("* `" + name + "` " + title + " (" + stars_str + ") [[" + str(isbn) + "](" + link + ")]\n")

f.close()
