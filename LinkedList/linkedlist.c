#include <stdlib.h>
#include "linkedlist.h" 

static link head = NULL;

link make_node(unsigned char item)
{
    link p = malloc(sizeof *p);
    p->item = item;
    p->next = NULL;
    return p;
}

void free_node(link p)
{
    free(p);
}

link search(unsigned char key)
{
    link p;
    for(p = head; p; p= p->next)
        if (p->item == key)
            return p;
    return NULL;
}

void insert(link p)
{
    p->next = head;
    head = p;
}

link delete(link p)
{
    link * pnext;
    for (pnext = &head; *pnext; pnext = &(*pnext) -> next)
        if (*pnext == p){
             *pnext = p->next;
             return p;
        } 
    return NULL;
}

void traverse(void (*visit)(link))
{
    link p;
    for (p = head; p; p = p->next)
        visit(p);
}

void destroy(void)
{
    link q, p = head;
    head = NULL;
    while (p) {
        q = p;
        p = p->next;
        free(q);
    }
}

void push(link p)
{
    insert(p);
}

link pop(void)
{
    if (head == NULL)
        return NULL;
    else
        return delete(head);
}
