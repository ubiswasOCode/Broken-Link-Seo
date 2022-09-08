url="https://www.w3schools.com"
import metadata_parser
page=metadata_parser.MetadataParser(url)
# print(page.metadata)
title=page.get_metadata('title')
print(title)
print()

ab=page.get_metadata('title')
if len(ab) >= 60:
    print(f"Title should be Greater than 60 characters {len(ab)} characters")
else:
    print(f"title is smaller than 60 characters {len(ab)} characters")
print(page.get_metadata('title'))
print()
print()

ab1=page.get_metadata("description")
if ab1 is None:
    print("No Desc")
elif len(ab1) >= 60:
    print(f"Title should be Greater than 60 characters {len(ab1)}  characters")
else:
    print(f"title is smaller than 60 characters {len(ab1)}characters")
print(page.get_metadata('description'))
print()
print()


ab2=page.get_metadata("keywords")
if ab2 is None:
    print("No Keywords")
elif len(ab2) >= 60:
    print(f"Title should be Greater than 60 characters {len(ab2)}  characters")
else:
    print(f"title is smaller than 60 characters {len(ab2)}characters")
print(page.get_metadata("keywords"))
print()
print()

ab3=page.get_metadata("viewport")
if ab3 is None:
    print("No Keywords")
elif len(ab3) >= 60:
    print(f"Title should be Greater than 60 characters {len(ab3)}  characters")
else:
    print(f"title is smaller than 60 characters {len(ab3)}characters")
print(page.get_metadata("viewport"))
print()
print()

ab4=page.get_metadata("robots")
if ab4 is None:
    print("No Keywords")
elif len(ab4) >= 60:
    print(f"Title should be Greater than 60 characters {len(ab4)}  characters")
else:
    print(f"title is smaller than 60 characters {len(ab4)}characters")
print(page.get_metadata("robots"))
print()
print()

ab5=page.get_metadata("open-graph")
if ab5 is None:
    print("No graph")
elif len(ab5) >= 60:
    print(f"Title should be Greater than 60 characters {len(ab5)}  characters")
else:
    print(f"title is smaller than 60 characters {len(ab5)}characters")
print(page.get_metadata("open-graph"))
