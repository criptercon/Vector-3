Documentación del Código en C++

Descripción del Programa
Este programa en C++ permite registrar los vértices y caras de una figura geométrica en 3D. Luego, imprime la figura en el formato OBJ, un estándar en gráficos 3D.

Funcionamiento del Código
El programa:

Solicita al usuario el número de vértices (con un máximo de 100).
Registra las coordenadas (x, y, z) de cada vértice.
Solicita el número de caras (con un máximo de 50).
Para cada cara, el usuario ingresa la cantidad de vértices (máximo 10).
Se ingresan los índices de los vértices que forman cada cara.
Imprime los datos en formato OBJ.

#include <iostream>  // Librería estándar para entrada y salida de datos

using namespace std;

int main() {
    // Definir los límites de la figura 3D
    const int MAX_VERTICES = 100;  // Máximo número de vértices permitidos
    const int MAX_FACES = 50;      // Máximo número de caras permitidas
    const int MAX_FACE_SIZE = 10;  // Máximo número de vértices por cara

    // Declaración de estructuras de datos
    float vertices[MAX_VERTICES][3]; // Matriz para almacenar los vértices (x, y, z)
    int faces[MAX_FACES][MAX_FACE_SIZE]; // Matriz para almacenar las caras (índices de vértices)
    int face_sizes[MAX_FACES]; // Arreglo que almacena cuántos vértices tiene cada cara

    int num_vertices = 0, num_faces = 0; // Variables para contar vértices y caras

    // Registro de VÉRTICES
    cout << "Ingrese el número de vértices: ";
    cin >> num_vertices;

    // Validación del número de vértices
    if (num_vertices > MAX_VERTICES || num_vertices <= 0) {
        cout << "Número de vértices fuera de rango.\n";
        return 1; // Finaliza el programa si el número no es válido
    }

    // Solicitar y almacenar los vértices
    for (int i = 0; i < num_vertices; i++) {
        cout << "Ingrese las coordenadas x, y, z del vértice " << (i + 1) << ": ";
        cin >> vertices[i][0] >> vertices[i][1] >> vertices[i][2];
    }

    // Registro de CARAS
    cout << "Ingrese el número de caras: ";
    cin >> num_faces;

    // Validación del número de caras
    if (num_faces > MAX_FACES || num_faces <= 0) {
        cout << "Número de caras fuera de rango.\n";
        return 1; // Finaliza el programa si el número no es válido
    }

    // Solicitar los datos de cada cara
    for (int i = 0; i < num_faces; i++) {
        cout << "Ingrese la cantidad de vértices de la cara " << (i + 1) << " (máximo " << MAX_FACE_SIZE << "): ";
        cin >> face_sizes[i];

        // Validación del tamaño de la cara
        if (face_sizes[i] > MAX_FACE_SIZE || face_sizes[i] <= 0) {
            cout << "Cantidad de vértices no válida.\n";
            return 1;
        }

        // Ingresar los índices de los vértices que forman la cara
        cout << "Ingrese los índices de los vértices de la cara (ejemplo: 1 2 3): ";
        for (int j = 0; j < face_sizes[i]; j++) {
            cin >> faces[i][j];

            // Validar que los índices estén en el rango permitido
            if (faces[i][j] < 1 || faces[i][j] > num_vertices) {
                cout << "Error: Índice fuera de rango. Debe estar entre 1 y " << num_vertices << ".\n";
                return 1;
            }
        }
    }

    // Impresión de la figura en formato OBJ
    cout << "\nSalida en formato OBJ:\n";

    // Imprimir los vértices en formato OBJ
    for (int i = 0; i < num_vertices; i++) {
        cout << "v " << vertices[i][0] << " " << vertices[i][1] << " " << vertices[i][2] << endl;
    }

    // Imprimir las caras en formato OBJ
    for (int i = 0; i < num_faces; i++) {
        cout << "f";
        for (int j = 0; j < face_sizes[i]; j++) {
            cout << " " << faces[i][j];
        }
        cout << endl;
    }

    return 0; // Fin del programa
}
Explicación del Código

Declaración de Variables
MAX_VERTICES = 100: Límite de vértices.
MAX_FACES = 50: Límite de caras.
MAX_FACE_SIZE = 10: Límite de vértices por cara.
vertices[MAX_VERTICES][3]: Matriz para almacenar las coordenadas de los vértices.
faces[MAX_FACES][MAX_FACE_SIZE]: Matriz para almacenar las caras.
face_sizes[MAX_FACES]: Arreglo que guarda el número de vértices de cada cara.

Entrada de Datos
Número de vértices: Se solicita y se almacena en num_vertices.
Coordenadas de cada vértice: Se almacenan en la matriz vertices.
Número de caras: Se almacena en num_faces.

Cada cara:

Se almacena la cantidad de vértices (face_sizes).
Se ingresan los índices de los vértices que la componen.

Validaciones
Se verifica que el número de vértices y caras esté en los límites definidos.
Se valida que los índices de los vértices de cada cara sean correctos.

Salida en Formato OBJ
Se imprime cada vértice en la forma v x y z.

Se imprimen las caras en la forma f 1 2 3.

Ejemplo de Uso
Entrada del Usuario

Ingrese el número de vértices: 4
Ingrese las coordenadas x, y, z del vértice 1: 0 0 0
Ingrese las coordenadas x, y, z del vértice 2: 1 0 0
Ingrese las coordenadas x, y, z del vértice 3: 1 1 0
Ingrese las coordenadas x, y, z del vértice 4: 0 1 0

Ingrese el número de caras: 1
Ingrese la cantidad de vértices de la cara 1 (máximo 10): 4
Ingrese los índices de los vértices de la cara 1 (ejemplo: 1 2 3): 1 2 3 4

Salida Generada
Salida en formato OBJ:
v 0 0 0
v 1 0 0
v 1 1 0
v 0 1 0
f 1 2 3 4

¿Cómo Compilar y Ejecutar el Programa?
Compilar en C++ (g++)

Ejecutar
./programa
