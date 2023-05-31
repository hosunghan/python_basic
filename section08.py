#파이썬 모듈과 패키지

#클라스 호출
from pkg.fibonacci import Fibonacci
Fibonacci.fib(300)

print('ex2:', Fibonacci.fib2(400))
print('ex3:', Fibonacci().title)


#클래스 alias
from pkg.fibonacci import Fibonacci as fb
fb.fib(200)

print('ex2:', fb.fib2(200))
print('ex3:', fb().title)

#함수
import pkg.calculations as c
print('ex4 : ', c.add(10, 100))
print('ex4 : ', c.mul(1, 100))


#함수
from pkg.calculations import div as d
print('ex5 : ', int(d(100,10)))

import pkg.print as p
p.prt1()
p.prt2()


