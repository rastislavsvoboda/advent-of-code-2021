from datetime import datetime

# pypy3.exe .\save.py 15

start = datetime.now()
lines = open('16.in').readlines()


H = lines[0].strip()

# H="D2FE28"
# H="38006F45291200"
# H="EE00D40C823060"

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


# print(H)
l = len(H)
# print(l)
total_l = l * 4

B = bin(int(H, 16))[2:]
# print(B)

while len(B) < total_l:
    B = "0" + B
# print(B)
# print(len(B))
assert len(B) == 4 * len(H), "Wrong length"


def read(data, n):
    part = data[:n]
    return part


# def read_grp(data):
#     res = ""
#     prefix, data = read_raw(data, 1)
#     val, data = read_raw(data, 4)
#     res += val
#     while prefix == "1":
#         prefix, data = read_raw(data, 1)
#         val, data = read_raw(data, 4)
#         res += val
#     ret = int(res,2)
#     return ret, data

def to_dec(b):
    return int(b, 2)


def parse(data, versions):
    value = 0
    i = 0
    v = to_dec(read(data[i:], 3))
    i += 3
    versions.append(v)
    t = to_dec(read(data[i:], 3))
    i += 3

    if t == 4:
        # literal
        val = ""
        while True:
            p = read(data[i:], 1)
            i += 1
            v = read(data[i:], 4)
            i += 4
            val += v
            if p == "0":
                break
        value = to_dec(val)
    else:
        # operator
        subs = []

        l_t = read(data[i:], 1)
        i += 1

        if l_t == "0":
            pkt_len = to_dec(read(data[i:], 15))
            i += 15
            frame_end = i+pkt_len
            while i < frame_end:
                read_cnt, v = parse(data[i:frame_end], versions)
                i += read_cnt
                subs.append(v)
        else:
            pkt_cnt = to_dec(read(data[i:], 11))
            i += 11
            for _ in range(pkt_cnt):
                read_cnt, v = parse(data[i:], versions)
                i += read_cnt
                subs.append(v)

        if t == 0:
            value = sum(subs)
        elif t == 1:
            value = 1
            for v in subs:
                value *= v
        elif t == 2:
            assert len(subs) >= 1
            value = min(subs)
        elif t == 3:
            assert len(subs) >= 1
            value = max(subs)
        elif t == 5:
            assert len(subs) == 2
            value = 1 if subs[0] > subs[1] else 0
        elif t == 6:
            assert len(subs) == 2
            value = 1 if subs[0] < subs[1] else 0
        elif t == 7:
            assert len(subs) == 2
            value = 1 if subs[0] == subs[1] else 0

    return i, value


versions = []
_, val = parse(B, versions)
# print("part1")
print(sum(versions))  # 967
# print("part2")
print(val)  # 12883091136209

stop = datetime.now()
print("duration:", stop - start)
