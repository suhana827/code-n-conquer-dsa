# # Write a function that takes a string and returns true if 
# # it's a palindrome (ignoring spaces and cases).

# def stringChecker():
#     word = input("Enter a word: ")
#     word = word.replace(" ", "").lower()   # remove spaces and lowercase
#     i = 0
#     j = len(word) - 1
#     while i < j:
#         if word[i] != word[j]:
#             return "false"
#         i += 1
#         j -= 1
#     return "true"

# print(stringChecker())    


# # reversing a string 

# word = input("Enter your name: ")
# reverse_word = ""
# for i in range(len(word) - 1, -1, -1):
#     reverse_word = reverse_word + word[i]
# print(reverse_word)


# # Checking if a string is palindrome(another way)

# string = input("Enter any word: ")
# reverse_word = ""
# for i in range(len(string) - 1, -1, -1):
#     reverse_word = reverse_word + string[i]
   
# if string == reverse_word:
#     print("true", string, reverse_word)
# else:
#     print("not a palindrome")  



# # Longest Word in a Sentence
# # Given a string sentence, write a function to return the longest
# word in it. Ignore punctuation.
   
# sentence = input("Enter a sentence: ")
# words = sentence.split()

# longest = ""
# for word in words:
#     if len(word) > len(longest):
#         longest = word

# print(longest)



# # Given two strings needle and haystack, return the index of the first occurrence 
# # of needle in haystack, or -1 if needle is not part of haystack.

# # Example 1:
# # Input: haystack = "sadbutsad", needle = "sad"
# # Output: 0
# # Explanation: "sad" occurs at index 0 and 6.
# # The first occurrence is at index 0, so we return 0.

# # Example 2:
# # Input: haystack = "leetcode", needle = "leeto"
# # Output: -1
# # Explanation: "leeto" did not occur in "leetcode", so we return -1.

def strStr(haystack, needle):
    n, m = len(haystack), len(needle)
    for i in range(n - m + 1):  
        if haystack[i:i+m] == needle:  
            return i
    return -1

haystack = "leetcode"
needle = "leeto"
print(strStr(haystack, needle))


