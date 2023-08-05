from flask import Flask, request, render_template
#from a import artist_searcher
import codecs
app = Flask(__name__)

singers={}
songs={}


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
    artist = request.form["last_artist_name"]
    #name = changer(name)
    print(artist)
    print(singers)
    artist_url = singers[artist]

    print(artist_url)
    songs = song_searcher(artist_url)




    return render_template("bbs_song.html", song = songs)





@app.route("/liric", methods=["POST"])
def liric():
    song = request.form["last_song_name"]

    Liric = songs[song]

    #name = changer(name)

    return render_template("bbs_final.html", Lilic = Lilic)


if __name__ == '__main__':
    app.debug = True  #デバッグモードTrueにすると変更が即反映される
    app.run()