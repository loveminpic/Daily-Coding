#include <stdio.h>
#include <stdlib.h>
#include "binary_search_tree.h"

BinaryTree *create_bts(){
    BinaryTree *bts = (BinaryTree*)malloc(sizeof(BinaryTree));
    bts->root = NULL;
    return bts;
}

void insert_bts(BinaryTree *bts, int data){
    if (bts==NULL){
        return;
    }
    bts->root = insert_node(bts->root, data);
}

TreeNode *insert_node(TreeNode *node, int data) {
    if(node == NULL){
        TreeNode *newnode = (TreeNode *)malloc(sizeof(TreeNode));
        newnode->data = data;
        newnode->left = NULL;
        newnode->right = NULL;
        return newnode;
    }
    if (data < node->data) {
        node->left = insert_node(node->left, data);
    } else if (data > node->data) {
        node->right = insert_node(node->right, data);
    }
    return node;

}


// search: 이진 탐색 트리에서 값을 찾는 함수
// delete: 이진 탐색 트리에서 노드를 삭제하는 함수
// find_min: 이진 탐색 트리에서 최솟값을 가진 노드를 찾는 함수
// find_max: 이진 탐색 트리에서 최댓값을 가진 노드를 찾는 함수
// preorder_traversal: 전위 순회 함수
// inorder_traversal: 중위 순회 함수
// postorder_traversal: 후위 순회 함수
// height: 이진 탐색 트리의 높이를 계산하는 함수
// is_empty: 이진 탐색 트리가 비어있는지 확인하는 함수
// clear: 이진 탐색 트리의 모든 노드를 삭제하고 메모리를 해제하는 함수