c = R_01[peakIndex-1:peakIndex+2]
d_sub = (c[2] - c[0]) / (2 * (- c[0] + 2*c[1] - c[2]))
d_01 = peakIndex - zeroIndex + d_sub