import numpy as np
import random

class RubikCube:

    def __init__(self, N: int):
        self.faces = {
            "Top": [
                ["⬜", "⬜", "⬜"], 
                ["⬜", "⬜", "⬜"], 
                ["⬜", "⬜", "⬜"]
                ],
            "Bottom": [
                ["🟨", "🟨", "🟨"], 
                ["🟨", "🟨", "🟨"], 
                ["🟨", "🟨", "🟨"]
                ],
            "Left": [
                ["🟩", "🟩", "🟩"], 
                ["🟩", "🟩", "🟩"], 
                ["🟩", "🟩", "🟩"]
                ],
            "Right": [
                ["🟦", "🟦", "🟦"], 
                ["🟦", "🟦", "🟦"], 
                ["🟦", "🟦", "🟦"]
                ],
            "Front": [
                ["🟥", "🟥", "🟥"], 
                ["🟥", "🟥", "🟥"], 
                ["🟥", "🟥", "🟥"]
                ]
                ,
            "Back": [
                ["🟧", "🟧", "🟧"], 
                ["🟧", "🟧", "🟧"], 
                ["🟧", "🟧", "🟧"]
                ]
        }

    def U(self, k = 1):
        
        if k == 1:
            front = self.faces['Front'][0]
            self.faces['Front'][0] = self.faces['Right'][0]
            self.faces['Right'][0] = self.faces['Back'][0]
            self.faces['Back'][0] = self.faces['Left'][0]
            self.faces['Left'][0] = front

        if k == -1:
            back = self.faces['Back'][0]
            self.faces['Front'][0] = self.faces['Left'][0]
            self.faces['Right'][0] = self.faces['Front'][0]
            self.faces['Back'][0] = self.faces['Right'][0]
            self.faces['Left'][0] = back

    def D(self, k = 1):
        if k == 1:
            front = self.faces['Front'][2]
            self.faces['Front'][2] = self.faces['Right'][2]
            self.faces['Right'][2] = self.faces['Back'][2]
            self.faces['Back'][2] = self.faces['Left'][2]
            self.faces['Left'][2] = front

        if k == -1:
            back = self.faces['Back'][2]
            self.faces['Front'][2] = self.faces['Left'][2]
            self.faces['Right'][2] = self.faces['Front'][2]
            self.faces['Back'][2] = self.faces['Right'][2]
            self.faces['Left'][2] = back

    def R(self, k = 1):

        if k == 1:

            top = self.faces['Top']

            self.faces['Top'][0][2] = self.faces['Front'][0][2]
            self.faces['Top'][1][2] = self.faces['Front'][1][2]
            self.faces['Top'][2][2] = self.faces['Front'][2][2]

            self.faces['Front'][0][2] = self.faces['Bottom'][0][2]
            self.faces['Front'][1][2] = self.faces['Bottom'][1][2]
            self.faces['Front'][2][2] = self.faces['Bottom'][2][2]

            self.faces['Bottom'][0][2] = self.faces['Back'][0][2]
            self.faces['Bottom'][1][2] = self.faces['Back'][1][2]
            self.faces['Bottom'][2][2] = self.faces['Back'][2][2]            

            self.faces['Back'][0][2] = top[0][2]
            self.faces['Back'][1][2] = top[1][2]
            self.faces['Back'][2][2] = top[2][2]

        if k == -1:

            back = self.faces['Back']

            self.faces['Top'][0][2] = self.faces['Back'][0][2]
            self.faces['Top'][1][2] = self.faces['Back'][1][2]
            self.faces['Top'][2][2] = self.faces['Back'][2][2]

            self.faces['Front'][0][2] = self.faces['Top'][0][2]
            self.faces['Front'][1][2] = self.faces['Top'][1][2]
            self.faces['Front'][2][2] = self.faces['Top'][2][2]

            self.faces['Bottom'][0][2] = self.faces['Front'][0][2]
            self.faces['Bottom'][1][2] = self.faces['Front'][1][2]
            self.faces['Bottom'][2][2] = self.faces['Front'][2][2]            

            self.faces['Back'][0][2] = back[0][2]
            self.faces['Back'][1][2] = back[1][2]
            self.faces['Back'][2][2] = back[2][2]

    def L(self, k = 1):

        if k == 1:

            top = self.faces['Top']

            self.faces['Top'][0][0] = self.faces['Front'][0][0]
            self.faces['Top'][1][0] = self.faces['Front'][1][0]
            self.faces['Top'][2][0] = self.faces['Front'][2][0]

            self.faces['Front'][0][0] = self.faces['Bottom'][0][0]
            self.faces['Front'][1][0] = self.faces['Bottom'][1][0]
            self.faces['Front'][2][0] = self.faces['Bottom'][2][0]

            self.faces['Bottom'][0][0] = self.faces['Back'][0][0]
            self.faces['Bottom'][1][0] = self.faces['Back'][1][0]
            self.faces['Bottom'][2][0] = self.faces['Back'][2][0]            

            self.faces['Back'][0][0] = top[0][0]
            self.faces['Back'][1][0] = top[1][0]
            self.faces['Back'][2][0] = top[2][0]

        if k == -1:

            back = self.faces['Back']

            self.faces['Top'][0][0] = self.faces['Back'][0][0]
            self.faces['Top'][1][0] = self.faces['Back'][1][0]
            self.faces['Top'][2][0] = self.faces['Back'][2][0]

            self.faces['Front'][0][0] = self.faces['Top'][0][0]
            self.faces['Front'][1][0] = self.faces['Top'][1][0]
            self.faces['Front'][2][0] = self.faces['Top'][2][0]

            self.faces['Bottom'][0][0] = self.faces['Front'][0][0]
            self.faces['Bottom'][1][0] = self.faces['Front'][1][0]
            self.faces['Bottom'][2][0] = self.faces['Front'][2][0]            

            self.faces['Back'][0][0] = back[0][0]
            self.faces['Back'][1][0] = back[1][0]
            self.faces['Back'][2][0] = back[2][0]


    def B(self, k = 1):

        if k == 1:
            front = self.faces['Front'][2]
            self.faces['Front'][2] = self.faces['Right'][2]
            self.faces['Right'][2] = self.faces['Back'][2]
            self.faces['Back'][2] = self.faces['Left'][2]
            self.faces['Left'][2] = front

        if k == -1:
            back = self.faces['Back'][2]
            self.faces['Front'][2] = self.faces['Left'][2]
            self.faces['Right'][2] = self.faces['Front'][2]
            self.faces['Back'][2] = self.faces['Right'][2]
            self.faces['Left'][2] = back

    def shuffle(self, moves=20):
        moves_list = [self.U, self.D, self.R, self.L, self.B]
        for _ in range(moves):
            move = random.choice(moves_list)
            move(random.choice([1, -1]))
        print("Cube shuffled!")

    def display(self):
        print("    ", " ".join(self.faces['Top'][0]))
        print("    ", " ".join(self.faces['Top'][1]))
        print("    ", " ".join(self.faces['Top'][2]))
        for i in range(3):
            print(
                " ".join(self.faces['Left'][i]), " ",
                " ".join(self.faces['Front'][i]), " ",
                " ".join(self.faces['Right'][i]), " ",
                " ".join(self.faces['Back'][i])
            )
        print("    ", " ".join(self.faces['Bottom'][0]))
        print("    ", " ".join(self.faces['Bottom'][1]))
        print("    ", " ".join(self.faces['Bottom'][2]))

class RubikSolver:

    def __init__(self, cube: RubikCube):
        
        self.cube = cube

    def top_cross(self):
        pass

    def top_corners(self):
        pass

    def oll(self):
        pass

    def pll(self):
        pass