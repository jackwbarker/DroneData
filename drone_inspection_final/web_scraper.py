import urllib.request
import urllib
import time

from bs4 import BeautifulSoup

website = "https://data.mendeley.com"

with urllib.request.urlopen('https://data.mendeley.com/datasets/hd96prn3nc/2') as response:
    html = response.read()

soup = BeautifulSoup(html, "html.parser")

image_list = soup.findAll("div", {"class":"filelist-file-actions"})
file_names = []

for wrapper in soup.findAll("div", {"class":"filelist-file-actions"}):
	anchors = wrapper.findAll("a")
	for a in anchors:
		file_names.append(website + a['href'][:-5])
file_names = list(set(file_names))

print("Done Loading in! -- Saving Files")

counter = 0
for file in file_names:
	newName = str(counter + 1) + ".jpg"
	try:
		urllib.request.urlretrieve(file, newName)
	except:
		print("Error Ocurred -- Moving onto next image")
		time.sleep(5)
		try:
			urllib.request.urlretrieve(file, newName)
			print("Success")
		except:
			print("No Success: " , file, "Count: ", count)

	counter += 1
	print("Progress: ", (counter*100)/len(file_names))