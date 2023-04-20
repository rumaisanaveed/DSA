def towerOfHanoi(n,src,helper,dest):
    if n == 1:
        print(f"Transfer of disk {n} from {src} to {dest}.")
        return
    towerOfHanoi(n-1,src,dest,helper)
    print(f"Transfer of disk {n} from {src} to {dest}.")
    towerOfHanoi(n-1,helper,src,dest)

towerOfHanoi(3,"S","H","D")