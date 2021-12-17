from datetime import datetime

# pypy3.exe .\save.py 16

start = datetime.now()
lines = open('16.in').readlines()

# hex
H = lines[0].strip()

# H = "D2FE28"
# H = "38006F45291200"
# H = "EE00D40C823060"

# part 1
# H="8A004A801A8002F478"
# H="620080001611562C8802118E34"
# H="C0015000016115A2E0802F182340"
# H="A0016C880162017C3686B18A3D4780"

# part 2
# H = "C200B40A82"
# H = "04005AC33890"
# H = "880086C3E88112"
# H = "CE00C43D881120"
# H = "D8005AC2A8F0"
# H = "F600BC2D8F"
# H = "9C005AC2F8F0"
# H = "9C0141080250320F1802104A08"


def toBin(h):
    return bin(int(h, 16))[2:].rjust(4, '0')


def product(lst):
    res = 1
    for x in lst:
        res *= x
    return res


def read(data, pos, size):
    val = data[pos:pos+size]
    # print(val)
    # val = "".join(val)
    return int(val, 2), pos+size


def parse(data, pos=0):
    global versions

    version, pos = read(data, pos, 3)
    versions.append(version)

    type_id, pos = read(data, pos, 3)
    if type_id == 4:
        value = 0
        prefix = 1
        while prefix == 1:
            prefix, pos = read(data, pos, 1)
            grp, pos = read(data, pos, 4)
            value = value*16 + grp
    else:
        sub_packets = []
        len_type_id, pos = read(data, pos, 1)
        if len_type_id == 0:
            pkt_len, pos = read(data, pos, 15)
            buf_end = pos+pkt_len
            while pos < buf_end:
                pkt, pos = parse(data, pos)
                sub_packets.append(pkt)
        else:
            pkt_cnt, pos = read(data, pos, 11)
            while len(sub_packets) < pkt_cnt:
                pkt, pos = parse(data, pos)
                sub_packets.append(pkt)

        if type_id == 0:
            value = sum(sub_packets)
        elif type_id == 1:
            value = product(sub_packets)
        elif type_id == 2:
            value = min(sub_packets)
        elif type_id == 3:
            value = max(sub_packets)
        elif type_id == 5:
            value = 1 if sub_packets[0] > sub_packets[1] else 0
        elif type_id == 6:
            value = 1 if sub_packets[0] < sub_packets[1] else 0
        elif type_id == 7:
            value = 1 if sub_packets[0] == sub_packets[1] else 0

    return value, pos


bins = "".join(map(toBin, H))
# bins = list(map(toBin, H))
# print(bins)
versions = []
val, rest = parse(bins)
# print(versions)
print(sum(versions))  # 967
print(val)  # 12883091136209


stop = datetime.now()
print("duration:", stop - start)
