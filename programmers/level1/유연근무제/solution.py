def solution(schedules, timelogs, startday):
    answer = 0

    # `enumerate`를 사용하여 인덱스(num)와 값(schedule)을 동시에 가져옴
    for num, schedule in enumerate(schedules):
        # 변수 초기화
        range_val = 0 
        is_success = True
        checkDay = startday
        
        s_quotient = schedule // 100
        s_remainder = schedule % 100
        
        s_remainder += 10 
        
        if s_remainder >= 60:
            r_quotient = (s_remainder // 60)*100
            r_remainder = s_remainder % 60
            range_val = r_quotient + r_remainder  + (s_quotient *100)
        else:
            range_val = s_remainder + (s_quotient * 100)
        
        

        for time in timelogs[num]:

            # 요일이 6 또는 7이면 건너뛰고 다음 기록으로 이동
            if checkDay == 6 or checkDay == 7:
                # `continue`를 사용하면 아래 코드가 실행되지 않음
                pass
            else:
                if time > range_val:
                    is_success = False

            # `checkDay`를 1씩 증가시키고 8이 되면 1로 순환
            checkDay = (checkDay % 7) + 1
            
            # `is_success`가 False가 되면 루프 중단
            if not is_success:
                break

        # 현재 사람의 모든 기록을 검토한 후, 성공 여부를 확인
        if is_success:
            answer += 1

    return answer