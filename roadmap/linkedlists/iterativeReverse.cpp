#include<iostream>
using namespace std;

template <typename n>
class node
{
  public:
    n data;
    node<n> *next;
    node(n data){
      this->data = data;
      this->next = NULL;
    }
};

template <typename n>
node<n>* reverse(node<n> * &head){

  node<n> *current = head;
  node<n> *prev = NULL;
  node<n> *temp = NULL;
  while(current != NULL){
    temp = current->next;
    current->next = prev;
    prev = current;
    current = temp;
  }
  head = prev;
  return head;
}

template <typename n>
void print(node<n>* &head){
  while(head!=NULL){
    cout << head->data;
    head = head->next;
  }
  cout << endl;
}

int main(){
  node<char> * a = new node<char>('A'); // head of list
  node<char> * r = new node<char>('R');
  node<char> * u = new node<char>('U');
  node<char> * e = new node<char>('E');
  node<char> * m = new node<char>('M');
  node<char> * head = a;
  a->next = r;
  r->next = u;
  u->next = e;
  e->next = m;

  print(head);
  reverse(head);
  cout << head->data << endl;
  print(head);
  return 0;
}
