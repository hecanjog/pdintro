from pippi import dsp
from matplotlib import pyplot as pp

x = range(32)

d3 = [ dsp.randchoose([1,4,5,8]) for p in x ]

d7 = [ dsp.randint(1, 8) for p in x ]

pp.subplot(211)

pp.plot(x, d3, 
    marker='x', 
    linestyle=' ', 
    color='m', 
    label='2bit Dynamics'
)

pp.xlabel('Time')
pp.ylabel('Loudness')
#pp.grid(True)
pp.ylim(0, 9)
pp.yticks(range(9), ['', 'ppp', 'pp', 'p', 'mp', 'mf', 'f', 'ff', 'fff', 'ffff', ''])
pp.xlim(-1,32)
pp.xticks(range(34), [ '' for t in range(34) ])
pp.legend()

pp.subplot(212)

pp.plot(x, d7, 
    marker='o', 
    linestyle=' ', 
    color='b', 
    label='3bit Dynamics'
)

pp.xlabel('Time')
pp.ylabel('Loudness')
#pp.grid(True)
pp.ylim(0, 9)
pp.yticks(range(9), ['', 'ppp', 'pp', 'p', 'mp', 'mf', 'f', 'ff', 'fff', 'ffff', ''])
pp.xlim(-1,32)
pp.xticks(range(34), [ '' for t in range(34) ])
pp.legend()
pp.savefig("dynamics.png")
#pp.show()
