def solution(bandage, health, attacks):
    # 붕대 기술 정보 추출
    casting_time = bandage[0]  # 붕대 시전 시간 (t초)
    heal_per_second = bandage[1]  # 초당 회복량 (x)
    additional_recovery_amount = bandage[2]  # 추가 회복량 (y)

    current_hp = health  # 현재 체력 (최대 체력으로 시작)
    current_time = 0     # 마지막 공격이 일어났거나 시뮬레이션이 시작된 시간

    # attacks 리스트를 순회하며 각 공격을 처리
    for attack_time, damage_dealt in attacks:
        # 1. 이전 공격 시간부터 현재 공격 시간 직전까지의 회복 계산
        # 회복 가능한 시간: (현재 공격 시간) - (이전 공격 시간) - 1
        # 예를 들어, 이전 공격이 5초에, 현재 공격이 10초에 있다면,
        # 6, 7, 8, 9초 (총 4초) 동안 회복 가능
        time_to_heal = attack_time - current_time - 1

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
        
        # 2. 몬스터에게 공격 당함
        current_hp -= damage_dealt

        # 3. 공격 후 체력 확인: 0 이하면 캐릭터 사망
        # 사망 시 즉시 -1 반환
        if current_hp <= 0:
            return -1 

        # 4. 현재 공격 시간을 다음 공격의 '이전 시간'으로 업데이트
        current_time = attack_time
    
    # 모든 공격을 성공적으로 마친 후 남은 체력 반환
    return current_hp