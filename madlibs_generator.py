#load for all the word

with open ("story.txt", encoding="utf-8") as f:
    story = f.read()
words = set()
start_of_word = -1

target_start= "<"
target_end=">"

for  i, char in enumerate(story):
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        word = story [ start_of_word : i +1]
        words.add(word)
        start_of_word = -1

answers={}

for word in words:
    answer = input("Enter a word for"+ word+ ":")
    answers[word] = answer

for word in words:
    story=story.replace(word, answers[word])
print(story)


"""I got this error((UnicodeDecodeError: 'charmap' codec 
can't decode byte 0x9d')) when i write ('story.txt, 'r' ).And 
this statement is not working for this computer 
bcz python took defult encoding which is charmap. 
using ('UTf-8')I said to python  use this and decode it. """