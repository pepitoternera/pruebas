#typing return multiple
from typing import Tuple, Generator

def prueba(a: int, b: int, c: float) -> Tuple[int,int,float]:
    return a,b,c

#funcion generadora con yield
def f_gen(lista_cosas: tuple) -> Generator:
    for i in lista_cosas:
        yield i

cosas = f_gen(prueba(1,2,3.4))
for i in cosas:
    print(i)