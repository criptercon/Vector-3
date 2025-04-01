num_vertices = int(input("Ingrese el número de vértices: "))

if num_vertices <= 0:
    print("Número de vértices no válido.")
else:
    vertices = []
    for i in range(num_vertices):
        x, y, z = map(float, input(f"Ingrese las coordenadas x, y, z del vértice {i + 1}: ").split())
        vertices.append((x, y, z))

    num_faces = int(input("Ingrese el número de caras: "))

    if num_faces <= 0:
        print("Número de caras no válido.")
    else:
        faces = []
        for i in range(num_faces):
            face_data = list(map(int, input(f"Ingrese los índices de los vértices de la cara {i + 1} (ejemplo: 1 2 3): ").split()))
            
            if any(v < 1 or v > num_vertices for v in face_data):
                print("Error: Índice fuera de rango.")
            else:
                faces.append(face_data)

        print("\nSalida en formato OBJ:")
        for v in vertices:
            print(f"v {v[0]} {v[1]} {v[2]}")
        
        for f in faces:
            print("f " + " ".join(map(str, f)))
