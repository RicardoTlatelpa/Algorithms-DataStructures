#include <iostream>
using namespace std;

class node{
  public:
    int val;
    node *next;
    node(int data){
      this->val = data;
      this->next = NULL;
    }
};

node* kReverse(node *head, int k)
{
  //base case
  if(head == NULL){
    return NULL;
  }

  //reverse the first k nodes
  node* prev = NULL;
  node* current = head;
  node* temp;

  int cnt = 1;

  while(current != NULL and cnt <= k){
    temp = current->next;
    current->next = prev;

    prev = current;
    current = temp;
    cnt++;
  }
  if(temp != NULL)
  {
    head->next = kReverse(temp,k);
  }
  return prev; 
}


int main(){
  node* head = NULL;
  node* n0 = new node(0);
  node* n1 = new node(1);
  node* n2 = new node(2);
  node* n3 = new node(3);
  node* n4 = new node(4);
  head = n0;
  n0->next = n1;
  n1->next = n2;
  n2->next = n3;
  n3->next = n4;
  node* tmp = head;
  while(tmp != NULL){
    cout << tmp->val << " ";
    tmp = tmp->next;
  }
  cout << endl;

  
  head = kReverse(head,3);
  tmp = head;
  while(tmp != NULL){
    cout << tmp->val << " ";
    tmp = tmp->next;
  }
  cout << endl;
  return 0;
}
