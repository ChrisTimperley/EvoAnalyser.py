import json
import sys
import os.path

# Converts log files from the old file format into the new format.
def convert(fn, target):
    with open(fn, 'r') as f:
        sections = f.read().split('=' * 80)[1:]

    # Enclosure
    enclosure = sections.pop(0).split('\n')[3:-1]
    enclosure = map(lambda s: tuple(map(int, s.split(': '))), enclosure)
    enclosure = dict(enclosure)

    # Initialisation
    init = sections.pop(0).split('\n')[3:-1]
    init = map(lambda s: tuple(s.split('; ')), init)
    init = map(lambda (i, g, f): (int(i), g, float(f)), init)

    # Generations
    gens = []
    while sections:
        gen = '\n'.join(sections.pop(0).split('\n')[3:-1]).split('-' * 80)[1:]

        # -- Selection
        sel = gen.pop(0).split('\n')[3:-1]
        sel = map(lambda s: tuple(map(int, s.split('; '))), sel)

        # -- Crossover
        crs = gen.pop(0).split('\n')[3:-1]
        crs = map(lambda s: tuple(s.split('; ')), crs)
        crs = map(lambda (i, p, g): (int(i), map(int, p.split(', ')), g), crs)

        # -- Mutation
        mut = gen.pop(0).split('\n')[3:-1]
        mut = map(lambda s: tuple(s.split('; ')), mut)
        mut = map(lambda (i, g): (int(i), g), mut)

        # -- Evaluation
        evl = gen.pop(0).split('\n')[3:-1]
        evl = map(lambda s: tuple(s.split('; ')), evl)
        evl = map(lambda (i, f): (int(i), float(f)), evl)

        gens.append((sel, crs, mut, evl))

    # Now let's transform into the new format.
    data = []

    for (i, g, f) in init:
        data.append({'generation': 0,
                     'position': i,
                     'fitness': f,
                     'genome': g,
                     'parents': []})

    for g, (sel, crs, mut, evl) in enumerate(gens):
        for (i, f) in evl:
            data.append({'generation': g + 1,
                         'position': i,
                         'fitness': f,
                         'genome': mut[i][1],
                         'parents': crs[i][2]})

    # Build the meta information.
    # Get the seed from the file name.
    meta = {'version': '0.0.1'}
    env = {'seed': int(os.path.basename(fn)[:-4])}
    problem = {'type': 'repair', 'enclosure': enclosure}

    # Build the file contents.
    meta = "[meta]\n" + json.dumps(meta) + "\n\n"
    env = "[environment]\n" + json.dumps(env) + "\n\n"
    problem = "[problem]\n" + json.dumps(problem) + "\n\n"
    data = "[data]\n" + '\n'.join(map(json.dumps, data))
    contents = meta + env + problem + data

    # Write to the target file.
    with open(target, 'w') as f:
        f.write(contents)

convert(sys.argv[1], sys.argv[2])
