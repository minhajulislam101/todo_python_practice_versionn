contents = ["a.txt","b.txt","c.txt","d.txt"]

for content in contents:
    file = open(content,'r')
    filenames = file.read()
    print(filenames)