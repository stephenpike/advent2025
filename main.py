import os

from dataclasses import dataclass

def main():
    print("Hello from advent2025!")

def read_text_file(path: str):
    with open(path) as f: 
        return f.read()

class Day_1:

    @dataclass
    class Instruction:
        direction: str
        value: int

    def __init__(self, data_path):
        self.data_path = data_path
        self.data = read_text_file(data_path)

        self.start_number = 50
        self.max_number = 99
        self.min_number = 0
        self.zero_counter = 0
        self.zero_passer_counter = 0

        self.current_number = self.start_number

    def parse_data(self):
        self.parsed_data = self.data.split()

    def parse_instruction(self, instruction):
        direction = instruction[0]
        value = int(instruction[1:])
        return self.Instruction(direction, value)

    def parse_instructions(self):
        self.parsed_instructions = [self.parse_instruction(i) for i in self.parsed_data]

    def update_pointer(self, instruction):
        if instruction.value == 0:
            raise ValueError("Instruction value is 0")

        if instruction.direction == "R":
            new_number = self.current_number + instruction.value
            while new_number > self.max_number:
                new_number = new_number - self.max_number - 1
                if new_number != 0 :
                    self.zero_passer_counter += 1
            self.current_number = new_number
            return

        if instruction.direction == "L":
            new_number = self.current_number - instruction.value
            starts_at_zero_flag = self.current_number == 0
            while new_number < self.min_number:
                self.zero_passer_counter += 1
                if starts_at_zero_flag:     
                    self.zero_passer_counter -= 1
                    starts_at_zero_flag = False                
                new_number = self.max_number + 1 + new_number
            self.current_number = new_number
            return
        
        raise ValueError("Direction must be 'L' or 'R'")
            
    def follow_instructions(self):
        for instruction in self.parsed_instructions:
            self.update_pointer(instruction)            
            if self.current_number == 0:
                self.zero_counter += 1
                self.zero_passer_counter += 1

    def solve(self):
        self.parse_data()
        self.parse_instructions()
        self.follow_instructions()        
        print("zero counter:", self.zero_counter)
        print("zero passer:", self.zero_passer_counter)

if __name__ == "__main__":
    main()
    day_1 = Day_1(os.path.join("data", "day_01.txt"))
    day_1.solve()