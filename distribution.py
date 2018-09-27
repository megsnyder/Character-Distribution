"""
distribution.py
Author: Meg
Credit: Noah

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
import string
text = input("Please enter a string of text (the bigger the better): ")
lower = (text).lower()
letters = list(lower)
y=0
z=0
n=0
m=1
b=0
allletters = list(string.ascii_lowercase)
number = []
newlett = []
ordlett = []
for i in allletters:
    x=0
    a=0
    for i in letters:
        if letters[x]==allletters[y]:
            a+=1
            newlett.append(allletters[y])
            number.append(a)
        x+=1
    y+=1
for i in newlett:
    if newlett[n]==newlett[m]:
        newlett.pop(m)
        number.pop(m)
        m+=1
    n+=1

tuples = list(zip(number, newlett))
print(tuples)

def compare(a, b):
    """
    compare - generic comparison function for testing two elements.
    """
    return b[0] < a[0]


def bsort(seq, cmp):
    """
    bsort - simple sorting algorithm that uses any comparison function
    seq - a list to be sorted
    cmp - a function for comparing two elements of seq
    """
    sorted = False  # assume the seq is not sorted to start with
    while not sorted:
        sorted = True   # assume it's already sorted correctly
        for index, value in enumerate(seq): # for every element in seq
            if index > 0:                   # past the first..
                if not cmp(seq[index-1], value):  # if this element is out of order
                    sorted = False          # then the list is not sorted yet
                    seq[index-1], seq[index] = seq[index], seq[index-1] # and swap it

    
bsort(tuples, compare)
set1=tuples[b]
for i in tuples:
  print(set1[0]*set1[1])
  b+=1
  set1=tuples[b]


