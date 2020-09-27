from cs50 import get_string


text = get_string("Text: ")
words = 1
sentences = 0
letters = 0
for character in text:
    if character.isalpha():
        letters = letters + 1
    if character is ' ':
        words = words + 1
    if character is '.' or character is '?' or character is '!':
        sentences = sentences + 1

L = (letters / words) * 100
S = (sentences / words) * 100
grade = round(0.0588 * L - 0.296 * S - 15.8)

if grade < 1:
    print("Before Grade 1")
elif grade >= 16:
    print("Grade 16+")
else:
    print(f"Grade {grade}")