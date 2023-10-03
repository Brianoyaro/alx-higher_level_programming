#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - inserts a node into a linked list
 * @head: head of linnked list to manioulate
 * @number: value of new node
 * Return: Null on error
 * else position of inserted new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *tmp;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	tmp = *head;
	if (tmp->n > new->n)
	{
		new->next = tmp;
		*head = tmp;
		return (new);
	}
	else
	{
		while (tmp->next)
		{
			if (tmp->next->n > new->n)
			{
				new->next = tmp->next;
				tmp->next = new;
				return (new);
			}
			tmp = tmp->next;
		}
		new->next = NULL;
		tmp->next = new;
	}
	return (new);
}
