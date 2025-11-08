maxN = 2*10**6
fact = [1] * maxN
fact_inv = [1] * maxN
mod = 998244353

for i in range(1, maxN):
    fact[i] = fact[i-1] * i % mod
    fact_inv[i] = pow(fact[i], mod - 2, mod)

def comb(n, k):#nCk
    assert n >= 0
    assert k >= 0
    assert n - k >= 0
    return fact[n] * fact_inv[n - k] % mod * fact_inv[k] % mod
