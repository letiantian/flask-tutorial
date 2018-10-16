import os
import urllib.parse
import codecs

ARTICLE = 'article'
dir_path = os.path.dirname(os.path.realpath(__file__))
article_dir_path = os.path.join(dir_path, '..', ARTICLE)

split_str = '\n<!-- flask-tutorial-info -->\n'

articles = [item for item in os.listdir(article_dir_path) if item.endswith('.md')]
articles.sort()
start_idx = 0
end_idx = len(articles)-1
for idx in range(len(articles)):
    file_name = articles[idx]
    file_path = os.path.join(dir_path, '..', ARTICLE, articles[idx])
    info_content = '\n---\n\n'
    if idx == start_idx:
        next_file_name = articles[idx+1]
        info_content += '* 下一篇 [{}]({})\n'.format(next_file_name[0:-3], urllib.parse.quote(next_file_name))
    elif idx == end_idx:
        prev_file_name = articles[idx-1]
        info_content += '* 上一篇 [{}]({})\n'.format(prev_file_name[0:-3], urllib.parse.quote(prev_file_name))
    else:
        prev_file_name = articles[idx-1]
        info_content += '* 上一篇 [{}]({})\n'.format(prev_file_name[0:-3], urllib.parse.quote(prev_file_name))
        next_file_name = articles[idx+1]
        info_content += '* 下一篇 [{}]({})\n'.format(next_file_name[0:-3], urllib.parse.quote(next_file_name))
    info_content += '\n> 本教程讲述如何使用 Python Flask Web 框架，如有错误/建议，欢迎交流。\n\n'

    file_content = codecs.open(file_path, encoding='utf-8').read()

    if split_str in file_content:
        start_pos = file_content.find(split_str)
        file_content = file_content[0:start_pos] + '\n' + split_str + '\n' + info_content
    else:
        file_content = file_content + '\n' + split_str + '\n' + info_content

    # print(file_content)
    codecs.open(file_path, mode='w', encoding='utf-8').write(file_content)