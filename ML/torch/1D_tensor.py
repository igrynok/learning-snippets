import torch

a = torch.tensor([1, 2, 3, 4, 6])

# access by index
print(a[4])
# slicing
print(a[1:])

print(a.shape)
# rank
print(a.ndimension())

# transforming 1D to 2D or a_col = a.view(-1, 1)
a_col = a.view(5, 1)
print(a_col)
print(a_col.ndimension())

# dot product
b = torch.tensor([1, 2, 3])
c = torch.tensor([0, 0, 1])
print(torch.dot(b, c))