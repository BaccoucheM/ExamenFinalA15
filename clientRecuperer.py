import requests

BASE_URL = 'http://localhost:5000'

def get_project(project_code):
    response = requests.get(f'{BASE_URL}/projects/{project_code}')
    return response.json()

if __name__ == '__main__':
    
    
    project_code= input('Entrez le Code du Projet: ')
    retrieved_project = get_project(project_code)
    print(f'Projet récupéré : {retrieved_project}')
