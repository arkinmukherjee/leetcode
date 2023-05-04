from collections import deque

class Solution:
    def calPoints(self, operations) -> int:
        scores = deque()

        for s in operations:
            match s:
                case '+':
                    last = int(scores.pop())
                    second_last = int(scores.pop())
                    new_score = last + second_last
                    scores.append(second_last)
                    scores.append(last)
                    scores.append(new_score)
                case 'D':
                    last = int(scores.pop())
                    new_score = int(last) * 2
                    scores.append(last)
                    scores.append(new_score)
                case 'C':
                    scores.pop()
                case _:
                    scores.append(int(s))

        sum = 0
        for i in range(0, len(scores)):
            sum = sum + int(scores.pop())

        return sum


def main():
    solution = Solution()
    ops = ["5", "2", "C", "D", "+"]
    sum = solution.calPoints(ops)
    print(sum)


if __name__ == "__main__":
    main()
