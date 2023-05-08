#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* nextNode;
};

struct Node* CreateNode(int data){
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));

    newNode->data = data;
    newNode->nextNode = NULL;

    return newNode;
}

struct Node* InsertNode(struct Node* current, int data) {
    struct Node* after = current->nextNode;
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));

    newNode->data = data;
    newNode->nextNode = after;
    current->nextNode = newNode;

    return newNode;
}
void DeleteNode(struct Node* delete, struct Node* head) {
    struct Node *next = head;
    if (delete == head) {
        free(delete);
        return;
    }

    while (next) {
        if(next->nextNode == delete){
            next ->nextNode = delete->nextNode;
        }
        next = next->nextNode;
    }
    free(delete);
}