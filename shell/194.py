# transpose_file.py
with open("file.txt") as f:
    # 读取每一行，并按空格分割成二维列表
    lines = [line.strip().split() for line in f.readlines()]