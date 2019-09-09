import math
def cal_det(Matrix,n,mod):
    #print(Matrix,n,mod)
    if n==1:
        return Matrix
    if n==2:
        return Matrix[0][0]*Matrix[1][1]-Matrix[0][1]*Matrix[1][0]
    else:
        matrix=[]
        column=[]
        Mul_Matrix=[]
        SUM=0
        for k in range(n):
            for l in range(n):
                for i in range(n):
                    #print(i)
                    for j in range(n):
                        if k==i or l==j:
                            continue
                        else:
                            column.append(Matrix[i][j])
                            #print(k,l,i,j)
                            #print(column)
                        #l+=1
                    #k+=1
                    if i!=k:
                        matrix.append(column)
                        #print(matrix,column,k,l,i,j)
                    column=[]
                Mul_Matrix.append(((-1)**(k+l)) * Matrix[k][l] * cal_det(matrix,n-1,mod))
                matrix=[]
    for i in range(n):
        SUM+=Mul_Matrix[i]
    return SUM
        #Matrix[n][n]=(-1)**(n+n)*cal_det(matrix,n
                




            
def cal_inverse(det,mod):
    a=mod
    b=det
    r=32767
    s1=0
    s2=1
    s=0
    while b!=0:
        q=a//b
        r=a-q*b
        s=s1-q*s2
        a=b
        b=r
        s1=s2
        s2=s
    return s1


def cal_adj(Matrix,n,mod):
        Mul_Matrix=[]
        column1=[]
        #print(Matrix,n,mod)
        if n==1:
            return Matrix
        if n==2:
            column1.append(Matrix[1][1])
            column1.append((-1)*Matrix[0][1])
            Mul_Matrix.append(column1)
            column1=[]
            column1.append((-1)*Matrix[1][0])
            column1.append(Matrix[0][0])
            Mul_Matrix.append(column1)
            return Mul_Matrix
            
        else:
            matrix=[]
            column=[]
            for k in range(n):
                for l in range(n):
                    for i in range(n):
                        #print(i)
                        for j in range(n):
                            if k==j or l==i:
                                continue
                            else:
                                column.append(Matrix[i][j])
                                #print(k,l,i,j)
                                #print(column)
                            #l+=1
                        #k+=1
                        if i!=l:
                            matrix.append(column)
                            #print(matrix,column,k,l,i,j)
                        column=[]
                    column1.append(((-1)**(k+l)) *  cal_det(matrix,n-1,mod))
                    matrix=[]
                Mul_Matrix.append(column1)
                column1=[]
                #print(Mul_Matrix)
        return Mul_Matrix















print('Program to find Matrix Inverse mod n')
n=int(input('Enter the size of square matrix  '))


Matrix=[]
column=[]
print(f'Enter the {n} * {n} ={n*n} elements in matrix')
for i in range(n):
    for j in range(n):
        column.append(int(input()))
    Matrix.append(column)
    column=[]
print('***********************************************************************\n\n')
print('Matrix entered is:')
for i in range(n):
    print(Matrix[i])
print('***********************************************************************\n\n')



#print(Matrix[1][1])

mod=int(input('Enter base of modulas  '))
for i in range(n):
    for j in range(n):
        Matrix[i][j]=Matrix[i][j] % mod
print('***********************************************************************\n\n')

print('Matrix after aplying mod is')
for i in range(n):
    print(Matrix[i])
print('***********************************************************************\n\n')



det=cal_det(Matrix,n,mod)

print('Determent is :',det)
print('***********************************************************************\n\n')

det=det%mod #if det is negative or aout of range of mod
print('Determent after applying mod is :',det)
print('***********************************************************************\n\n')

inverse=0
if math.gcd(det,mod)==1:
    inverse=cal_inverse(det,mod)# calculating inverse of det
    print('Determent Inverse is:',inverse)
    print('***********************************************************************\n\n')
    inverse=inverse%mod #if inverse <0
    print('Determent  Inverse after applying mod(if det  Inverse is negative) is:',inverse)
    print('***********************************************************************\n\n')



    #Calculating Adjoint:
    inverse_matrix=cal_adj(Matrix,n,mod)
    print('Adjoint Matrix is \n')
    for i in range(n):
        print(inverse_matrix[i])

    print('***********************************************************************\n\n')

            


    #inverse of Matrix:

    for i in range(n):
        for j in range(n):
            inverse_matrix[i][j]=(inverse*inverse_matrix[i][j]) % mod




    #printing Inverse matrix



    print('Inverse Matrix is  \n')

    for i in range(n):
        print(inverse_matrix[i])

    print('***********************************************************************\n\n')






    #Verification Step:
    #If original Matrix multiplied by inverse % mod= identity matrix then we did it correctly
    identity_matrix=[]
    column2=[]
    SUM=0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                SUM+=Matrix[i][k]*inverse_matrix[k][j]
            column2.append(SUM)
            SUM=0
        identity_matrix.append(column2)
        column2=[]
    print('Matrix verification before mod \n')

    for i in range(n):
        print(identity_matrix[i])

    print('***********************************************************************\n\n')





    for i in range(n):
        for j in range(n):
            identity_matrix[i][j]=identity_matrix[i][j] % mod
    print('Modulas base is : ',mod)

    print('Identity Matrix is \n')
    for i in range(n):
        print(identity_matrix[i])
else:
    print("Inverse can't be found")
    exit
        
x=input('Press Enter to exit!')
