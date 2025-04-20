import re

cas0 = re.compile(r"-?[0-9]+")
cas1 = re.compile(r"-?%0x[0-9a-f]{1,16}")
cas2 = re.compile(r"-?%0o[0-7]{1,8}")
cas3 = re.compile(r"-?%0b[01]{1,20}")

cases = [cas0, cas1, cas2, cas3]


def match_cases(line):
    for cas in cases:
        if cas.fullmatch(line):
            return True
    return False


num = input()

res = match_cases(num)
res0, res1, res2 = False, False, False

if not res:
    if "E" in num:
        main, exp = num.split("E")

        if "." in main:
            main0, main1 = main.split(".")
        else:
            main0, main1 = main, "1"

        res0 = match_cases(main0)

        if main1:
            if "%" in main1:
                while main1[0] == "0":
                    main1 = main1[1:]
            if main1[0] == "-":
                res1 = False
            else:
                res1 = match_cases(main1)

        if exp == "":
            res2 = True
        else:
            if exp[0] not in ("-", "+"):
                res2 = False
            else:
                res2 = match_cases(exp[1:])

if res or res1 and res2 and res0:
    print("YES")
else:
    print("NO")
