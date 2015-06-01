sentence = "+d====+a+"

alphabet = 'abcdefghijklmnopqrstuvwxyz'
answer = "true"
if sentence[0].lower() in alphabet:
    answer = "false"
letters = [l for l in sentence if l.lower() in alphabet] 

if answer <> "false":
    for l in letters:
        try:
            if sentence[sentence.index(l)-1] <> "+" or sentence[sentence.index(l)+1] <> "+":
                answer = "false"
                continue
        except:
            answer = "false"
            break
print answer
