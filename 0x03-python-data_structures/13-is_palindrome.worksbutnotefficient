#include "lists.h"
/**
 * copy - creates a copy of a linked list
 * @head: headnode of list to copy
 * Return: created list copy
 */
listint_t *copy(listint_t **head)
{
	listint_t *head2, *tmp;

	head2 = NULL;
	if (*head == NULL)
		return (head2);
	else
	{
		tmp = *head;
		while (tmp)
		{
			add_nodeint_end(&head2, tmp->n);
			tmp = tmp->next;
		}
	}
	return (head2);
}
/**
 * reverse - reverses a linked list
 * @head2: head of list to reverse
 * Return: reversed list
 */
listint_t *reverse(listint_t **head2)
{
	listint_t *prev, *curr, *next;

	prev = NULL;
	curr = *head2;
	next = curr->next;
	while (curr->next != NULL)
	{
		curr->next = prev;
		prev = curr;
		curr = next;
		next = next->next;
	}
	curr->next = prev;
	return (curr);
}
/**
 * is_palindrome - checks if a list is a palindrome
 * @head: head of node to check
 * Return: 0 if not a palindrome
 * else 1 if it is infact a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *original, *shadow;

	if (*head == NULL)
		return (1);
	else
	{
		original = *head;
		shadow = copy(&original);/*takes a double pointer; instead of head I could use &original*/
		shadow = reverse(&shadow);
		while ((original != NULL) && (shadow != NULL))
		{
			if (original->n == shadow->n)
			{
				original = original->next;
				shadow = shadow->next;
			}
			else
			{
				free_listint(shadow);
				return (0);/*not a palindrome*/
			}
		}
	}
	free_listint(shadow);
	return (1);
}
