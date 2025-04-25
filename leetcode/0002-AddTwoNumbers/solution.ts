/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    let dummyHead = new ListNode(0);
    let dummyNode = dummyHead;
    let l1Dummy = l1;
    let l2Dummy = l2;
    let carry = 0;

    while (l1Dummy || l2Dummy){
        let l1Val = (l1Dummy !== null) ? l1Dummy.val : 0;
        let l2Val = (l2Dummy !== null) ? l2Dummy.val : 0;
        let sumDigits = l1Val + l2Val + carry;

        let node = new ListNode(sumDigits % 10);
        dummyNode.next = node;

        carry = Math.floor(sumDigits / 10);

        if(l1Dummy) l1Dummy = l1Dummy.next;
        if(l2Dummy) l2Dummy = l2Dummy.next;
        dummyNode = dummyNode.next;
    }


    if (carry>0){
        let node = new ListNode(1)
        dummyNode.next = node;
    }
    return (dummyHead.next) ? dummyHead.next : dummyHead
};