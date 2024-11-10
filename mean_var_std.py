import numpy as np

def calculate(input_list):
    # Vérifier que la liste contient exactement 9 éléments
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convertir la liste en un tableau Numpy 3x3
    array = np.array(input_list).reshape(3, 3)
    
    # Calculs pour les axes 0 (lignes), 1 (colonnes), et pour la matrice aplatie
    calculations = {
        'mean': [array.mean(axis=0).tolist(), array.mean(axis=1).tolist(), array.mean().tolist()],
        'variance': [array.var(axis=0).tolist(), array.var(axis=1).tolist(), array.var().tolist()],
        'standard deviation': [array.std(axis=0).tolist(), array.std(axis=1).tolist(), array.std().tolist()],
        'max': [array.max(axis=0).tolist(), array.max(axis=1).tolist(), array.max().tolist()],
        'min': [array.min(axis=0).tolist(), array.min(axis=1).tolist(), array.min().tolist()],
        'sum': [array.sum(axis=0).tolist(), array.sum(axis=1).tolist(), array.sum().tolist()]
    }
    
    return calculations
