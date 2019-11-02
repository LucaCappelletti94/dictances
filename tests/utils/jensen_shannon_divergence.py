import scipy

def jensen_shannon_divergence(p, q):
    p /= p.sum()
    q /= q.sum()
    m = (p + q) / 2
    return (scipy.stats.entropy(p, m) + scipy.stats.entropy(q, m)) / 2