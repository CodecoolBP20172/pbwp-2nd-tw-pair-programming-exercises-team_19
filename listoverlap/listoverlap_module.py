def listoverlap(list1, list2):
    our_list = []
    for list_element in list1:
        if list_element in list2:
            if list_element not in our_list:
                our_list.append(list_element)
    return our_list


def main():
    return


if __name__ == '__main__':
    main()
