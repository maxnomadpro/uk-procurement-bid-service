import json, os, urllib.request, hashlib, datetime
FEED='https://www.contractsfinder.service.gov.uk/Published/Notices/OCDS/Search?limit=10'
req=urllib.request.Request(FEED,headers={'Accept':'application/json','User-Agent':'procurebid/1.0'})
with urllib.request.urlopen(req,timeout=30) as r: data=json.load(r)
open('feed.json','w').write(json.dumps(data,sort_keys=True,indent=2))
# deterministic heuristic; no LLM variability in scoring
records=data.get('releases',data.get('records',[]))
def text(x): return json.dumps(x,sort_keys=True).lower()
def score(x):
 t=text(x); s=50
 if any(k in t for k in ['framework','dynamic purchasing','call-off']): s+=10
 if any(k in t for k in ['software','information technology','consultancy','data']): s+=10
 if any(k in t for k in ['construction','works','vehicle']): s-=10
 return max(0,min(100,s))
out=[]
for r in records:
 s=score(r); out.append({'id':r.get('ocid') or r.get('id'),'title':(r.get('tender') or {}).get('title') or r.get('title'),'bid_score':s,'decision':'BID' if s>=60 else 'NO_BID'})
result={'service_version':'1.0.0','algorithm':'deterministic-v1','source':FEED,'retrieved_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'items':out}
open('sample-output.json','w').write(json.dumps(result,sort_keys=True,indent=2)+'\n')
