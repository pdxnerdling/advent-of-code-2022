from sys import argv
 
def get(q):
    x = q[0].replace(",", "").strip().split("=")
    x = int(x[1])
    y = q[1].replace(",", "").replace(":", "").strip().split("=")
    y = int(y[1])
    return (x,y)

def go(filename, line):
    f = open(filename, 'r')
    data = f.read().splitlines()
    line_beacons = set()
    no_beacon = set()
    for d in data:
        row = d.split()
        s = get(row[2:4])
        b = get(row[8:10])
        dist = abs(s[0]-b[0]) + abs(s[1]-b[1])
        if (s[1]+dist >= line and line >= s[1]-dist):
            line_add = dist-abs(s[1]-line)
            if b[1] == line:
                line_beacons.add(b[0])
            no_beacon.add(s[0])
            for i in range(1, line_add+1):
                no_beacon.add(s[0]+i)
                no_beacon.add(s[0]-i)
    for b in line_beacons:
        no_beacon.remove(b)
        pass
    print(len(no_beacon))
     
if __name__ == "__main__":
    filename = argv[1]
    #dir_sizes = go(filename, 10) 
    dir_sizes = go(filename, 2000000) 