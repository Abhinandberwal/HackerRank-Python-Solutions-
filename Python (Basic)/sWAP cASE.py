#sWAP cASE
#You are given a string and your task is to swap cases. 
#In other words, convert all lowercase letters to uppercase letters and vice versa.
def swap_case(s):
    output='';
    for i in s:
        if(i.isupper()==True):
            output+=(i.lower());
        elif(i.islower()==True):
            output+=(i.upper());
        else:
            output+=i;
    return output;
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)