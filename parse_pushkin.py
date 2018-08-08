# -*- coding: utf-8 -*-

import requests
import lxml.html
from collections import OrderedDict
import json
import re
import os
from bs4 import BeautifulSoup
from pprint import pprint


class DictDownloader():
    """
	Класс для скачивания таблиц словоизменения из азербайджанского викисловаря и преобразования их в словарь вида
	{лемма: [{форма_1:{грамматическая информация}}
				...
			{форма_n:{грамматическая информация}}]}.
	На выходе - файл json.
	"""

    def __init__(self):
        self.file_path = os.path.split(os.path.abspath(__file__))[0]
        self.s = requests.Session()
        self.s.headers.update(
            {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})

    def download_web_page(self):
        dictionary = OrderedDict()
        url = 'http://www.wysotsky.com/0009/300.htm'
        t = self.s.get(url)
        t.encoding = 'windows-1251'
        t = t.text
        root = lxml.html.fromstring(t)
        entries = [p for p in root.xpath('//p') if p.xpath('//a[@name]')]
        print(lxml.html.tostring(entries[0]))
        # for el in entries:
        #     title = [el.xpath('//b/text()')][0]
            # print(title)

            # dictionary[el.xpath('//a/@name')] = OrderedDict([()])

    def text2html(self):
        with open('temp.txt') as f:
            text = f.read()
        root = lxml.html.fromstring(text)
        print(root)


if __name__ == '__main__':
    downloader = DictDownloader()
    # print('Downloading dict...')
    # downloader.download_web_page()
    downloader.text2html()
