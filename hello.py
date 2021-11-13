# typing return multiple
from typing import Tuple, Generator


def prueba(a: int, b: int, c: float) -> Tuple[int, int, float]:
    return a, b, c


# funcion generadora con yield
def f_gen(lista_cosas: tuple) -> Generator:
    for cosa in lista_cosas:
        yield cosa


cosas = f_gen(prueba(1, 2, 3.4))
for i in cosas:
    print(i)


# list comprehension:
cosas2 = [i for i in prueba(1, 2, 3.4)]
print(cosas2)


#%%
# generador mediante list comprehension : con parentesis
cosas3 = (i for i in prueba(1, 2, 3.4))
print(cosas3)


# puedo wrapearlo en una lista
print(list(cosas3))
#%%
