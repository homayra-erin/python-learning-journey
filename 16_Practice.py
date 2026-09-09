#Return practice question.
#1.Write a function square(num) that returns the square of a number,
def square(num):
    return num**2
Result=square(5)
print(Result)

#2.Write a function that takes a string and returns the count of vowels & constants separately.
def countVowCon(Sentence):

    #define vowels
    vowels="aeiouAEIOU"

    countVowel = 0
    countConsonant = 0

    for i in Sentence:
        if(i.isalpha()):
            if(i in vowels):
                countVowel+=1
            else:
                countConsonant+=1

    return countVowel,countConsonant
   
#Function call
vowels,Consonants=countVowCon("I am puzzled")
print(vowels,Consonants)

#3.Define a function convert_to_upper(word) that returns the uppercase version of the string.
def convert_to_upper(word):
    print()