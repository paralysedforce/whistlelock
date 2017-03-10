from pitch_track import track
from distance import edit_distance

track1 = track('./sample_data/all_star/trent/trent4.wav')
track2 = track('./sample_data/all_star/trent/trent2.wav')
print(edit_distance(track2, track1, 1, 1))
