import random
import string
import os


def alphabetical(test):
    alphabetical = string.ascii_lowercase
    ran = random.choice(range(15, 20))
    for i in range(ran):
        test = test + str(random.choice(alphabetical))
    return test


def integers(test):
    integers = string.digits
    y = random.choice(range(3, 15))
    for i in range(y):
        test = test + str(random.choice(integers))
    return test, y


def alphanumerics(test):
    mix = string.ascii_lowercase + string.digits
    ran = random.choice(range(15, 20))
    for i in range(ran):
        test = test + str(random.choice(mix))

    for i in range(random.choice(range(10))):
        test = test + ' '

    for i in range(random.choice(range(10))):
        test = ' ' + test

    return test


def real_numbers(test):
    while True:
        test, y = integers(test)
        i = random.choice(range(y))
        # print(test[:i], test[i:])
        rn = test[:i] + '.' + test[i:]

        if rn[-1] == '0':
            # print('nope')
            continue
        else:
            break

    return rn


test = ''
filename = 'files\list.csv'
file_size = 0
f = open(filename, "w")
# for i in tqdm(range(100), desc="Loading..."):
while file_size <= 10485760:

    alphabet = alphabetical(test)
    # print('test1', alphabet)

    integ, y = integers(test)
    # print('test2', integ)

    alpnum = alphanumerics(test)

    # print('test3', alpnum)

    real_num = float(real_numbers(test))
    # print('test4', real_num)

    list = []

    list.extend([alphabet] + [alpnum] + [(str(real_num))] + [(str(int(integ)))])

    # print(list)

    while list:
        value = random.choice(list)
        list.remove(value)
        # print(value)
        file_size = os.stat(filename).st_size
        f.write(value + ',' + ' ')
    print(str(file_size) + 'MB/10485760MB')

print("Complete.")
input("Press Enter to continue...")
f.close()

# 10 Megabytes = 10485760 Bytes
