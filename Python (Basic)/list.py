#list
#Consider a list (list = []). You can perform the following commands:
#insert i e: Insert integer  at position .
#print: Print the list.
#remove e: Delete the first occurrence of integer .
#append e: Insert integer  at the end of the list.
#sort: Sort the list.
#pop: Pop the last element from the list.
#reverse: Reverse the list.
#Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. 
#Iterate through each command in order and perform the corresponding operation on your list.

if __name__ == '__main__':
    N = int(input())
    output=[] ;
    for i in range(0,N):
        a = input().split();
        if a[0]=="print":
            print(output)
        elif a[0]=="insert":
            output.insert(int(a[1]),int(a[2]))
        elif a[0]=="remove":
            output.remove(int(a[1]))
        elif a[0] =="append":
            output.append(int(a[1]))
        elif a[0]=="sort":
            output.sort();
        elif a[0]=="pop":
            output.pop();
        else :
            output.reverse();