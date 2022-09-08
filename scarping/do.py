from re import search

url = "https://www.javatpoint.com/"
a=['https://www.javatpoint.com/python-tutorial','https://www.javatpoint.com/python-data-types','https://www.javatpoint.org/',
   'https://www.geeksforgeeks.org/','https://www.geeksforgeeks.co/','https://www.geeksforgeeks.com/','https://app.planmans.com/']
#
# if any("javatpoint" in word for word in a):
#
#
#
# else:
#     print("no")
# ab=[]
# ab1=[]
#
# if any(url in word for word in a):
#     print("yes")
# else:
#     print("no")



# filter_object = filter(lambda ab: url in ab, a)
#
# # Convert the filter object to list
# print(list(filter_object))



# if url in a:
#     print(f'{url} is present in the list')
# else:
#     print(f'{url} is not present in the list')


# for i in a:
#     if i.__contains__(url) :
#         print(i, " is containing "+url)
internals = []
externals = []
for links in a:
    if url in links:
        print(links, "----> ", "Internal")
        internals.append(links)
    else:
        print(links, "----> ", "External")
        externals.append(links)
print(internals)
print(externals)