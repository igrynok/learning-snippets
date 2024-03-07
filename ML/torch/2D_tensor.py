import torch

a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]

A = torch.tensor(a)
print(A)
print(A.ndimension())
print(A.shape)
print(A[0][1])
print(A[0, :2])