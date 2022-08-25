# for custom imports
import sys # for import from parent directory
import os # for import from parent directory
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from flask import render_template, url_for, redirect, request


# custom imports
from src.search_engine.search_engine import SearchEngine
from src.utils.formatting import wordtrie_format
from flask_app import app


# instantiation
cwd = os.getcwd()
SE_PATH = os.path.join(cwd, 'anime_search_engine/anime_search_engine_v3.pkl')
PC_PATH = os.path.join(cwd, 'precomputed_v3')
SE = SearchEngine(SE_PATH, PC_PATH)


@app.route('/', methods=['GET'])
async def empty():
    """Redirects users to home page."""
    return redirect(url_for('home'))

@app.route('/home/', methods=['Get'])
async def home():
    """Returns the home page of the app."""
    trending = SE.trending(250)
    pic = trending[0].get_info()['mal_stats']['main_picture']['large']
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

@app.route('/anime', methods=['GET'])
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
    SE.add_click(item_name)
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
    