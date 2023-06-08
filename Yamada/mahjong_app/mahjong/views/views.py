from flask import request, redirect, url_for, render_template, flash, session
from mahjong import app
import random
from mahjong import db
from mahjong.models.tiles import Tiles

tiles =[]
tilelink_list = []

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
        return render_template('index.html', tilelinks=tilelink_list)

@app.route('/<int:num>', methods=['GET'])
def tileselect(num):
    global tilelink_list
    global tiles
    if request.method == 'GET':
        temp = tilelink_list[13]
        tilelink_list[13] = tilelink_list[num]
        tilelink_list[num] = temp
        tumonum = random.randint(1,34)
        tumopai = Tiles.query.get(tumonum)
        tilelink_list[13] = tumopai.link
        return render_template('index.html', tilelinks=tilelink_list)
        

@app.route('/tumo')
def tumo():
    return render_template('tumo.html')

@app.route('/')
def reload():
    return render_template('index.html')