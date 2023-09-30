#include <math.h>
#include <stdio.h>

int main() {
				int floor = 0;
				char c;
				int count = 0;
				int entered_basement = -1;

				FILE * file = fopen("../input.txt", "r");

				if (file == NULL) {
								printf("File couldn't be opened\n");
								return 1;
				}

				while ((c = fgetc(file)) != EOF)	{
								switch (c) {
												case '(':
																++floor;
																break;
												case ')':
																--floor;
																break;
												default:
																break;
								}
								++count;
								if (entered_basement == -1 && floor < 0) entered_basement = count;
				}
				printf("First time in basement: %d\nFinal floor: %d\n", floor);
				return 0;
}	
