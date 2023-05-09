t = int(input())
for _ in range(t):
    n = int(input())
    # 2행 n열임 -> 2행은 고정
    arr = []
    for _ in range(2):
        arr.append(list(map(int, input().split())))

    # 0은 그대로이고, 1부터 연산을 시작해야함
    for i in range(1, n):
        # 1이면 왼쪽 위, 왼쪽 아래를 각각 더해줌
        if i == 1:
            arr[0][i] += arr[1][i - 1]
            arr[1][i] += arr[0][i - 1]
        # 선택할수 있는것중 최댓값을 선택해서 계속해서 더해나감
        else:
            arr[0][i] += max(arr[1][i - 1], arr[1][i - 2])
            arr[1][i] += max(arr[0][i - 1], arr[0][i - 2])
    # 2행중 최댓값을 출력        
    print(max(arr[0][n - 1], arr[1][n - 1]))