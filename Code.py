#-------------------------UTPC Begginer D.-----------------------------
#def count_distinct_sums(A, B):
#    possible_sums = set()
#
#    for x in range(A + 1):
#        for y in range(B + 1):
#            possible_sums.add(x + 3 * y)
#
#    return len([s for s in possible_sums if s > 0])
#
#A = int(input())
#B = int(input())
#print(count_distinct_sums(A, B))
#n = int(input())
#scores = [int(input()) for _ in range(n)]
#
#a1 = scores[0]
#sorted_scores = sorted(scores, reverse=True)
#
#if a1 in sorted_scores[:n//2]:
#   print("YES")
#else:
#    print("NO")



#---------------UTPC Begginer B.----------------------
# def calculate_checksum(card_number, n):
#     S = 0
#     for i in range(n - 2):
#         digit = int(card_number[i])
#         if (i + 1) % 2 == 1:
#             S += digit
#         else:
#             S += 2 * digit
#     return S % 100
#
#
# def solve(n, card_number):
#     expected_last_two_digits = int(card_number[-2:])
#     calculated_checksum = calculate_checksum(card_number, n)
#
#     if expected_last_two_digits == calculated_checksum:
#         return "YES", card_number
#
#     for i in range(n - 2):
#         original_digit = card_number[i]
#         for new_digit in '0123456789':
#             if new_digit == original_digit:
#                 continue
#             new_card_number = card_number[:i] + new_digit + card_number[i + 1:]
#             new_checksum = calculate_checksum(new_card_number, n)
#             if new_checksum == expected_last_two_digits:
#                 return "YES", new_card_number
#
#     return "NO", ""
#
#
# n = int(input())
# card_number = input()
#
# result, corrected_number = solve(n, card_number)
# print(result)
# if result == "YES":
#     print(corrected_number)



#----------------UTPC Begginer A.------------
# def max_twirls(n, s):
#     direction_map = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
#
#     target = [direction_map[c] for c in s]
#
#     best = {0: 0, 1: 0, 2: 0, 3: 0}
#
#     for i in range(n):
#         new_best = {}
#
#         for dir_facing in range(4):
#             left_turn = (dir_facing - 1) % 4
#             right_turn = (dir_facing + 1) % 4
#
#             new_best[left_turn] = max(new_best.get(left_turn, 0),
#                                       best[dir_facing] + (1 if left_turn == target[i] else 0))
#             new_best[right_turn] = max(new_best.get(right_turn, 0),
#                                        best[dir_facing] + (1 if right_turn == target[i] else 0))
#
#         best = new_best
#
#
#     return max(best.values())
#
#
# n = int(input())
# s = input()
#
# print(max_twirls(n, s))



#--------------Московскую 2017 и 1С олимпиада-------------------
# import sys
# import bisect
#
#
# def main():
#     n, q = map(int, sys.stdin.readline().split())
#
#     starts = []
#     ends = []
#
#     for _ in range(n):
#         l, r = map(int, sys.stdin.readline().split())
#         starts.append(l)
#         ends.append(r)
#
#     starts.sort()
#     ends.sort()
#
#     results = []
#     for _ in range(q):
#         t = int(sys.stdin.readline())
#
#         bears_start = bisect.bisect_right(starts, t)
#
#         bears_end = bisect.bisect_left(ends, t)
#
#         results.append(str(bears_start - bears_end))
#
#     sys.stdout.write("\n".join(results) + "\n")
#
#
# if __name__ == "__main__":
#     main()

#--------------------Московскую 2017 и 1С олимпиада----------------
# def find_mit_time(N):
#     k = 1
#     current_max = 5
#
#     while N > current_max:
#         k += 1
#         current_max *= 5
#
#     return "MIT time" if k == 1 else f"MIT^{k} time"
#
#
# T = int(input())
#
# for _ in range(T):
#     N = int(input())
#     print(find_mit_time(N))


#----------------------------B. M(IT)+--------------------------
# def is_repetitive(S):
#     while S:
#         if S.startswith("MIT"):
#             S = S[3:]
#         elif S.startswith("IT"):
#             S = S[2:]
#         else:
#             return "NO"
#     return "YES"
#
# def done():
#     T = int(input())
#     for _ in range(T):
#         input()
#         S = input().strip()
#         print(is_repetitive(S))
# done()


#---------------------Missing Numbers Queries----------------------
# import sys
# class FenwickTree:
#     def __init__(self, n):
#         self.n = n
#         self.tree = [0] * (n + 1)
#
#     def update(self, idx, delta):
#         while idx <= self.n:
#             self.tree[idx] += delta
#             idx += idx & -idx
#
#     def query(self, idx):
#         result = 0
#         while idx > 0:
#             result += self.tree[idx]
#             idx -= idx & -idx
#         return result
#
#     def range_query(self, left, right):
#         return self.query(right) - self.query(left - 1)
#
#
# def solve():
#     N, Q = map(int, input().split())
#     arr = list(map(int, input().split()))
#
#     bit = [FenwickTree(N) for _ in range(N + 1)]
#
#     for i in range(N):
#         bit[arr[i]].update(i + 1, 1)
#
#     result = []
#
#     for _ in range(Q):
#         query = list(map(int, input().split()))
#
#         if query[0] == 1:
#
#             x = query[1]
#             y = query[2]
#             old_value = arr[x - 1]
#
#             if old_value != y:
#                 bit[old_value].update(x, -1)
#                 bit[y].update(x, 1)
#                 arr[x - 1] = y
#
#         elif query[0] == 2:
#             l = query[1]
#             r = query[2]
#
#             for num in range(1, N + 1):
#                 if bit[num].range_query(l, r) == 0:
#                     result.append(str(num))
#                     break
#
#     sys.stdout.write("\n".join(result) + "\n")
#
# solve()





#--------------------------G. Grid and Numbers Game ----------------------------
# def is_valid_move(N, M, grid, i, j):
#     current_value = grid[i][j]
#     if i > 0 and grid[i - 1][j] == current_value - 1:
#         return False
#     if i < N - 1 and grid[i + 1][j] == current_value - 1:
#         return False
#     if j > 0 and grid[i][j - 1] == current_value - 1:
#         return False
#     if j < M - 1 and grid[i][j + 1] == current_value - 1:
#         return False
#     return True
#
#
# def has_valid_move(N, M, grid):
#     for i in range(N):
#         for j in range(M):
#             if grid[i][j] > 0 and is_valid_move(N, M, grid, i, j):
#                 return True
#     return False
#
#
# def game_winner(N, M, grid):
#     odd_count = 0
#     for row in grid:
#         odd_count += sum(1 for x in row if x % 2 == 1)
#
#     if has_valid_move(N, M, grid):
#         if odd_count % 2 == 1:
#             return "YES"
#         else:
#             return "NO"
#     else:
#         return "NO"
#
# T = int(input())
# for _ in range(T):
#     N, M = map(int, input().split())
#     grid = [list(map(int, input().split())) for _ in range(N)]
#
#     print(game_winner(N, M, grid))

