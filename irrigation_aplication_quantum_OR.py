from qiskit  import QuantumCircuit
from qiskit_aer import QasmSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def OR_quantum_port(a: int, b: int) -> int:


    circuit = QuantumCircuit(4, 1) # A, B, resultado, auxiliar


    # Inicializar entradas
    if a == 1:
        circuit.x(0) # solo seco
    if b == 1:
        circuit.x(1) # sem chuva

    # OR(A, B) = A XOR B XOR (A AND B)
    circuit.cx(0, 2)
    circuit.cx(1, 2)
    circuit.ccx(0, 1, 3)
    circuit.cx(3, 2)

    # Medir qubit 2 (resultado)
    circuit.measure(2, 0)

    # Executingn simulation
    simulator = QasmSimulator()
    result = simulator.run(circuit, shots=100).result().get_counts()
    output = int(max(result, key=result.get))
    return output

# Simulando sensores
def sensor_simulation():
    """
    Simula leituras dos sensores:
    - solo_seco = 1 se o solo estiver seco
    - sem_chuva = 1 se não houver previsão de chuva
    """
    # Exemplo 1: Solo úmido, com chuva - Desativado (ideal)
    #return {'solo_seco': 0, 'sem_chuva': 0}

    # Exemplo 2: Solo úmido, sem previsão de chuva - Ativado (manter)
    return {'solo_seco': 0, 'sem_chuva': 1}

    # Exemplo 3: Solo seco, com chuva - Ativado (complemento)
    #return {'solo_seco': 1, 'sem_chuva': 0}

    # Exemplo 4: Solo seco, sem previsão de chuva - Ativado (extremo)
    #return {'solo_seco': 1, 'sem_chuva': 1}
    

# IoT Application
def irrigation_system():
    sensores = sensor_simulation()
    solo = sensores['solo_seco']
    clima = sensores['sem_chuva']

    print(f"\n[Sensores] Solo seco: {solo}, Sem chuva: {clima}")

    start_irrigation = OR_quantum_port(solo, clima)

    if start_irrigation:
        print("💦 Irrigação ATIVADA!\n")
    else:
        print("✅ Irrigação NÃO necessária.\n")


# Executing
irrigation_system()