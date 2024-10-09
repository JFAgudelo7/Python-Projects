# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 19:08:34 2024

https://www.youtube.com/watch?v=Ew44dS0mw-E

In this project, we will build a web scraper to extract data from software job postings from a public forum so that we can count and see which technologies are the most in-demand.
 We will then visualize the data on a graph. This tutorial is suitable for Python beginners.

"""
import numpy as np
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup as bs


def main():
    url = "https://news.ycombinator.com/item?id=41709301"
    response = requests.get(url)

    soup = bs(response.content, 'html.parser')
    elements = soup.find_all(class_='ind', indent=0) # the underscore class_ in is to be able to use the python reserved class word for other things
    comments = [e.find_next(class_="comment") for e in elements] #To get the inner comments

    keywords = {"python": 0, 'Javascript': 0, "java": 0, "html": 0, "c#": 0, "artificial": 0, "implementation": 0, "data-analyst": 0}

    for comment in comments:
        comment_text = comment.get_text().lower()
        words = comment_text.split(' ')
        words = {w.strip(".,/:;!@+()[]|") for w in words} #The strip() method removes any leading, and trailing whitespaces or characters passed as parameters
        #print(comment_text)
        #print(words)
        for k in keywords:
            if k in words:
                keywords[k] += 1
    print(keywords)

    print(f"Comments: {len(elements)}")
    #print(response.content)



if __name__ == "__main__":
    main()