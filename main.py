# Built-in imports

def reverse(text):
    """
    Given a string, reverses the string
    
    Parameter
    ---------
    text: string

    Returns
    -------
    string
    """
    if len(text) < 2:
        return text
    return reverse(text[1:]) + text[0]
    

str = input("Palindrome check: ")

def is_palindrome(str):
    """
    Given a string, checks if string is a palindrome
    
    Parameter
    ---------
    text: string

    Returns
    -------
    True or False: bool
    """
    
    for char in str:
        if char in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ ":
            str = str.replace(char, "")

    # print(len(str))

    if len(str) < 2:
        return True
        
    if str[0] == str[-1]:
        return is_palindrome(str[1:-1])
    else:
        return False
        
            
   
    ##### Method without recursion (uses reverse() from earlier):
    # if len(str) % 2 == 0:
    #     # print(len(str)/2)
    #     firsthalf = str[:int(len(str)/2)]
    #     # print(firsthalf)
    #     secondhalf = str[int(len(str)/2):]
    #     if reverse(firsthalf) == secondhalf:
    #         return True
    #     else:
    #         return False

    # if len(str) % 2 == 1:
    #     # print(len(str)//2)
    #     firsthalf = str[:len(str)//2]
    #     # print(firsthalf)
    #     secondhalf = str[len(str)//2 + 1:]
    #     # print(secondhalf)
    #     if reverse(firsthalf) == secondhalf:
    #         return True
    #     else:
    #         return False

print(is_palindrome(str))
    


