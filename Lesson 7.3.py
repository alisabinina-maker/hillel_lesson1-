def second_index(text, some_str):
        # Find the first occurrence
        first = text.find(some_str)

        # If substring not found even once
        if first == -1:
            return None

        # Find the second occurrence, starting after the first
        second = text.find(some_str, first + 1)

        # If no second occurrence
        if second == -1:
            return None

        return second
assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')