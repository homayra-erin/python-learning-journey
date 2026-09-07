name="Homayra"

vowel="aeiouAEIOU"

vowels=0
const = 0

for i in name:
    if (i in vowel):
        vowels += 1
    else:
        const += 1
print(vowels)
print(const)