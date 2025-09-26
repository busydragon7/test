a=input("Enter any string  : ")

alphabets = [ch for ch in a if ch.isalpha()]
alphabets.reverse()

r=[]
i=0
for ch in a:
    if ch.isalpha():
        r.append(alphabets[i])
        i += 1
    else:
        r.append(ch)

print("".join(r))