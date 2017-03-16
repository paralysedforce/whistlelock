import numpy as np
import math

def edit_distance(s1, s2, del_cost, ins_cost, sub_cost_base, sub_cost = None):
    """Calculates Levenshtein distance between s1 and s2, with substitution
    costs given by the L1 norm"""
    d = np.zeros((len(s1)+1, len(s2)+1), dtype=int, order='F')
    m = len(s1) + 1; n = len(s2) + 1

    if not sub_cost:
        def sub_cost(c1, c2): return (del_cost+ins_cost)-(del_cost+ins_cost)*math.pow(sub_cost_base, -abs(c1 - c2))

    for i in range(m):
        d[i, 0] = i * del_cost
    for j in range(n):
        d[0, j] = j * ins_cost

    for jj in range(len(s2)):
#        if jj%100 == 0:
 #           print jj,"/",len(s2)
        for ii in range(len(s1)):
            i, j = ii + 1, jj + 1
            if s1[ii] == s2[jj]:
                d[i, j] = d[i-1, j-1]
            else:
#                print(s1[ii], s2[jj], sub_cost(s1[ii], s2[jj]))
                d[i, j] = min([d[i-1, j] + del_cost,
                    d[i, j-1] + ins_cost,
                    d[i-1, j-1]+ sub_cost(s1[ii], s2[jj])])
    return d[-1, -1]

import librosa
import pitch_track

def test_twinkle_trent():
#    a1 = np.array([1, 2, 3])
 #   a2 = np.array([1, 2, 9])
    results = np.zeros((3,3))
    for i in range(3):
        for j in range(3):
            f1 = 'sample_data/twinkle_twinkle/trent/trent%d.wav' % (i+1)
            f2 = 'sample_data/twinkle_twinkle/trent/trent%d.wav' % (j+1)
            tune1 = pitch_track.pitch_track(f1)
            tune2 = pitch_track.pitch_track(f2)
            print f1, f2

            results[i][j] = edit_distance(tune1, tune2, 1, 1, 2)
#            print(edit_distance(tune1, tune2, 100, 1))
    print results


def main():
    test_twinkle_trent()
#    print edit_distance(pitch_track.pitch_track('sample_data/twinkle_twinkle/trent/trent1.wav'), pitch_track.pitch_track('sample_data/twinkle_twinkle/trent/trent2.wav'), 1, 1)
 #   print edit_distance(pitch_track.pitch_track('sample_data/twinkle_twinkle/trent/trent2.wav'), pitch_track.pitch_track('sample_data/twinkle_twinkle/trent/trent1.wav'), 1, 1)

if __name__ == '__main__':
    main()
