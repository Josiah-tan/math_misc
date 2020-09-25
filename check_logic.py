import numpy as np#B, q1, q2 = [int(i) for i in input("B q1 q2 ").split()]
class Output:
    #put the output functions here, the parameters should be written in order of input
    def q1_star(self, B, q1, q2):
        return not(not(B and not(q1)) and not(q2))

    def q2_star(self, B, q1, q2):
        return not(B or q1)

class TruthTable(Output):
    def __init__(self, num_inputs, num_outputs):
        # sets the number of inputs and the number of outputs for the truth table
        self.num_inputs = num_inputs
        self.num_outputs = num_outputs
    def create_table(self):
        # just initilises a table 
        self.table_rows = 2 ** self.num_inputs
        self.table_cols = self.num_inputs + self.num_outputs
        self.truth_table = np.zeros((self.table_rows, self.table_cols))
        self.input_init()
    def input_init(self):
        # basically sets the 1s and 0s as coording to the style requirements
        for col in range(self.num_inputs):
            counter = 0
            bit = 0
            limit = self.table_rows / (2**(col + 1))
            for row in range(self.table_rows):
                self.truth_table[row][col] = bit
                counter += 1
                if counter >= limit:
                    counter = 0
                    bit = bit == 0
                

    def calc_outputs(self):
        #hardcoded stuff, could use some improving
        for row in range(self.table_rows):
            self.truth_table[row][self.num_inputs] = self.q1_star(*self.truth_table[row, 0:self.num_inputs])
            self.truth_table[row][self.num_inputs + 1] = self.q2_star(*self.truth_table[row, 0:self.num_inputs])
                

truth_table = TruthTable(3, 2)
truth_table.create_table()
print("Initialised Table")
print(truth_table.truth_table)
truth_table.calc_outputs()
print("Final Table")
print(truth_table.truth_table)
