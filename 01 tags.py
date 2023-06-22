import requests
from bs4 import BeautifulSoup

with open('sample.html', "r") as f :
    html_doc = f.read()


# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify())
# print(soup.title, type(soup.title))
# print(soup.title.string, type(soup.title.string))

# print(soup.div)  # It will give first div
# print(soup.find_all('div')) # get all the div 
# print(soup.find_all('div')[0]) 

# print(soup.find_all('a')) 
# for link in soup.find_all('a'):
#     print(link.get('href'))
#     print(link.get_text())

# s = soup.find(id="link3")
# print(s.get('href'))

# print(soup.select("div.italic")) # will give all the div with class italic
# print(soup.select("span#italic"))
# print(soup.span.get('class'))

# print(soup.find(class_="italic"))
# print(soup.find_all(class_="italic"))


# for child in soup.find(class_="container").children:
#     print(child)

# for parent in soup.find(class_="box").parents:
#     print(parent)


####### Modify the existing tags #######
'''
cont = soup.find(class_="container")
cont.name = "span"
cont["class"] = "myclass class"
cont.string = "I am converted to a span tag"
print(cont)
'''


####### Insert the new tag #######
'''
# Create a new <ul> tag
new_ul = soup.new_tag('ul')

# Create new <li> tags and add them to the <ul> tag
new_li1 = soup.new_tag('li')
new_li1.string = 'Home'
new_ul.append(new_li1)

new_li2 = soup.new_tag('li')
new_li2.string = 'About'
new_ul.append(new_li2)

soup.html.body.insert(0, new_ul)
with open("modified.html", "w") as f:
    f.write(str(soup))
'''


# cont = soup.find(class_="container")
# print(cont.has_attr("class"))

def has_class_but_not_id(tag):
    return tag.has_attr("class") and not tag.has_attr("id")

results = soup.find_all(has_class_but_not_id)
for result in results : 
    print(result, "\n\n")