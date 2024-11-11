from cube import RubikCube
import numpy as np

# Example usage
if __name__ == "__main__":
    print('=======INITIAL STATE=======')
    dimension = 3  # Change this to create a different NxN cube
    cube = RubikCube(dimension)
    cube.display()

    print('=======SUFFLE=======')

    cube.shuffle()
    cube.display()