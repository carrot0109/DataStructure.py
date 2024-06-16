M = 13      # 테이블 크기
table = [0] * M     # 테이블 정의

def hashFn(key):        # 해쉬 함수
    return key % M      # mod 를 이용한 해쉬값

def hashFn2(key):       # 이중 해시법에 사용할 새로운 해시함수
    return 11 - (key % 11)      # M 보다 작은 소수 사용 --> 처음 해시값이 같아도 그 후 새로운 소수를 사용하기 때문에 2차 집중 해결 가능

def getLinear(v, i):
    return (v + i) % M

def getQuadratic(v, i):     # 이차조사법 --> 군집 완화
    return (v + i * i) % M

def getDouble(v, i, key):       # 이중 해싱법
    return (v + i * hashFn2(key)) % M

def insert(key):
    v = hashFn(key)     # 원하는 키의 해시값
    i = 0       # 이동 횟수

    while i < M:        # M - 1 번까지 이동 가능 --> M 번 이동했다는 것은 자리가 없다는 의미이므로 불필요
        b = getLinear(v, i)     # 해시값 갱신 (이동하므로 새로운 해시값이 할당)
        # b = getQuadratic(v, i)      
        # b = getDouble(v, i, key)

        if table[b] == 0 or table[b] == -1:       # 해시값이 0 이라는 것은 공백을 의미 
            table[b] = key      # 공백인 자리에 키 대입
            return      # 반복문 종료
        else:       # 이 공간이 비어있지 않을 때
            i += 1      # 한 칸 이동

def search(key):        # 원하는 키가 있는지 탐색
    v = hashFn(key)   
    i = 0      

    while i < M:
        b = getLinear(v, i)
        # b = getQuadratic(v, i)
        # b = getDouble(v, i, key)

        print('[%d] ' %table[b], end='')        # 칸을 이동해가면서 계속 그 칸에 있는 값들을 출력

        if table[b] == 0:       # 값이 0 이면 값이 없다는 것을 의미
            return 0
        elif table[b] == key:       # 키와 같으면 키를 출력
            return table[b]
        else:       # 0 도 아니고 원하는 키도 아니라면 한 칸 이동
            i += 1
    
    return 0

def delete(key):
    v = hashFn(key)
    i = 0

    while i < M:
        b = getLinear(v, i)
        # b = getQuadratic(v, i)
        # b = getDouble(v, i, key)

        if table[b] == 0:
            print('No key to delete')
            return
        elif table[b] == key:
            table[b] = -1       # 0 으로 한다면 위의 조건에 걸려 그 다음칸으로 나아갈 수 없음 --> 결과적으로 오류
            return
        else:
            i += 1

def display():
    print()
    print('Bucket   Key')
    print('============')

    for i in range(M):      # table 크기만큼 출력
        print('HT[%2d] : %2d' %(i, table[i]))       # 순서대로 출력


if __name__ == '__main__':
    data = [45, 27, 88, 9 ,71, 60, 46, 38, 24]
    for d in data:
        print('h(%2d) = %2d ' %(d, hashFn(d)), end='')
        insert(d)       # table 에 삽입
        print(table)

    display()

    print()
    print('Search(46) --> ', search(46))

    delete(60); display()     
    print('Search(46) --> ', search(46))

    print(); insert(21)
    display()       # -1 로 변경된 자리에도 새로운 값이 들어가는 것을 확인