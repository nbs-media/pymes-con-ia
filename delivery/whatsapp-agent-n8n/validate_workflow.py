#!/usr/bin/env python3
from pathlib import Path
import json, sys
p=Path(__file__).with_name('pymes-whatsapp-lead-response-agent.workflow.json')
w=json.loads(p.read_text(encoding='utf-8'))
errors=[]
if not isinstance(w.get('nodes'),list) or not w['nodes']: errors.append('nodes missing')
if not isinstance(w.get('connections'),dict): errors.append('connections missing')
ids=set(); names=set()
for n in w.get('nodes',[]):
    for key in ['id','name','type','typeVersion','position','parameters']:
        if key not in n: errors.append(f"node {n.get('name')} missing {key}")
    if n.get('id') in ids: errors.append(f"duplicate node id {n.get('id')}")
    ids.add(n.get('id'))
    if n.get('name') in names: errors.append(f"duplicate node name {n.get('name')}")
    names.add(n.get('name'))
for src, groups in w.get('connections',{}).items():
    if src not in names: errors.append(f"connection source missing node: {src}")
    for branch_group in groups.get('main',[]):
        for edge in branch_group:
            if edge.get('node') not in names: errors.append(f"connection target missing node: {edge.get('node')}")
required_env=['META_PHONE_NUMBER_ID','META_ACCESS_TOKEN','OPENAI_API_KEY','SHEET_ID','BUSINESS_NAME','OWNER_WHATSAPP']
text=p.read_text(encoding='utf-8')
for env in required_env:
    if env not in text: errors.append(f"required env placeholder missing: {env}")
required_nodes=['WhatsApp Inbound Webhook','Structured FAQ / Knowledge Base','Draft Response with LLM','Append Lead to Google Sheets','Send WhatsApp Reply via Meta','Notify Owner on WhatsApp','Workflow Error Trigger']
for rn in required_nodes:
    if rn not in names: errors.append(f"required node missing: {rn}")
if errors:
    print('INVALID')
    for e in errors: print('-',e)
    sys.exit(1)
print('VALID')
print(f"nodes={len(w['nodes'])}")
print(f"connections={len(w['connections'])}")
print('required_env='+','.join(required_env))
