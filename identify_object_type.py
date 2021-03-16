import csv

with open('files\list.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    for row in csvreader:
        for elem in row:
            value = elem.replace(' ', '')

            if value.isdigit():
                output = value + ' - integer \n'
                print(output)

            else:
                try:
                    if float(value):
                        output = value + ' - real numbers \n'
                        print(output)

                except:
                    if any(map(str.isdigit, value)):
                        output = value + ' - alphanumeric \n'
                        print(output)
                    elif value == '':
                        break
                    else:
                        output = value + ' - alphabetical strings \n'
                        print(output)
input("Press Enter to continue...")