with open('in_file.txt', mode='r', encoding='utf-8') as f:
    ryad = f.read()

    kol = 0
    for line in ryad.split("\n"):
        if line:
            num, mat, num2 = line.split()
            num = int(num)
            num2 = int(num2)
            if mat == '+' and kol == 0:
                otv = num + num2
                with open('out_file.txt', mode='a', encoding='utf-8') as p:
                    p.write(str(num)) + p.write(' + ') + p.write(str(num2)) + p.write(' = ') + p.write(
                        str(otv))
            if mat == '-' and kol == 0:
                otv = num - num2
                with open('out_file.txt', mode='a', encoding='utf-8') as p:
                    p.write(str(num)) + p.write(' - ') + p.write(str(num2)) + p.write(' = ') + p.write(
                        str(otv))
            if mat == '*' and kol == 0:
                otv = num * num2
                with open('out_file.txt', mode='a', encoding='utf-8') as p:
                    p.write(str(num)) + p.write(' * ') + p.write(str(num2)) + p.write(' = ') + p.write(
                        str(otv))
            if mat == '/' and kol == 0:
                otv = num + num2
                with open('out_file.txt', mode='a', encoding='utf-8') as p:
                    p.write(str(num)) + p.write(' / ') + p.write(str(num2)) + p.write(' = ') + p.write(
                        str(otv))
            if mat == '+' and kol != 0:
                otv = num + num2
                with open('out_file.txt', mode='a', encoding='utf-8') as p:
                    p.write('\n') + p.write(str(num)) + p.write(' + ') + p.write(str(num2)) + p.write(' = ') + p.write(
                        str(otv))
            if mat == '-' and kol != 0:
                otv = num - num2
                with open('out_file.txt', mode='a', encoding='utf-8') as p:
                    p.write('\n') + p.write(str(num)) + p.write(' - ') + p.write(str(num2)) + p.write(' = ') + p.write(
                        str(otv))
            if mat == '*' and kol != 0:
                otv = num * num2
                with open('out_file.txt', mode='a', encoding='utf-8') as p:
                    p.write('\n') + p.write(str(num)) + p.write(' * ') + p.write(str(num2)) + p.write(' = ') + p.write(
                        str(otv))
            if mat == '/' and kol != 0:
                otv = num + num2
                with open('out_file.txt', mode='a', encoding='utf-8') as p:
                    p.write('\n') + p.write(str(num)) + p.write(' / ') + p.write(str(num2)) + p.write(' = ') + p.write(
                        str(otv))
        kol += 1

