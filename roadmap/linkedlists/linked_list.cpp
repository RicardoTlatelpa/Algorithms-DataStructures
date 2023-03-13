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

void insertAtHead(node* &head, int data){
  if(head==NULL){
    head = new node(data);
    return;
  }   
  //otherwise
  node *n = new node(data);
  n->next = head;
  head = n;
}

void insertAtMiddle(node* &h, int pos, int data){
  if(pos == 0){
    insertAtHead(h, data);
  }
  else 
  {
    int p = 0;
    node *head = h;
    while(head!=NULL)
    {
      if(p == (pos-1)){
        break;
      }
      p += 1;
      head = head->next;
    }
    node * n = new node(data);
    if(head->next != NULL){
      n->next = head->next;
      head->next = n;
    }
    else{
      // semantic 
      if(pos > p){
        cout << "Out of bounds, so inserted at end of list." << endl;
      }
      head->next = n;
    }
  }
}

void printLinkedList(node* head){
  while(head!=NULL){
    cout << head->data << " ";
    head = head->next;
  }
  cout << endl;
}

int main()
{
  node* head = NULL;
  insertAtHead(head,4);
  insertAtHead(head,3);
  insertAtHead(head,2);
  insertAtHead(head,1);
  insertAtHead(head,0);
  printLinkedList(head);
  insertAtMiddle(head,3,100);
  printLinkedList(head);
  return 0;
}
