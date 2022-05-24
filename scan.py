# -*- coding: utf-8 -*-

import sys
import argparse
from lib.init import Init


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('url', help="website", type=str)
	parser.add_argument('-k', '--keys', dest="key_words", nargs='+', help="Keys words u wanna scan", type=str, default="")
	args = parser.parse_args()
	
	scan = Init(args)
	scan.start()

if __name__ == '__main__':
	main()

