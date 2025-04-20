lst = []
lst_sorted = []
while s := input():
    t = eval(s)
    lst.append(t)
    lst_sorted.append(sorted(t))

lst_res = []
while lst_sorted:
    res_idx = 0
    for idx, cur_tpl in enumerate(lst_sorted):
        for new_tpl in lst_sorted[idx+1:]:
            if (cur_tpl[0] <= new_tpl[0] and cur_tpl[1] <= new_tpl[1] and cur_tpl[2] <= new_tpl[2] and cur_tpl != new_tpl):
                break
        else:
            res_idx = idx
            break

    lst_res.append(lst[res_idx])
    lst_sorted.pop(res_idx)
    lst.pop(res_idx)

for e in lst_res:
    print(*e, sep=", ")
