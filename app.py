from flask import Flask, render_template, request
from distance import edit_distance
from pitch_track import track

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def calc_dist():
    if request.method == 'POST':
        wav = request.files['filename']
        pt = track(wav)
        return render_template('transmit.html', dist=edit_distance(pt,pt,1,1))
    else:
        return render_template('transmit.html', dist=None)


if __name__ == '__main__':
	app.run()
