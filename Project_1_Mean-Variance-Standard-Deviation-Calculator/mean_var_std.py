import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    d = np.array(list).reshape(3, 3)

    return {
        'mean': [np.mean(d, axis=0).tolist(),
                 np.mean(d, axis=1).tolist(),
                 np.mean(d).item()],
        'variance': [np.var(d, axis=0).tolist(),
                     np.var(d, axis=1).tolist(),
                     np.var(d).item()],
        'standard deviation': [np.std(d, axis=0).tolist(),
                                np.std(d, axis=1).tolist(),
                                np.std(d).item()],
        'max': [np.max(d, axis=0).tolist(),
                np.max(d, axis=1).tolist(),
                np.max(d).item()],
        'min': [np.min(d, axis=0).tolist(),
                np.min(d, axis=1).tolist(),
                np.min(d).item()],
        'sum': [np.sum(d, axis=0).tolist(),
                np.sum(d, axis=1).tolist(),
                np.sum(d).item()]
    }
