from flask import request, redirect, url_for, render_template, flash, session
from mahjong import app
import random
from mahjong import db
from mahjong.models.tiles import Tiles

tiles =[]
tilelink_list = []
count = 1

def distribute(tile_list):
    for i in range(14):
        tile_list[i] = random.randint(1,34)
    for t in tile_list:
        if tile_list.count(t) >= 5:
            distribute(tile_list)
        else:
            global tiles
            tiles = tile_list
            tile_list.sort()

@app.route('/', methods=['GET', 'POST'])
def playtile():
    if request.method == 'GET':
        tile_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        tilelinks = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        distribute(tile_list)
        for j in range(14):
            tile = Tiles.query.get(tile_list[j])
            tilelinks[j] = tile.link
        global tilelink_list
        tilelink_list = tilelinks
        global count
        count = 1
        return render_template('index.html', tilelinks=tilelink_list, count=count)

@app.route('/<int:num>', methods=['GET'])
def tileselect(num):
    global tilelink_list
    global tiles
    global count
    if request.method == 'GET':
        tiles.pop(num)
        tiles.sort()
        tumonum = random.randint(1,34)
        tiles.append(tumonum)

        for k in range(14):
            new_tile = Tiles.query.get(tiles[k])
            tilelink_list[k] = new_tile.link

        count = count + 1
        return render_template('index.html', tilelinks=tilelink_list, count=count)

@app.route('/tumo')
def tumo():
    global count
    return render_template('tumo.html', count=count)

@app.route('/')
def reload():
    return render_template('index.html')

@app.route('/tumo', methods=['POST'])
def hancalc():
    if request.method == 'POST':
        h = int(request.form['hannum'])
        return render_template('han.html', h=h)