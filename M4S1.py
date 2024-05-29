import requests

def listar_marcas():
    url = "https://parallelum.com.br/fipe/api/v1/carros/marcas"
    headers = {'user-agent': 'MyStudyApp'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

marcas = listar_marcas()
if marcas:
    for marca in marcas:
        print(f"ID: {marca['codigo']}, Nome: {marca['nome']}")
else:
    print("Falha ao obter marcas.")

def listar_modelos(id_marca):
    url = f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{id_marca}/modelos"
    headers = {'user-agent': 'MyStudyApp'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

id_marca = 21 
modelos = listar_modelos(id_marca)
if modelos:
    for modelo in modelos['modelos']:
        print(f"ID: {modelo['codigo']}, Nome: {modelo['nome']}")
else:
    print("Falha ao obter modelos.")

class FipeIterator:
    def __init__(self, id_marca):
        self.id_marca = id_marca
        self.headers = {'user-agent': 'MyStudyApp'}
        self.url = f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{id_marca}/modelos"
        self.modelos = self._fetch_modelos()
        self.index = 0 

    def _fetch_modelos(self):
        response = requests.get(self.url, headers=self.headers)
        if response.status.get(self.url, headers=self.headers):
            return response.json()['modelos']
        else:
            return[]
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.modelos):
            modelo = self.modelos[self.index]
            self.index += 1 
            return modelo
        else:
            raise StopIteration
        
id_marca = 21 
fipe_iterator = FipeIterator(id_marca)

for modelo in fipe_iterator:
    print(f'ID: {modelo['codigo']}, Nome: {modelo['nome']}')