import requests, json

raw = []
current = 'https://api.open5e.com/spells/'
while current != None:
    r = requests.get(current).json()
    raw.extend(r['results'])
    current = r['next']
processed = []
for item in raw:
    if item['duration'] == 'Instantaneous':
        dur = 'instant'
    elif item['duration'] == 'Until dispelled':
        dur = 'dispelled'
    else:
        try:
            if 'up to' in item['duration'].lower():
                dur = {
                    'quatity':int(item['duration'].lower().split('up to ')[1].split(' ')[0]),
                    'type':item['duration'].lower().split('up to ')[1].split(' ')[1],
                    'up_to':True
                }
            else:
                dur = {
                    'quatity':int(item['duration'].lower().split(' ')[0]),
                    'type':item['duration'].lower().split(' ')[1],
                    'up_to':False
                }
        except:
            dur = item['duration'].lower()
    try:
        rang = int(item['range'].split(' ')[0])
    except ValueError:
        rang = item['range'].lower()
    processed.append({
        'name':item['name'],
        'slug':item['slug'],
        'desc':item['desc'],
        'higher_level':item['higher_level'],
        'casting_time':{
            'quantity':int(item['casting_time'].split(' ',maxsplit=1)[0]),
            'type':item['casting_time'].split(' ',maxsplit=1)[1]
        },
        'duration':dur,
        'range':rang,
        'components':item['components'].split(', '),
        'material':item['material'],
        'ritual':item['ritual'] == 'yes',
        'level':{
            'label':item['level'],
            'number':int(item['level_int'])
        },
        'categories':{
            'school':item['school'].lower(),
            'classes':[i.lower() for i in item['dnd_class'].split(', ')],
            'archetype':item['archetype'],
            'circles':item['circles']
        },
        'targets':[],
        'effects':[],
        'concentaration':item['concentration'] == 'yes',
        'document__slug':item['document__slug'],
        'document__title':item['document__title'],
        'document__license_url':item['document__license_url']
    })
with open('spells.json','r') as f:
    old = json.load(f)

for i in range(len(old)):
    for k in processed[i].keys():
        if not k in old[i].keys():
            old[i][k] = processed[i][k]

with open('new_spells.json','w') as f:
    f.write(json.dumps(old,indent=4))