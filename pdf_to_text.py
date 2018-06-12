import PyPDF2
newfile2=open('hello2.txt','w')
file=open('JavaBasics-notes.pdf','rb')
pdfreader=PyPDF2.PdfFileReader(file)

print(pdfreader.getNumPages())
pageobj=pdfreader.getPage(2)

newfile2.write(pageobj.extractText())

print(pageobj.extractText())

file.close()
newfile2.close()
