
word_dict = {}
with open('unigram_freq.csv') as f:
    for line in f.readlines():
        word, freq = line.split(',')
        if len(word) == 5:
            word_dict[word] = freq


with open('freq.csv', 'w') as f:
    for k,v in word_dict.items():
        f.writelines(['{},{}'.format(k,v)])
