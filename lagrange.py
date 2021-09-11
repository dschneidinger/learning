import numpy as np


def kinetic_energy(A): # takes matrix input, vector is [mass, Vx, Vy, Vz], calculates total kinetic energy of point masses 
    i = 0
    j = 1
    T = 0
    for i in range(0, len(A)):
        for j in range(1, len(A[i])):
            T += .5*A[i][0]*(A[i][j]**2.)
            j += 1

        i += 1
    return T


def potential_energy(A): # Takes matrix input [mass, x, y, z], calculates total potential energy between point masses
    G = 6.67e-11
    i = 0
    Grav_PE = 0.
    j = 1
    for i in range(0, len(A)):
        k = i + 1
        for k in range(i+1, len(A)):
            rsqd = 0.0
            for j in range(1, len(A[i])):
                rsqd += (A[k][j]-A[i][j])**2
                j += 1
            r = np.sqrt(rsqd)
            Grav_PE += G * A[i][0] * A[k][0] / r
            k += 1
        i += 1
    return Grav_PE


def lagrangian(pos, vel):
    L = kinetic_energy(vel) - potential_energy(pos)
    return L


x1 = [2., 1., 3., 4.]
x2 = [2., 4., 3., 5.]
x3 = [2., 3., 2., 7.]

v1 = [2., 4., 7., 1.]
v2 = [2., 2., 2., 1.]
v3 = [2., 5., 7., 2.]
positionmatrix = [x1, x2, x3]
velocitymatrix = [v1, v2, v3]

print(kinetic_energy(velocitymatrix))
print(potential_energy(positionmatrix))




#print(kinetic_energy(matrix))


