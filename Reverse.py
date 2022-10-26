2. Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]

l =[[1, 2], ["a", "b"], [5, 6, 7]]
l=l[::-1]

for i in range(len(l)):
    (l[i])=(l[i])[::-1]
print(l)
