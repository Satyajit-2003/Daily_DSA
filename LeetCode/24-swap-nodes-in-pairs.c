#include <stdio.h>
#include <stdlib.h>


struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* swapPairs(struct ListNode* head){
    typedef struct ListNode node;
    node* dummy = (node *)malloc(sizeof(node));
    dummy->next = head;

    node* prev = dummy;
    node* curr = head;

    node *next, *temp;
    while (curr && curr->next){
        next = curr->next->next;
        temp = curr->next;

        curr->next = next;
        temp->next = curr;
        prev->next = temp;

        prev = curr;
        curr = curr->next;
    }
    return dummy->next;
}

int main(){
    struct ListNode *head = (struct ListNode *)malloc(sizeof(struct ListNode));
    head->val = 1;
    head->next = (struct ListNode *)malloc(sizeof(struct ListNode));
    head->next->val = 2;
    head->next->next = (struct ListNode *)malloc(sizeof(struct ListNode));
    head->next->next->val = 3;
    head->next->next->next = (struct ListNode *)malloc(sizeof(struct ListNode));
    head->next->next->next->val = 4;
    head->next->next->next->next = NULL;

    struct ListNode *result = swapPairs(head);

    while (result){
        printf("%d ", result->val);
        result = result->next;
    }
}