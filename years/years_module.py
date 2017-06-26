import datetime
name = input('Type your name: ')
age = int(input('Type your age: '))

def years(age):
    leftover = 100 - age
    result = 2016 + leftover
    return result


def main():
    return


if __name__ == '__main__':
    main()


print(years(age))
#datetime.date.today().timetuple()
