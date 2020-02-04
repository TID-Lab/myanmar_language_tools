# -*- coding: utf-8 -*-

import mm_segmenter as mm
import random
import json
import io
import unicodecsv as csv

random.seed(100)
def is_Test():
	return random.randrange(0,100) < 10

segmenter = mm.Segmenter()
size = 0
with io.open('output-objects-target.json', encoding='utf-8') as inputFile, io.open('text-for-annotation.csv','w', encoding='utf8') as outputFile, io.open('machine-segemented-output.csv', 'w', encoding='utf-8') as wordFile:
	for line in inputFile:
		# csvwriter = csv.writer(wordFile)
		lineDict = json.loads(line)
		if 'message' in lineDict.keys():
			text = lineDict['message']
		else: 
			text = ''
		if len(text) > 10 and is_Test():
			words = segmenter.segment(text)
			# print words
			outputFile.write(text + '\n')
			wordFile.write(','.join(words) + '\n')
			# csvwriter.writerow(words)
			size += 1

# input = 'ကမာ္ဘ, အနှံ့, လူမှု, မီဒီယာ, များ, တွင်,  မိနစ်ပိုင်းအတွင်း,  မြင်တွေ့, ခဲ့ကြရသည်။ ယခု, သတင်း, အား, � Android, application, တွင်, ဖတ်ရန်, - https://goo.gl/VHxHq4 � '
# output = segmenter.segment(input)
# for word in output:
# 	print word