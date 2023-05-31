
#!-------------------------------------------------------------------------------------------------------------------------------------
#%                                                      PATTERN PROGRAM
#!-------------------------------------------------------------------------------------------------------------------------------------
## Example-1

#%  * * * * * 
#%  * * * * * 
#%  * * * * * 
#%  * * * * * 
#%  * * * * * 
'''
for i in range(1,6):
    for i in range(1,6):
        print('*',end=' ')
    print()
'''






## Example-2

#%  1 1 1 1 1 
#%  2 2 2 2 2
#%  3 3 3 3 3
#%  4 4 4 4 4
#%  5 5 5 5 5
'''
dummy=1
for i in range(1,6):
    for j in range(1,6):
        print(dummy,end=' ')
    dummy+=1
    print()
'''






## Example-3

#%  1 1 1 1 1 
#%  3 3 3 3 3
#%  5 5 5 5 5
#%  7 7 7 7 7
#%  9 9 9 9 9
'''
dummy=1
for i in range(1,6):
    for j in range(1,6):
        print(dummy,end=' ')
    dummy+=2
    print()
'''






## Example-4

#%  1 2 3 4 5 
#%  1 2 3 4 5
#%  1 2 3 4 5
#%  1 2 3 4 5
#%  1 2 3 4 5
'''
for i in range(1,6):
    dummy=1
    for j in range(1,6):
        print(dummy,end=' ')
        dummy+=1
    print()
'''






## Example-5

#%  1 2 3 4 5 
#%  6 7 8 9 10
#%  11 12 13 14 15
#%  16 17 18 19 20
#%  21 22 23 24 25
'''
dummy=1
for i in range(1,6):
    for j in range(1,6):
        print(dummy,end=' ')
        dummy+=1
    print()
'''





## Example-6

#%  A A A A A 
#%  B B B B B
#%  C C C C C
#%  D D D D D
#%  E E E E E
'''
dummy=65
for i in range(1,6):
    for j in range(1,6):
        print(chr(dummy),end=' ')
    dummy+=1
    print()
'''






## Example-7

#%  A B C D E 
#%  A B C D E
#%  A B C D E
#%  A B C D E
#%  A B C D E
'''
for i in range(1,6):
    dummy=65
    for j in range(1,6):
        print(chr(dummy),end=' ')
        dummy+=1
    print()
'''





## Example-8

#%  A B C D E 
#%  F G H I J
#%  K L M N O
#%  P Q R S T
#%  U V W X Y
'''
dummy=65
for i in range(1,6):
    for j in range(1,6):
        print(chr(dummy),end=' ')
        dummy+=1
    print()
'''


























