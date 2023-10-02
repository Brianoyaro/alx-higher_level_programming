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
	/*char *e_rr = "malloc failled";*/
	listint_t *slow, *fast;

	slow = malloc(sizeof(listint_t));
	/*if (!slow)
	{
		printf("%s\n", e_rr);
		return (0);
	}*/
	fast = malloc(sizeof(listint_t));
	/*if (!fast)
	{
		printf("%s\n", e_rr);
		return (0);
	}*/
	fast = list;
	slow = list;
	while (slow && fast->next->next && slow->next)
	{
		fast = fast->next->next;
		if (slow == fast)
			return (1);
		slow = slow->next;
	}
	return (0);
}
