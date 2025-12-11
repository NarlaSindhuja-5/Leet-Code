class Solution:
    def countCoveredBuildings(self, n, buildings):
        row = {}
        col = {}

        for x, y in buildings:
            if y not in row:
                row[y] = []
            row[y].append(x)

            if x not in col:
                col[x] = []
            col[x].append(y)

        for y in row:
            row[y].sort()
        for x in col:
            col[x].sort()

        covered = 0

        for x, y in buildings:
            xs = row[y]
            ys = col[x]

            xi = xs.index(x)
            yi = ys.index(y)

            has_left = xi > 0
            has_right = xi < len(xs) - 1
            has_down = yi > 0
            has_up = yi < len(ys) - 1

            if has_left and has_right and has_down and has_up:
                covered += 1

        return covered
