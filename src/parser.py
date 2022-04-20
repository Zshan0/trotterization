from typing import List, Tuple
import numpy as np


pauli_map = {"I": 0, "X": 1, "Y": 2, "Z": 3}


def parse(string: str) -> np.ndarray:
    """
    Parses the input.
    input format:
    Tau, k, n
    (p_{11})_(q_{11}) ...
    (p_{21}_(q_{21})) ...
    Where p_{11} is the pauli matrix present in the first term of the sum
    and is being applied on the qubit q_{11}.

    returns:
    matrix A of size k x n
    m_{ij} - operator acting present in the ith term acting on jth qubit.
    """

    string = string.upper()

    string_lines = string.splitlines()
    tau, k, n = map(int, string_lines[0].split())

    A = np.zeros((tau, n))

    for ind, row in enumerate(string_lines[1:]):
        operators = row.split()
        assert len(operators) <= k

        for operator in operators:
            gate, qubit = operator.split("_")
            qubit = int(qubit)
            pauli_num = pauli_map[gate]
            A[ind][qubit] = pauli_num

    return A


def main():
    string = """3 3 10
    x_0 y_1
    x_1 x_2
    z_0"""
    print(parse(string))


if __name__ == "__main__":
    main()
