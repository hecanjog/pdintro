from pippi import dsp
from matplotlib import pyplot as pp

xlen = 32

x = range(xlen)

sine = dsp.wavetable('sine2pi', xlen) 

left = [ sine[i % len(sine)] for i in range(xlen) ]
right = [ sine[(i + 10) % len(sine)] for i in range(xlen) ]

pp.bar(x, left, 
    width=0.4,
    color='m', 
    label='Left'
)

pp.bar([xx + 0.5 for xx in x ], right, 
    width=0.4,
    color='b', 
    label='Right'
)

pp.xlabel('Samples')
pp.ylabel('Amplitude')
pp.xlim(0, 31)
pp.ylim(-1, 1)

pp.legend()
pp.savefig("stereo.png")
