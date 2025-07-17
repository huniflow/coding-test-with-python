
[문제](https://school.programmers.co.kr/learn/courses/30/lessons/250137)

```python

if current_hp < health:
    if diff < casting_time:
        current_hp += diff
    else:
         q = diff // casting_time
         current_hp += (diff + q * additional_recovery_amount)

```

여기서 내가 못한 건 아래 로직을 통합하지 못한거 어차피 나누면 몫이 나오는데 굳이 왜 그렇게 생각했는지 
그리고 공격 도중 죽으면 -1 return 하는 부분을 까먹었던 것 같다. 

```python

 if time_to_heal > 0: # 회복 가능한 시간이 있다면 체력 회복 로직 실행
            # 회복 시간 동안 붕대 감기 추가 회복이 몇 번 가능한지 계산
            num_additional_heals = time_to_heal // casting_time
            
            # 총 회복량 = (회복 가능한 시간 * 초당 회복량) + (추가 회복 횟수 * 추가 회복량)
            total_healing_during_gap = (time_to_heal * heal_per_second) + \
                                       (num_additional_heals * additional_recovery_amount)
            
            current_hp += total_healing_during_gap
            
            # 체력은 최대 체력을 초과할 수 없습니다.
            if current_hp > health:
                current_hp = health

```