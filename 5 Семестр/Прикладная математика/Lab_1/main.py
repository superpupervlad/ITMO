import sys 
 
from app.simplex import simplex 

def print_results(res):
    print('Точка:')
    print(res[0])
    print('Значение:')
    print(res[1])
    print()

if __name__ == "__main__": 
    if len(sys.argv) == 1:
        for i in range(1, 8):
            print_results(simplex(f'./data/{i}.json'))
    else:
        print(simplex(sys.argv[1]))
