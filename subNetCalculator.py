
class SubNCalc:

    def __init__(self):
        self.start_menu()

    def open_file(self):
        print('Please put file name:')
        self.user_input = 'my.txt'  # input()
        try:
            with open(self.user_input, "r") as sub_net_list:
                sub_net_list = sub_net_list.readlines()
                sub_net_list = [x.rstrip('\n') for x in sub_net_list]
                new_list = []
                for line in sub_net_list:
                    if len(line) < 1 or line.startswith(' '):
                        pass
                    else:
                        new_list.append(line)
                return new_list
        except FileNotFoundError:
            print("Please checks if file is in directory")
            self.start_menu()

    def max_number(self, power):
        dict_b = {8: 256, 7: 128, 6: 64, 5: 32, 4: 16, 3: 8, 2: 4, 1: 2}
        range_last = 0
        for a, b in dict_b.items():
            if a == power:
                range_last = b - 1
        return range_last

    def up_to_eight(self, power, sn_list):
        sn_list = sn_list[0].split('.')
        sn = [int(x) for x in sn_list]
        ip_list = []
        power = power
        max_numb = (2 ** power) - 1
        num_list = [x for x in range(sn[3] + 1, max_numb + sn[3])]
        for x in num_list:
            ip_list.append(str(sn[0]) + '.' + str(sn[1]) + '.' + str(sn[2]) + '.' + str(x))
        return ip_list

    def below_sixteen(self, power, sn_list):
        sn_list = sn_list[0].split('.')
        sn = [int(x) for x in sn_list]
        ip_list = []
        power = power
        all_number = ((2 ** 8) * (2 ** (power - 8))) - 2
        power_r = power - 8
        max_numb = (2 ** power_r)
        last_num_list = [x for x in range(0, 256)]
        tir_num_list = [x for x in range(sn[2], max_numb + sn[2])]
        for x in tir_num_list:
            for z in last_num_list:
                ip_list.append(str(sn[0]) + '.' + str(sn[1]) + '.' + str(x) + '.' + str(z))
        ip_list.pop()
        ip_list = ip_list[1::]
        return ip_list

    def above_sixteen(self, power, sn_list):
        sn_list = sn_list[0].split('.')
        sn = [int(x) for x in sn_list]
        ip_list = []
        power = power
        all_number = (2 * (2 ** 8) * (2 ** (power - 16))) - 2
        power_r = power - 16
        max_numb = (2 ** power_r)
        last_num_list = [x for x in range(0, 256)]
        tir_num_list = [x for x in range(0, 256)]
        sec_num_list = [x for x in range(sn[1], max_numb + sn[1])]
        for c in sec_num_list:
            for x in tir_num_list:
                for z in last_num_list:
                    ip_list.append(str(sn[0]) + '.' + str(c) + '.' + str(x) + '.' + str(z))
        ip_list.pop()
        ip_list = ip_list[1::]
        return ip_list

    def sub_net_mask(self):
        sub_list = self.open_file()
        s = [x.replace('/', ',') for x in sub_list]
        sn_length = [x.split(',') for x in s]
        for x in sn_length:
            if len(x) != 4:
                print('incorrect input in txt file')
                break
        else:
            all_ip_list = []
            for y in sn_length:
                power = 32 - int(y[1])
                if power <= 8:
                    a = self.up_to_eight(power, y)
                    for x in a:
                        all_ip_list.append(x + ',' + y[2] + ',' + y[3])
                elif 8 < power <= 16:
                    a = self.below_sixteen(power, y)
                    for x in a:
                        all_ip_list.append(x + ',' + y[2] + ',' + y[3])
                elif power > 16:
                    a = self.above_sixteen(power, y)
                    for x in a:
                        all_ip_list.append(x + ',' + y[2] + ',' + y[3])
            print(sn_length)
            return all_ip_list

    def save_file(self):
        with open('my_list.csv', 'w+') as my_file:
            titles = 'ip_address,reason,requested_by'
            my_file.write(titles)
        with open('my_list.csv', 'a+') as my_file:
            if self.sub_net_mask():
                inner_list = self.sub_net_mask()
                my_file.write('\n')
                for x in inner_list:
                    my_file.write(x)
                    my_file.write('\n')
                return self.start_menu()
            else:
                print("Please correct mistake")

    def start_menu(self):
        print("Please choose:\n1) To upload txt file\n0) To exit")
        self.user_input = input()
        while self.user_input != '0':
            if self.user_input == '1':
                self.save_file()
            elif self.user_input == '0':
                print('Bye!')
                break
            else:
                self.start_menu()


SubNCalc()

# ip_address = y[0].split('.')
# ip_address = [int(a) for a in ip_address]
# print(ip_address)
'''if y[1] // 8 == 4:
    print('No addresses')
elif y[1] // 8 == 3:
    main_part = y[0][:-1]
    print(main_part)
elif y[1] // 8 == 2:
    main_part = y[0][:-3]
    print(main_part)
elif y[1] // 8 == 1:
    main_part = y[0][0:4]
    print(main_part)'''
'''a = {8: 256, 7: 128, 6: 64, 5: 32, 4: 16, 3: 8, 2: 4, 1: 2}
range_last = 0
for a, b in a.items():
    if a == power:
        range_last = b - 1
print(range_last)'''
'''max_number = (2 ** power) - 1
ip_list = []
num_list = [x for x in range(1, max_number)]
main_part = y[0][:-1]
for x in num_list:
    ip_list.append(main_part+str(x)+','+y[2]+','+y[3])'''
'''ip_list = []
max_number = ((2 ** 8) * (2 ** (power - 8))) - 2
power_r = power - 8
main_part = y[0][:-3]
last_num = (2 ** power_r)
last_num_list = [x for x in range(0, 256)]
tir_num_list = [x for x in range(0, last_num)]
for x in tir_num_list:
    for z in last_num_list:
        ip_list.append(main_part + str(x) + '.' + str(z)+','+y[2]+','+y[3])
ip_list.pop()
ip_list = ip_list[1::]
for x in ip_list:
    all_ip_list.append(x)'''
'''ip_list = []
max_number = (2 * (2 ** 8) * (2 ** (power - 16))) - 2
power_r = power - 16
main_part = y[0][0:4]
last_num = (2 ** power_r)
last_num_list = [x for x in range(0, 256)]
tir_num_list = [x for x in range(0, 256)]
sec_num_list = [x for x in range(0, last_num)]
for c in sec_num_list:
    for x in tir_num_list:
        for z in last_num_list:
            ip_list.append(main_part + str(c) + '.' + str(x) + '.' + str(z)+','+y[2]+','+y[3])
ip_list.pop()
ip_list = ip_list[1::]
for x in ip_list:
    all_ip_list.append(x)'''


