# Jaelee Hutchinson
# 12 Checkpoint

def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")

    # reverse and print list
    fruit_list.reverse()
    print(fruit_list)

    # add orange
    fruit_list.append("orange")
    print(fruit_list)

    # find apple and add cherry before apple
    indexApple = fruit_list.index("apple")
    fruit_list.insert(indexApple, "cherry")
    print(fruit_list)

    # remove banana
    fruit_list.remove("banana")
    print(fruit_list)

    # pop the last element
    fruit_list.pop()
    print(fruit_list)

    # sort fruit list
    fruit_list.sort()
    print(fruit_list)

    # clear fruit list
    fruit_list.clear()
    print(fruit_list)


main()    







