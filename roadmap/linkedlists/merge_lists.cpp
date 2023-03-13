#include<iostream>
using namespace std;

class node {
public:
  int data;
  node* next;
  node(int data){
    this->data = data; 
    next = NULL;
  }

};

node * merge(node* a, node* b)
{
    if(a == NULL){
        return b;
    }
    if(b == NULL){
        return a;
    }

    node* c;
    if(a->data < b->data){
        c = a;
        c->next = merge(a->next, b);
    }
    else{
        c = b;
        c->next = merge(a, b->next);
    }
    return c;
}

node * midPoint(node *head)
{
    node * slow = head;
    node * fast = head->next;

    while(fast != NULL && fast->next != NULL){
        slow = slow->next;
        fast = fast->next->next;
    }
}

node* mergeSort(node * head)
{
    //base case
    if(head == NULL || head->next == NULL){
        return head;
    }
    // break at mid
    node * mid = midPoint(head);
    node * a = head;
    node * b = mid->next;
    mid->next = NULL;
    // recursive sorting
    a = mergeSort(a);
    b = mergeSort(b);
    //
    return merge(a,b);
}

int main()
{
    return 0;
}