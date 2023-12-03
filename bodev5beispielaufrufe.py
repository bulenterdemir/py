from bodev5self import *

points=[(-2,2), (1,3), (2,2), (6,-2)]
lines=[(1,1), (-1,4)]
#points=[(1,2), (3,4), (5,6), (7,8)]
#lines=[(1,2), (2,4)]
d0=get_linedistance(points, lines[0])
d1=get_linedistance(points, lines[1])
print([d0, d1])

(a, b) = get_optimal_line(points)
print(a)
print(b)

c = get_linedistance(points, (a,b))
print(c)

d = distance_to_opt(points,lines)
print(d)