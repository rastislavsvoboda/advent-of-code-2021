from datetime import datetime
from itertools import islice
from collections import namedtuple

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

Packet = namedtuple('Packet', ['version', 'type_id', 'value', 'sub_packets'])


def gen_bin(hex_iter):
    for hex_val in hex_iter:
        bin_val = bin(int(hex_val, 16))[2:]
        missing_0_cnt = 4 - len(bin_val)
        for _ in range(missing_0_cnt):
            yield "0"
        for b in bin_val:
            yield b


def product(lst):
    res = 1
    for x in lst:
        res *= x
    return res


def gt(lst):
    return 1 if lst[0] > lst[1] else 0


def lt(lst):
    return 1 if lst[0] < lst[1] else 0


def eq(lst):
    return 1 if lst[0] == lst[1] else 0


def take(iterable, n):
    return islice(iterable, 0, n, 1)


def read_next(bin_iter, size):
    try:
        val = ""
        for _ in range(size):
            val += next(bin_iter)
        return int(val, 2)
    except StopIteration:
        # print("StopIteration")
        return None


def read_literal(bin_iter):
    value = 0
    prefix = 1
    while prefix == 1:
        prefix = read_next(bin_iter, 1)
        group = read_next(bin_iter, 4)
        value = value * 16 + group
    return value


def read_packets_by_len(bin_iter, size):
    packets = []
    sub_iter = take(bin_iter, size)

    while True:
        sub_packet, sub_iter = read_packet(sub_iter)
        if sub_packet == None:
            break
        packets.append(sub_packet)
    return packets


def read_packets_by_cnt(bin_iter, cnt):
    packets = []
    for x in range(cnt):
        # print(space + "sub pkt:", x)
        sub_packet, bin_iter = read_packet(bin_iter)
        if sub_packet == None:
            break
        packets.append(sub_packet)
    return packets


def read_packet(bin_iter):
    sub_packets = []
    value = 0

    ver = read_next(bin_iter, 3)
    if ver == None:
        return None, bin_iter

    type_id = read_next(bin_iter, 3)

    if type_id == 4:
        value = read_literal(bin_iter)
    else:
        len_type_id = read_next(bin_iter, 1)
        if len_type_id == 0:
            pkt_len = read_next(bin_iter, 15)
            # print("pkt_len:", pkt_len)
            sub_packets += read_packets_by_len(bin_iter, pkt_len)
        else:
            pkt_cnt = read_next(bin_iter, 11)
            # print("pkt_cnt:", pkt_cnt)
            sub_packets += read_packets_by_cnt(bin_iter, pkt_cnt)

        ops = {
            0: sum,
            1: product,
            2: min,
            3: max,
            # 4 is literal
            5: gt,
            6: lt,
            7: eq,
        }

        value = ops[type_id](list(map(lambda pckt: pckt.value, sub_packets)))

    return Packet(ver, type_id, value, sub_packets), bin_iter


def traverse(packet, versions):
    versions.append(packet.version)
    for p in packet.sub_packets:
        traverse(p, versions)


packet, rest = read_packet(gen_bin(iter(H)))

# tail = "".join(rest)
# print(tail)
# assert tail == ("0" * len(tail)), "Not all data consumed, some 1 in the rest"

versions = []
traverse(packet, versions)
# print("versions:", versions)
print(sum(versions))
print(packet.value)

# 967
# 12883091136209


stop = datetime.now()
print("duration:", stop - start)
