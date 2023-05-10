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
    if(data < node->data){
        node->left = insert_node(node->left, data);
    } else if (data > node->data) {
        node->right = insert_node(node->right, data);
    }else if (data == node->data){
        return node;
    }
    return node;
}

void preorder(TreeNode *node) {
    if(node){
        printf("%d",node->data);
        preorder(node->left);
        preorder(node->right);
    }
}

void inorder(TreeNode *node) {
    if(node){
        inorder(node->left);
        printf("%c",node->data);
        inorder(node->right);
    }
}

void postorder(TreeNode *node) {
    if(node){        
        postorder(node->left);
        postorder(node->right);
         printf("%c",node->data);
    }
}

int find_min(BinaryTree *bts){
    if(bts && bts->root){
        TreeNode *current = bts->root;
        while (current->left != NULL) {
            current = current->left;
        }
        return current->data;
    }
}

int find_max(BinaryTree *bts){
    if(bts && bts->root){
        TreeNode *current = bts->root;
        while (current->right != NULL) {
            current = current->right;
        }
        return current->data;
    }
}

int find_height(TreeNode *node) {
    if (node == NULL) {
        return -1; // 높이를 0이 아닌 -1로 시작하는 이유는 빈 트리의 높이가 -1로 정의되기 때문입니다.
    }
    int left_height = find_height(node->left);
    int right_height = find_height(node->right);
    return (left_height > right_height) ? left_height + 1 : right_height + 1;
}

int find_tree_height(BinaryTree *bts) {
    if (bts == NULL) {
        return -1;
    }
    return find_height(bts->root);
}

int is_empty(BinaryTree *bts) {
    if (bts == NULL || bts->root == NULL){
        return 1;
    }
    return 0;
}

void clear_bts(TreeNode *node){
    if (node == NULL) {
        return;
    }
    clear_bts(node->left);
    clear_bts(node->right);
    free(node);
}

void delete_bts(BinaryTree *bts) {
    if (bts == NULL) {
        return;
    }
    clear_bts(bts->root);
    free(bts);
}

int search_bts(TreeNode *node, int data){
    if (node == NULL) {
        return 0;
    }

    if (data == node->data) {
        return 1;
    } else if (data < node->data) {
        return search_bts(node->left, data);
    } else {
        return search_bts(node->right, data);
    }
}

int search_tree_bts(BinaryTree *bts, int data){
    if (bts == NULL) {
        return 0;
    }
    return search_bts(bts->root, data);
}

void delete_bts(BinaryTree *bts, int data) {
    if (bts == NULL) {
        return;
    }
    bts->root = delete_node(bts->root, data);
}

TreeNode *delete_node(TreeNode *node, int data) {
    if (node == NULL) {
        return NULL;
    }

    if (data < node->data) {
        node->left = delete_node(node->left, data);
    } else if (data > node->data) {
        node->right = delete_node(node->right, data);
    } else {
        // Case 1: No child
        if (node->left == NULL && node->right == NULL) {
            free(node);
            return NULL;
        }
        // Case 2: One child (right)
        else if (node->left == NULL) {
            TreeNode *temp = node->right;
            free(node);
            return temp;
        }
        // Case 2: One child (left)
        else if (node->right == NULL) {
            TreeNode *temp = node->left;
            free(node);
            return temp;
        }
        // Case 3: Two children
        else {
            TreeNode *temp = find_min(node->right);
            node->data = temp->data;
            node->right = delete_node(node->right, temp->data);
        }
    }
    return node;
}

// delete: 이진 탐색 트리에서 노드를 삭제하는 함수
