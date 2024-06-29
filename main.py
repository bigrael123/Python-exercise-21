names = ("Michael", "Adam", "Eve", "Samael", "Langdon", "Gabriel", "Sasuke", "Naruto", "Kakashi", "Sakura")

for name in names:
    print(f"\nWord: {name} Vowels:")
    for letter in name:
        if(letter in "aeiouAEIOU"):
         print(letter, end="")
    