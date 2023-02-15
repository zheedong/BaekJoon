n = int(input())

def make_int(a1, a2, a3, a4, a5):
	return 10**4 * a1 + 10**3 * a2 + 10**2 * a3 + 10 * a4 + a5

def check_no_duple(lst):
	if sorted(lst) == sorted(list(set(lst))):
		return True
	return False

flag = False

for d in range(10):
	for e in range(10):
		for h in range(1, 10):
			for l in range(10):
				for o in range(10):
					for r in range(10):
						for w in range(1, 10):

							if not check_no_duple([d, e, h, l, o, r, w]):
								continue

							if (o + d) % 10 != n % 10:
								continue

							h_word = make_int(h, e, l, l, o)
							w_word = make_int(w, o, r, l, d)

							# The Case
							if n == (h_word + w_word):
								flag = True
								print(f"{' ' * (7 - len(str(h_word)))}{h_word}")
								print(f"+{' ' * (6 - len(str(w_word)))}{w_word}")
								print("-" * 7)
								print(f"{' '  * (7 - len(str(n)))}{n}")
								break

						if flag:
							break
					if flag:
						break
				if flag:
					break
			if flag:
				break
		if flag:
			break
	if flag:
		break
if not flag:
	print("No Answer")
