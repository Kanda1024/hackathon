from flask import Flask, request, render_template
from namechanger import changer
from a import artist_searcher
import codecs
app = Flask(__name__)

singers={}


@app.route("/")
def bbs():
    message = "Hello world"
    file = codecs.open("articles.txt", "r", "utf-8")
    lines = file.readlines()
    file.close()
    return render_template("bbs.html", message = message)

@app.route("/arti", methods=["POST"])
def arti():
    artist = request.form["artist_name"]
    song = request.form["song_name"]
    message = "アーティスト名：" + artist + "\n 曲名："+song

    #name = changer(name)

    singers = artist_searcher(artist)

    """
    file = codecs.open("articles.txt", "a", "utf-8")
    file.write(singer_urls + "," +  + "\n")
    file.close()
    """

    return render_template("bbs_artist.html", message = message, artist = artist, song = song, singers = singers)

@app.route("/songname", methods=["POST"])
def songname():
    artist = request.form["last_artist_name"]
    #name = changer(name)
    artist_url = singers[artist]


    return render_template("bbs_songs.html", message = message, artist = artist, song = song)

@app.route("/result", methods=["POST"])
def result():
    artist = request.form["artist_name"]
    song = request.form["song_name"]
    message = "アーティスト名：" + artist + "\n 曲名："+song

    #name = changer(name)

    file = codecs.open("articles.txt", "a", "utf-8")
    file.write(artist + "," + song + "\n")
    file.close()

    return render_template("bbs_result.html", message = message, artist = artist, song = song)


if __name__ == '__main__':
    app.debug = True  #デバッグモードTrueにすると変更が即反映される
    app.run()