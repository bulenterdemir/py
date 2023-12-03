def get_linedistance(points, line):
    #print("average(points)=", np.mean(points))
    #print("average(line)=", np.mean(lines))
    qabstand = 0
    for x in range(0, len(points)):
        #print("line(0)=", line[0])
        #print("points[x]=", points[x])
        #print("points[x][0]=", points[x][0])
        #print("points[x][1]=", points[x][1])
        a = ( 
                (line[0]*points[x][0]) +    #a.xi
                line[1] -                   #b
                points[x][1]                #yi
            ) ** 2
        qabstand += a
    return qabstand

def get_optimal_line(points):
    #print("s1=", sum(t[0] for t in points))
    xmean = sum(p[0] for p in points) / len(points)
    ymean = sum(p[1] for p in points) / len(points)
    #print("xmean=", xmean)
    #print("ymean=", ymean)
    a=0
    a = (sum( ((p[0]-xmean)*(p[1]-ymean))  for p in points)) / (sum( (p[0]-xmean)**2  for p in points))
    b = ymean - a * xmean
    return (a, b)

def distance_to_opt(points, lines):
    a = []
    for line in lines:
        a.append([get_linedistance(points, line), line])
    m = min(a)
    n = m[1]
    nqd = get_linedistance(points, n)
    
    o = get_optimal_line(points)
    oqd = get_linedistance(points, o) #quadratic distance of the optimal line
    
    diff = oqd - nqd    
    
    return diff

