#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - checks for a loop
 * @list: pointer to head node
 * Return: 0 no loop
 * else 1 on loop
 */
int check_cycle(listint_t *list)
{
	/*listint_t *slow, *fast;

	slow = malloc(sizeof(listint_t));
	fast = malloc(sizeof(listint_t));
	fast = list;
	slow = list;
	while (slow && fast->next->next && slow->next)
	{
		fast = fast->next->next;
		if (slow == fast)
			return (1);
		slow = slow->next;
	}
	return (0);*/
	listint_t *fast;

	/*fast = malloc(sizeof(listint_t));*/
	fast = list;
	while (list && list->next && fast->next->next)
	{
		fast = fast->next->next;
		if (list == fast->next->next)
			return (1);
		list = list->next;
	}
	return (0);
}
