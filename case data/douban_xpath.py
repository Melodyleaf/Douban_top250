# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 19:58:45 2022

@author: x
"""

from lxml import etree #import etree
import time #import time
import random #import random
import requests,json #import requests json

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'}

# 处理字符串中的空白符，并拼接字符串
def processing(strs):
    s='' #定义保存内容的字符串
    for n in strs:
        n=''.join(n.split()) # 去除空字符
        s=s+n # 拼接字符串
    return s # 返回拼接后的字符串 

#get movie information
def get_movie_info(url):
    res = requests.get(url, headers=headers) #send requests to douban url
    html = etree.HTML(res.text) #parse html text str
    div_all = html.xpath('//div[@class="info"]') #""info in url,not ''
    for div in div_all:
        names = div.xpath('//div[@class="hd"]/a/span/text()') #get movie names
        name = processing(names) #processing movie names
        infos = div.xpath('//div[@class="bd"]/p/text()') #get director and actor names
        info = processing(infos)
        score = div.xpath('//div[@class="bd"]/div/span[2]/text()') #get score
        rating_number = div.xpath('//div[@class="bd"]/div/span[4]/text()') #get rating numbers
        summary = div.xpath('//div[@class="bd"]/p[@class="quote"]/span/text()') #get evaluation summary
        print("movie name: ",name)
        print("actor name: ",info)
        print("score: ",score)
        print("rating_number:",rating_number)
        print("summary: ",summary)
        print("---------------------")
        
if __name__ == '__main__':
    for i in range(0,250,25): #0-250 movies, each page=25 movies:
        url = 'https://movie.douban.com/top250?start={page}@filter='.format(page=i)
        get_movie_info(url) #get movie infos by url
        time.sleep(random.randint(1,2)) #waiting 1-3s random 
    