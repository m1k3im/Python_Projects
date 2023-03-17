def TimeCount(speed1, speed2, distance):
    return distance/(speed2-speed1)


x= int(input('Введите скорость Джерри:\n'))
y= int(input('Введите скорость Тома:\n'))
s= int(input('Введите расстояние:\n'))

if y-x>0 :
    print('Том догонит Джерри через: ',round(TimeCount(x,y,s)),' секунд.')
else:
    print('Том не сможет догнать Джерри')