n, m = map(int, input().split())

site_pw_hash = dict()

for _ in range(n):
    site_url, password = input().split()
    site_pw_hash[site_url] = password
    
output_list = []
    
for _ in range(m):
    output_list.append(site_pw_hash[input()])
    
for output in output_list:
    print(output)