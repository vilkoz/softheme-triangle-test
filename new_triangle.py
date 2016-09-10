import random
import time

while(1):
    print("Choose triangle:\n 1) simple_triangle.txt\n 2) triangle.txt\n 3) easy.txt\n 4) generate")
    choise = input(">")
    if choise == '1':
        file = 'simple_triangle.txt'
        break
    elif choise == '2':
        file = 'triangle.txt'
        break
    elif choise == '3':
        file = 'easy.txt'
        break
    elif choise == '4':
        row = 1
        outp = ''
        rows = int(input('Enter number of rows >'))
        f = open('gen_tri.txt', 'w')
        for i in range(0, rows):
            for j in range(0, row):
                outp = outp+' '+str(random.randint(0, 99)).zfill(2)
            f.write(outp+'\n')
            row += 1
            outp = ''
        file = 'gen_tri.txt'
        break
    else:
        print("Invalid input, try again")


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
def progress(workdone):
    print("\rProgress: [{0:50s}] {1:.1f}%".format('#' * int(workdone * 50), workdone*100), end="", flush=True)

def clear_line(line_tmp):
    dirt_line = line_tmp.split(' ')
    line_list = []
    for i in dirt_line:
        line_list.append(i.replace('\n', ''))
    return line_list

bold = "\033[1m"
reset = "\033[0;0m"
finished = 0
maxsum = 0
line_list = []
line_list1 = []
times = 0
begins = []
begin_max = []
max_pos = []
f = open(file, 'r')
gopa = f.readlines()
f.close()
pos_begin = 0
workdone = 0.0

print('starting calculation')
while(1):

    # line_list = clear_line(gopa[0])
    # triangle_sum += line_list[pos]
    pos = pos_begin
    path = []
    max_numbers = []
    triangle_sum = 0
    maxsum = 0

    for j in range(1, len(gopa)+1):
        if finished:
            print('position is:'+str(pos))
        line = gopa[-j]
        line_list = clear_line(line)
        # print(str(line_list))

        if pos-1 < 0:
            start_ind = 0
        else:
            start_ind = pos-1
        if pos+1 > len(line_list):
            end_ind = len(line_list)
        else:
            end_ind = pos+1

        newmax = max(line_list[start_ind:end_ind+1])
        triangle_sum += int(newmax)
        pos_old = pos
        for i in range(0, len(line_list)):
            if newmax == line_list[i]:
                pos = i
                if pos-1 == pos_old or pos == pos_old or pos+1 == pos_old:
                    break
                else:
                    continue

        path.append(int(pos))
        max_numbers.append(max(line_list))
    if finished:
        print('max numbers: '+str(' '.join(max_numbers)))
    path.reverse()
    if finished:
        print('path is: '+str(path))
    if finished:
        print('sum is:'+str(triangle_sum))
    for i in range(0, len(max_numbers)):
        maxsum += int(max_numbers[i])
    if finished:
        print('sum of max_numbers is:'+str(maxsum))
    fit = (triangle_sum/maxsum)*100
    if finished:
        print('maximum fit is: '+str(fit)+"%")

    line_num = 0
    for line in gopa:
        line_list = clear_line(line)
        max_line = max(line_list)
        for i in range(0, len(line_list)):
            if line_list[i] == max_line:
                line_list[i] = color.RED+bold+str(line_list[i])+color.END
        line_list[path[line_num]] = color.GREEN+str(line_list[path[line_num]])+color.END

        output = ' '.join(line_list)
        if finished:
            print(output)
        line_num += 1
    max_pos.append(int(triangle_sum))
    if not finished:
        progress(float(pos_begin/len(gopa)))
    if finished:
        break
    if pos_begin == len(gopa):
        finished = 1
        maximum_sum = max(max_pos)
        for i in range(0, len(max_pos)):
            if max_pos[i] == maximum_sum:
                pos_begin = i
    if not finished:
        pos_begin += 1
