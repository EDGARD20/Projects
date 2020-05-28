
"""
Programming Practice: Is It Palindrome?
New to programming, Zargisu wants to write a program
to determine if a word is palindrome. They say a word
palindrome that can be read from left to right. For
example, Madam is a palindrome but tehran is not a
palindrome. Now you have to help Zaragisu write this program.
Please note that lowercase or uppercase letters do not
matter as we said Madam is a palindrome just as maDAM is
a palindrome.

Input Sample:

madam
Output Sample:

palindrome
 

Input Sample:

tehran
Output Sample:

not palindrome
"""
words = input()
words = words.lower()

words_reverse = list(words)
words_reverse.reverse()
separator = ''

if words == separator.join(words_reverse):
    print('palindrome')
else:
    print('not palindrome')
