#put an input prompt then save it into name variable
name = input("Enter file:")

#filter if length of name is < 1, name will automatic to mbox-short.txt
if len(name) < 1 : name = "mbox-short.txt"
    
#variable handle for file handler for the file name
handle = open(name)

#set empty constructor of dictionary as count, final
count = dict()
final = dict()

#create a storage with none value and empty string
storage = None
storageKey = ""

#apply definite loop to read the lines inside handle
for lines in handle:
    
    #filter the lines only that has From:
    if lines.startswith("From:"):
        #print(lines.split()[1])
        
        #storage as key of count and the value itterated by 1
        count[lines.split()[1]] = count.get(lines.split()[1],0) + 1
        
#apply definite loop for key and value pair for the items inside count
for key,value in count.items(): 
    
    #filter the largest 
    if value > storage or value is None :
        
        #manipulate the storage from global
        storage = value
        storageKey = key
        
#print the value of the storageKey and storage
print(storageKey,storage)
        