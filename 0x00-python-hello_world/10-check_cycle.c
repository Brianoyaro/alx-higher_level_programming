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
	listint_t *fast;

	fast = list;
	/*while (list && list->next && fast->next->next)*/
	while (fast && fast->next)
	{
		fast = fast->next->next;
		if (list == fast->next->next)
			return (1);
		list = list->next;
	}
	return (0);
}
