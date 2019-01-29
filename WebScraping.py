# in command shell:
# virtualenv -p python InsertTitle
# cd InsertTitle
# .\\Scripts\activate
#pip install requests beautifulsoup4
import requests
from bs4 import BeautifulSoup

base_url = "https://www.yelp.com/search?find_desc=Restaurants&find_loc="
loc = "New York,NY"
page = 0
current_page = 0
url = base_url + loc + "&start=" + str(page)

yelp_r = requests.get(url)

# yelp_r -- <Response 200>

print(yelp_r.status_code) #200

yelp_soup = BeautifulSoup(yelp_r.text, "html.parser")


print(yelp_soup.prettify())

print(yelp_soup.findAll("a"))

for link in yelp_soup.findAll("a"):
	print(link) #finding all links

print(yelp_soup.findAll("li", {"class": "regular-search-result"}))

print(yelp_soup.findAll("a", {"class": "biz-name"}))

for name in yelp_soup.findAll("a", {"class": "biz-name"}):
	print(name.text) #getting just the name

businesses = yelp_soup.findAll("div", {"class": "biz-listing-large"})
for biz in businesses:
	title = biz.findAll("a", {"class":"biz-name"})[0].text
	print(title)

	address = biz.findAll("address")[0].text
	print(address)
	print("\n")
	phone = biz.findAll("span", {"class", "biz-phone"})[0].text
	print(phone)

file_path = "yelp-{loc}.text".format(loc = loc)

# make text doc listing
with open(file_path, "a") as textfile:
	businesses = yelp_soup.findAll("div", {"class": "biz-listing-large"})
	for biz in businesses:
		title = biz.findAll("a", {"class":"biz-name"})[0].text
		print(title)

		address = biz.findAll("address")[0].text
		print(address)
		print("\n")
		phone = biz.findAll("span", {"class", "biz-phone"})[0].text
		print(phone)
		page_line = "{title}\n{address}\n{phone}\n\n".format(
			title = title,
			address = address,
			phone = phone
			)
		textfile.write()

while current_page < 201:
	url = base_url + loc + "&start=" + str(current_page)
	yelp_r = requests.get(url)
	yelp_soup = BeautifulSoup(yelp_r.text, "html.parser")
	businesses = yelp_soup.findAll("div", {"class": "biz-listing-large"})
	file_path = "yelp-{loc}.text".format(loc = loc)
	with open(file_path, "a") as textfile:
		businesses = yelp_soup.findAll("div", {"class": "biz-listing-large"})
		for biz in businesses:
			title = biz.findAll("a", {"class":"biz-name"})[0].text
			print(title)
			second_line = ""
			first_line = ""
			try:
				address = biz.findAll("address")[0].contents

				for item in address:
					if "br" in str(item):
						second_line += item.getText().strip(" \n\tr")
					else:
						first_line = item.strip(" \n\tr")
				print(first_line)
				print(second_line)
			except:
				pass
			print("\n")
			
			try:
				phone = biz.findAll("span", {"class", "biz-phone"})[0].getText().strip(" \n\t\r")
			except:
				phone = None
			print(phone)
			page_line = "{title}\n{address}\n{address_1}\n{address_2}\n{phone}\n\n".format(
				title = title,
				address_1 = first_line,
				address_2 = second_line,
				phone = phone
				)
			textfile.write()
	current_page += 10
