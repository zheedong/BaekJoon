n, m = map(int, input().split())

pokemon_dict = {}

for i in range(0, n):
    pokemon_name = input()
    pokemon_dict[pokemon_name] = i + 1
    pokemon_dict[str(i+1)] = pokemon_name
    
for j in range(0, m):
    test_problem = input()
    print(pokemon_dict[test_problem])