from sys import argv
import timeit
 
def get(q):
    x = q[0].replace(",", "").strip().split("=")
    x = int(x[1])
    y = q[1].replace(",", "").replace(":", "").strip().split("=")
    y = int(y[1])
    return (x,y)

def determine_position(filename, line):
    f = open(filename, 'r')
    data = f.read().splitlines()
    manifest = []
    for d in data:
        row = d.split()
        s = get(row[2:4])
        b = get(row[8:10])
        manifest.append([s, b])
    for i in range(line):
        mapping = []
        for m in manifest:
            s = m[0]
            b = m[1]
            dist = abs(s[0]-b[0]) + abs(s[1]-b[1])
            if (s[1]+dist >= i and i >= s[1]-dist):
                line_add =abs(dist-abs(s[1]-i))
                low = max(0, s[0]-line_add)
                high = min(line, s[0]+line_add)
                mapping.append([low, high]) 
                mapping.append([low, high])
        mapping.sort(key = lambda row: row[0])
        high = 0
        low = 0
        for pair in mapping:
            if high == line:
                break
            if low > pair[0]:
                break
            if high+1 < pair[0]:
                return([high+1, i])
            if pair[1] > high:
                high = pair[1]

def execute(args):
    filename = args[1]
    #dir_sizes = go(filename, 20) 
    position = determine_position(filename, 4000000) 
    print(position[0]*4000000+position[1])

if __name__ == "__main__":
    print(timeit.timeit(lambda: execute(argv), number=1)/60)