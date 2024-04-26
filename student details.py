x=input('enter the detail')
members={'name':'sha','roll no':'32','marks':'45','result':'pass'}
members={'name':'des','roll no':'33','marks':'43','result':'pass'} 
members={'name':'efw','roll no':'34','marks':'49','result':'pass'}
members={'name':'des','roll no':'35','marks':'47','result':'pass'}
members={'name':'deh','roll no':'36','marks':'46','result':'pass'}
while True:
    if x=='nothing':
        break
    elif x in members: 
        print('name',members[name])
        print('rollno',members[rollno])
        print('marks',members[marks])
        print('result',members[result])
    else:
         print('it is not found')
   