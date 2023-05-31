#파이썬 클래스 상세 이해
#self, 클래스, 인스턴스 변수

#선언
# class 클래스명:
#     함수
#     함수
#     함수


#클래스와 인스턴스의 차이 중요함
#네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
#클래스 변수 : 직접 사용 가능, 객체 보다 먼저 생성
#인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용

from queue import PriorityQueue

from pandas import period_range


class UserInfo:
    def __init__(self, name) -> None:
        self.name=name
    def user_inpo_p(self):
        print('name : ', self.name)

#네임스페이스
user1=UserInfo('Kim')
user1.user_inpo_p()
user2=UserInfo('Park')
user2.user_inpo_p()

print(id(user1))
print(id(user2))

print(user1.__dict__)
print(user2.__dict__)


#self의 이해
class SelfTest:
    def function1():
        print('function1 called')
    def function2(self):
        print(id(self))
        print('function2 called')

self_test = SelfTest()
# self_test.function1() #instance error
SelfTest.function1()
self_test.function2()

print(id(self_test))
SelfTest.function2(self_test)


class Warehouse:
    #클래스 변수
    stock_num=0
    def __init__(self, name):
        self.name=name
        Warehouse.stock_num+=1
    def __del__(self):
        Warehouse.stock_num-=1

user1=Warehouse('Kim')
user2=Warehouse('Park')
user3=Warehouse('Lee')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(Warehouse.__dict__) #클래스 네임스페이스, 클래스 변수(공유)

print(user1.stock_num)
print(user2.stock_num)
print(user3.stock_num)

del user1
print(user2.stock_num)
print(user3.stock_num)

#상속, 다중 상속
#슈퍼클래스(부모) 및 서브클래스(자식) -> 모든 속성, 메소드 사용

class Car: #Parent Class
    def __init__(self, tp, color) -> None:
        self.type=tp
        self.color=color

    def show(self):
        return "Car Class show method!"
    
class BmwCar(Car): #Sub Class
    def __init__(self, car_name, tp, color) -> None:
        super().__init__(tp, color)
        self.car_name=car_name

    def show_mode(self):
        return 'Your Car name : %s' % self.car_name

class BenzCar(Car): #Sub Class
    def __init__(self, car_name, tp, color) -> None:
        super().__init__(tp, color)
        self.car_name=car_name

    def show_mode(self):
        return 'Your Car name : %s' % self.car_name
    
    def show(self):
        print(super().show())
        return 'Car info : %s, %s, %s' % (self.car_name, self.type, self.color)


#일반 사용
model1=BmwCar('530d', 'sedan', 'red')

print(model1.color) #Super
print(model1.type) #Super
print(model1.car_name) #Sub
print(model1.show())#Super
print(model1.show_mode()) #Sub
print(model1.__dict__)

# Method Overriding
model2=BenzCar('220d', 'sub', 'black')
print(model2.show())

#Inheritance Info(상속 정보를 리스트로 반환)
print(BmwCar.mro())
print(BenzCar.mro())


#다중상속
class X():
    pass

class Y():
    pass

class Z():
    pass

class A(X,Y):
    pass
class B(Y,Z):
    pass
class M(B,A,Z):
    pass

print(M.mro())
print(A.mro())
