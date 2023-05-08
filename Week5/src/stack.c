#include <stdio.h>
#include <stdlib.h>
#include "stack.h"

Stack *newstack(int capa){
    Stack *arr = (Stack*) malloc(sizeof(Stack));
    arr->max = capa;
    arr->top = -1;
    arr->data = (int *)malloc(sizeof(int) * capa);
    return arr;
}

int is_empty(Stack *arr){
    if (arr->top == -1) {
        return 1;
    }
    return 0;
}

int is_full(Stack *arr){
    if (arr->top == (arr->max)-1){
        return 1;
    }   
    return 0;
}

void push(Stack *arr, int data){
    if (is_full(arr)) {
        printf("stack is FULL!");
        return;
    }
    arr->top++;
    arr->data[arr->top] = data;
}

int pop(Stack *arr) {
    if (is_empty(arr)){
        printf("stack is empty!");
        return 0 ;
    }
    int value = arr->data[arr->top];
    arr->top--;
    return value;
} 

void free_stack(Stack *arr) {
    if (arr) {
        if (arr->data) {
            free(arr->data);
        }
        free(arr);
    }
}