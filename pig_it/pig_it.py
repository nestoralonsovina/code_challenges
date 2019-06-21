def pig_it(text):
    text = text.split()
    new = []
    for word in text:
        word = list(word)
        word.append(word[0])
        word.pop(0) 
        word = ''.join(word)
        if word.isalpha():
            word = word + 'ay'
        new.append(word)
    new = ' '.join(new)
    return (new)

assert pig_it('Pig latin is cool') == 'igPay atinlay siay oolcay'
assert pig_it('This is my string') == 'hisTay siay ymay tringsay'
