class Solution:
    def validateCoupons(self, code, businessLine, isActive):
        valid_lines = ["electronics", "grocery", "pharmacy", "restaurant"]
        result = []

        for i in range(len(code)):
            if not isActive[i]:
                continue

            if businessLine[i] not in valid_lines:
                continue

            if len(code[i]) == 0:
                continue

            ok = True
            for ch in code[i]:
                if not (ch.isalnum() or ch == "_"):
                    ok = False
                    break

            if ok:
                result.append((businessLine[i], code[i]))

        order = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        }

        result.sort(key=lambda x: (order[x[0]], x[1]))

        ans = []
        for item in result:
            ans.append(item[1])

        return ans
