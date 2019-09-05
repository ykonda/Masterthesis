frames = get_overlapping_frames(data, frameSize)
for frame in frames:
    F, n, x = calcFft(frame)
