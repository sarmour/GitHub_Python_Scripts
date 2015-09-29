""" Need to decode the following string

'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.''

clues:
K->M
O->Q
E->G
"""

def translatetext(sentence):
    alph = 'abcdefghijklmnopqrstuvwxyz'

    newsentence = ''
    for l in sentence:
        if l in alph:
            # print (alph.index(l) + 2)%26
            newsentence += alph[(alph.index(l) + 2)%26]
        else:
            newsentence += l
    return newsentence

encodedstr = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

print translatetext(encodedstr)

# answer = "i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url."

print translatetext("http://www.pythonchallenge.com/pc/def/map.html")

