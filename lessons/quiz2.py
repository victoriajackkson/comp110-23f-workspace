def shrink(input: list[int]) -> list[int]:
    """Get values of list that are even and less than 7."""
    my_list: list[int] = []
    idx: int = 0
    while idx < len(input):
        if input[idx] % 2 == 0 and input[idx] < 7:
            my_list.append(input[idx])
        idx += 1
    return my_list