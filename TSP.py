import sys
from itertools import permutations

def tsp_brute_force(graph):
    num_vertices = len(graph)
    # Membuat daftar semua kemungkinan permutasi kunjungan
    all_permutations = permutations(range(1, num_vertices))
    min_distance = sys.maxsize
    optimal_path = []

    # Melakukan perhitungan jarak minimum dan menyimpan jalur optimal
    for permutation in all_permutations:
        current_path = list(permutation)
        current_distance = 0

        # Menambahkan jarak dari titik awal ke titik pertama dalam permutasi
        current_distance += graph[0][current_path[0]]

        # Menambahkan jarak antara setiap pasangan titik dalam permutasi
        for i in range(num_vertices - 2):
            current_distance += graph[current_path[i]][current_path[i + 1]]

        # Menambahkan jarak dari titik terakhir dalam permutasi ke titik awal
        current_distance += graph[current_path[-1]][0]

        # Memperbarui jarak minimum dan jalur optimal jika ditemukan permutasi dengan jarak lebih kecil
        if current_distance < min_distance:
            min_distance = current_distance
            optimal_path = [0] + current_path + [0]

    return min_distance, optimal_path

# Contoh penggunaan
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

min_dist, opt_path = tsp_brute_force(graph)
print("Jarak Terpendek:", min_dist)
print("Jalur Optimal:", opt_path)
