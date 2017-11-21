#!/usr/bin/python3


def split_long_text( content ):
    "This prints a passed info into this function"
    import re
    print ("content = %s" % content)
    m = re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', content)
    sentences = []
    t_ele = 0
    max_words = 20
    for i in m:
        print (i)
        t_ele = len(sentences)
        if (t_ele == 0):
            sentences.append(i)
        elif (t_ele > 0):
            last_element = sentences[t_ele - 1]
            #print ("last sentence [%s]" % last_element)
            word_count = len(last_element.split())
            if (word_count <= max_words):
                sentences[t_ele - 1] = sentences[t_ele - 1] + " " + i 
            else:
                sentences.append(i)
            #print ("last array sentence [%s]" % sentences[t_ele - 1])
            word_count = len(sentences[t_ele - 1].split())
            #print ("word count [%d]" % word_count)
            #input("Press Enter to continue...")
        #t_ele = len(sentences)
        #print ("total element: %d" % t_ele)
            
    for num, line in enumerate(sentences):
        print ("item [%d] [%s]" % (num, line))

    #input("Press Enter to continue...")
    return;

if __name__ == '__main__':
    print("This only executes when %s is executed rather than imported" % __file__)
    split_long_text("""Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true... Well, with a probability of .9 it isn't.""")

