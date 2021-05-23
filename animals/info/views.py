from django.shortcuts import render
import json
# from django.http import HttpResponse

def family(request, fam):
    if fam in [f['name'] for f in families]:
        index = ''
        for f in families:
            if f['name'] == fam:
                index = f['id']
                break
        ani_lst = []
        for a in animals:
            if a['family'] == index:
                print(a['family'])
                ani_lst.append(a['name'])
        return render(request, 'family.html', {'family':fam, 'ani_lst':ani_lst})
    else:
        return render(request, 'family.html', {'family':"unknown"})

def animal(request, ani):
    for a in animals:
            info = []
            if a['name'] == ani:
                info.append('id: ' + str(a['id'])) 
                info.append('name: ' + a['name'])
                info.append('legs: ' + str(a['legs']))
                info.append('weight: ' + str(a['weight']))
                info.append('height: ' + str(a['height']))
                info.append('speed: ' + str(a['speed']))
                for f in families:
                    if f['id'] == a['family']:
                        info.append('family: ' + f['name'])
                break
    if info == []:
        ani = "Unknown"
    return render(request, 'animal.html', {'animal':ani, 'info':info})

def fetch_data(filename):
    with open(filename) as f:
        data = json.load(f)
    return data

data = fetch_data('/Users/lidu/Development/GitHub/Venv/animal_info/animals/info/animal.json')
families = data['families']
animals = data['animals']
# print(families)
# print(animals)
# print(family('Caninae'))