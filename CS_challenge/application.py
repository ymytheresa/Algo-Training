from itertools import chain, combinations

class solution:
    def array_sum(array, target):
        array_copy = [*array]
        result_set = []
        result = []
        powerset = list(array)
        powerset = chain.from_iterable([combinations(powerset, r) for r in range(len(powerset) + 1)])

        for subset in powerset:
            if sum(subset) == target:
                if len(subset) == 0:
                    continue
                result_set = list(subset)
                break
    
        array_selected = [False] * len(array)
        result_index = []
        while result_set != []:
            # try to find index for this number
            search_val = result_set.pop(0)
            idx = array_copy.index(search_val)
            while array_selected[idx]:
                idx = array_copy.index(search_val, idx + 1)
            array_selected[idx] = True
            result_index.append(idx)


        return result_index