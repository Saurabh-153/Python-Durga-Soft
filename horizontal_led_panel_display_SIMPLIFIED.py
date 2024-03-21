def print_row(*col):
	for i in range(5):
		if i in col:
			print('*',end=' ')
		else:
			print(' ',end=' ')

def row_0():
	print_row(0)

def row_2():
	print_row(2)

def row_0_4():
	print_row(0,4)

def row_1_2_3():
	print_row(1,2,3)

def row_0_1_2_3():
	print_row(0,1,2,3)

def row_0_1_2_3_4():
	print_row(0,1,2,3,4)

def row_0_2_4():
	print_row(0,2,4)

def row_0_2():
	print_row(0,2)
def row_1_3():
	print_row(1,3)
def row_0_3():
	print_row(0,3)
def row_0_3_4():
	print_row(0,3,4)
def row_1():
	print_row(1)
def row_4():
	print_row(4)
def row_0_1_3_4():
	print_row(0,1,3,4)

C2=C3=C4=E1=E2=E4=E5=F1=F2=F4=F5=F6=G2=L0=L1=L2=L3=L4=L5=P4=P5=P6=S2=Z5=row_0

A1=A2=A4=A5=A6=B1=B2=B4=B5=C1=C5=D1=D2=D3=D4=D5=G1=G4=G5=H0=H1=H2=H4=H5=H6=K0=K6=M0=M3=M4=M5=M6=N0=N1=N5=N6=O1=O2=O3=O4=O5=P1=P2=Q1=Q2=Q3=R1=R2=R6=S1=S5=U0=U1=U2=U3=U4=U5=V0=V1=V2=V3=V4=W0=W1=W2=W3=W6=X0=X1=X5=X6=Y0=Y1=row_0_4

I1=I2=I3=I4=I5=J1=J2=J3=J4=T1=T2=T3=T4=T5=T6=V6=X3=Y3=Y4=Y5=Y6=Z3=row_2

A0=C0=C6=G0=G6=O0=O6=Q0=S0=S3=S6=U6=Y2=row_1_2_3
B0=B3=B6=D0=D6=P0=P3=R0=R3=row_0_1_2_3
A3=E0=E3=E6=F0=F3=H3=I0=I6=J0=L6=T0=Z0=Z6=row_0_1_2_3_4
M2=N3=Q4=W4=row_0_2_4
J5=K2=K4=R4=row_0_2
V5=X2=X4=row_1_3
K1=K5=R5=row_0_3
N4=Q5=row_0_3_4
J6=Z4=row_1
S4=Z1=row_4
M1=W5=row_0_1_3_4

def G3():
	print_row(0,2,3,4)
def K3():
	print_row(0,1)
def N2():
	print_row(0,1,4)
def Q6():
	print_row(1,2,3,4)
def Z2():
	print_row(3)
word=input('Enter Any Word To print Horizontally:')
for i in range(7):
	for ch in word:
		exec(ch+str(i)+'()')
		print(end=' ')
	print()