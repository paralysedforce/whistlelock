from flask import Flask, render_template, request
from distance import edit_distance
from pitch_track import track

app = Flask(__name__)

@app.route('/', methods=['POST'])
def calc_dist():
	wav = request.files['filename']
	pt = track(wav)
	return render_template('IdontknowwhatImdoing.html', dist=edit_distance(pt,pt,1,1))

if __name__ == '__main__':
	app.run()