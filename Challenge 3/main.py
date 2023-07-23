#We have a nested object. We would like a function where you pass in the object and a key and
#get back the value.
#The choice of language and implementation is up to you.
#Example Inputs
#object = {“a”:{“b”:{“c”:”d”}}}
#key = a/b/c
#object = {“x”:{“y”:{“z”:”a”}}}
#key = x/y/z
#value = a


def get_value_from_nested_object(nested_object, key):
    keys = key.split('/')
    current_object = nested_object

    try:
        for k in keys:
            current_object = current_object[k]
        return current_object
    except (KeyError, TypeError):
        return None

# Example usage:
object1 = {"a": {"b": {"c": "d"}}}
key1 = "a/b/c"
print(get_value_from_nested_object(object1, key1))  # Output: "d"

object2 = {"x": {"y": {"z": "a"}}}
key2 = "x/y/z"
print(get_value_from_nested_object(object2, key2))  # Output: "a"


