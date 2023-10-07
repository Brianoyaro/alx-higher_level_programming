#include "lists.h"
#include <stdio.h>
/**
 * node_number - finds number of nodes in a linked list
 * @head: head pointer of the linked list
 * Return: number of nodes in the linked list
 */
int node_number(listint_t *head)
{
	int n = 0;
	listint_t *current;

	current = head;
	while (current)
	{
		n++;
		current = current->next;
	}
	return (n);
}
/**
 * firstnodeend - finds specified node at h1
 * @head: head node of linked list
 * @h1: node number to find
 * Return: node at h1
 */
listint_t *firstnodeend(listint_t *head, int h1)
{
	int n = 1;
	listint_t *current;

	current = head;
	while (n < h1)
	{
		current = current->next;
		n++;
	}
	return (current);
}
/**
 * reverse - reverses a linked list
 * @head: head nonde of linked list
 * @h1: itteration stop while reversing
 * Return: pointer to first node of reversed list
 */
listint_t *reverse(listint_t **head, int h1)
{
	listint_t *prev, *curr, *latter;

	prev = NULL;
	curr = *head;
	latter = curr->next;
	while (h1 > 0)
	{
		curr->next = prev;
		prev = curr;
		/*printf("prev-n is %i\n", prev->n);*/
		curr = latter;
		latter = latter->next;
		h1--;
	}
	/*printf("After reverse\n");
	print_listint(prev);*/
	return (curr);
}
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: head of list
 * Return: 1 if list is a palindrome
 * else 0 if list is not a palindrome
 */
int is_palindrome(listint_t **head)
{
	int h1 = 0, h2 = 0, nodes = 0;
	/*listint_t *first, *second, *startpoint;*/
	listint_t *second, *startpoint;

	if (*head == NULL)
		return (1);/*empty is a palindrome*/
	nodes = node_number(*head);
	if (nodes % 2 == 0)
	{
		h1 = nodes / 2;
		h2 = h1 + 1;
	}
	else
	{
		h1 = nodes / 2;
		h2 = h1 + 2;
	}
	/*first = firstnodeend(*head, h1);*/
	second = firstnodeend(*head, h2);
	startpoint = reverse(head, h1);

	/*REVERSE EITHER HALVF FIRST!!*/
	while ((startpoint != NULL) && (second != NULL))
	{
		if (startpoint->n == second->n)
		{
			startpoint = startpoint->next;
			second = second->next;
		}
		else
		{
			break;
		}
	}
	if (second != NULL)
		return (0);
	return (1);
}
