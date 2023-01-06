import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

plt.style.use('ggplot')

bi = np.random.randint(0,2,16)
print(bi)
b = 2*bi-1
print(b)
ln=len(b)
print(ln)
sig_len=4

bb=b.repeat(sig_len)
print(len(bb))
bbx=np.arange(sig_len*ln)
Rb = int(1000000) #taxa de amostragem
Tb = 1/Rb #periodo do bit
Tc = Tb/4 #periodo do chip

 #delta t
t_max = float((16*sig_len-1)*Tc)#tempo maximo
print(t_max)
print(Tc)
vetor_tempo=[]
vetor_tempo_bit = []
for i in np.arange(0,t_max+Tc,Tc):# gerando vetor tempo
    vetor_tempo.append(i)
for i in np.arange(0,t_max+Tc,0.000001):# gerando vetor tempo
    vetor_tempo_bit.append(i)
print(vetor_tempo_bit)
print(len(vetor_tempo_bit))
lens=len(bb)
print(lens)
# Sinal entrada
plt.figure(figsize=(8, 4.5))
plt.suptitle(r'espalhando')
plt.subplot(311)
plt.step(vetor_tempo_bit,b)
plt.title(r'Entrada')

#PN Code
chip = [1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1]
pr_sig=chip
print(pr_sig)
plt.subplot(312)
plt.step(vetor_tempo,pr_sig)
plt.title(r'PN Code')

# Spread Signal
C=np.multiply(bb,pr_sig)
print(sum(C))
if sum(C) != 0:
    pass
else:
    plt.subplot(313)
    plt.step(vetor_tempo,C)
    plt.title(r'Espalhando o sinal')
    plt.tight_layout()
    plt.subplots_adjust(top=0.88)
    ## De-spreading data
    plt.figure(figsize=(8, 4.5))
    plt.suptitle(r'Desespalhando')
    plt.subplot(311)
    C = np.multiply(bb, pr_sig)
    plt.step(vetor_tempo, C)
    plt.title(r'Sinal espalhado')
    plt.subplot(312)
    plt.step(vetor_tempo, pr_sig)
    plt.title(r'PN Code')
    D = np.multiply(C, pr_sig)
    plt.subplot(313)
    plt.step(vetor_tempo, D)
    plt.title(r'Saída')
    plt.tight_layout()
    plt.subplots_adjust(top=0.88)

# De-spreading with wrong PN code
#plt.figure(figsize=(8, 4.5))
#plt.suptitle(r'Desespalhando o sinal com PN errado')
#plt.subplot(311)
#plt.step(bbx,C)
#plt.title(r'Sinal Espalhado')
#plt.subplot(312)
#pr_sig_w=np.random.randint(2, size=lens)
#plt.step(bbx,pr_sig_w)
#plt.title(r'Pn Code')
#D=np.logical_xor(C,pr_sig_w)
#plt.subplot(313)
#plt.step(bbx,D)
#plt.title('Saida')

plt.tight_layout()
plt.subplots_adjust(top=0.88)

plt.show()