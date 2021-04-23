#The included code stub will read an integer, , from STDIN.
#Without using any string methods, try to print the following:
#123.......n.
#Note that "...." represents the consecutive values in between.
if __name__ == '__main__':
    n = int(input())
    num=1
    while num<=n:
        print(num,end='')
        num+=1