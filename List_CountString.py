
#count spaces
string1 = "Hello I hope you are having a nice day!"
print(string1.count(" "))
print("count of spaces in string1 is {}".format(string1.count(" ")))

#count letter 
string2 = 'aaabbbbbcc'
print(string2.count('b'))

string3 = 'Prayers'
print(list(string3))
listOne = [char for char in string3 ]
print(listOne)

#Convert from list to string
ToString = ''.join([str( e ) for e in listOne] )
print(ToString)
