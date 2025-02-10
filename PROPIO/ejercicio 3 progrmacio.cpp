#include <iostream>
#include <vector>

void Ordenar_Vector(std::vector<int>& vec) {
    int n = vec.size();
    for (int k = 0; k < n - 1; ++k) {
        for (int g = 0; g < n - k - 1; ++g) {
            if (vec[g] > vec[g + 1]) {
                // Intercambiar vec[g] y vec[g + 1]
                std::swap(vec[g], vec[g + 1]);
            }
        }
    }
}

int main() {
    int n; // Declaración de variable n, la cual es la cantidad de n numero de posiciones del vector.

    // Solicitar el tamaño del vector
    std::cout << "Ingrese el numero de elementos del vector: ";
    std::cout << std::endl; // Salto de linea en blanco
    std::cin >> n;

    std::vector<int> vec(n);

    // Cargar el vector
    std::cout << "Ingrese los elementos del vector:\n";
    std::cout << std::endl; // Salto de linea en blanco
    for (int k = 0; k < n; ++k) {
        std::cout << "Elemento " << k + 1 << ": ";
        std::cin >> vec[k];
    }

    // Ordenar el vector
    Ordenar_Vector(vec);

    // Mostrar el vector ordenado
    std::cout << "\nVector ordenado de forma ascendente:\n";
    std::cout << std::endl; // Salto de linea en blanco
    for (int k = 0; k < n; ++k) {
        std::cout << vec[k] << " ";
    }
    std::cout << std::endl; // Salto de linea en blanco

    return 0;
}
