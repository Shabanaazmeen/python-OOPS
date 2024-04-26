#def reverse_string(string):
  #  return string[::-1]
#string=input('enter the string')
#reversestring=reverse_string(string)
#print(reverse_string(string))
def count_vowels(string):
    string = string.lower()
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for char in string:
        if char in vowels:
            count=count+1
        return count
string=(input('enter the element' ))  
print(count_vowels(string))  