t, m, s = map(int, input().split())
d = int(input())
carry, ns = (s + d) // 60, (s + d) % 60
carry, nm = (m + carry) // 60, (m + carry) % 60
nt = (t + carry) % 24
print(f"{nt} {nm} {ns}")