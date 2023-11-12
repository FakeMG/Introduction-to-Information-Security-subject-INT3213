alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_dict = {}

for index, letter in enumerate(alphabet):
    alphabet_dict[letter] = index

def convertName(s:str) -> int:
    sum = 0
    
    for i in range(len(s) - 1, -1, -1):
        sum += alphabet_dict[s[i]] * pow(26, len(s) - 1 - i)    

    return sum