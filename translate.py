#!/usr/bin/python3

from googletrans import Translator
translator = Translator()
#translator.translate('안녕하세요.', dest='zh-cn')
#print (translator.translate('안녕하세요.', dest='zh-cn'))
#print (translator.translate('saya mahu pergi ke tandas.', dest='en'))
print (translator.translate('I want to go to toilet.', dest='zh-cn'))

