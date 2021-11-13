from methods import *
from pymongo import MongoClient


MYURL = 'http://127.0.0.1:8000/'
# Establishing connection with database
try:
	client = MongoClient('mongodb://127.0.0.1:27017/',serverSelectionTimeoutMS=8000)
	print("MongoDB connected...")
except:
	print("Could not connect to MongoDB")


# Access database
urldb = client['Shorted_URL_list']

# Access collection of the database
urllist = urldb.urls

#creating a instance of the URLShortener method
nb_shortener = URLShortener()

#using dictionary
dict_obj = {}



#Driver Code
#keep on taking input untill encounters a NULL value
while True:

	choice = int(input('\n0 to quit, \n1 to short URL  \n2 to make a search \nEnter : '))
	
	#Enter 0 to quit
	if choice == 0:
		break
	
	#Enter 1 to short URL
	elif choice == 1:
		url = input('Enter URL : ')
		short_url = nb_shortener.shortenUrl(url)
		short_url = MYURL+short_url
		#print last shorten  url
		print("Shortened URL : ",short_url)

		#updating dict after every iteration
		dict_obj[short_url] = url

		#updating db after every iteration and avoiding the chances of duplicity
		for i in range(2): 
		    dict_obj['i'] = i 
		    if '_id' in dict_obj: 
		        del dict_obj['_id'] 
		print('dict_obj',dict_obj)
		mongoUrlList = urllist.insert_one(dict_obj)
		print(mongoUrlList.inserted_id)


	#Enter 2 to make a search
	elif choice == 2:
		keyUrl = input('Enter the shortern url to get original one : ')
		org_url = urllist.find({},{keyUrl:0})
		
		for x in org_url:
			if x.__contains__(keyUrl):
				print(x[keyUrl])
				break
			
		
		

	#bad input
	else:
		print('Opps! Try again.')