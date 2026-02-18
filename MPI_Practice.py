from mpi4py import MPI
comm=MPI.COMM_WORLD
rank=comm.Get_rank()
if rank==0:
    n=int(input("Enter no.of elements"))
    data=[]
    for i in range(n):
        num=int(input("Enter Elements"))
        data.append(num)
    total=sum(data)
    print("Sum of all",total)
    comm.send(data,dest=1)
    comm.send(data,dest=2)
elif rank==1:
    data=comm.recv(source=0)
    even_sum=0
    for num in data:
        if num%2==0:
            even_sum+=num
    print("Sum of even",even_sum)
elif rank==2:
    data=comm.recv(source=0)
    odd_sum=0
    for num in data:
        if num%2!=0:
            odd_sum+=num
    print("sum of odd",odd_sum)