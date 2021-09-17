# https://www.acmicpc.net/problem/5532

vac_day = int(input())
total_math_page = int(input())
total_lang_page = int(input())
day_math_page = int(input())
day_lang_page = int(input())

print(int(vac_day-(max(total_math_page/day_math_page, total_lang_page/day_lang_page))))
