#!/bin/env python3.7

import os, sys, re


for file in sys.argv[1:]:
	with open(file) as I:
		text = I.read()
	
	lines = text.split('\n')

	if len(lines) < 3:
		print('there should be at least 3 lines')
		exit(1)

	if len(lines[1].strip()) > 0:
		print('the title should be separated from the message with a blank line')
		exit(1)

	if not lines[0][0].isupper():
		print('the first line of commit message should be capitalized')
		exit(1)

	if any(len(line) > 72 for line in lines):
		print('lines should be wrapped at 72 characters')
		exit(1)
