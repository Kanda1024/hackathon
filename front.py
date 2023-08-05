from flask import Flask, request, render_template
from main import artist_searcher, song_searcher, liric_seacher
import codecs
app = Flask(__name__)


@app.route("/")
def bbs():
    message = "Hello world"
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

    return render_template("bbs_artist.html", singers = singers)

@app.route("/songname", methods=["POST"])
def songname():
    artist_url = request.form["last_artist_name"]
    songs = song_searcher(artist_url)

    return render_template("bbs_song.html", songs = songs)


@app.route("/liric", methods=["POST"])
def liric():
    song_url = request.form["last_song_name"]
    Liric = liric_seacher(song_url)
    #print(Lilic)

    return render_template("bbs_final.html", Liric = Liric)


if __name__ == '__main__':
    app.debug = True  #デバッグモードTrueにすると変更が即反映される
    app.run()