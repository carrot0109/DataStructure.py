# '''문자열'''
# str1 = 'Hello'
# str2 = 'Hi'

# # name = input('Input your name : ')
# print(str1, '\t\"How are you\"')
# print(str1[0], str1[-1])


# '''형식지정자'''
# hobby = 'Tennis'
# age = 21
# pi = 3.1415

# print('Hobby : %s, Age : %d, Pi : %lf' %(hobby, age, pi))
# print('Pi : %f' %(pi))      # 소수점 6자리
# print('Pi : %7.2f' %(pi))       # 공백 포함하여 정렬

# n1 = 2
# n2 = 123
# n3 = 32

# print('%3d' %n1)
# print('%3d' %n2)
# print('%3d' %n3)


'''리스트'''
# L1 = [3, 5, 7, 9]
# L2 = ['A', 'B', 'C', 'D']

# print(L1)

# for i in L2:
#     print(i, end = " ")
# print()

# print(L2[0])

# L2[1] = L1[-1]
# print(L2)

# L1.append(11)
# print(L1)

# print(L1.pop())
# print(L1)       # 뺴낸 원소가 삭제됨

# L2.extend(L1)   # L2를 확장시킨다는 의미(따라서 L1은 그대로)
# print(L1)
# print(L2)


'''딕셔너리'''
dic = {'apple':'사과', 'banana':'바나나'}
print(dic)

for key in dic:
    print(key)    # key만 출력됨

for key in dic:
    print('%s --> %s' %(key, dic[key]))     # key를 인덱스로 생각

dic['grape'] = '포도'   # 새로운 키, 밸류 추가
print(dic)

dic.update({'orange': '오렌지', 'mandarin':'귤'})   # 여러개의 항목을 한 번에 추가
print(dic)

print(dic.keys)     # 키값만 출력
print(dic.values)   # 값만 출력
