from datetime import datetime

# pypy3.exe .\save.py 4

start = datetime.now()
text = open('4.in').read()
# text = open('4.ex1').read()


def get_data(text):
    nums = []
    boards = []
    first = True
    for grp in text.split('\n\n'):
        if first:
            nums = [int(x) for x in grp.split(',')]
            first = False
        else:
            entries = []
            for row in grp.split('\n'):
                entries.append(row)
            boards.append(parse_entry(entries))
    return nums, boards


def parse_entry(entries):
    rows = []
    for entry in entries:
        nums = [int(x) for x in entry.split()]
        rows.append(nums)

    return rows


def mark_number(num, mark, board):
    for r in range(5):
        for c in range(5):
            if board[r][c] == num:
                mark[(r, c)] = True


def has_five_matching(mark):
    for r in range(5):
        cnt = 0
        for c in range(5):
            if (r,c) in mark:
                cnt += 1
        if cnt == 5:
            return True
    
    for c in range(5):
        cnt = 0
        for r in range(5):
            if (r,c) in mark:
                cnt += 1
        if cnt == 5:
            return True

    return False


def sum_unmarked(mark, bingo):
    sum = 0
    for r in range(5):
        for c in range(5):
            if (r, c) not in mark:
                sum += int(bingo[r][c])
    return sum


def solve(text, part):
    nums, boards = get_data(text)
    # print(nums)

    # marks for boards
    M = []
    for i in range(len(boards)):
        M.append({})

    order = []
    for num in nums:
        for i, board in enumerate(boards):
            mark_number(num, M[i], board)
            if has_five_matching(M[i]) and i not in order:
                order.append(i)

        if part == 1:
            # until first winner
            if len(order) == 1:
                break
        else:
            # until all winners
            if len(order) == len(M):
                break

    # print("order of winners", order)
    board_index = order[-1]
    sum = sum_unmarked(M[board_index], boards[board_index])
    # print("sum of all unmarked numbers", sum)
    # print("the number that was just called", num)
    return sum * num


print(solve(text, 1))  # 23177
print(solve(text, 2))  # 6804

stop = datetime.now()
print("duration:", stop - start)
