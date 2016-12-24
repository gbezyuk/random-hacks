from math import pi

def frange(x, y, tabulation_step):
  while x < y:
    yield x
    x += tabulation_step

def s(r):
    return r * r * pi

def ds(r0, r1):
    return abs(s(r1) - s(r0))

def tabulate(r0, dr, r1):
    for r in frange(r0, r1, dr):
        yield (r, s(r), ds(r+dr, r))

print "] r0 = 10, r1 = 20"
print "tabulating with dr = 2.0"
for line in tabulate(10.0, 2.0, 20.0):
    print line

print "tabulating with dr = 1.0"
for line in tabulate(10.0, 1.0, 20.0):
    print line

print "tabulating with dr = .5"
for line in tabulate(10.0, .5, 20.0):
    print line