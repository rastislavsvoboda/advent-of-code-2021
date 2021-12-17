from datetime import datetime

# pypy3.exe .\save.py 16

start = datetime.now()
lines = open('16.in').readlines()

# hex
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
hex_len = len(H)
bin_len = hex_len * 4

# binary
B = bin(int(H, 16))[2:]
# print(B)
missing_0_cnt = bin_len - len(B)

B = ("0" * missing_0_cnt) + B
# print(B)
assert len(B) == bin_len, "Wrong length"


def read(data, size):
    val, rest = data[:size], data[size:]
    return int(val, 2), rest


def parse(data, level, versions):
    space = " " * level
    # print(space + "parse:", data)
    value = 0

    version, data = read(data, 3)
    # print(space + "version:", version)
    versions.append(version)

    type_id, data = read(data, 3)

    if type_id == 4:
        # literal
        prefix = 1
        while prefix == 1:
            prefix, data = read(data, 1)
            group, data = read(data, 4)
            value = value * 16 + group
    else:
        # operator
        sub_packets = []

        len_type_id, data = read(data, 1)

        if len_type_id == 0:
            pkt_len, data = read(data, 15)
            # print(space + "pkt_len:", pkt_len)
            data, sub_data = data[pkt_len:], data[:pkt_len]
            while len(sub_data) > 0:
                val, sub_data = parse(sub_data, level + 1, versions)
                sub_packets.append(val)
        else:
            pkt_cnt, data = read(data, 11)
            # print(space + "pkt_cnt:", pkt_cnt)

            for x in range(pkt_cnt):
                # print(space + "sub pkt:", x)
                val, data = parse(data, level + 1, versions)
                # print(space + "val:", val)
                sub_packets.append(val)

        if type_id == 0:
            value = sum(sub_packets)
        elif type_id == 1:
            value = 1
            for v in sub_packets:
                value *= v
        elif type_id == 2:
            assert len(sub_packets) >= 1
            value = min(sub_packets)
        elif type_id == 3:
            assert len(sub_packets) >= 1
            value = max(sub_packets)
        elif type_id == 5:
            assert len(sub_packets) == 2
            value = 1 if sub_packets[0] > sub_packets[1] else 0
        elif type_id == 6:
            assert len(sub_packets) == 2
            value = 1 if sub_packets[0] < sub_packets[1] else 0
        elif type_id == 7:
            assert len(sub_packets) == 2
            value = 1 if sub_packets[0] == sub_packets[1] else 0

    # print(space + "packet:", value)
    return value, data


versions = []
value, rest = parse(B, 0, versions)
# print(rest)
assert rest == ("0" * len(rest)), "Not all data consumed, some 1 in the rest"
# print("part1")
print(sum(versions))  # 967
# print("part2")
print(value)  # 12883091136209


stop = datetime.now()
print("duration:", stop - start)
