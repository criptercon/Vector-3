MAX_VERTICES = 100
MAX_FACES = 50
MAX_FACE_SIZE = 10 

num_vertices = int(input("Ingrese el número de vértices: "))

if num_vertices <= 0 or num_vertices > MAX_VERTICES:
    print(f"Error: El número de vértices debe estar entre 1 y {MAX_VERTICES}.")
else:
    vertices = []

    for i in range(num_vertices):
        x, y, z = map(float, input(f"Ingrese las coordenadas x, y, z del vértice {i + 1}: ").split())
        vertices.append((x, y, z))

    num_faces = int(input("Ingrese el número de caras: "))

    if num_faces <= 0 or num_faces > MAX_FACES:
        print(f"Error: El número de caras debe estar entre 1 y {MAX_FACES}.")
    else:
        faces = []

        for i in range(num_faces):
            face_size = int(input(f"Ingrese la cantidad de vértices de la cara {i + 1}: "))

            if face_size <= 0 or face_size > MAX_FACE_SIZE:
                print(f"Error: Una cara debe tener entre 1 y {MAX_FACE_SIZE} vértices.")
                break
            
            face_data = list(map(int, input(f"Ingrese los índices de los vértices de la cara {i + 1} (ejemplo: 1 2 3): ").split()))

            if len(face_data) != face_size or any(v < 1 or v > num_vertices for v in face_data):
                print("Error: Índices fuera de rango o cantidad incorrecta de vértices.")
                break

            faces.append(face_data)

        print("\nSalida en formato OBJ:")

        for v in vertices:
            print(f"v {v[0]} {v[1]} {v[2]}")

        for f in faces:
            print("f " + " ".join(map(str, f)))
