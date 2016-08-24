import re
import itertools

crypto_alpha = "send + More == Money"  # Crypto Alpha Equation
crypto_alpha = crypto_alpha.upper()
words = re.findall("[A-Z]+", crypto_alpha.upper())  # Find the all words given in the equation
print("Each words are  : ", words)
first_letters = {word[0] for word in words}
join_words = ''.join(words)  # join all words as a string
print("Join all words : ", join_words)
print("First letters of the words are  : ", first_letters)
n = len(first_letters)
unique_chars = set(join_words)  # Find all unique characters
print("Individual characters of the words  : ", unique_chars)
assert len(unique_chars) <= 10, "Too large alphabets"  # checks whether characters less than 10 as we only 9 numbers 0-9
sorted_characters = ''.join(first_letters) + ''.join(unique_chars - first_letters)
print("Sorted characters are : ", sorted_characters)
ascii_values = tuple(ord(char) for char in sorted_characters)  # find all ascii values of each characters
print("Ascii values of characters : ", ascii_values)
digits = tuple(ord(c) for c in '0123456789')       # Select all digits from 0-9(Ascii values )
print("digits are : ", digits)
zero = digits[0]            # The digit should be stored because first letters should not take digit '0'
for guess in itertools.permutations(digits, len(ascii_values)):     # Checking for all permutations
    if zero not in guess[:n]:           # Checking that digit '0' is not in first letters
        equation = crypto_alpha.translate(dict(zip(ascii_values, guess)))  # Python method to translate digits as equation
        if eval(equation):           # Evaluating equation whether equation is true or not.
            print(equation)
            print("Got it")
            break;


