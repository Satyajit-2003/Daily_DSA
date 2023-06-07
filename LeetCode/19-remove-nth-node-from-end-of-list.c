/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
    typedef struct ListNode node;
    int remove_n_node(node* head, int n){
        if (! head->next){
            return n-1;
        }
        int res = remove_n_node(head->next, n);
        printf("%d %d\n", res, head->val);
        if (res == -1){
            head->next = head->next->next;
        }
        return res-1;
    }
    int res = remove_n_node(head, n);
    if (! res){
        head = head->next;
    }
    return head;
}

int main(){
    struct ListNode* head = (struct ListNode*)malloc(sizeof(struct ListNode));
    head->val = 1;
    head->next = (struct ListNode*)malloc(sizeof(struct ListNode));
    head->next->val = 2;
    head->next->next = (struct ListNode*)malloc(sizeof(struct ListNode));
    head->next->next->val = 3;
    head->next->next->next = (struct ListNode*)malloc(sizeof(struct ListNode));
    head->next->next->next->val = 4;
    head->next->next->next->next = (struct ListNode*)malloc(sizeof(struct ListNode));
    head->next->next->next->next->val = 5;
    head->next->next->next->next->next = NULL;
    removeNthFromEnd(head, 2);

    printf("\n\n");
    while (head){
        printf("%d\n", head->val);
        head = head->next;
    }
    

    return 0;
}