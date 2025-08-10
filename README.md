# quantum-error-correction
This repo contains code for a decoder based on belief propagation. This decoder is used to correct errors in quantum communication where noise is modeled as pauli errors.

The decoder gives a list of most probable syndromes, on top of this, I am also using a technique called ordered statistics to figure out the most probable syndrome and its corresponding error vector.

Apart from this, I have also simulated results for different parity check matrices (used to generate the codebook to be used in the communication channel). These parity check matrices are based on cyclic graphs, popularly used in classical error correction. Edge-augmented versions of this parity check matricies are also used for simulations. 

Automation has been implemented to generate parity check matrices of color codes and surface codes along with their edge-augmented version, with a given order.
