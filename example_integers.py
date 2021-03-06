from codegen.codegen_llvm_builder import codegen_compile
import numpy as np

iter = 1000
r = np.int64(((1 / 1.61803398875) * (1 << 63)))


def foo(x: float):
    for i in range(iter):
        #     x += x * r
        x = x * (-x + 1) * r
    return x


cfoo = codegen_compile(foo, 'int')
print(cfoo)
print(cfoo(17))
print(foo(17))
# print(cfoo.llvm_code)
# print(cfoo.target_asm)


def ufoo(x: float):
    for i in range(iter):
        x = x * (x - 1) * r
    return x


cufoo = codegen_compile(ufoo, 'uint')
print(cufoo)
print(cufoo(17))
print(ufoo(17))
# print(cufoo.llvm_code)
# print(cufoo.target_asm)
