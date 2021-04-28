#String Validators
#Task :
#You are given a string S.
#Your task is to find out if the string S contains: alphanumeric characters, 
#alphabetical characters, digits, lowercase and uppercase characters.

def function1(s):
    for i in range(len(s)):
        if(s[i].isalnum()):
            return True;
            break;
    return False;

def function2(s):
    for i in range(len(s)):
        if(s[i].isalpha()):
            return True;
            break;
    return False;
    
def function3(s):
    for i in range(len(s)):
        if(s[i].isdigit()):
            return True;
            break;
    return False;

def function4(s):
    for i in range(len(s)):
        if(s[i].islower()):
            return True;
            break;
    return False;

def function5(s):
    for i in range(len(s)):
        if(s[i].isupper()):
            return True;
            break;
    return False;

if __name__ == '__main__':
    s = input()
    
    alphanumeric=function1(s)
    alphabetical=function2(s)
    digits= function3(s)
    lowercase=function4(s)
    uppercase=function5(s)
    print(alphanumeric)
    print(alphabetical)
    print(digits)
    print(lowercase)
    print(uppercase)