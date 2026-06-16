import numpy as np
from tqdm import tqdm

def simulation(N):
    return 4 * sum(np.sum(np.random.uniform(-1, 1, 2)**2) < 1 for _ in tqdm(range(N))) / N


if __name__ == "__main__":
    N = 1_000_000
    print(simulation(N))
