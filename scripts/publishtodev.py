import os

import frontmatter
import json
import requests

post = frontmatter.load('test.md')
keys = post.keys()

with open('article-template.json') as article_template:
    article = json.load(article_template)
    actual_article = article['article']

for (k, v) in actual_article.items():
    if k in keys:
        if k == "tags":
            actual_article[k] = post[k].split(",")
        else:
            actual_article[k] = post[k]
actual_article['body_markdown'] = post.content


headers = {
    'Content-Type': 'application/json',
    'api-key': os.environ['API_KEY'],
}

data = json.dumps(article)
response = requests.post('https://dev.to/api/articles', headers=headers, data=data)
print(f'Article posted to Dev.to and ID is: {response.json()["id"]}')