#count vowels of string

#input string="hello world"

def count_vowels(string):
    count = 0
    vowels = "aeiouAEIOU"
    for char in string:
        if char in vowels:
            count += 1
    return count
text = "Hello, World!"
print("Number of vowels:", count_vowels(text))