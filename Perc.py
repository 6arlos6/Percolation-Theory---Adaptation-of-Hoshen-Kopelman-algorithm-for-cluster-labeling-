import numpy as np
import matplotlib.pyplot as plt
def R_matrix(L, p): #Matriz de unos y ceros.
		r = np.random.rand(L,L);
		R = np.zeros((L,L));
		for i in range(0,L):
			for j in range(0,L):
				if r[i,j] <= p:
					R[i,j] = 1;
				elif r[i,j] > p:
					R[i,j] = 0;
		return R
def Find(L, a, b, c, d, Lw): #Busca elementos en matriz.
	x = L[a,b];
	y = L[c,d];
	find_rc = Find_prim(L,x,Lw);
	row = find_rc[0];
	col = find_rc[1];

	for i in range(0,len(col)):
		aa = row[i];
		bb = col[i];
		L[aa,bb] = y; #cambie item
	return L
def Find_prim(a, b, Lw): #Complemento de la funcion Find.
	size = a.shape;
	row = np.array([], dtype=np.int64);
	col = np.array([], dtype=np.int64);
	#if len(b) == 1:
	for i in range(0,Lw):
		for j in range(0,Lw):
			if a[i,j] == b:
				row = np.append(row, i);
				col = np.append(col, j);
				#elif len(b) > 1: #Posible trabajo futuro.
					#size_b = b.shape;
					#for i in range(0,size[0]):
						#for j in range(0,size[1]):
							#for k in range(size_b[1]):
								#if a[i,j] == b[k]:
									#row = np.append(row, i);
									#col = np.append(row, j); 
	return [[row],[col]]
def Label(L, p): #Crea la matriz de clusters.
	R = R_matrix(L,p);
	iD = 1;
	label = np.zeros((L,L));
	for i in range(0,L):
		for j in range(0,L):
			if R[i,j]:
				l_a = Above_left(i,j,R);
				above = l_a[0];
				left = l_a[1];

				if left == 0 and above == 0:
					label[i,j] = iD;
					iD = iD + 1;
				elif left != 0 and above == 0:
					label[i,j] = label[i,j-1];
				elif left == 0 and above != 0:
					label[i,j] = label[i-1,j];
				else:
					Lab_prim = Find(label,i,j-1,i-1,j,L);
					label = Lab_prim;
					label[i,j] = label[i-1,j];
	return label
def Above_left(i, j, R): #Complementa la funcion Label.
	if i > 0 and j > 0:
		above = R[i-1,j];
		left = R[i,j-1];
	elif i > 0 and j == 0:
		above = R[i-1,j];
		left = 0;
	elif i == 0 and j > 0:
		above = 0;
		left = R[i,j-1];
	else:
		above = 0; 
		left = 0;
	return (above,left)

def main(): # Ejecutable.
	Lw = 200;
	p = 0.6;
	L = Label(Lw,p);
	print(L)
	plt.imshow(L)
	plt.colorbar()
	plt.show()

main()