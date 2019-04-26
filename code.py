import json
data = json.load(open('data (1).json'))
word= input('Enter the word : \n')
def translation(w):
    return data[w]
if word in data:
    return translation(word)
else:
    return f'Word does not exist'
