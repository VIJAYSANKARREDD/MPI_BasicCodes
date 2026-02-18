from mpi4py import MPI
comm=MPI.COMM_WORLD
rank=comm.Get_rank()
if rank==0:
    text=input("enter string")
    comm.send(text,dest=1)
    comm.send(text,dest=2)
elif rank==1:
    text=comm.recv(source=0)
    vowels="AEIOUaeiou"
    vowelsList=""
    for ch in text:
        if ch in vowels:
            vowelsList+=ch
    print("vowels",vowelsList)
elif rank==2:
    text=comm.recv(source=0)
    vowels="AEIOUaeiou"
    consonantList=""
    for ch in text:
        if ch.isalpha() and ch not in vowels:
            consonantList+=ch
    print("ConsonantList:",consonantList)