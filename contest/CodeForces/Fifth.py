# s = {}
# firs_name = None
# max_score = float("-inf")
# for _ in range(int(input())):
#     name, score = input().split()
#     score = int(score)
#     if name in s:
#         s[name] += score
#     else:
#         s[name] = score
#
#     if s[name] > max_score:
#         max_score = s[name]
#         firs_name = name
#
# print(firs_name)
#

s = {}
score_log = []
firs_name = ""
max_score = float("-inf")
n = int(input())
for _ in range(n):
    name, score = input().split()
    score = int(score)
    if name in s:
        s[name] += score
    else:
        s[name] = score

    score_log.append((name, score))

    if s[name] > max_score:
        max_score = s[name]


s_ = {}
for name, score in score_log:
    if name in s_:
        s_[name] += score

    else:
        s_[name] = score

    if s_[name] == max_score:
        firs_name = name
        break


print(firs_name)
