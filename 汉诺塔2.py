def hanoi(n,x,y,z):

    if n==1:

        print(x,"-->",z)

    else:

        hanoi(n-1,x,z,y)

        print(x,"-->",y)

        hanoi(n-1,y,x,z)


n=2
hanoi(n,"x","y","z")
