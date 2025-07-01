class Testor:
    def __init__(self, test_input):
        self.number_of_test_cases = test_input[0]
        self.test_cases = test_input[1:]

    def __count_A(self, case):
        count = 0
        for i in range(5):
            if case[i] == 'A':
                count = count + 1
        return count

    def compare(self):

        for case in self.test_cases:
            count = self.__count_A(case)

            if count > 2:
                print('A')
            else:
                print('B')


testor = Testor([8, 'ABABB', 'ABABA', 'BBBAB', 'AAAAA',
                'BBBBB', 'BABAA', 'AAAAB', 'BAAAA'])
testor.compare()
