# 4.2
# 크기와 색깔을 사용자에게 입력 받고 조건에 맞는 과일 출력
# size = input('small or big: ')
# color = input('green or other: ')
# if size == 'small':
#     small = True
# else:
#     small = False
#
# if color == 'green':
#     green = True
# else:
#     green = False
#
# if small:
#     if green:
#         print('완두콩')
#     else:
#         print('체리')
# else:
#     if green:
#         print('수박')
#     else:
#         print('호박')

# 방법2
small = True
green = True
if small:
    if green:
        print('완두콩')
    else:
        print('체리')
else:
    if green:
        print('수박')
    else:
        print('호박')

# True, False를 랜덤으로 추출
import random
small = random.choice([True, False])
green = random.choice([True, False])
print(small)
print(green)
if small:
    if green:
        print('완두콩')
    else:
        print('체리')
else:
    if green:
        print('수박')
    else:
        print('호박')