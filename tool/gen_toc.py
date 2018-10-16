import os
import urllib.parse

ARTICLE = 'article'
dir_path = os.path.dirname(os.path.realpath(__file__))
article_dir_path = os.path.join(dir_path, '..', ARTICLE)

articles = [item for item in os.listdir(article_dir_path)]
articles.sort()
for file_name in articles:
    # print(file_name)
    print('* [{}](article/{})  '.format(file_name[0:-3], urllib.parse.quote(file_name)))