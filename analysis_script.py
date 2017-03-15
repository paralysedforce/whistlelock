import os, random
import pdb
from collections import namedtuple
from pitch_track import track
from distance import edit_distance
import pickle

def match_songs():
    random.seed(42)
    pitch_tracks = dict()
    basedir = os.path.join(os.getcwd(), 'sample_data')

    print('Parsing through test dir...')
    for subdir in os.listdir(basedir):
            print(subdir)
            os.chdir(os.path.join(basedir, subdir, 'trent'))
            cwd = os.getcwd()
            for f in os.listdir(cwd):
                    tempdir = os.path.join(cwd, f)
                    pitch_tracks[tempdir] = track(tempdir)

            os.chdir(os.path.join(basedir, subdir, 'vyas'))
            cwd = os.getcwd()
            for f in os.listdir(cwd):
                    tempdir = os.path.join(cwd, f)
                    pitch_tracks[tempdir] = track(tempdir)
    print("Done.")

    trackdata = namedtuple('trackdata', ['title_match', 'artist_match',
        'track1', 'track2', 'distance'])
    output = []
    maxiter = 10
    progress = int(maxiter / 10)

    for i in range(maxiter):
            if i % progress == 0:
                num = int(i / progress)
                inv = 10 - num
                print(num * "x" + " " * inv + "|")

            track_one = random.choice(list(pitch_tracks.keys()))
            track_one_title = track_one.split('/')[-3]
            track_one_artist = track_one.split('/')[-2]

            temp = random.random()
            if temp > .5:
                track_two = random.choice(list(pitch_tracks.keys()))
            else:
                if temp > .25:
                    tempdir = os.path.join(basedir, track_one_title, 'trent')
                else:
                    tempdir = os.path.join(basedir, track_one_title, 'vyas')

                tempfile = random.choice(os.listdir(tempdir))
                track_two = os.path.join(tempdir, tempfile)

            track_two_title = track_two.split('/')[-3]
            track_two_artist = track_two.split('/')[-2]

            data = trackdata(track_one_title==track_two_title, 
                    track_one_artist==track_two_artist, 
                    track_one,
                    track_two,
                    edit_distance(pitch_tracks[track_one], pitch_tracks[track_two], 1, 1))

            output.append(data)
    return output

def main():
    output = match_songs()
    with open('output.pickle', 'w') as f:
        pickle.dump(output, f)

if __name__ == '__main__':
    main()

