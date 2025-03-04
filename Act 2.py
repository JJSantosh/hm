def pal(t):
    end=len(t)-1
    start=0
    while(start<end):
        if(t[start]!=t[end]):
            return False
        
        start=start+1
        end=end-1
    return True

tup=(1,3,2,4,5,6)
if(pal(tup)):
    print("palindrome series")
else:
    print("not a palindrome series")