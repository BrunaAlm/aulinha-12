import math
print( math.factorial(6))


#TRABALHANDO COM DICIONÁRIOS


classe = {"Breno": 4.5,
          "Bruna": 9.5,
          "Gabrieli": 5.4,
          "Murilo":7.0,
          "Poliana": 8.5}
notas = classe.values()
média = sum(notas)/5
print("A média da classe é ", média)



dic = {"Salgado": 4.50,
        "Lanche": 6.50,
       "Suco": 3.00,
       "Refrigerante": 3.50,
       "Doce": 1.00}
print(dic)



D = {"arroz": 17.30,"feijão": 12.50,"carne": 23.90,"alface": 3.40}
print(D)

D["carne"] = 25.0
D["tomate"] = 8.80
print(D)


T = (10,20,30,40,50)
a,b,c,d,e = T
print("a =",a,"b =",b)

print("d + e =",d+e)