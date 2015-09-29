def distance_matrix(patches, metric):
    return distance_matrix_symmetrical(patches, metric)

# Assumes the metric is symmetrical.
def distance_matrix_symmetrical(patches, metric):
    width = len(patches)
    matrix = []
    for y in range(width):
        row = [float(metric(patches[x], patches[y])) for x in range(y)] + [0.0]
        matrix.append(row)

    # Fill in the rest of the matrix.
    for y in range(width):
        matrix[y].extend([matrix[x][y] for x in range(y + 1, width)])
    return matrix

# Produces a distance matrix from a given set of patches, using a provided
# distance metric.
def distance_matrix_asymmetrical(patches, metric):
    matrix = []
    for p1 in patches:
        row = [0.0 if p1 == p2 else float(metric(p1, p2)) for p2 in patches]
        matrix.append(row)
    return matrix

def matrix_to_string(matrix):
    return '\n'.join(map(lambda row: ', '.join(map(str, row)), matrix))

def normalised_levenshtein(s1, s2):
    return levenshtein(s1, s2) / float(max(len(s1), len(s2)))

# Adapted from:
# https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Levenshtein_distance#Python
def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)
    if len(s2) == 0:
        return len(s1)
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return previous_row[-1]

#
def distance_from_origin(problem, patch):
    return levenshtein(problem.lines(), patch.to_lines(problem))

def distances_from_origin(problem, patches):
    return map(lambda p: distance_from_origin(problem, p), patches)
