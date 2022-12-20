import json


def json_loader(): return json.load(open('posts.json', encoding='utf-8'))


def findingPosts(word):
    return list(filter(lambda x: word in x['content'], json_loader()))


def write_to_json(content, file):
    ll: list = json_loader()
    ll.append({"pic": file, "content": content})
    with open('posts.json', 'w', encoding='utf-8') as filee:
        filee.write(json.dumps(ll, ensure_ascii=False))