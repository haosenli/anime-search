# for custom imports
import sys # for import from parent directory
import os
from urllib import request # for import from parent directory
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from flask import Flask, redirect, url_for, render_template, request, jsonify


# custom imports
from src.search_engine.search_engine import SearchEngine
from src.utils.formatting import wordtrie_format


# start flask app
app = Flask(__name__)

# instantiation
cwd = os.getcwd()
SE_PATH = os.path.join(cwd, 'website/anime_search_engine/anime_search_engine_v3.pkl')
PC_PATH = os.path.join(cwd, 'website/precomputed_v3')
SE = SearchEngine(SE_PATH, PC_PATH)

@app.route('/', methods=['GET'])
async def empty():
    """Redirects users to home page."""
    return redirect(url_for('home'))

@app.route('/home/', methods=['Get'])
async def home():
    """Returns the home page of the app."""
    trending = SE.trending(250)
    pic = 'https://images.unsplash.com/photo-1554034483-04fda0d3507b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80'
    return render_template('results.html',
                           title='AnimeSearch | Home', 
                           pic=pic,
                           animes=trending)

@app.route('/search/', methods=['GET'])
async def search():
    """Returns the search results from the query."""
    # search
    query = request.args.get('q', None)
    animes = await SE.search(query, limit=250)
    if animes:
        pic = animes[0].get_info()['mal_stats']['main_picture']['large']
        return render_template('results.html', 
                               animes=animes, 
                               title='AnimeSearch | Search Results',
                               pic=pic,
                               num_results=len(animes))
    return render_template('error.html', 
                           title='AnimeSearch | No Results')

@app.route('/anime/', methods=['GET'])
async def anime():
    """Returns an anime page."""
    name = request.args.get('q', None)
    wtf_name = wordtrie_format(name)
    item = SE.get_item(wtf_name)
    if item is None:
        return render_template('error.html',
                               title='AnimeSearch | Error')
    # update click count
    SE.add_click(wtf_name)
    recommends = await SE.recommend(wtf_name, limit=100)
    pic = item.get_info()['mal_stats']['main_picture']['large']
    return render_template('detail.html', 
                           title='AnimeSearch | Detail', 
                           pic=pic,
                           anime=item,
                           recommends=recommends)

@app.route('/random/', methods=['GET'])
async def random():
    """Returns a random anime page."""
    item = SE.random_item()
    item_name = item.get_name()
    recommends = await SE.recommend(item_name, limit=100)
    pic = item.get_info()['mal_stats']['main_picture']['large']
    return render_template('detail.html',
                           pic=pic,
                           title='AnimeSearch | Random',
                           anime=item,
                           recommends=recommends)
    
@app.route('/about/', methods=['GET'])
async def about():
    """Returns an about page."""
    return render_template('about.html', title='AnimeSearch | About')

@app.route('/api/trending/', methods=['GET'])
async def api_trending():
    """API endpoint for trending animes."""
    limit = int(request.args.get('limit', 10))
    if limit > 100:
        limit = 100
    trending = SE.trending(limit)
    trending = [item.serialize() for item in trending]
    return jsonify(trending=trending)

@app.route('/api/search/', methods=['GET'])
async def api_search():
    """API endpoint for searching animes."""
    query = request.args.get('q', None)
    limit = int(request.args.get('limit', 10))
    result = await SE.search(query, limit)
    result = [item.serialize() for item in result]
    return jsonify(result=result)

@app.route('/api/random/', methods=['GET'])
async def api_random():
    return jsonify(SE.random_item().serialize())

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))