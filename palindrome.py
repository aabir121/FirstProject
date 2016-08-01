print "We will check for palindrome"

inp=raw_input("Enter a string: ")

length=len(inp)
print length
i=0
new_inp=""
for letter in reversed(range(length)):
    new_inp=new_inp+inp[letter]

print "%s" % (new_inp)

flag=True

for i in range(0,length):
    if(inp[i]!=new_inp[i]):
        flag=False
        print "Not a plaindrome"
        break

if(flag==True):
    print "%s is a palindrome" % (inp)