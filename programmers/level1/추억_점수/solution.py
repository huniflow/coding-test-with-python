def solution(name, yearning, photo):
    answer = []
    
    result_dict = dict(zip(name, yearning))
    
    for p in photo:
        sum = 0
        for people in p:
            sum += result_dict.get(people, 0)
        
        answer.append(sum)
    
    return answer