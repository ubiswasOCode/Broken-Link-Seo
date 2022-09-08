url="https://www.w3schools.com"
import metadata_parser
import requests

from bs4 import BeautifulSoup

page=metadata_parser.MetadataParser(url)
# print(page.metadata)
title=page.get_metadata('title')
print(title)
print()

ab=page.get_metadata('title')
print("Congratulations your webpage is using a title tag.")
print(page.get_metadata('title'))
print()
print()

ab1=page.get_metadata("description")
if ab1 is None:
    print("No Desc")
elif len(ab1) >= 160:
    print(f"Title should be Greater than 160 characters {len(ab1)}  characters")
else:
    print(f"title is smaller than 160 characters {len(ab1)}characters")
print(page.get_metadata('description'))
print()
print()


ab2=page.get_metadata("keywords")

print(page.get_metadata("keywords"))
print()
print()

request = requests.get(url)

Soup = BeautifulSoup(request.text, 'lxml')

# creating a list of all common heading tags
heading_tags = ["h1", "h2", "h3"]
for tags in Soup.find_all(heading_tags):
    print(tags.name + ' -> ' + tags.text.strip())


##For Images

images = Soup.findAll('img')
for image in images:
    images = []
    for img in Soup.findAll('img'):
        images.append(img.get('src'))

    print(images)


##Style Tags
style_tags = ["style"]
for tags in Soup.find_all(style_tags):
    taggg=tags.name + ' -> ' + tags.text.strip()
    print("total Style Tags is", len(taggg))

##Underscore
a=[]
for link in Soup.find_all('a'):
    under=link.get('href')
    if "_" in under:
        a.append(under)
        print("Check",a)




