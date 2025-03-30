import numpy as np

def l1_distance(x, y):
    return abs(x - y)

def l2_distance(x, y):
    return (x - y) ** 2

def cosine_similarity(x, y):
    return x.dot(y) / (np.linalg.norm(x) * np.linalg.norm(y))
