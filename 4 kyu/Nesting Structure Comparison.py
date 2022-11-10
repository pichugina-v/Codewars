def same_structure_as(original, other):
    if isinstance(original, list) and isinstance(other, list):
        if len(original) == len(other):
            for org, oth in zip(original, other):
                if isinstance(org, list) and isinstance(oth, list):
                    if not same_structure_as(org, oth):
                        return False
                if isinstance(org, list) != isinstance(oth, list): 
                    return False
            return True
    return False
