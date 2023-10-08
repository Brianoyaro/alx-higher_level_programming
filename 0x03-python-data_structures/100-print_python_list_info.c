#include <Python.h>
#include <stdio.h>
void print_python_list_info(PyObject *p)
{
	Py_ssize_t list_size = PyList_Size(p);
	Py_sszie_t allocated = ((PyListObject *) p)->allocated;
	printf("[*] Size of Python List = %zd\n", list_size);
	printf("[*] Allocated = %zd\n", allocated);

}
