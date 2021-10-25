import heapq
from datetime import datetime

def get_priority(duty, off_percent):
    '''
    duty가 주어지면, 해당 duty가 다음 날 shift 탐색을 위해 힙에 더해질 때의 우선순위를 계산
    우선순위는 조건 적합성을 수치화한 것으로, 낮을수록 조건에 부합하는 (우선순위가 높은) duty임을 의미함
    '''
    d, e, n = (0, 0, 0)  # day, evening, night 근무 수 초기화

    for shift in duty[2:]:  # 현재까지 짠 해당 월의 duty에 대해
        if shift == 'T':
            d += 1
        elif shift == "E":
            e += 1
        elif shift == "N":
            n += 1

    max_shift = max(d, e, n)
    rest_percent = (len(duty[2:]) - sum([d, e, n])) / len(duty[2:]) 
    
    # DAY, EVENING, NIGHT 근무 수의 편차가 클수록 우선순위가 낮아짐
    # 누적 OFF가 0에서 떨어질수록 우선순위가 낮아짐
    if duty[2:].count("N") == 8:  # NIGHT 근무 8일으로 RECOVERY OFF 필요
        # NIGHT 근무가 8일인 경우 우선순위가 비교적 낮아짐 (+20)
        priority = ((3 * max_shift) - (d + e + n) + abs(rest_percent - off_percent) * 100 + 20)
    else:
        priority = ((3 * max_shift) - (d + e + n) + abs(rest_percent - off_percent) * 100)

    return priority


def get_final_duty(queue, off_percent, final_duties):
    while queue:
        now = heapq.heappop(queue)
        now_priority, now_days_left, now_duty = now[0], now[1], now[2]  # 현재까지 짠 duty

        # 조건을 만족하는 duty 찾음
        if now_days_left == 0:
            heapq.heappush(final_duties, (now_priority, now_duty[2:]))
            continue

        # 조건을 만족하는 duty 충분히 찾음
        if len(final_duties) >= 10:
            return

        # 월 NIGHT 횟수에 따른 가지치기
        if now_duty[2:].count("N") >= 9:
            continue

        for next_shift in ['T', 'E', 'N', 'O']:
            # 전일 근무에 따른 가지치기
            if now_duty[-2] == now_duty[-1] == next_shift:
                continue
            if now_duty[-1] == 'E' and next_shift == 'T':
                continue
            if now_duty[-1] == 'N':  # 전날이 NIGHT
                if now_duty[-2] == 'N':  # 전전날도 NIGHT
                    if next_shift != 'O':  # 다음은 무조건 OFF
                        continue
                else:
                    if next_shift != 'N':
                        continue

            if 'O' not in now_duty[-5:] and next_shift != 'O':
                continue

            if now_duty[-2] == 'N' and now_duty[-1] == 'O' and next_shift == 'T':
                continue

            combined_duty = now_duty + next_shift  # 다음날 shift를 추가한 새 duty

            next_priority = get_priority(combined_duty, off_percent)  # 전체 duty의 우선순위 (조건 적합성) 계산

            heapq.heappush(queue, (next_priority, now_days_left - 1, combined_duty))


def makes_duty(prev_month_duty, year, month):
    

    queue = []  # duty 찾기 위한 우선순위 큐
    best = dict()  # 각 듀티 순서 중 가장 좋은 경우 저장
    final_duties = []  # 최종으로 가능한 duty 저장
    initial_weekday = datetime(year, month, 1).weekday()  # 해당 월의 1일의 요일 반환 (월:0 ~ 일:6)

    # 월에 따라 며칠의 duty를 짜야하는지 확인
    thirty_one = [1, 3, 5, 7, 8, 10, 12]
    thirty = [4, 6, 9, 11]

    if month in thirty_one:
        days_left = 31
    elif month in thirty:
        days_left = 30
    else:
        days_left = 28

    weekend_count = 0

    for day in range(days_left):
        if (initial_weekday + day) % 7 >= 5:
            weekend_count += 1

    off_percent = (weekend_count/days_left)

    heapq.heappush(queue, (0, days_left, prev_month_duty))
    get_final_duty(queue, off_percent, final_duties)

    return final_duties[0][1]