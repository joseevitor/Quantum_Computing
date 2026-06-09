from qiskit  import QuantumCircuit
from qiskit_aer import QasmSimulator

def OR_simulation(a: int, b: int) -> int:
    # 3 qubits (A, B, output), 1 classic bit to measure
    circuit = QuantumCircuit(3, 1)

    # initialize the A (q0) and B (q1)
    if a==1:
        circuit.x(0)   # qubit A
    if b==1:
        circuit.x(1)   # qubit B


    # use De Morgan: OR = NOT(NOT A AND NOT B)
    circuit.x(0)                    # NOT A
    circuit.x(1)                    # NOT B
    circuit.ccx(0, 1, 2)            # AND(NOT A, NOT B) -> q2
    circuit.x(2)                      # NOT of result -> OR(A, B)
    circuit.x(0)                      # reset A
    circuit.x(1)                      # reset B
    
    # To measure to output (q2)
    circuit.measure(2, 0)


    # Simulation
    simulator = QasmSimulator()
    job =simulator.run(circuit, shots=1)
    result = job.result().get_counts()


    # Return the binary value measured (like an int)
    return int(max(result, key=result.get))

# Generate table true
print("\n Table True - Port OR (Simulated with Qiskit)\n")
print("| A | B | OR |")
print("|---|---|----|")

for a in [0, 1]:
    for b in [0, 1]:
        result = OR_simulation(a, b)
        print(f"| {a} | {b} | {result}  |")

print("|---|---|----|\n")