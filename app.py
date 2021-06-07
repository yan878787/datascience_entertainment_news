from flask import Flask, jsonify, request
import requests
import json

app = Flask(__name__)
#json 中文回傳
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def home():
    return ' Team 2 entertainment news playgroud'

def _news_api(q, n=10, w=30):
    #string to list
    q = q.split(',')
    #assignment 1's url posted on Heroku
    url = 'https://assisgnment4getfile.herokuapp.com/'
    r = requests.get(url)
    news = r.json()
    result = []
    for var in news:
        #check news'title
        title_well = True # if title read fine then keeping on
        for qq in q:
            if qq in var['title']:
                continue
            title_well = False # if false then break
            break
        #check news'content
        #logic is same as title
        content_well = True
        for qq in q:
            if qq in var['content']:
                continue
            content_well = False
            break
        #if result >= the number of setted news then break
        if len(result) >= n:
            break
        #Once either title or content reading well, we can read out all of element of news
        if title_well or content_well:
            title = var['title'] #from defalut var's number to setted n
            content = var['content'][:w]
            url = var['url']
            yimg = var['yimg']
            result.append({
                'title':title,
                'content':content,
                'url':url,
                'yimg':yimg
            })
    return result
    
@app.route('/news_api')
def news_api():
    try:
        q = request.args.get('q')
        n = int(request.args.get('n'))
        w = int(request.args.get('w'))
        data = json.loads(json.dumps(_news_api(q, n, w)))
        return jsonify(data)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run()