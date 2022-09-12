import metadata_parser
import requests

from bs4 import BeautifulSoup

url=input("Enter Url")

error={}

warning={}

page=metadata_parser.MetadataParser(url)
# print(page.metadata)

title_tag=page.get_metadata('title')
print("Congratulations your webpage is using a title tag.")

if title_tag is None:
   error['title']="titile is Missing"
   # print(error)
elif len(title_tag)>=30  and len(title_tag)<=350:
    warning['title']="titile is big"
else:
   print("titile is best")

# print(page.get_metadata('title'))
print(title_tag)
print()


desc=page.get_metadata("description")
if desc is None:
    error['description'] = "description is Missing"
elif len(desc) >= 160 :
    print(f"description should be Greater than 160 characters {len(desc)}  characters")
    warning['description'] = "description is Big"
else:
   print("description is best")

print(page.get_metadata('description'))
print()
print()


keyword=page.get_metadata("keywords")
if keyword is None:
    error['keyword'] = "keyword is Missing"
elif len(keyword) >= 10:
    warning['Keyword'] = "Keyword is huge"
else:
    print(f"Keyword is Less than 10 keywords")
print(page.get_metadata("keywords"))
print()
print()

request = requests.get(url)

Soup = BeautifulSoup(request.text, 'lxml')

# creating a list of all common heading tags
heading_tags = ["h1"]
for tags in Soup.find_all(heading_tags):
    print(tags.name + ' -> ' + tags.text.strip())

    li=(tags.name)
    li1=li.split()
    # print(li1)
    if len(li1) is None:
        error['h1'] = "h1 is Missing"
    elif len(li1) >=2:
        warning['h1'] = "h1 is huge"
    else:
        print("it h1 is Best")


#
##H2 Tags
heading2_tags = ["h2"]
for tags2 in Soup.find_all(heading2_tags):
    print(tags2.name + ' -> ' + tags2.text.strip())
    # print(tags,"---------------tags")

    convert_lst = (tags2.name)
    convert_split = convert_lst.split()
    if len(convert_split) is None:
        error['h2'] = "h2 is Missing"
    elif len(convert_split) >=2:
        warning['h2'] = "h2 is huge"
    else:
        print("h2 is Best")

##H3 Tags
heading3_tags = ["h3"]
for tags3 in Soup.find_all(heading3_tags):
    print(tags3.name + ' -> ' + tags3.text.strip())
    # print(tags,"---------------tags")

    convert_lst1 = (tags3.name)
    convert_split1 = convert_lst1.split()

    if len(convert_split1) is None:
        error['h3'] = "h3 is Missing"
    elif len(convert_split1) >= 3:
        warning['h3'] = "h3 is huge"
    else:
        print("h3 is Best")
#
# ##For Images
#
images = Soup.findAll('img')
for image in images:
    images = []
    for img in Soup.findAll('img'):
        images.append(img.get('src'))
        if len(images) is None:
            error['img'] = "img is Missing"
        elif len(images) >= 200 :
            warning['img'] = "img is huge"
        else:
            print("image is Best")
#
#
#
##Style Tags
style_tags = ["style"]
for tags in Soup.find_all(style_tags):
    taggg=tags.name + ' -> ' + tags.text.strip()

    if len(taggg) is None:
        error['style'] = "style is Missing"
    elif len(taggg) >= 100:
        warning['style'] = "style is huge"
    else:
        print("style is Best")
#
# ##Underscore
anc=[]
for link in Soup.find_all('a'):
    under=link.get('href')
    if "_" in under:
        anc.append(under)
        if len(anc) is None:
            error['a'] = "anchor tag is Missing"
        elif len(anc) >= 100:
            warning['a'] = "anchor tag is huge"
        else:
            print("anchor tag is Best")


ERR=1
WARN=0.5

err=len(error)
warn=len(warning)

case=9
temp=case


for i in range(1,err+1):
    temp=temp-ERR
    print(temp,"-------error")

for j in range(1,warn+1):
    temp=temp-WARN
    print(temp,"---------warn")

percent=(temp/case)*100
print(percent)

