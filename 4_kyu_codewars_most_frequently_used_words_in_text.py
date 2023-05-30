from collections import Counter
import re

text = """In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."""

text2 = '''"  //wont won't won't"'''

text3 = '''"e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"'''

def top_3_words(text):
    count = Counter([i for i in re.findall(r"'?[a-z0-9']+'?", text.lower())]).most_common(3)
    return [i for i, k in count] if re.search('\w+', text) else []


print(top_3_words("a a a  b  c c  d d d d  e e e e e"))
print(top_3_words(text))
print(top_3_words(text2))
print(top_3_words(text3))