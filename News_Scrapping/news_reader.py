from bs4 import BeautifulSoup
import requests

# Get all inputs from users
while True:
	try:
		election = int(input('Select "1" if you want the information printed on console or select "2" if you want it exported to an html file: '))
		if election not in [1,2]:
			print('Sorry, only option 1 or option 2 are allowed')
			continue
	except ValueError:
		print('You did not select a number. Please try again')
		continue
	else:
		break

filter_words = input('Write the word or phrase you are looking for on the titles. Otherwise, press enter to continue without filtering: ')

# Here starts the script

x = requests.get('https://www.ambito.com/')

soup = BeautifulSoup(x.text, 'html.parser')

all_titles = soup.find_all(['h1', 'h2'], class_='title')

#base functions for election 1, to avoid repeating code

def election_1(title_arg):
	print("-", title_arg.text)
	link = title_arg.find('a')
	print(link.get('href'))
	print("")

if election == 1:
	filtered = False
	for title in all_titles:
		if filter_words and (filter_words in title.text):
			election_1(title)
			filtered = True
		elif filter_words == "":
			election_1(title)
	if filter_words and (filtered == False):
		print('Nothing found with that filter :(')

elif election == 2:
	filtered = False
	with open('noticias_del_dia.html', 'w') as list_of_links:
		list_of_links.write('<!DOCTYPE html><html><head><title>Noticias del día</title></head><body>')
		for title in all_titles:
			if filter_words and (filter_words in title.text):
				list_of_links.write(str(title))
				filtered = True
			elif filter_words == False:
				list_of_links.write(str(title))
		if filter_words and (filtered == False):
			print('Nothing found with that filter :(')
		list_of_links.write('</body></html>')

print('All done!')
