
if __name__ == '__main__':
    with open('data.csv', 'w') as f:
        f.write("Name,Gender,Age\n")
        f.write("Jacob,Male,18\n")

    with open('data.csv', 'r') as f:
        context = f.read()
        print(context)



