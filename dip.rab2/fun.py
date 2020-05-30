def raship(Uold):
    nx=len(Uold)
    ny=len(Uold[0])
    nz=len(Uold[0][0]) 
    a=1.5
    h1=(float)(1/(nx-1))
    h2=(float)(1/(ny-1))
    h3=(float)(1/(nz-1))
    tau=h1/100
    q1 = (a * tau) / (h1 * h1)
    q2 = (a * tau) / (h2 * h2)
    q3 = (a * tau) / (h3 * h3) 
    Unew=[[[0 for _ in range(nz)] for _ in range(ny)] for _ in range(nx)]
    U1=[[[0 for _ in range(nz)] for _ in range(ny)] for _ in range(nx)]
    U2=[[[0 for _ in range(nz)] for _ in range(ny)] for _ in range(nx)]

    for i in range(nx):
        for j in range(ny):
            Unew[i][j][0]=0
            Unew[i][j][nz-1]=0
            U1[i][j][0]=0
            U1[i][j][nz-1]=0
            U2[i][j][0]=0
            U2[i][j][nz-1]=0
    for i in range(nx):
        for k in range(nz):       
            Unew[i][0][k]=0
            Unew[i][ny-1][k]=0
            U1[i][0][k]=0
            U1[i][ny-1][k]=0
            U2[i][0][k]=0
            U2[i][ny-1][k]=0
    for j in range(ny):
        for k in range(nz): 
            Unew[0][j][k]=0
            Unew[nx-1][j][k]=0
            U1[0][j][k]=0
            U1[nx-1][j][k]=0
            U2[0][j][k]=0
            U2[nx-1][j][k]=0

    #1прогонка      
    L,B=[0 for _ in range(nx)],[0 for _ in range(nx)]
    for j in range(1,ny-1):
        for k in range(1,nz-1):
            L[1]=q1/(1+2*q1)
            B[1]=Uold[1][j][k]/(1+2*q1)
            for i in range(2,nx-1):
                L[i] = q1 / (-q1*L[i-1]+1+2*q1)
                B[i] = (Uold[i][j][k] +q1* B[i - 1]) / (-q1*L[i - 1] + 1 + 2*q1)
            U1[nx - 2][j][k] = B[nx - 2]
            for i in reversed(range( 1,nx-1)):
                U1[i][j][k]= L[i] * U1[i + 1][j][k] + B[i]       
    L,B=[0 for _ in range(ny)],[0 for _ in range(ny)]
    #2прогонка
    for i in range(1,nx-1):
        for k in range(1,nz-1):
            L[1]=q2/(1+2*q2)
            B[1]=U1[i][1][k]/(1+2*q2)
            for j in range(2,ny-1):
                L[j] = q2 / (-q2*L[j-1]+1+2*q2)
                B[j] = (U1[i][j][k] +q2* B[j - 1]) / (-q2*L[j - 1] + 1 +2*q2)
            U2[i][ny - 2][k] = B[ny - 2]
            for j in reversed(range( 1,ny-1)):
                U2[i][j][k]= L[j] * U2[i][j+1][k] + B[j]
    L,B=[0 for _ in range(nz)],[0 for _ in range(nz)]
    #3прогонка
    for i in range(1,nx-1):
        for j in range(1,ny-1):
            L[1]=q3/(1+2*q3)
            B[1]=U2[i][1][k]/(1+2*q3)
            for k in range(2,nz-1):
                L[k] = q3/ (-q3*L[k-1]+1+2*q3)
                B[k] = (U2[i][j][k] +q3* B[k-1]) / (-q3* L[k-1] + 1 + 2 * q3)
            Unew[i][j][nz-2] = B[nz - 2]
            for k in reversed(range( 1,nz-1)):
                Unew[i][j][k]= L[k] * Unew[i][j][k+1] + B[k]
    return Unew
