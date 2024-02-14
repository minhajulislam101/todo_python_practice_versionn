member = input("Add a New Member :")

file = open('member.txt','r')
old = file.readlines()
file.close()
old.append(member+"\n")

file = open('member.txt','w')
old =file.writelines(old)
file.close()




