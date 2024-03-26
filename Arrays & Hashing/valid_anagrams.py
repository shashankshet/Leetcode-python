# valid anagrams
s="A man, a plan, a canal: Panama"

s = [x for x in s if x.isalnum()]
res = "".join(s).lower()

if(res==res[::-1]):
    print("True")
else:
    print("falase")
