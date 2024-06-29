# Write your solution here
from difflib import get_close_matches


wordlist = []

with open("wordlist.txt") as new_file:

    for line in new_file:
        line = line.strip()
        wordlist.append(line)

text = input("Write text: ")
# text = "This is acually a good and usefull program"
split_text = text.split()
output_str = []
suggestions = []

for word in split_text:
    cur_word = ""
    if word.lower() not in wordlist:
        # store misspelled words
        suggestions.append(word)
        cur_word = "*" + word + "*"
    else:
        cur_word = word
    
    output_str.append(cur_word)

print(" ".join(output_str))
print("suggestions: ")
for word in suggestions:
    print(f"{word}: {', '.join(get_close_matches(word, wordlist))}")
