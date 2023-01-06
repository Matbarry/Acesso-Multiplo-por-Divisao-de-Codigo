import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')
r1 = np.random.randint(0, 2, 16)  # gera um vetor aleatório de bits
r2 = np.random.randint(0, 2, 16)

# modulação polar
s = 2 * r1 - 1  # modulando o sinal aleatorio para polar
s2 = 2 * r2 - 1
b1 = np.repeat(s, 4)
b2 = np.repeat(s2, 4)
print(b1)
chip = [1, -1, 1, -1]
chip_er = [1, -1, -1, -1]
chip_1 = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1,
          -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1,
          1, -1]
chip_errado = [1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1,
               1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1,
               1, -1, -1, -1, 1, -1, -1, -1, ]
chip_2 = [1, 1, -1, -1]
chip_2_64 = [1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1,
             -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1,
             -1, -1, ]

espalhado = []
espalhado_errado = []
espalhado_chip1 = []
espalhado_chip2 = []

for i in np.arange(0, 16, 1):
    a = chip[0] * s[i]
    b = chip[1] * s[i]
    c = chip[2] * s[i]
    d = chip[3] * s[i]
    espalhado.append(a)
    espalhado.append(b)
    espalhado.append(c)
    espalhado.append(d)
    f = chip_er[0] * s[i]
    v = chip_er[1] * s[i]
    b = chip_er[2] * s[i]
    w = chip_er[3] * s[i]
    espalhado_errado.append(f)
    espalhado_errado.append(v)
    espalhado_errado.append(b)
    espalhado_errado.append(w)

print(s[0])
print(s)
print(chip)
print(espalhado)

Rb = int(1000000)  # taxa de bits
Tb = 1 / Rb
Tc = Tb / 4

# tempo max
t_max = float((16 * 4 - 1) * Tc)
print(t_max + Tc)
# vetores de tempo

vetor_tempo_bit = []

vetor_tempo = []

for i in np.arange(Tc, t_max + 2 * Tc, Tc):  # gerando vetor tempo
    vetor_tempo.append(i)
for i in np.arange(0, 0.000016, 0.000001):  # gerando vetor tempo
    vetor_tempo_bit.append(i)
print(vetor_tempo)
# plotando o sinal de entrada
plt.figure(figsize=(8, 4.5))
plt.suptitle(r'Processo de espalhamento')
plt.subplot(311)
plt.step(vetor_tempo, b1)
plt.title(r'Entrada')
plt.tight_layout()
plt.subplots_adjust(top=0.88)
# chip
plt.subplot(312)
plt.step(vetor_tempo, chip_1)
plt.title(r'Código PN')
plt.tight_layout()
plt.subplots_adjust(top=0.88)

# espalhando
plt.subplot(313)
plt.step(vetor_tempo, espalhado)
plt.title('Sinal espalhado')
plt.tight_layout()
plt.subplots_adjust(top=0.88)

# zoom entrada
plt.figure(figsize=(8, 4.5))
plt.suptitle(r'Processo de espalhamento')
plt.subplot(311)
plt.step(vetor_tempo, b1)
plt.xlim(0.000004, 0.000006)
plt.title(r'Entrada')
plt.tight_layout()
plt.subplots_adjust(top=0.88)
# chip
plt.subplot(312)
plt.step(vetor_tempo, chip_1)
plt.xlim(0.000004, 0.000006)
plt.title(r'Código PN')
plt.tight_layout()
plt.subplots_adjust(top=0.88)

# espalhando
plt.subplot(313)
plt.step(vetor_tempo, espalhado)
plt.xlim(0.000004, 0.000006)
plt.title('Sinal espalhado')
plt.tight_layout()
plt.subplots_adjust(top=0.88)

# recuperando
recuperado = []
recuperado_errado = []
for i in np.arange(0, 64, 1):
    cont = chip_1[i] * espalhado[i]
    cont_errado = chip_1[i] * espalhado_errado[i]
    recuperado.append(cont)
    recuperado_errado.append(cont_errado)

plt.figure(figsize=(8, 4.5))
plt.suptitle(r'Processo de recuperação')
plt.subplot(311)
plt.step(vetor_tempo, espalhado)
plt.title(r'Sinal espalhado')
plt.tight_layout()
plt.subplots_adjust(top=0.88)

plt.subplot(312)
plt.step(vetor_tempo, chip_1)
plt.title(r'Código PN')
plt.tight_layout()
plt.subplots_adjust(top=0.88)

plt.suptitle(r'Recuperando o sinal')
plt.subplot(313)
plt.step(vetor_tempo, recuperado)
plt.title(r'Saída')
plt.tight_layout()
plt.subplots_adjust(top=0.88)

# zom no recuperado
plt.figure(figsize=(8, 4.5))
plt.suptitle(r'Processo de recuperação')
plt.subplot(311)
plt.step(vetor_tempo, espalhado)
plt.xlim(0.000004, 0.000006)
plt.title(r'Sinal espalhado')
plt.tight_layout()
plt.subplots_adjust(top=0.88)

plt.subplot(312)
plt.step(vetor_tempo, chip_1)
plt.xlim(0.000004, 0.000006)
plt.title(r'Código PN')
plt.tight_layout()
plt.subplots_adjust(top=0.88)

plt.suptitle(r'Recuperando o sinal')
plt.subplot(313)
plt.step(vetor_tempo, recuperado)
plt.xlim(0.000004, 0.000006)
plt.title(r'Saída')
plt.tight_layout()
plt.subplots_adjust(top=0.88)

# chip errado
plt.figure(figsize=(8, 4.5))
plt.suptitle(r'Processo de espalhamento (errado)')
plt.subplot(311)
plt.step(vetor_tempo, b1)
plt.title(r'Entrada')
plt.tight_layout()
plt.subplots_adjust(top=0.88)
# chip
plt.subplot(312)
plt.step(vetor_tempo, chip_errado)
plt.title(r'Código PN errado')
plt.tight_layout()
plt.subplots_adjust(top=0.88)

# espalhando
plt.subplot(313)
plt.step(vetor_tempo, espalhado_errado)
plt.title('Sinal espalhado errado')
plt.tight_layout()
plt.subplots_adjust(top=0.88)

# recuperando sinal errado
plt.figure(figsize=(8, 4.5))
plt.suptitle(r'Processo de recuperação')
plt.subplot(311)
plt.step(vetor_tempo, espalhado_errado)
plt.title(r'Sinal espalhado (errado)')
plt.tight_layout()
plt.subplots_adjust(top=0.88)

plt.subplot(312)
plt.step(vetor_tempo, chip_errado)
plt.title(r'Código PN errado')
plt.tight_layout()
plt.subplots_adjust(top=0.88)

plt.suptitle(r'Recuperando o sinal (errado)')
plt.subplot(313)
plt.step(vetor_tempo, recuperado_errado)
plt.title(r'Saída')
plt.tight_layout()
plt.subplots_adjust(top=0.88)

espalhado_chip1 = []
espalhado_chip2 = []

for i in np.arange(0, 16, 1):
    a = chip[0] * s[i]
    b = chip[1] * s[i]
    c = chip[2] * s[i]
    d = chip[3] * s[i]
    espalhado_chip1.append(a)
    espalhado_chip1.append(b)
    espalhado_chip1.append(c)
    espalhado_chip1.append(d)
    f = chip_2[0] * s[i]
    v = chip_2[1] * s[i]
    b = chip_2[2] * s[i]
    w = chip_2[3] * s[i]
    espalhado_chip2.append(f)
    espalhado_chip2.append(v)
    espalhado_chip2.append(b)
    espalhado_chip2.append(w)

mt = []
for i in np.arange(0, 64, 1):
    h = espalhado_chip1[i] + espalhado_chip2[i]
    mt.append(h)

sm_c1 = 0
sm_c2 = 0
sm_c3 = 0
sm_c4 = 0
for i in np.arange(0, 4, 1):
    soma_1 = chip[i] * chip[i]
    sm_c1 = sm_c1 + soma_1
    soma_2 = chip_2[i] * chip_2[i]
    sm_c2 = sm_c2 + soma_2
    soma_3 = chip[i] * chip_2[i]
    sm_c3 = sm_c3 + soma_3

print("A correlação entre C1 e C1 é: ", sm_c2 / 4)
print("A correlação entre C2 e C2 é: ", sm_c1 / 4)
print("A correlação entre C1 e C2 é: ", sm_c3 / 4)

plt.figure(figsize=(8, 4.5))
plt.suptitle(r'Dois Usuários')
plt.subplot(311)
plt.step(vetor_tempo, b1)
plt.title(r'Sinal m1(t)')
plt.tight_layout()
plt.subplots_adjust(top=0.88)
plt.subplot(312)
plt.step(vetor_tempo, b2)
plt.title(r'Sinal m2(t)')
plt.tight_layout()
plt.subplots_adjust(top=0.88)

plt.figure(figsize=(8, 4.5))
plt.suptitle(r'Dois Usuários')
plt.subplot(311)
plt.step(vetor_tempo, espalhado_chip1)
plt.title(r'Sinal m1(t)c1(t)')
plt.tight_layout()
plt.subplots_adjust(top=0.88)
plt.subplot(312)
plt.step(vetor_tempo, espalhado_chip2)
plt.title(r'Sinal m2(t)c2(t)')
plt.tight_layout()
plt.subplots_adjust(top=0.88)

plt.subplot(313)
plt.step(vetor_tempo, mt)
plt.title(r'Sinais m1(t)c1(t)+m2(t)c2(t)')
plt.tight_layout()
plt.subplots_adjust(top=0.88)

plt.figure(figsize=(8, 4.5))
plt.suptitle(r'Sinais m1(t)c1(t)+m2(t)c2(t)')
plt.subplot(311)
plt.step(vetor_tempo, mt)
plt.title(r'Sinais somados')
plt.tight_layout()
plt.subplots_adjust(top=0.88)

plt.subplot(312)
plt.step(vetor_tempo, b1)
plt.title(r'Sinais m1(t)c1(t)c1(t)+m2(t)c2(t)c1(t)')
plt.tight_layout()
plt.subplots_adjust(top=0.88)

plt.subplot(313)
plt.step(vetor_tempo, b1)
plt.title(r'Sinal original m1(t)')
plt.tight_layout()
plt.subplots_adjust(top=0.88)

plt.figure(figsize=(8, 4.5))
plt.suptitle(r'Sinais m1(t)c1(t)+m2(t)c2(t)')
plt.subplot(311)
plt.step(vetor_tempo, mt)
plt.title(r'Sinais somados')
plt.tight_layout()
plt.subplots_adjust(top=0.88)

plt.subplot(312)
plt.step(vetor_tempo, b2)
plt.title(r'Sinais m1(t)c1(t)c2(t)+m2(t)c2(t)c2(t)')
plt.tight_layout()
plt.subplots_adjust(top=0.88)

plt.subplot(313)
plt.step(vetor_tempo, b2)
plt.title(r'Sinal original m2(t)')
plt.tight_layout()
plt.subplots_adjust(top=0.88)
# Sinais somados
plt.show()
