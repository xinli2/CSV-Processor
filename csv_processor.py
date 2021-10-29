###
### Author: Xin Li
### Description:  In this short PA, you will be writing a program
### that reads in a CSV file with no column labels, and can compute
### a maximum, minimum and average of a column.
###
def main():
    file_name = input('Enter CSV file name:\n')
    column_number = input('Enter column number:\n')
    column_operation = input('Enter column operation:\n')
    column_number=int(column_number)-1
    file = open(file_name, 'r')
    lines = file.readlines()
    lst = []
    lst_2D=[]
    i = 0
    for line in lines:
        line = line.strip('\n')
        line = line.split(',')
        for i in line:
            lst_2D.append(float(i))
        lst.append(lst_2D)
        lst_2D=[]
    if column_operation =='min':
        min(lst, column_number)
    if column_operation =='max':
        max(lst, column_number)
    if column_operation =='avg':
        avg(lst, column_number)


def min(lst, column_number):
    min=[]
    min_number = 1000
    for line in lst:
        min.append(line[column_number])
    for num in min:
        if num < min_number:
            min_number = num
    print('The minimum value in column',column_number+1 ,'is:',min_number)

def max(lst, column_number):
    max=[]
    max_number = 0
    for line in lst:
        max.append(line[column_number])
    for num in max:
        if num > max_number:
            max_number = num
    print('The maximum value in column', column_number+1,'is:',max_number)

def avg(lst, column_number):
    avg = []
    sum = 0
    for line in lst:
        avg.append(line[column_number])
    for num in avg:
        sum += num
    average = sum / len(avg)
    print('The average for column',column_number+1 ,'is:',average)


main()
