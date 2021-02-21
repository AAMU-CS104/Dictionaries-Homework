"""
The wordcount program that we did in the medium difficulty section is actually a simplified version of the linux program wc. 

You can see it in action by typing the following line in your shell or repl.it console: 

echo "my cat is a tabby cat" | wc

The output is: 
     1       6      22

This means that the string we gave it contains 1 line, 6 words, and 22 characters. 

In this file, implement the wordcount utility so that it takes in a file and counts the words inside the file. 

"""

import sys

# +++your code here+++

def print_words(filename):
  # TODO: implement a function that will read the file and count the words. 
  print("This code is not implemented yet.")
  pass

###

# This basic command line argument parsing code is provided and
# calls the print_words() function which you need to implement.
def main():
  if len(sys.argv) != 2:
    print('usage: python extra_credit.py file')
    sys.exit(1)

  filename = sys.argv[1]
  print_words(filename)

if __name__ == '__main__':
  main()
