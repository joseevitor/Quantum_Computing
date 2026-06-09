# Quantum Computing with Qiskit

## Overview

This repository explores the fundamental concepts of **Quantum Computing** through practical implementations using **Qiskit**, IBM's open-source quantum computing framework.

The project covers core quantum phenomena, quantum algorithms, quantum state representations, and advanced topics such as **density matrices** and **partial trace operations**, providing both theoretical understanding and hands-on examples.


## What is Quantum Computing?

Quantum Computing is a computational paradigm based on the principles of **Quantum Mechanics**, enabling information processing in ways that are impossible for classical computers.

Unlike classical computers, which use **bits** that can only be `0` or `1`, quantum computers use **qubits**, which can exist in multiple states simultaneously through the phenomenon of **superposition**.

Combined with **entanglement** and **quantum interference**, quantum computers can solve specific problems significantly faster than classical systems.


## Fundamental Concepts

### Qubit (Quantum Bit)

The basic unit of information in quantum computing.

A qubit can exist in a quantum state represented as:

[
|\psi\rangle = \alpha|0\rangle + \beta|1\rangle
]

where:

* α and β are complex probability amplitudes
* |α|² + |β|² = 1

Unlike a classical bit, a qubit can represent both 0 and 1 simultaneously until measurement.


### Superposition

Superposition allows a quantum system to occupy multiple states at the same time.

For example:

[
\frac{|0\rangle + |1\rangle}{\sqrt{2}}
]

represents a qubit with equal probability of being measured as 0 or 1.


### Entanglement

Entanglement is a uniquely quantum phenomenon where two or more qubits become correlated.

An example Bell state:

[
|\Phi^+\rangle = \frac{|00\rangle + |11\rangle}{\sqrt{2}}
]

Measuring one qubit immediately determines the state of the other, regardless of distance.


### Quantum Interference

Quantum algorithms manipulate probability amplitudes to:

* Amplify correct solutions
* Suppress incorrect solutions

This mechanism provides the computational advantage behind many quantum algorithms.


### Decoherence

Decoherence occurs when a quantum system interacts with its environment and loses its quantum properties.

It is one of the main challenges in building reliable quantum computers.


## Bloch Sphere

The Bloch Sphere is a geometric representation of a single qubit state.

* North Pole → |0⟩
* South Pole → |1⟩
* Any other point → Quantum superposition

It provides an intuitive visualization of quantum states and quantum gates.


## Dirac Notation (Bra-Ket Notation)

Quantum states are commonly represented using Dirac notation.

Examples:

Ket:

[
|\psi\rangle
]

Bra:

[
\langle \psi|
]

Inner Product:

[
\langle \phi | \psi \rangle
]

This notation is extensively used throughout quantum mechanics and quantum computing.


## Density Matrices

In addition to state vectors, quantum states can be represented using **density matrices**.

A pure state:

[
\rho = |\psi\rangle\langle\psi|
]

Density matrices are useful for:

* Mixed quantum states
* Noise modeling
* Open quantum systems
* Quantum information analysis

Using Qiskit, density matrices allow deeper inspection of quantum systems beyond simple state vectors.


## Partial Trace

The **Partial Trace** is a mathematical operation used to observe a subsystem of a larger quantum system.

For an entangled system:

[
\rho_{AB}
]

the reduced state of subsystem A is obtained through:

[
\rho_A = Tr_B(\rho_{AB})
]

Applications:

* Entanglement analysis
* Quantum information theory
* Quantum communication
* Reduced density matrices

This repository includes practical examples using Qiskit's `partial_trace()` function.


## QASM (Quantum Assembly Language)

QASM is a low-level quantum programming language similar to Assembly in classical computing.

Example:

```qasm
OPENQASM 2.0;

qreg q[2];
creg c[2];

h q[0];
cx q[0], q[1];

measure q -> c;
```

Qiskit can transpile quantum circuits into QASM, allowing inspection of hardware-level instructions.


## Quantum Cryptography

Quantum Cryptography leverages quantum mechanical principles to provide secure communication.

A key property is that observing a quantum state alters it, making eavesdropping detectable.

Applications include:

* Quantum Key Distribution (QKD)
* BB84 Protocol
* Secure quantum communications


## Technologies Used

* Python
* Qiskit
* NumPy
* Matplotlib


## Learning Objectives

This repository aims to:

* Understand the foundations of quantum computing
* Explore quantum algorithms through simulation
* Learn quantum state representations
* Study density matrices and partial trace operations
* Develop practical experience with Qiskit
* Build intuition for quantum information processing


## References

* IBM Quantum Documentation
* Qiskit Documentation
* Nielsen & Chuang — *Quantum Computation and Quantum Information*
* MIT Quantum Information Science Courses
* Quantum Country
* Aprendaket
