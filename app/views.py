from app import app
from flask import jsonify, abort
from .utils import load_news, load_comments, get_count_comments_by_news_id


@app.route('/', methods=['GET'])
def get_news():
    news_list = load_news()
    count_comments_by_news_id = get_count_comments_by_news_id()

    result = [
        {**news, 'comments_count': count_comments_by_news_id[news['id']]}
        for news in news_list
    ]

    return jsonify({'news': result, 'news_count': len(result)})


@app.route('/news/<int:id>', methods=['GET'])
def get_news_by_id(id):
    news_list = load_news()
    comments_list = load_comments()

    news = next((n for n in news_list if n['id'] == id), None)

    if news is None:
        abort(404)

    comments = [c for c in comments_list if c['news_id'] == id]
    return jsonify({
        **news,
        'comments': comments,
        'comments_count': len(comments)
    })
