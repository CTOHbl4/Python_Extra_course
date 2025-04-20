def fill_line(matr: list[list[int]], line: list[int]) -> None:
    matr.append(line.copy())


def read_matr() -> list[list[int]]:

    matr: list[list[int]] = []

    line = list(map(int, input().split(", ")))

    fill_line(matr, line)

    dim: int = len(line)

    for _ in range(dim - 1):
        line = list(map(int, input().split(", ")))
        fill_line(matr, line)

    return matr


def calc_det2x2(a11: int, a12: int, a21: int, a22: int) -> int:
    return a11*a22 - a12*a21


def switch_lines_nonzero(matr: list[list[int]]) -> int:
    idx: int = 0
    for e in range(1, len(matr)):
        if matr[e][0] != 0:
            idx = e
            break

    if not idx:
        return idx

    matr[0], matr[idx] = matr[idx], matr[0]
    return -1


def step(matr: list[list[int]]) -> tuple[list[list[int]], int, int]:
    new_matr: list[list[int]] = []

    mul = 1
    if matr[0][0] == 0:
        if not (mul := switch_lines_nonzero(matr)):
            return ([[0]], 0, 1)

    d_mul = matr[0][0]

    for x in range(1, len(matr)):
        line: list[int] = []
        for y in range(1, len(matr)):
            line.append(calc_det2x2(matr[0][0], matr[0][y], matr[x][0], matr[x][y]))
        fill_line(new_matr, line)

    return new_matr, mul, d_mul


def main() -> None:
    matr = read_matr()

    mul = 1
    D = 1
    while len(matr) > 1:
        matr, step_mul, d_mul = step(matr)
        deg = (len(matr) - 1)

        if deg > 0 and matr[0][0] != 0:
            D *= d_mul ** deg

        mul *= step_mul

    print(matr[0][0]//D*mul)


if __name__ == "__main__":
    main()
