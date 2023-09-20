class NaturalMergeSorter:
    def __init__(self):
        return
    
    def get_sorted_run_length(self, integer_list, start_index):
        if start_index  >= len(integer_list):
            return 0
        length = 1
        current_index = start_index

        while current_index < len(integer_list) - 1:
            if integer_list[current_index] <= integer_list[current_index + 1]:
                length += 1
            else:
                break
            current_index += 1

        return length


    def natural_merge_sort(self, integer_list):
        length = len(integer_list)
        merge_count = 0

        i = 0
        while True:
            left_length = self.get_sorted_run_length(integer_list, i)
            left_last_idx = i+left_length-1

            # checks if whole list is sorted
            if left_length == length:
                break

            right_start = i + left_length
            right_length = self.get_sorted_run_length(integer_list, right_start)
            right_last_idx = i + left_length + right_length-1

            print(integer_list)
            print(f'left:{i},{left_last_idx}  right={right_last_idx}')
            print()
            if right_length > 0:
                self.merge(integer_list, i , left_last_idx, right_last_idx )
                merge_count += 1

            if right_start+ right_length >= length:
                i = 0
            else:
                i =  right_start + right_length

        print('result:', integer_list)
        print('total merge calls: ', merge_count)

 

    def merge(self, numbers, left_first, left_last, right_last):
        merged_size = right_last - left_first + 1

 

        merged_numbers = [None] * merged_size
        merge_pos = 0
        left_pos = left_first
        right_pos = left_last + 1

 

        # Add smallest element from left or right partition to merged numbers
        while left_pos <= left_last and right_pos <= right_last:
            if numbers[left_pos] <= numbers[right_pos]:
                merged_numbers[merge_pos] = numbers[left_pos]
                left_pos += 1
            else:
                merged_numbers[merge_pos] = numbers[right_pos]
                right_pos += 1

 

            merge_pos += 1

 

        # If left partition isn't empty, add remaining elements to merged_numbers
        while left_pos <= left_last:
            merged_numbers[merge_pos] = numbers[left_pos]
            left_pos += 1
            merge_pos += 1

 

        # If right partition isn't empty, add remaining elements to merged_numbers
        while right_pos <= right_last:
            merged_numbers[merge_pos] = numbers[right_pos]
            right_pos += 1
            merge_pos += 1

 

        # Copy merged numbers back to numbers
        for merge_pos in range(merged_size):
            numbers[left_first + merge_pos] = merged_numbers[merge_pos]