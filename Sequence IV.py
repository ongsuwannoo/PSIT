''' Sequence IV '''
def main():
    ''' for loop '''
    num = int(input())
    for j in range(1, num**2+1):
        print(j, end=' ')
        if j % num == 0:
            print()

main()
