import os,sys,json,time,random
import urllib.request as UR
NB=110000
INF=1000000
VMG=(0,100,320,330,500,1000,0)
PBM=(0,0,4,8,16,28,45,0)
PM='kkkkuuuummoqllmpkkkoljiklmmgkkkk'
NM='aceecgkkekmnelnoeknoelmncgklacee'
BM='giiiikkkiklmillmikmmimmmilkkgiii'
KM='eccaeccaeccaeccageecigggookkoqmk'
CMG=[0]*832
TM=(None,PM,NM,BM,None,None,KM)
for _a in range(1,7):
 for _s in (1,-1):
  _o=(_s*_a+6)*64; _m=TM[_a]
  for _q in range(64):
   _r=_q>>3; _f=_q&7; _h=((7-_r) if _s>0 else _r)*4+(_f if _f<4 else 7-_f)
   CMG[_o+_q]=_s*(VMG[_a]+((ord(_m[_h])-107)*5 if _m else 0))
B=[0]*64;CNT=[0]*13;PS=[0]
SIDE=1;CAST=0;EP=-1;KW=4;KB=60;HASH=0
U=[];TT={}
ND=[0];T0=[0.0];KIL=[[0,0]for _ in range(128)];HIS=[0]*4096;RP={}
_g=random.Random(987654321).getrandbits
Z=[[_g(64) for _ in range(64)] for _ in range(13)]
ZS=_g(64)
KN=[[] for _ in range(64)];RAYS=[None]*64
D8=((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
ALLD=range(8)
for _sq in range(64):
 _r,_f=_sq>>3,_sq&7
 KN[_sq]=[(_r+dr)*8+_f+df for dr,df in ((-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)) if 0<=_r+dr<8 and 0<=_f+df<8]
 RAYS[_sq]=[[(_r+k*dr)*8+_f+k*df for k in range(1,8) if 0<=_r+k*dr<8 and 0<=_f+k*df<8] for dr,df in D8]
CK={0:13,4:12,7:14,56:7,60:3,63:11}
CST8=((1,4,(5,6),(4,5,6)),(2,4,(3,2,1),(4,3,2)),(4,60,(61,62),(60,61,62)),(8,60,(59,58,57),(60,59,58)))
EPF=1<<18;CSTF=1<<19;DBLF=1<<20
class _Abort(Exception): pass
def A(sq,by):
 for d in ((0,2) if by>0 else (5,7)):
  _r=RAYS[sq][d]
  if _r and B[_r[0]]==by: return True
 for t in KN[sq]:
  if B[t]==by*2: return True
 for d in ALLD:
  _r=RAYS[sq][d]
  if _r and B[_r[0]]==by*6: return True
  for t in _r:
   p=B[t]
   if p:
    if p==by*5 or p==(by*3 if d in (0,2,5,7) else by*4): return True
    break
 return False
def _bad(): return A(KW if SIDE<0 else KB,SIDE)
def _chk(): return A(KW if SIDE>0 else KB,-SIDE)
def SF(fen):
 global SIDE,CAST,EP,KW,KB,HASH
 parts=fen.split(); rows=parts[0].split('/')
 B[:]=[0]*64; CNT[:]=[0]*13
 PS[:]=[0]; HASH=0; U.clear()
 for i,row in enumerate(rows):
  r=7-i; f=0
  for ch in row:
   if ch.isdigit(): f+=int(ch)
   else:
    p=("pnbrqk".index(ch.lower())+1)*(1 if ch.isupper() else -1); sq=r*8+f
    B[sq]=p; j=p+6; CNT[j]+=1; HASH^=Z[j][sq]; j=j*64+sq; PS[0]+=CMG[j]
    if abs(p)==6: KW,KB=(sq,KB) if p>0 else (KW,sq)
    f+=1
 SIDE=1 if len(parts)<2 or parts[1]=='w' else -1
 if SIDE<0: HASH^=ZS
 cs=parts[2] if len(parts)>2 else '-'
 CAST=sum(1<<i for i,ch in enumerate("KQkq") if ch in cs)
 EP=-1
 if len(parts)>3 and parts[3]!='-': EP=(int(parts[3][1])-1)*8+(ord(parts[3][0])-97)
def G(caps=False):
 ms=[]; s=SIDE; b=B; apnd=ms.append
 for sq in range(64):
  p=b[sq]
  if not p or (p>0)!=(s>0): continue
  ap=abs(p); r=sq>>3; f=sq&7
  def ad(t):
   tp=b[t]
   if not tp:
    if not caps: apnd(sq|(t<<6))
   elif (tp>0)!=(s>0): apnd(sq|(t<<6)|(abs(tp)<<15))
   return tp
  def adp(to,cp):
   for pr in (5,4,3,2): apnd(sq|(to<<6)|(pr<<12)|(cp<<15))
  if ap==1:
   u=sq+8*s; prm=r==(6 if s>0 else 1)
   if not b[u]:
    if prm: adp(u,0)
    elif not caps:
     apnd(sq|(u<<6))
     if r==(1 if s>0 else 6) and not b[sq+16*s]: apnd(sq|((sq+16*s)<<6)|DBLF)
   for df in (-1,1):
    if 0<=f+df<8:
     t=u+df; tp=b[t]
     if tp and (tp>0)!=(s>0):
      if prm: adp(t,abs(tp))
      else: apnd(sq|(t<<6)|(abs(tp)<<15))
     elif t==EP: apnd(sq|(t<<6)|(1<<15)|EPF)
  elif ap==2:
   for t in KN[sq]: ad(t)
  else:
   for d in ((0,2,5,7) if ap==3 else ((1,3,4,6) if ap==4 else ALLD)):
    for t in RAYS[sq][d][:1 if ap==6 else 7]:
     if ad(t): break
   if ap==6 and not caps:
    for bit,fr,emp,safe in CST8:
     if fr==sq and (CAST&bit) and all(not b[x] for x in emp) and all(not A(x,-s) for x in safe): apnd(sq|(safe[-1]<<6)|CSTF)
 return ms
def make(m):
 global SIDE,CAST,EP,KW,KB,HASH
 U.append((B[:],CNT[:],PS[:],CAST,EP,KW,KB,HASH))
 fr=m&63; to=(m>>6)&63; pr=(m>>12)&7
 p=B[fr]; s=1 if p>0 else -1; ap=abs(p)
 cap=0; csq=to
 if m&EPF: csq=to-8*s; cap=B[csq]
 elif B[to]: cap=B[to]
 np=s*pr if pr else p
 i=(p+6)*64+fr; j=(np+6)*64+to; dmg=CMG[j]-CMG[i]
 HASH^=Z[p+6][fr]^Z[np+6][to]
 B[to]=np; B[fr]=0
 if cap:
  HASH^=Z[cap+6][csq]; k=(cap+6)*64+csq; dmg-=CMG[k]
  CNT[cap+6]-=1
  if csq!=to: B[csq]=0
 if pr: CNT[p+6]-=1; CNT[np+6]+=1
 if m&CSTF:
  rf,rt=(to+1,to-1) if to&4 else (to-2,to+1); rp=B[rf]
  HASH^=Z[rp+6][rf]^Z[rp+6][rt]
  i=(rp+6)*64+rf; j=(rp+6)*64+rt; dmg+=CMG[j]-CMG[i]
  B[rt]=rp; B[rf]=0
 PS[0]+=dmg
 if ap==6: KW,KB=(to,KB) if s>0 else (KW,to)
 CAST&=CK.get(fr,15)&CK.get(to,15)
 EP=((fr+to)//2) if (m&DBLF) else -1
 SIDE=-s; HASH^=ZS; RP[HASH]=RP.get(HASH,0)+1
def unmake():
 global SIDE,CAST,EP,KW,KB,HASH
 RP[HASH]-=1
 b,c,q,CAST,EP,KW,KB,HASH=U.pop()
 B[:]=b; CNT[:]=c; PS[:]=q; SIDE=-SIDE
def _pw(pl,en,s):
 ex=[-1]*8 if s>0 else [8]*8
 for sq in en:
  r=sq>>3
  if (r-ex[sq&7])*s>0: ex[sq&7]=r
 emg=eeg=0
 for sq in pl:
  r=sq>>3; f=sq&7; rp=r if s>0 else 7-r
  if (ex[f]-r)*s<=0 and (f==0 or (ex[f-1]-r)*s<=0) and (f==7 or (ex[f+1]-r)*s<=0): emg+=PBM[rp]; eeg+=PBM[rp]*2
 return emg*s, eeg*s
def E():
 n=CNT; ph=(n[8]+n[4])+(n[9]+n[3])+2*(n[10]+n[2])+4*(n[11]+n[1])
 if ph>24: ph=24
 wp=[]; bp=[]
 for sq in range(64):
  p=B[sq]
  if p==1: wp.append(sq)
  elif p==-1: bp.append(sq)
 a,b=_pw(wp,bp,1); c,d=_pw(bp,wp,-1)
 emg=a+c; eeg=b+d
 if n[9]>=2: emg+=26; eeg+=42
 if n[3]>=2: emg-=26; eeg-=42
 tot=PS[0]+(emg*ph+eeg*(24-ph))//24
 return (tot if SIDE>0 else -tot)+10
def Q(alpha,beta,ply):
 ND[0]+=1
 if ND[0]>=NB or ply>=80: return E()
 inchk=_chk()
 if inchk: best=-INF
 else:
  best=E()
  if best>=beta: return beta
  if best>alpha: alpha=best
 ms=G(caps=not inchk)
 ms.sort(key=lambda m:((m>>15)&7)*1000-VMG[abs(B[m&63])]+((m>>12)&7)*900,reverse=True)
 legal=0
 for m in ms:
  make(m)
  if _bad(): unmake(); continue
  legal+=1
  sc=-Q(-beta,-alpha,ply+1)
  unmake()
  if sc>best:
   best=sc
   if sc>alpha: alpha=sc
   if alpha>=beta: break
 if inchk and not legal: return -900000+ply
 return best
def search(depth,alpha,beta,ply,nullok):
 global SIDE,EP,HASH
 if depth<=0: return Q(alpha,beta,ply)
 ND[0]+=1
 if ND[0]>=NB: raise _Abort
 if (ND[0]&2047)==0 and time.time()-T0[0]>8.5: raise _Abort
 if ply>=110: return E()
 inchk=_chk()
 if inchk: depth+=1
 if ply>0 and RP.get(HASH,0)>1: return 0
 ent=TT.get(HASH); ttm=ent[3] if ent else 0
 if ent and ply>0 and ent[0]>=depth and (ent[1]==0 or (ent[1]==1 and ent[2]>=beta) or (ent[1]==2 and ent[2]<=alpha)): return ent[2]
 if nullok and not inchk and depth>=3 and beta<899000 and any(CNT[SIDE*i+6] for i in range(2,6)):
  _oe=EP; EP=-1; SIDE=-SIDE; HASH^=ZS; sc=-search(depth-3,-beta,-beta+1,ply+1,False); EP=_oe; SIDE=-SIDE; HASH^=ZS
  if sc>=beta: return beta
 ms=G()
 kk=KIL[ply]; k0,k1=kk[0],kk[1]; hs=HIS
 ms.sort(key=lambda m:(1<<28) if m==ttm else ((1<<26)+(VMG[(m>>15)&7] if (m>>15)&7 else VMG[(m>>12)&7])*1000-VMG[abs(B[m&63])]) if ((m>>15)&7 or (m>>12)&7) else ((1<<24)+300000 if m==k0 else (1<<24)+200000 if m==k1 else (1<<24)+min(hs[m&4095],199999)),reverse=True)
 best=-INF; bm=0; legal=0; a0=alpha
 for m in ms:
  cap=(m>>15)&7; pr=(m>>12)&7
  make(m)
  if _bad(): unmake(); continue
  legal+=1
  r=0
  if depth>=3 and not cap and not pr and not inchk and legal>=5: r=1 if legal<10 else 2
  sc=-search(depth-1,-beta,-alpha,ply+1,True) if legal==1 else -search(depth-1-r,-alpha-1,-alpha,ply+1,True)
  if legal>1 and r and sc>alpha: sc=-search(depth-1,-alpha-1,-alpha,ply+1,True)
  if legal>1 and sc>alpha and sc<beta: sc=-search(depth-1,-beta,-alpha,ply+1,True)
  unmake()
  if sc>best: best=sc; bm=m
  if sc>alpha: alpha=sc
  if alpha>=beta:
   if not cap and not pr:
    if k0!=m: kk[1]=k0; kk[0]=m
    hs[m&4095]+=depth*depth
   break
 if not legal: return -900000+ply if inchk else 0
 fl=2 if best<=a0 else (1 if best>=beta else 0)
 if len(TT)>600000: TT.clear()
 TT[HASH]=(depth,fl,best,bm)
 return best
def _uci(m):
 fr=m&63; to=(m>>6)&63; pr=(m>>12)&7
 return chr(97+(fr&7))+str((fr>>3)+1)+chr(97+(to&7))+str((to>>3)+1)+("nbrq"[pr-2] if pr else "")
def _fallback(legal):
 return max(legal,key=lambda u:VMG[abs(B[(ord(u[2])-97)+8*(ord(u[3])-49)])] if B[(ord(u[2])-97)+8*(ord(u[3])-49)] else (100 if len(u)>4 else 0))
def _legal(m):
 make(m); ok=not _bad(); unmake(); return ok
def CM(fen,legal=None):
 try:
  SF(fen)
  RP.clear(); RP[HASH]=1
  ND[0]=0; T0[0]=time.time()
  moves=[m for m in G() if _legal(m)]
  best=moves[0]
  try:
   d=1
   while ND[0]<NB:
    search(d,-INF,INF,0,True)
    ent=TT.get(HASH)
    if ent and ent[3] in moves: best=ent[3]
    d+=1
  except _Abort: pass
  u=_uci(best)
  if legal is not None and u not in legal: return _fallback(legal)
  return u
 except Exception:
  try:
   if legal: return _fallback(legal)
  except Exception: pass
  return None
def _post(url,path,obj):
 req=UR.Request(url+path,data=json.dumps(obj).encode(),headers={"Content-Type":"application/json"})
 with UR.urlopen(req,timeout=30) as r: return json.loads(r.read().decode())
def main():
 url=os.environ.get("MAKEFUN_ENV_URL")
 if not url: return
 while True:
  resp=_post(url,"/game",{})
  if not isinstance(resp,dict) or resp.get("status")=="done": break
  while resp.get("status")=="your_move":
   mv=CM(resp["fen"],resp.get("legal_moves"))
   if not mv: mv=_fallback(resp["legal_moves"])
   resp=_post(url,"/move",{"game":resp["game"],"move":mv})
if __name__=="__main__": main()
