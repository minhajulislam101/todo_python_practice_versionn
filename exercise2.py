filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for filename in zip(filenames):
  file =  open(f"test/{filename}",'w')
  file.writelines("Hello")