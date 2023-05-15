import string

# 대문자가 들어있는 배열선언
upper_case = list(string.ascii_uppercase)
# 소문자가 들어있는 배열선언
lower_case = list(string.ascii_lowercase)

def is_name(word):
    # 첫번째 글자
    start = word[0]
    # 나머지 글자
    end = word[1:]
    # 첫번째가 대문자가 아니라면 False를 리턴
    if start not in upper_case:
        return False
    for i in end:
        # 만약 소문자가 아니라면 False를 리턴
        if i not in lower_case:
            return False
    # 모두 통과한다면 True를 리턴
    return True

t = int(input())
for test in range(1, t + 1):
    n = int(input())
    s = input()
    # 각 문장을 담을 배열선언
    tmp = []
    # 문자을 자르기위한 check_idx 값 설정
    check_idx = 0

    for i in range(len(s)):
        # 구두점을 만난다면
        if s[i] == '!' or s[i] == '.' or s[i] == '?':
            # 해당 문장까지 tmp 배열에 넣어주고
            tmp.append(s[check_idx:i])
            # 구두점과 공백을 건너뛰기 위하여 check_idx를 2더해줌
            check_idx = i + 2
    
    # 문장만큼 answer 배열선언
    answer = [0] * len(tmp)

    # 문장을 돌면서
    for idx in range(len(tmp)):
        # 문장을 단어로 쪼개서 배열에 담음
        word_arr = tmp[idx].split(' ')
        # 이름이 몇개인지 체크하기 위한 cnt 변수 선언
        cnt = 0
        # 단어를 돌면서
        for word in word_arr:
            # 해당 단어가 이름인지 체크한다
            if is_name(word):
                # 이름이면 cnt를 1올려준다
                cnt += 1
        # 이름의 개수를 answer 배열에 기록해준다
        answer[idx] = cnt
    
    # 출력
    print(f'#{test} ', end='')
    print(*answer)