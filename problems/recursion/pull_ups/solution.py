def pulls(k, m):
    if m == 1:
        return k
    else:
        return pulls(k, m-1) + (k+m-1) + (k+m-2)
    
if __name__ == '__main__':
    k = int(input())
    m = int(input())
    print(pulls(k, m))

