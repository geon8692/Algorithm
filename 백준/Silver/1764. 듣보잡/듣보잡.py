n, m = map(int, input().split())

n_set = {input() for _ in range(n)}
m_set = {input() for _ in range(m)}

res = sorted(n_set & m_set)

print(len(res))

for item in res:
  print(item)