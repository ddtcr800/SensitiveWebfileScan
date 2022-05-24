# -*- coding: utf-8 -*-


from config import *

import re

class GenerateDcit:
	def __init__(self, keywords):
		self.exts = self._getexts()

		self.keywords = []

		if KEY_WORDS:
			self.keywords += KEY_WORDS

		if keywords:
			self.keywords += keywords


	def _getexts(self):
		with open('dict/ext.txt', 'r') as f:
			exts = f.readlines()
		return [ext.strip() for ext in exts]

	def generate(self):
		for e in self.exts:
			for kw in self.keywords:
				yield e.replace('$',kw)



