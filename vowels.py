z=input("Enter a word: ")
vowels=set("aeiou")

# Initialize the count of vowels
x = 0

# Loop through each character in the input word
for i in z:
    # Check if the character is a vowel
    if i in vowels:
        x += 1
# Print the total number of vowels
print(f"Number of vowels: {x}")
