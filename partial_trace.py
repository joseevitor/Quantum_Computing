from qiskit import QuantumCircuit, Aer, execute
from qiskit.quantum_info import DensityMatrix, partial_trace

# Creation of a simple quantum circuit with 2 qubits
qc = QuantumCircuit(2)
qc.h(0)           # Make a superposition on qubit 0
qc.cx(0, 1)       # Create an entanglement between the qubits

# simulation of final state
backend = Aer.get_backend('statevector_simulator')
job = execute(qc, backend)
result = job.result()
state = result.get_statevector(qc)

# build of density matrix from the vector of state
density_matrix = DensityMatrix(state)

# aplying partial trace to obtain the matrix of qubit 0 (discarding the qubit 1)
reduced_dm = partial_trace(density_matrix, [1])
print(reduced_dm)