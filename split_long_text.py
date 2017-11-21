#!/usr/bin/python3

#print (translator.translate('I want to go to toilet.', dest='zh-cn'))

def trans( content,  lang ):
    from googletrans import Translator
    translator = Translator()
    out_lang = ""
    "This prints a passed info into this function"
    print ("Content  : ", content)
    print ("Lang     : ", lang)
    out_lang = translator.translate(content, lang) 
    #print ("Out_lang : ", out_lang.text)
    #input("Press Enter to continue...")
    return out_lang.text;
