---
title: "Storing data with dicts"
menu: main
weight: 5
---

Dictionaries (also called dicts) are another key datastructure we'll need to use to write a pipeline.
In particular, dicts allow efficient key-value storage of any type of data. 

To create a dict, we use syntax like the following.

```
example = {}
type(example)
```
```
dict
```

We can then store values in our dict using indexing.
The index is referred to as the "key",
and the stored data is referred to as the "value".

```
example['key'] = 'value'
example['key']
```
```
'value'
```

In addition, keys can be stored using any type of value.
Let's add several more values to demonstrate this.

```
example[1] = 2
example[4] = False
example['test'] = 5
example[7] = 9
```

To retrieve all keys in the dictionary, we can use the `.keys()`method.
Note how we used the `list()` function to turn our resulting output into a list.

```
list(example.keys())
```
```
['key', 1, 4, 'test', 7]
```

Likewise, we can retrieve all the values at once, using `.values()`

```
list(example.values())
```
```
['value', 2, False, 5, 9]
```

{{<admonition title="Dictionary order">}}
Note that the order of keys and values in a dictionary should not be relied upon.
We'll create dictionary another way to demonstrate this:

```
unordered = {'a': 1, 
             'b': 2,
             'c': 3,
             'd': 4}
```
```
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

Depending on your version of Python, the dictionary will either be in order, or out of order. 
If you are on Python 3.6+ dictionaries are ordered.
This is a new feature [and should not be relied upon](https://mail.python.org/pipermail/python-dev/2016-September/146348.html). 

Iterate through and print the dictionary's keys in both forward and reverse order.

(To iterate through the dict in a specific order, you will need to sort the keys using the `sorted()` function)
{{</admonition>}}

## [Next section](../functions/)

