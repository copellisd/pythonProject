#frequency of a char in string using dict
#wap for find the frequency of each character in a string
string="automation"

char_count={}

for char in  string:
    char_count[char]=char_count.get(char,0)+1

print(char_count)