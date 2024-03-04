import torch
import numpy as np

data = [[1, 2], [3, 4]]

# create tensor directly from an array
x_data = torch.tensor(data)
print('Tensor from an array:')
print(x_data)
print()

# create tensor from a numpy array
np_array = np.array(data)
x_np = torch.from_numpy(np_array)
print('Tensor from numpy array:')
print(x_np)
print()

# tensor retains properties of another tensor
x_ones = torch.ones_like(x_np)
print(f"Ones Tensor: \n {x_ones} \n")
print()

x_rand = torch.rand_like(x_data, dtype=torch.float)
print(f"Random Tensor: \n {x_rand} \n")


# shape

shape = (2,3,)
rand_tensor = torch.rand(shape)
ones_tensor = torch.ones(shape)
zeros_tensor = torch.zeros(shape)

print(f"Random Tensor: \n {rand_tensor} \n")
print(f"Ones Tensor: \n {ones_tensor} \n")
print(f"Zeros Tensor: \n {zeros_tensor}")