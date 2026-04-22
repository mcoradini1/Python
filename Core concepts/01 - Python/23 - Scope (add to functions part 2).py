
'''SCOPE
L - LOCAL (current function we are in)
E - ENCLOSING FUNCTIONS (function that called the current function)
G - GLOBAL (module which the function is defined)
B - BUILT-IN (built-in namespace)
'''

def update1():
    x.append(1)

x = [1,1]

#IT WILL FIRST LOOK INSIDE THE FUCNTION FOR X, IF IT CANNOT FIND IT WILL GO OUTSIDE


def update (n, x):
    n = 2
    x.append (4)
    print(f'update: n: {n} \nx: {x}\n')

def main():
    n = 1
    x = [0,1,2,3]
    print(f'main: {n} \nx: {x}\n')
    update(n, x)
    print(f'main: {n} \nx: {x}\n')

main()