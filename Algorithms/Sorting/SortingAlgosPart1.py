def bubble_sort_asc(ip: list):
    ip_len = len(ip)
    for i in range(0, ip_len):
        for j in range(0, ip_len-i-1):
            if ip[j] > ip[j+1]:
                ip[j], ip[j+1] = ip[j+1], ip[j]

    return ip


def bubble_sort_desc(ip: list):
    ip_len = len(ip)
    for i in range(0, ip_len):
        for j in range(0, ip_len-i-1):
            if ip[j] < ip[j+1]:
                ip[j+1], ip[j] = ip[j], ip[j+1]

    return ip


def selection_sort_asc(ip: list):
    ip_len = len(ip)
    for i in range(ip_len):
        min_idx = i
        for j in range(i+1, ip_len):
            if ip[min_idx] > ip[j]:
                min_idx = j
        ip[i], ip[min_idx] = ip[min_idx], ip[i]
    return ip


def selection_sort_desc(ip: list):
    ip_len = len(ip)
    for i in range(ip_len):
        max_idx = i
        for j in range(i+1, ip_len):
            if ip[j] > ip[max_idx]:
                max_idx = j
        ip[i], ip[max_idx] = ip[max_idx], ip[i]
    return ip


if __name__ == "__main__":
    ip_list = [13, 0, 5, 3, 6, 7, 8, 25, 31, 11, 2, 9, 16, 23, ]
    print(ip_list)

    print(bubble_sort_asc(ip_list))
    print(bubble_sort_desc(ip_list))
    print(selection_sort_asc(ip_list))
    print(selection_sort_desc(ip_list))

    print(bubble_sort_asc(ip_list) == selection_sort_asc(ip_list))
    print(bubble_sort_desc(ip_list) == selection_sort_desc(ip_list))

