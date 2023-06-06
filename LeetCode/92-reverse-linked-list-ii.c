/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseBetween(struct ListNode* head, int left, int right){
    if (left == right){
        return head;
    }
    struct ListNode* dummy = (struct ListNode * )malloc(sizeof(struct ListNode));
    dummy->next = head;

    struct ListNode* prev = NULL;
    struct ListNode* next = NULL;
    struct ListNode* curr = head;
    struct ListNode* Lprev = dummy;

    for (int i = 1; i < left; i++){
        Lprev = curr;
        curr = curr->next;
    }
    
    for (int i = 0; i < right-left+1; i++){
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    Lprev->next->next = curr;
    Lprev->next = prev;

    return dummy->next;
}