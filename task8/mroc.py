import re


def mro_checker():
    reg = re.compile(r"(\w+)\s*[\(\),:]")
    cls_line = re.compile(r"\s*class\s*[\w,\(\)\s]+:")

    flag = True
    dct_classes = {}
    while line := input():
        if not flag:
            break

        if cls_line.match(line):
            res = reg.findall(line)
            cur_parents = res[1:]
            dct_classes[res[0]] = cur_parents
            new_parents = []
            for idx, cls in enumerate(cur_parents):
                check = dct_classes[cls]
                lst_check_order = []

                # simplify parents
                if cls not in new_parents and not len(check):
                    new_parents.append(cls)
                for par in check:
                    # simplify parents
                    if par not in new_parents:
                        new_parents.append(par)
                    if par in cur_parents:
                        cur_par_idx = cur_parents.index(par)
                        # children before parents
                        if cur_par_idx < idx:
                            flag = False
                            break
                        else:
                            lst_check_order.append(cur_par_idx)
                # correctness of order
                for i in range(len(lst_check_order)-1):
                    if lst_check_order[i] >= lst_check_order[i+1]:
                        flag = False
                        break
            dct_classes[res[0]] = new_parents

    while line:
        line = input()

    return flag


if mro_checker():
    print("Yes")
else:
    print("No")
