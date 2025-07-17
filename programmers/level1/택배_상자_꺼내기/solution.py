def solution(n, w, num):
    answer = 0
    height = 0
    if n%w == 0:
      height = n//w
    else :
      height = n//w +1
    
    # n= w
    answer =1 
    
    for i in range(1, height):
        if w * i >= num:
            # i가 짝수 일 때 오른쪽에서 시작
            order = 0
            if i%2 == 0:
                order = (w*i - num) + 1
            else: 
                order = w - (w*i - num)
            

            answer = height - i 
        
            last_num = w*(height-1)
            print(last_num)
            current = 0
            if height%2 ==0:
                current = (w + 1) - (n - last_num)
                if current <= order <= w:
                    answer = answer+1      
            else:
                current = n - last_num
                if 1 <= order <= current:
                     answer = answer+1
            
            break;
        
    
    return answer