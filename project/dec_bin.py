

def power_by(num):
    if num == 1:
        print 1
        return 1
    if num == 0:
        print 0
        return 0
    arr = []
    t = True
    power = 1
    while t == True:

        if num > power and num < 2 * power:
            arr.append(power)
            t=False
        else:
            if num == power * 2:
                arr.append(power)
                arr.append(power * 2)
                t = False
            else:
                arr.append(power)
                power = power * 2

    bin_number(arr,num)

def bin_number(power,num):
    bin = []
    power.reverse()
    for x in power:
        if num >= x:
            num = num - x
            bin.append(1)
        else:
            bin.append(0)

    print bin
##########################################

def check_dec_bin(num):

    count_power=[]
    count_power = power_by(num)
    return count_power





