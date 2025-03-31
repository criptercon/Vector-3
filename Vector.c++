#include <iostream>

using namespace std;

int main() {
    const int MAX_VERTICES = 100;
    const int MAX_FACES = 50;
    const int MAX_FACE_SIZE = 10;

    float vertices[MAX_VERTICES][3];
    int faces[MAX_FACES][MAX_FACE_SIZE];
    int face_sizes[MAX_FACES];

    int num_vertices = 0, num_faces = 0;
  
    cout << "Ingrese el número de vértices: ";
    cin >> num_vertices;

    if (num_vertices > MAX_VERTICES || num_vertices <= 0) {
        cout << "Número de vértices fuera de rango.\n";
        return 1;
    }

    for (int i = 0; i < num_vertices; i++) {
        cout << "Ingrese las coordenadas x, y, z del vértice " << (i + 1) << ": ";
        cin >> vertices[i][0] >> vertices[i][1] >> vertices[i][2];
    }

    cout << "Ingrese el número de caras: ";
    cin >> num_faces;

    if (num_faces > MAX_FACES || num_faces <= 0) {
        cout << "Número de caras fuera de rango.\n";
        return 1;
    }

    for (int i = 0; i < num_faces; i++) {
        cout << "Ingrese la cantidad de vértices de la cara " << (i + 1) << " (máximo " << MAX_FACE_SIZE << "): ";
        cin >> face_sizes[i];

        if (face_sizes[i] > MAX_FACE_SIZE || face_sizes[i] <= 0) {
            cout << "Cantidad de vértices no válida.\n";
            return 1;
        }

        cout << "Ingrese los índices de los vértices de la cara (ejemplo: 1 2 3): ";
        for (int j = 0; j < face_sizes[i]; j++) {
            cin >> faces[i][j];

            if (faces[i][j] < 1 || faces[i][j] > num_vertices) {
                cout << "Error: Índice fuera de rango. Debe estar entre 1 y " << num_vertices << ".\n";
                return 1;
            }
        }
    }

    cout << "\nSalida en formato OBJ:\n";

    for (int i = 0; i < num_vertices; i++) {
        cout << "v " << vertices[i][0] << " " << vertices[i][1] << " " << vertices[i][2] << endl;
    }

    for (int i = 0; i < num_faces; i++) {
        cout << "f";
        for (int j = 0; j < face_sizes[i]; j++) {
            cout << " " << faces[i][j];
        }
        cout << endl;
    }

    return 0;
}
