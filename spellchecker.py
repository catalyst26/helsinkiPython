# write your solution here
wordlist = []

with open("wordlist.txt") as new_file:

    for line in new_file:
        line = line.strip()
        wordlist.append(line)

text = input("Write text: ")
# text = "This is acually a good and usefull program"
split_text = text.split()
output_str = []

for word in split_text:
    cur_word = ""
    if word.lower() not in wordlist:
        cur_word = "*" + word + "*"
    else:
        cur_word = word
    
    output_str.append(cur_word)

print(" ".join(output_str))
    