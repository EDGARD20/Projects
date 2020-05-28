

class GetStatistic:
    def __init__(self):
        pass

    def get_number_student(self):
        return int(input())

    def get_list_student(self):
        list_student = []
        temp = input().split()
        list_student.extend(temp)
        return list(map(int, list_student))

    def get_avg(self, lst):
        return sum(lst) / len(lst)


class CompareStatistic:
    def __init__(self):
        pass

    def compare_list(self, list1, list2):
        if list1[0] > list2[0]:
            self.print_out(list1)
            self.print_out(list2)
            print('A')
        elif list2[0] > list1[0]:
            self.print_out(list1)
            self.print_out(list2)
            print('B')
        elif list1[0] == list2[0]:
            if list1[1] > list2[1]:
                self.print_out(list1)
                self.print_out(list2)
                print('A')
            elif list2[1] > list1[1]:
                self.print_out(list1)
                self.print_out(list2)
                print('B')
            else:
                self.print_out(list1)
                self.print_out(list2)
                print('Same')

    def print_out(self, list_a):
        for k in range(0, len(list_a)):
            print(list_a[k])



if __name__ == "__main__":
    m = GetStatistic()

    List_classA = []
    List_classB = []
    result1 = m.get_number_student()
    for i in range(1, 4):
        result_statistic = m.get_list_student()
        List_classA.append(m.get_avg(result_statistic))
    result2 = m.get_number_student()
    for i in range(1, 4):
        result_statistic = m.get_list_student()
        List_classB.append(m.get_avg(result_statistic))

    CS = CompareStatistic()
    CS.compare_list(List_classA, List_classB)




