#include<stdio.h>
#include<stdlib.h>

typedef struct treeNode {
	int key;
	struct treeNode *left;
	struct treeNode *right;
	struct treeNode *parent;
}treeNode;

void insertTree(treeNode **root, int k); 
treeNode *getNode( treeNode *node, int k); 
treeNode *searchTree( treeNode *node, int k, int *depth); 

int main() {

	int num;
	treeNode *root = NULL;
	treeNode *p1 = NULL, *p2 = NULL;
	treeNode *LCA = NULL;
	int p1_depth = 1, p2_depth = 1;
	int depth_diff, i;

	printf("Enter numbers into tree. to exit(-1):");
	do {
		scanf("%d", &num);
		if( num == -1 )
			break;

		insertTree( &root, num );  /* for now lets construct a BST with the input numbers */ 
	} while(1);

	printf("Enter first number:");
	scanf("%d", &num);
	p1 = searchTree( root, num, &p1_depth);
	if( p1 == NULL ) {
		printf("Number %d not present in tree. Exiting\n", num);
		exit(1);
	}

	printf("---p1:%d (depth :%d)---\n", p1->key, p1_depth);

	printf("Enter second number:");
	scanf("%d", &num);
	p2 = searchTree( root, num, &p2_depth);
	if( p2 == NULL ) {
		printf("Number %d not present in tree. Exiting\n", num);
		exit(1);
	}

	printf("---p2:%d (depth :%d)---\n", p2->key, p2_depth);

	if( p1_depth != p2_depth ) {
		depth_diff = abs (p1_depth - p2_depth);
		if( p1_depth > p2_depth ) {
			for( i = 0; i < depth_diff; i++) {
				p1 = p1->parent;
			}
		} 
		else {
			for( i = 0; i < depth_diff; i++) {
				p2 = p2->parent;
			}
		}
	} 

	while( p1 != p2 ) {
		p1 = p1->parent;
		p2 = p2->parent;
	}

	if( p1 == NULL || p2 == NULL ) {
		printf("Something Wrong !!. Should not happen. \n");
		exit(1);
	}

	LCA = p1;
	printf("Least Common Ancestor is %d.\n", LCA->key);
	
	return 1;
}

treeNode *searchTree( treeNode *node, int k, int *depth) {

	if(!node)
		return NULL;

	if(node->key == k)
		return node;

	(*depth)++;
	if( k < node->key )
		return searchTree( node->left, k, depth);
	else
		return searchTree( node->right, k, depth);
}

treeNode *getNode( treeNode *node, int k) {
	
	if(!node)
		return NULL;	/* error condition */

	if( node->left == NULL && node->right == NULL )
		return node;

	if( k <= node->key) {
		if( node->left )
			return getNode( node->left, k);
		else
			return node;
	} 
	else if( k > node->key) {
		if( node->right )
			return getNode( node->right, k);
		else
			return node;
	}
}

void insertTree(treeNode **root, int k) {

	treeNode *ptr, *node;

	ptr = (treeNode *) malloc ( sizeof( treeNode ));
	ptr->left = NULL;
	ptr->right = NULL;
	ptr->key = k;

	if( *root == NULL ) {
		*root = ptr;
		(*root)->parent = NULL;
		return;
	}
	
	if ( (node = getNode( *root, k)) == NULL ) {
		printf("ERROR!!");
		exit(1);
	}

	/* OK. we got node */ 
	if( k <= node->key ) 
		node->left = ptr;
	else
		node->right = ptr;

	ptr->parent = node;
	return;
}
