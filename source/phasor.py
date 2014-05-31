from pippi import dsp
from matplotlib import pyplot as pp

xlen = 60

x = range(xlen)

points = dsp.wavetable('line', xlen) 
rpoints = dsp.breakpoint([ dsp.rand(-1, 1) for i in range(10) ], xlen)

pp.plot(x, rpoints,
    linestyle=' ',
    marker='x',
    color='b',
    label='Value from buffer'
)

pp.plot(x, points,
    linestyle='dotted',
    color='b',
    label='Phasor'
)

pp.xlabel('Samples')
pp.ylabel('Values')
pp.xlim(0, xlen - 1)
pp.xticks(range(xlen), ['' for i in range(xlen)])
pp.ylim(-1, 1)

pp.grid(True, which='major', linewidth=1.0, axis='y', alpha=0.25)

pp.legend()
pp.savefig("phasor.png")
