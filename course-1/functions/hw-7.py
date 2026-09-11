"""def iterate(f, x, n):
    result = []
    for i in range(1, n+1):
        result.append(f(x) if i == 1 else f(result[-1]))
    return result
def fun(x): return (0.5*(x+2/x))
f = fun
print(iterate(f, 1, 6))"""

# Part 2
def apply_functions(fs, x):
    val = x
    for f in reversed(fs):
        val = f(val)
    return val

print("\nPart 2 Output:")
fs = ['...'.join, str.split, str.lower]
x = 'WHAT IS THIS?'
print(apply_functions(fs, x))