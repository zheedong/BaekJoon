#include <stdio.h>
#pragma warning (disable : 4996)

int main() {
	int total_time = 0;
	//String Convert to Number
	/*
	Loop for all string
		if c < 'S'
			(c - 'A') / 3 + 2 -> n
			if n == 'S' - 'A' //Case 'S'
				n = 7
		else
			(c - 'A' - 1) / 3 + 2 -> n
			if n == 10 //Case 'Z'
				n = 9 
	ret char_Arr[] = {'3', '4', ...}
	*/
	char inp_arr[16] = { '\0', };
	scanf("%s", inp_arr);

	for (int i = 0; inp_arr[i]; i++) {
		int n = 0;
		if (inp_arr[i] <= 'S') {
			n = ((inp_arr[i] - 'A') / 3) + 2;
			if (inp_arr[i] == 'S')
				n = 7;
		}
		else {
			n = ((inp_arr[i] - 'A' - 1) / 3) + 2;
			if (inp_arr[i] == 'Z')
				n = 9;
		}
		inp_arr[i] = n;
	}

	//Time for each number n + 1 sec
	/*
	Loop for all arr
		all_time += arr[i] + 1;
	*/
	(int*)inp_arr;
	for (int i = 0; inp_arr[i]; i++) {
		total_time += inp_arr[i] + 1;
	}
	printf("%d", total_time);

	return 0;
}
