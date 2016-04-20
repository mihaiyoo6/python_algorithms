# input = [14, 33, 27, 10, 35, 19, 42, 44]
input = [14, 33, 27, 10, 35, 19, 42, 44, 22]
# input = []
# input = [12]
print('your input : ', input)


def merge_sort(input_list):
    list_length = int(len(input_list))

    if list_length == 0:
        print('your list is empty')
        return True
    if list_length == 1:
        return input_list

    middle_point = int(list_length / 2)
    # print('middle_point ', middle_point)
    right_list = merge_sort(input_list[:middle_point])
    left_list = merge_sort(input_list[middle_point:])

    return merge(right_list, left_list)


def merge(right_list, left_list):
    result = []

    # print("sorting...", right_list, left_list)

    while right_list and left_list:
        # print("right ", right_list)
        # print("left ", left_list)
        if right_list[0] > left_list[0]:
            result.append(left_list[0])
            left_list.pop(0)
        else:
            result.append(right_list[0])
            right_list.pop(0)

    while right_list:
        result.append(right_list[0])
        right_list.pop(0)

    while left_list:
        result.append(left_list[0])
        left_list.pop(0)

    return result

        # r_len = len(right_list)
        # r_index = 0
        # l_len = len(left_list)
        # l_index = 0
        # o_index = 0
        #
        # while r_index < r_len and l_index < l_len:
        #     if right_list[r_index] > left_list[l_index]:
        #         list[o_index] = left_list[l_index]
        #         l_index += 1
        #     else:
        #         list[o_index] = right_list[r_index]
        #         r_index += 1
        #
        #     o_index += 1
        # return list(list)



        # if list_length == 1:
        #     if right_list[0] > left_list[0]:
        #         print('r>l')
        #         if not right_list[0] in output:
        #             output.append(right_list[0])
        #         if not left_list[0] in output:
        #             output.append(left_list[0])
        #     else:
        #         print('r<l')
        #         if not left_list[0] in output:
        #             output.append(left_list[0])
        #         if not right_list[0] in output:
        #             output.append(right_list[0])


output = merge_sort(input)
print("your output: ", output)
