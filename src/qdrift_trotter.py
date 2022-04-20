import numpy as np
from qiskit import QuantumCircuit
from qiskit.circuit.library import PauliEvolutionGate
from qiskit.opflow import I, Z, X, Y, PauliSumOp
from qiskit.synthesis import QDrift

from parser import parse
pauli_gates = [I, X, Y, Z]


def get_operator(A: np.ndarray, _time: float) -> PauliSumOp:
    final_operator = None
    for term in A:
        operator = pauli_gates[int(term[0])]

        for gate in term[1:]:
            operator = pauli_gates[int(gate)] ^ operator

        if final_operator == None:
            final_operator = operator
        else:
            final_operator = final_operator + operator

    assert final_operator is not None
    final_operator = final_operator * _time
    assert final_operator is not None

    return final_operator


def inbuilt_trotter(operator:PauliEvolutionGate, _order:int, _r: int) -> QuantumCircuit:
    print(_r)
    trotterizor = QDrift(reps=_r) # order 1 always.
    circ = trotterizor.synthesize(operator)
    return circ

def main():
    string = """2 2 3
    x_0 x_1
    z_0 z_1
    """
    A = parse(string)
    _order, _time, _r = 1, 2.0, 2
    operator = get_operator(A, _time)
    operator = PauliEvolutionGate(operator)
    circ = inbuilt_trotter(operator, _order, _r)
    decomposed = circ.decompose()
    print("High-level circuit:")
    print(circ)
    print("Low-level circuit:")
    print(decomposed)



if __name__ == "__main__":
    main()