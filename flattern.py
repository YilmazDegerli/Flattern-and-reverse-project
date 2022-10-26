1. Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]

l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
new_l = []
def flattern(x):
    for i in x :
        if isinstance(i,list):
            flattern(i)
        else:
            new_l.append(i)

flattern(l)
print(new_l)
