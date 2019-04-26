import json
from difflib import get_close_matches
data = json.load(open('data .json'))
word= input('Enter the word : \n')
def translation(w):
    return data[w]
if word in data:
    print(translation(word))
else:
    closest=get_close_matches(word,data,n=1,cutoff=0.8)

    choice=input(f' Did you mean {closest[0]} ? Y or N \n')
    if choice== 'Y':
        print(translation(closest[0]))
    else:
        print('word does not exist')
