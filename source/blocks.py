from pippi import dsp
from matplotlib import pyplot as pp

xlen = 32

x = range(xlen)

sine = dsp.wavetable('sine2pi', xlen) 

control = dsp.breakpoint([ dsp.rand(-1, 1) for i in range(5) ], xlen)

blocks = [ sine[i % len(sine)] for i in range(xlen) ]

pp.bar(x, control, 
    width=0.8,
    color='m', 
    label='Control rate data'
)

pp.plot(x, blocks,
    linestyle='dotted',
    color='b',
    label='Signal rate data'
)

pp.xlabel('Blocks')
pp.ylabel('Values')
pp.xlim(0, 31)
pp.xticks(range(32), ['' for i in range(32)])
pp.ylim(-1, 1)

pp.grid(True, which='major', linewidth=1.0, axis='x', alpha=0.25)

pp.legend()
pp.savefig("blocks.png")
