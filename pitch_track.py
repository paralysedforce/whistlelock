from __future__ import division, print_function
import aubio
import sys
import matplotlib.pyplot as plt
import numpy as np
import distance

def track(fn):
    sr = 44100
    n_fft = 4096
    hop_size = 512

    tolerance = .8

    pitch_o = aubio.pitch('yinfft', n_fft, hop_size, sr)
    pitch_o.set_unit('midi')
    pitch_o.set_tolerance(tolerance)

    strings = []
    pitches = []
    confidences = []
    time_plt = []
    pitch_plt = []

    s = aubio.source(fn, sr, hop_size)
    total_frames = 0
    while True:
        samples, read = s()
        pitch = pitch_o(samples)[0]
        confidence = pitch_o.get_confidence()
        time = total_frames / sr

    #    print("%f %f %f" % (time, pitch, confidence))
        pitches.append(pitch)
        confidences.append(confidence)

        if confidence > .95 and pitch >= 1:
            time_plt.append(time)
            pitch_plt.append(pitch)

        total_frames += read
        if read < hop_size: 
            break

    # Processing
    pitch_plt = np.array(pitch_plt, dtype=np.float64)
    pitch_median = np.median(pitch_plt[:50])
    pitch_plt -= pitch_median
    time_plt = np.array(time_plt)
    time_plt -= time_plt[0]

    strings.append(np.array_str(pitch_plt)[1:pitch_plt.size-1])

    # intervals = np.zeros(pitch_plt.size-1)
    # for j in range(intervals.size):
    #     intervals[j] = pitch_plt[j+1]-pitch_plt[j]

    #plt.plot(time_plt, pitch_plt)
    #plt.show()

    return pitch_plt
  

def calculate_vectors(time_arr, pitch_arr):
    """
    Convert frame by frame data into a series of vectors containing information
    between frames.

    Inputs:
    time_arr: 1D numpy array containing the time in seconds of the sample at the
        ith index
    pitch_arr: 1D numpy array containing the sampled pitch/frequncy at the ith
        index

    --------------------------
    Output:
    """
    N = len(time_arr)
    vectors = np.zeros((N-1, 3))

    if len(pitch_arr) != N:
        raise ValueError

    for i in range(N - 1):
        dt = time_arr[i+1] - time_arr[i]
        f0 = pitch_arr[i]
        df = pitch_arr[i+1] - pitch_arr[i]

        vector = np.array([dt, f0, df])
        vectors[i, :] = vector
    return vectors

if __name__ == '__main__':
    main()
