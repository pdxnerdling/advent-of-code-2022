from sys import argv

def get_marker(input_string, marker_length):
    input_string = list(input_string)
    for i in range(len(input_string)-marker_length):
        if len(set(input_string[i:i+marker_length])) == marker_length:
            return i+marker_length
    return 0

def get_packet_and_message_markers(filename):
    f = open(filename, 'r')
    for line in f:
        packet_marker = get_marker(line, 4)
        message_marker = get_marker(line, 14)
        print('(Part1)Packet Marker: ' + str(packet_marker))
        print('(Part2)Message Marker: ' + str(message_marker))
        print()

if __name__ == "__main__":
    filename = argv[1]
    get_packet_and_message_markers(filename)