from typing import List
from qiskit.circuit.library import PauliEvolutionGate
from parser import parse, get_operator

from inbuilt_naive import inbuilt_trotter
from suzuki_trotter import suzuki_trotter
from qdrift_trotter import qdrift_trotter


from visual_utilities import plot_line_graphs

ORDER = [False, False, True]

methods = {
    "Inbuilt Standard": inbuilt_trotter,
    "qDRIFT": qdrift_trotter,
    "Suzuki": suzuki_trotter,
}


def get_gate_complexity(operator: PauliEvolutionGate, _order: int, _r: int) -> dict:
    gate_complexity = {}

    for ind, method in enumerate(methods):
        if ORDER[ind]:
            circ = methods[method](operator, _order=_order, _r=_r)
        else:
            circ = methods[method](operator, _r=_r)

        gate_complexity[method] = circ.depth()

    return gate_complexity


def get_gate_complexity_range(
    operator: PauliEvolutionGate, _order: int, r_list: List[int]
) -> dict:
    gate_complexities = {method: [] for method in methods}

    for r in r_list:
        gate_complexity = get_gate_complexity(operator, _order, r)
        for method in gate_complexity:
            gate_complexities[method].append(gate_complexity[method])

    return gate_complexities


def main():
    string = """2 2 3
    x_0 x_1
    z_0 z_1
    """
    _order, _time, _r = 2, 2.0, 2
    r_list = list(range(11))[1:]

    A = parse(string)
    operator = get_operator(A, _time)
    operator = PauliEvolutionGate(operator)

    gate_complexities = get_gate_complexity_range(operator, _order, r_list)
    labels = ("r values", "gate complexity")
    title = "Gate complexity for Trotter number"
    plot_line_graphs(r_list, gate_complexities, labels, title)


if __name__ == "__main__":
    main()
