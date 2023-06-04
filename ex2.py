poem_lines = [str(input()).lower() for _ in range(int(input()))]

vowels = ['a', 'e', 'i', 'o', 'u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']

vowels_count = 0
consonants_count = 0

for poem_line in poem_lines:
    for vowel in vowels:
        vowels_count += poem_line.count(vowel)

    for consonant in consonants:
        consonants_count += poem_line.count(consonant)

print("Number of vowels: ", vowels_count)
print("Number of consonants: ", consonants_count)