/*
 * Name: Abhishek Goswami
 * Date: 3/11/2011
 * Pb  : Median of Arrays Pb
 * Submission 2
 */

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<limits.h>

#define LINE_LENGTH_MAX 1000
#define ARRAY_SIZE_MAX 100

int main( int argc, char *argv[]) {
	
	FILE *fp;
	char line[LINE_LENGTH_MAX];
	char *c;
	int A[ARRAY_SIZE_MAX], B[ARRAY_SIZE_MAX];
	int a_size = 0, b_size = 0;
	int i, j, k, l, total_size, median_index, count;
	
	double median;
	int x, y;

	fp = fopen(argv[1], "r");
	if(fp == NULL) {
		printf("Cannot open file. Exiting\n"); fflush(stdout);
		return 1;
	}
	
	/* getting array A elements from file*/

	memset(line, 0, sizeof(line));
	fgets(line, LINE_LENGTH_MAX, fp); 
	c = strtok( line, "=");
	
	while ( (c = strtok( NULL, ",")) != NULL ) {
		A[a_size++] = atoi(c);
		if( a_size > ARRAY_SIZE_MAX ) {
			printf("Array Size Exceeded. Exiting\n"); fflush(stdout);
			fclose(fp);
			return 1;
		}
	}

	/* getting array B elements from file */
	
	memset(line, 0, sizeof(line));
	fgets(line, LINE_LENGTH_MAX, fp); 
	c = strtok( line, "=");
	while ( (c = strtok( NULL, ",")) != NULL ) {
		B[b_size++] = atoi(c);
		if( b_size > ARRAY_SIZE_MAX ) {
			printf("Array Size Exceeded. Exiting\n"); fflush(stdout);
			fclose(fp);
			return 1;
		}
	}

	fclose(fp);
	
	printf("\nArray A elements\n");
	for( i = 0; i < a_size; i++)
		printf("A[%d]=%d\n", i, A[i]);

	printf("\nArray B elements\n");
	for( i = 0; i < b_size; i++)
		printf("B[%d]=%d\n", i, B[i]);


	//printf("a_size=%d b_size=%d\n", a_size, b_size);

	total_size = a_size + b_size;
	median_index = (total_size + 1) / 2;


	i = j = 1;  /* i keeps track of A[], j keeps track of B[]
				 * NOTE: may need to kickstart the (log n) search in between
				 * hence use the variables k and l to keep previous state information
				 */ 
	k = l = 0;  /* k keeps state for i (if needed), l keeps state for j (if needed) */

	count = 1;  /* keeps track of overall progress hence count < median_index */

	while ( count < median_index ) {

		if ( count + i >= median_index ) {
			k += (i - 1);
			i = 1;
		}
		if ( count + j >= median_index ) {
			l += (j - 1);
			j = 1;
		}
		if( k + i > a_size ) {
			count += j;
			j *= 2;
			continue;
		} else if ( l + j > b_size ) {
			count += i;
			i *= 2;
			continue;
		}
		if( A[k+i-1] <= B[l+j-1] ) {
			count += i;
			i *= 2;
		} else {
			count += j;
			j *= 2;
		}
	}

	if( (total_size % 2) == 1 ) {
		
		/* |A U B| is odd, get median */
		
		if ( k+i > a_size ) 
			median = B[l+j-1];
		else if  (l+j > b_size )
			median = A[k+i-1];
		else
			median = ( A[k+i-1] <= B[l+j-1] ) ? A[k+i-1] : B[l+j-1];
	} else {

		/* |A U B| is even, get middle elements x and y */
		
		if ( k+i > a_size ) {
			x = B[l+j-1];
			y = B[l+j];
		}
		else if  (l+j > b_size ) {
			x= A[k+i-1];
			y= A[k+i];
		}
		else {
			if ( A[k+i-1] <= B[l+j-1] ) {
				x = A[k+i-1];
				i++;
			} else {
				x = B[l+j-1];
				j++;
			}

			if( k+i > a_size )
				y = B[l+j-1];
			else if ( l+j > b_size )
				y = A[k+i-1];
			else
				y = ( A[k+i-1] <= B[l+j-1] ) ? A[k+i-1] : B[l+j-1];
		}

		/* take average to get median */

		median = ( x + y ) / 2.0;
	}
	
	printf("\n\nMedian of A and B is : %f\n\n\n", median);	
	return 1;
}
