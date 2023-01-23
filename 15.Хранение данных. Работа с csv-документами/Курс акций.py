import csv


def read_csv(path):
    with open('yndx_share_price.csv', 'r', encoding='utf-8') as file:
        lines = csv.reader(file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        head = next(lines)
        lines = list(lines)
        arr = []
        for line in lines:
            arr.append(int(line[0].split(',')[-1]))
        return arr


def rmax(b):
    n = len(b)
    b = [max(b) + 1] + b + [max(b) + 1]
    ans = [0] * (n + 2)
    st = [0]
    for i in range(1, n + 1):
        while not (b[st[-1]] > b[i]):
            k = st.pop()
            ans[k] = i - k
        st.append(i)
    return ans[1:n + 1]


def write_txt(a, path):
    with open(path, 'w') as out_file:
        print(*a, file=out_file)


if __name__ == "__main__":
    path1 = 'yndx_share_price.csv'
    path2 = 'predict.txt'
    write_txt(rmax(read_csv(path1)), path2)