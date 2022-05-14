def wordcount(fname):
    try:
        fhand=open(fname)
    except:
        print('File can not be opened')
        exit()

    count=dict()
    for line in fhand:
        words=line.split()
        for word in words:
            if word not in count:
                count[word]=1
            else:
                count[word]+=1
    return(count)
def most_used_word(dictionary):
    return max(dictionary, key=dictionary.get)
def less_used_word(dictionary):
    return min(dictionary, key=dictionary.get)

count=wordcount('sample3.txt')

print(most_used_word(count))
print(less_used_word(count))
