from qutip import basis, tensor

A = basis(2, 0)

B = tensor(A, A)

C = tensor(A, A, A)
