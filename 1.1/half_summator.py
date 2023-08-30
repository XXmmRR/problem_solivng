'''Наиболее простая арифметическая цепь называется полусумматор. Исследуйте и реализуйте её.'''


def half_adder(A, B):
    S = A ^ B  # Исключающее ИЛИ (XOR)
    C_out = A & B  # И (AND)
    return (S, C_out)


def full_adder(A, B, C_in):
    S = A ^ B ^ C_in
    C_OUT = (A and B) or (C_in and (A ^ B))
    return S, C_OUT


def eight_byte_adder(A1, A2, A3, A4, A5, A6, A7, A8, B1, B2, B3, B4, B5, B6, B7, B8):
    s1, c_out = full_adder(A1, B1, 0)
    s2, c_out = full_adder(A2, B2, c_out)
    s3, c_out = full_adder(A3, B3, c_out)
    s4, c_out = full_adder(A4, B4, c_out)
    s5, c_out = full_adder(A5, B5, c_out)
    s6, c_out = full_adder(A6, B6, c_out)
    s7, c_out = full_adder(A7, B7, c_out)
    s8, c_out = full_adder(A8, B8, c_out)
    return s1, s2, s3, s4, s5, s6, s7, s8


print(half_adder(0, 1))
print(full_adder(1, 1, 1))