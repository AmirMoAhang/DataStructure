def Hanoi(numberOfDisks, fromRod, toRod, auxRod):
    if numberOfDisks == 1:
        print(f"disk {numberOfDisks} moved from Rod {fromRod}, to Rod {toRod}")
        return
    Hanoi(numberOfDisks - 1, fromRod=fromRod, toRod = auxRod, auxRod = toRod)
    print(f"disk {numberOfDisks} moved from Rod {fromRod}, to Rod {toRod}")
    Hanoi(numberOfDisks - 1, fromRod = auxRod, toRod=toRod, auxRod= fromRod)
    
    
    
Hanoi(4, 'A', 'c', 'B')