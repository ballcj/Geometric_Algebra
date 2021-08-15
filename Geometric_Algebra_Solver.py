# Idea of this program is to create a geometric algebra solver
#   solving for uv = u*v + u∧v, given u and v vectors.

# Importing the libraries needed
from numpy import *

# Asking the user for vector size and vector values
D = input('What dimension are your vectors? ')
if D == '1':
    u = int(input('Please input a value for vector u '))
    v = int(input('Please input a value for vector v '))
    uv = u*v
    print('uv = ', uv)
elif D == '2':
    ux = int(input('Please input a value for vector u top position '))
    uy = int(input('Please input a value for vector u bottom position '))
    vx = int(input('Please input a value for vector v top position '))
    vy = int(input('Please input a value for vector v bottom position '))
    uvD = ux*vx + uy*vy
    uvW = vx*uy - vy*ux
    if uvW < 0:
        uv = print('uv = ',uvD,uvW,'xy')
    else:
        uv = print('uv = ',uvD,'+',uvW,'xy')
elif D == '3':
    ux = int(input('Please input a value for vector u top position '))
    uy = int(input('Please input a value for vector u middle position '))
    uz = int(input('Please input a value for vector u bottom position '))
    vx = int(input('Please input a value for vector v top position '))
    vy = int(input('Please input a value for vector v middle position '))
    vz = int(input('Please input a value for vector v bottom position '))
    uvD = ux*vx + uy*vy + uz*vz
    uvW = array([vx*uy - vy*ux,vx*uz - vz*ux,vy*uz - vz*uy])
    uv = print('uv = ',uvD,'+',uvW[:,newaxis])
else:
    print('Sorry the dimension in which you enter is not computable by this application')
