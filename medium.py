"""
WORD COUNT
==========
In this section, we are going to implement a word count program that takes a string and counts the number of times each word appears. 

You will take a sentence (string input) from the user using the input() function and count the number of times each word appears. 

You will print each word, followed by a colon (:), and the number of times it appears in the string. Your output should take the following format: 

word: count

For example, the following sample input: 

"my cat is a tabby cat"

Should result in the following output: 

my: 1
cat: 2
is: 1
a: 1
tabby: 1

"""

# Here is some starter code. =)

def main():
  print("Please enter a string: ")
  s = input()
  print("You entered: " + s)
