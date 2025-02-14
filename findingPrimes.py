def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    
    return is_prime

def find_prime_pair(N, is_prime):
    for A in range(2, 2 * N):
        if is_prime[A] and is_prime[2 * N - A]:
            return A, 2 * N - A

def main():
    T = int(input())
    N_list = [int(input()) for _ in range(T)]
    
    max_N = max(N_list)
    max_limit = 2 * max_N
    is_prime = sieve_of_eratosthenes(max_limit)
    
    for N in N_list:
        A, B = find_prime_pair(N, is_prime)
        print(A, B)

if __name__ == "__main__":
    main()
