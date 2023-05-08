#include <stdio.h>
#include <stdlib.h>
#include "queue.h"

int main(){
    // Stack *stack = newstack(5);

    // push(stack, 1);
    // push(stack, 2);
    // push(stack, 3);

    // printf("Pop: %d\n", pop(stack));
    // printf("Pop: %d\n", pop(stack));

    // free_stack(stack);

    Queue *que = q_create(); // 수정된 부분
    q_push(que,4);
    int temp = q_pop(que);

    printf("%d", temp);

    free(que);
    return 0;

}