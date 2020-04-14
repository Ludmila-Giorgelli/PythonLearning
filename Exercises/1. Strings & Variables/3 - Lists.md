In very simple words, a `List` is a collection of elements. We use `Lists` to store collections of elements that have some sort of relationship between them, most of the times so we can [iterate](https://www.techopedia.com/definition/3821/iteration) through them. 

There's many other ways to create collections of elements, such as `Dictionaries` and `Tuples`, but lists are usually the simplest form of collections and the one everyone learns first. Later on we'll learn the differences between each collection type.

This is how you create an list:

```python
animals = ["Dog","Cow","Beaver"]
```  

`Lists` are zero-indexed, meaning the first item of the list is actually the item number `0`. The second item is `1` and so on. This is how the above list's indexes would look like.

| Index  | Value |
| ------ | ----- |
| 0  | "Dog"  |
| 1  | "Cow"  |
| 2  | "Beaver"  |

### Exercises

Tip: [This link](https://www.w3schools.com/python/python_lists.asp) has the answers to pretty much all the above exercises

##### 1: Write a script that prints the second item of the `Animals` list.
```python
animals = ["Dog","Cow","Beaver"]
# line that prints the second item on the animals list
```
##### 2: Write a script that adds an item called `Cat` to the `Animals` list and then prints it.
```python
animals = ["Dog","Cow","Beaver"]
# line that adds the new item to the list
# line that prints the new item
```
##### 3: Write a script that always prints the [second to last](https://www.yourdictionary.com/second-to-last) item, no matter how many items are in the list.
```python
animals = ["Dog","Cow","Beaver"]
# line that prints the second to last item
animes = ["JoJo", "Hunter x Hunter", "Yuri on Ice", "Given", "One Piece"]
# similar line as above but pointing to the "animes" list
```
##### 4: Write a script that prints the amount of items on the list
```python
animes = ["JoJo", "Hunter x Hunter", "Yuri on Ice", "Given", "One Piece"]
# line that prints the amount of items in the list
```
