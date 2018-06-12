from rake_nltk import rake


#from nlp_rake import rake
filenames = ['D:\\Upasna\\Data Science\\stopwords.txt','D:\\Upasna\\Data Science\\hello2.txt']

#stoppath = 'D:\\Upasna\\Data Science\\stopwords.txt'

rake_object = rake.Rake(stoppath, 5, 3, 4)

#sample_file = open("D:\\Upasna\\Data Science\\hello2.txt", 'r')
#text = sample_file.read()

for hello2 in filenames:
	with open(hello2,'r') as fp:
		results[hello2] = rake_object.run(fp.read())

#keywords = rake_object.run(text)

#  print results
print("Keywords:", results)
