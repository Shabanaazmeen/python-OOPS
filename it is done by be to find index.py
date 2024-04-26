l=[35,27,92,47,11]
l=[int(x) for x in l ]
key=int(input('enter the key')) 
for i in l:
   if [i]==key:
    print(f"key{key}found at index{i}.")
    
else:
    print('it is not found')

