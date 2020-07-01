def ispalindrome(word):
    """ will check if the string is a palindrome"""
    return reverse(word) == word   
def reverse(word):
    """ this will reverse the string """
    rev = ''
    for chr in word:
        rev = chr + rev 
    return rev
def spliter(word):
    """ split the word into group of letters """
    splited_word = list()
    
    if len(word) % 2 == 0:
        
        splited_word.append(word[0:len(word)//2])
        splited_word.append(word[len(word)//2:])
    
    else:
        splited_word.append(word[0:len(word)//2])
        splited_word.append(word[len(word)//2 + 1:])
    return splited_word
    
def ispalindrome2(word):
    """ this will check if the second group reversed 
    is the to the first item from the spliter function"""
    
    return spliter(word)[0] == reverse(spliter(word)[1])

def ispalindrome3(word):
    """ chceks for the similarity of the items in the 
    string satrting from the first and last items """
    i = 0
    j = len(word) - 1
    while i < j and word[i] == word[j]:
        i += 1
        j -= 1

    return i >= j   

        
    
v = ispalindrome3('racecarer')
print(v)



