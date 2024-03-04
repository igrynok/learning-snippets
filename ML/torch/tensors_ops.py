import torch

tensor = torch.ones(4, 4)
tensor[:1] = 0
print(tensor)

# joining tensors
t1 = torch.cat([tensor, tensor, tensor], dim=1)
print(t1)

# multiplying tensors
# element-wise
print(f"tensor.mul(tensor) \n {tensor.mul(tensor)} \n")
# alternative syntax
print(f"tensor * tensor \n {tensor * tensor}")

# dot product
print(f"tensor.matmul(tensor.T) \n {tensor.matmul(tensor.T)} \n")
# Alternative syntax:
print(f"tensor @ tensor.T \n {tensor @ tensor.T}")

# in-place operations
print(tensor)
tensor.add_(5)
print(tensor)