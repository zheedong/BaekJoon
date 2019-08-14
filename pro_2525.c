#include <stdio.h>
#pragma warning(disable:4996)

int timeUP(int minute, int *time) {
	if (minute < 60) {
		return minute;
	}
	*time += 1;
	return timeUP(minute - 60, time);
}

int dayUP(int time) {
	if (time < 24) {
		return time;
	}
	time -= 24;
	return dayUP(time);
}

int main() {
	int time = 0;
	int minute = 0;
	int how_long = 0;

	scanf("%d %d", &time, &minute);
	scanf("%d", &how_long);

	minute += how_long;
	minute = timeUP(minute, &time);
	time = dayUP(time);
	printf("%d %d\n", time, minute);

	return 0;
}