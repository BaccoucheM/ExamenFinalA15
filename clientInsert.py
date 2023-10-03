import requests

BASE_URL = 'http://localhost:5000'

def create_project(code_projet, description):
    data = {'Code_projet': code_projet, 'Description': description}
    response = requests.post(f'{BASE_URL}/projects', json=data)
    return response.json()

if __name__ == '__main__':
   
# Demandez à l'utilisateur de saisir les valeurs 
    code_projet = input('Entrez le Code du Projet: ')
    description = input('Entrez la Description du Projet: ')

    # Utilisez les valeurs saisies  pour créer un projet
    created_project = create_project(code_projet, description)
    print(f'Projet créé : {created_project}')