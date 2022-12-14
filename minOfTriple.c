#include <stdio.h>

int minOfTriple(int x, int y, int z) {
	if (x < y) {
		if (x < z) {
			return x;
		}
		return z;
	}
	if (y < z) {
		return y;
	}
	return z;
}

int readInt(char* text) {
	int value;
	do {
		printf(text);
		fflush(stdin);
	} while(scanf("%d", &value) == 0);
	return value;
}


int main() {
	int a, b, c;
	
	a = readInt("write a: ");
	b = readInt("write b: ");
	c = readInt("write c: ");
	
	printf("min of numbers: %d", minOfTriple(a, b, c));
	return 0;
}


