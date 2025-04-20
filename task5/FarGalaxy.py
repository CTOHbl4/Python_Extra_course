all_stars = dict()

star_idx = 0
while s := input():
    one_star = s.split()
    if len(one_star) <= 1: # no spaces
        break
    x = float(one_star[0])
    y = float(one_star[1])
    z = float(one_star[2])
    star = one_star[3] + "/" + str(star_idx)
    all_stars[star] = (x, y, z)
    star_idx += 1

dist_res, i_res, j_res = 0, 0, 0

for i in all_stars.keys():
    for j in all_stars.keys():

        (x1, y1, z1) = all_stars[i]
        (x2, y2, z2) = all_stars[j]
        dist = (x1 - x2)**2 + (y1-y2)**2 + (z1-z2)**2
        if dist > dist_res:
            dist_res, i_res, j_res = dist, i , j

name1 = i_res.split("/")[0]
name2 = j_res.split("/")[0]
print(*sorted((name1, name2)))
