/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode* add_recur(struct ListNode* l1, struct ListNode* l2, int carry, struct ListNode * last_node){
        int a = 0, b = 0;
        if (l1){
            a = l1->val;
        }if (l2){
            b = l2->val;
        }
        int res = a + b + carry;
        if (res == 0 && ! l1 && ! l2){
            return last_node;
        }
        struct ListNode * new_node = (struct ListNode *)malloc(sizeof(struct ListNode));
        new_node->val = res % 10;
        new_node->next = NULL;
        if (last_node){
            last_node->next = new_node;
        }
        if (l1 && l2){
            struct ListNode* this_node = add_recur(l1->next, l2->next, res/10, new_node);
        } else if(l1){
            struct ListNode* this_node = add_recur(l1->next, NULL , res/10, new_node);
        } else if (l2){
            struct ListNode* this_node = add_recur(NULL, l2->next, res/10, new_node);
        }
        return new_node;      

    }

    return add_recur(l1, l2, 0, NULL);
}