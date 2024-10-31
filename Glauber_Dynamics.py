import numpy as np
import matplotlib.pyplot as plt

class GlauberDynamics:
    """
    A class for simulating the spin flips in an Ising Model

    Args:
        grid (array): Lattice of particles' spins, -1 = down | +1 = up
        temp (float, opt.): Temperature of the model. Default is 0
        seed (float, opt.): Random seed for simulation, Default is None
        store_history (bool, opt.): Keeps a record of past steps. Default is False.

    Attributes:
        history (list, opt.): Record of past grids

    Methods:
        step: Simulate a single step of the process
        run: Simulate the process for a given number of steps

    Notes:
        Algorithm used: https://en.wikipedia.org/wiki/Glauber_dynamics
    """
    def __init__(self, grid, temp= 0, seed= None, store_history= False):
        self.grid = grid
        self.temp = temp
        self.seed = seed
        # boundary conditions, edges are given values of 0
        self.grid_copy = np.pad(grid, pad_width= 1)
        self.store_history = store_history
        if store_history == True:
            self.history == []
        pass
    
    def step(self):
        """Chooses a random lattice site and determines if it flips."""
        np.random.seed(self.seed)
        i = np.random.randint(1, len(self.grid_copy[0]) - 1)
        j = np.random.randint(1, len(self.grid_copy) - 1)

        spin_sum = self.grid_copy[i+1][j] + self.grid_copy[i][j+1] + self.grid_copy[i-1][j] + self.grid_copy[i][j-1]
        del_E = 2*self.grid_copy[i][j]*spin_sum

        if self.temp != 0:
            p = 1/(1 + np.e**(del_E/self.temp))
        else:
            p = 0

        if np.random.rand() < p:
            self.grid_copy[i][j] *= -1

        if self.store_history == True:
            self.history.append(self.grid_copy)

    def run(self, n):
        """
        Simulates spin flips for n_steps.

        Args:
            n (int): The number of steps to simulate
        """    
        for i in range(n):
            self.step()
        

    def __str__(self):
        """
        Prints the current grid. Red = Up | Blue = Down | White = Boundary
        """
        plt.figure()
        plt.imshow(self.grid_copy, cmap='coolwarm')
        plt.title("Current State")
        plt.show()
        return "PyPlot"
        
# Testing Block
myGrid = np.random.choice((-1,1), size= (4,5))
print(myGrid)
model = GlauberDynamics(myGrid, temp= 0)
print(model)
