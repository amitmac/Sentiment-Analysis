import re

def tokenizer(text):
    text = re.sub('<[^>]*>','',text)
    emoticons = re.findall('((?::|;|=)(?:-?)(?:[D|d|)|(|P|p|/|x|X]))',text)
    text = re.sub('[\W]+',' ',text.lower())
    text += ' '.join(emoticons).replace('-','')
    tokenized = [w for w in text.split() if w not in stop]
    return tokenized