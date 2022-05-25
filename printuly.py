for _ in range(10):
    print("*" * _)

for i in range(10):
    for j in range(10):
        print(j * i, end='\t')
    print()