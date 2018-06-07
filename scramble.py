import string, random, re

def scramble(unscrambled):

    splitter = re.compile(r'\s')

    words = splitter.split(unscrambled)

    for word in words:
        length = len(word)

        if length < 4: continue

        if length == 4:
            scrambled = u'%c%c%c%c' % (word[0], word[2], word[1], word[3])

        else:
            mid = list(word[1:-1])

            random.shuffle(mid)

            scrambled = u'%c%s%c' % (word[0], ''.join(mid), word[-1])
            
        unscrambled = unscrambled.replace(word, scrambled, 1)

    

    return unscrambled



if __name__ == '__main__':

    txt=open('sample.txt','r')

    file=txt.readline()
    
    new_file=open('scrambled.txt','w')

    new_file.write(scramble(file))

    new_file.close()
