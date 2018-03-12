#1. Uppercase a String
string = "hello, this is Sam Sun!"
print(string.upper())

#2. Capitalize a String
print(string[0].capitalize() + string[1:])

#3. Reverse a String
def reverse(u):
    u = "".join(reversed(u))
    return u

print("The original string is : ", string)
print("The reversed string (using reversed) is : ", reverse(string))

#4. Leetspeak
paragraph = "The future belongs to those who believe in the beauty of their dreams. --- Eleanor Roosevelt"
#set up the leet dictionary
leet = { "A" : "4", 
         "E" : "3",
         "G" : "6",
         "I" : "1",
         "O" : "0",
         "S" : "5",
         "T" : "7" }
leetspeak = ""
print("Let's start leet conversion!")
for char in paragraph.upper():
    if char in leet:
        leetspeak += leet[char]
    else:
        leetspeak += char
print(leetspeak)

#5. Long-long Vowels
x = "spoon"
longVowel = x[0:2] + "o" * 5 + x[4]
print(longVowel)

y = "cake"
longVowelB = y[0:1] + "a" * 5 + y[2:4]
print(longVowelB)

z = "sheep"
longVowelC = z[0:2] + "e" * 5 + z[4:5]
print(longVowelC)

#6. Caesar Cipher
plaintext = "A woman is like a tea bag you cant tell how strong she is until you put her in hot water Eleanor Roosevelt"
def caesar(plaintext, shift):  
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", 
                "j", "k", "l", "m", "n", "o", "p", "q", "r", 
                "s", "t", "u", "v", "w", "x", "y", "z"]  
    ciphertext = " "

    for i in range(0, len(plaintext.lower())):
        letter = plaintext.lower()[i]                  
        # Find the number position of the ith letter
        if letter != " ":
            num_in_alphabet = alphabet.index(letter)        

            # Find the number position of the cipher by adding the shift    
            cipher_num = (num_in_alphabet + shift) % len(alphabet)   

            # Find the cipher number you computed
            cipher_letter = alphabet[cipher_num]          
        else:
            cipher_letter = " "
        # Add the cipher letter to the ciphertext
        ciphertext = ciphertext + cipher_letter            
        
            
    return ciphertext
    
print(caesar(plaintext, 1))

# decipher the following text, shift = 13, but need to try every time??
ciphertextB = "lbh zhfg hayrnea jung lbh unir yrnearq" 
print(caesar(ciphertextB, 13))







    


















