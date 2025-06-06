from random import randint 

# A ideia desse arquivo maravilhoso aqui é servir como um módulo do arquivo Jogo.py
# Entretanto se você tirar o final do código que está comentado do comentário ele funciona como um jogo a parte
# Vale entretanto ressaltar que esse joguinho aqui não estava funcionando da última vez que eu testei só para deixar bem claro

nums1, nums2, soma_nat, subt_nat, mult_nat, div_nat, respostas = {}, {}, {}, {}, {}, {}, {}
qnt_acerto = 0
qnt_perguntas = 10
teto = 9

#parte que preenche as listas
def preenchedor(nums1, nums2, teto, qnt_perguntas):
    for i in range(0, qnt_perguntas):
        nums1[i] = randint(0,teto)
        nums2[i] = randint(0,teto)

# A função somador tem a importante tarefa de construir a lista soma_nat
# A lista soma_nat funciona como um gabarito para as questões de soma
def somador(nums1, nums2, soma_nat, qnt_perguntas):
    preenchedor(nums1, nums2, teto, qnt_perguntas)
    for i in range(0, qnt_perguntas):
        soma_nat[i] = nums1[i] + nums2[i]

# A função subtraidor tem uma função parecida com a função somador
# Mas nesse caso ela constrói a lista sub_nat
def subtraidor(nums1, nums2, subt_nat, qnt_perguntas):
    preenchedor(nums1, nums2, teto, qnt_perguntas)
    for i in range(0, qnt_perguntas):
        if nums1[i] < nums2[i]:
            aux = nums1[i]
            nums1[i] = nums2[i]
            nums2[i] = aux
    subt_nat[i] = nums1[i] - nums2[i]

def multiplicador(nums1, nums2, mult_nat):
    teto = 10
    preenchedor(nums1, nums2, teto, qnt_perguntas)
    for i in range(0, qnt_perguntas):
        mult_nat[i] = nums1[i] * nums2[i]



"""
somador(nums1, nums2, soma_nat, qnt_perguntas)
#parte que faz as perguntas

print("Fase 1 (Adição): ")
for i in range(qnt_perguntas):
    print("Quanto é ", nums1[i]," + ", nums2[i],"?")
    respostas[i] = int(input())
    if respostas[i] == soma_nat[i]:
        print("acertou miseravi")
        qnt_acerto += 1


print("Voce acertou:", qnt_acerto, "perguntas") 
qnt_acerto = 0


subtraidor(nums1,nums2,subt_nat)
print("Fase 2 (subtração): ")
for i in range(qnt_perguntas):
    print("Quanto é ", nums1[i]," - ", nums2[i],"?")
    respostas[i] = int(input())
    if respostas[i] == subt_nat[i]:
        print("acertou miseravi")
        qnt_acerto += 1

print("Voce acertou:", qnt_acerto, "perguntas") 
qnt_acerto = 0

multiplicador(nums1,nums2,mult_nat)
print("Fase 3 (Multiplicação): ")
for i in range(qnt_perguntas):
    print("Quanto é ", nums1[i]," x ", nums2[i],"?")
    respostas[i] = int(input())
    if respostas[i] == mult_nat[i]:
        print("acertou miseravi")
        qnt_acerto += 1

print("Voce acertou:", qnt_acerto, "perguntas") 
qnt_acerto = 0

"""