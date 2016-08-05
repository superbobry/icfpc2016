#!/usr/bin/env python
# Usage python to_js.py < problem.txt
# Result will be printed to stdout

import re
import sys


def parse_vertex(s):
    if "/" in s:
        return float(s.split("/")[0]) / int(s.split("/")[1])
    else:
        return float(s)


def to_js(lines):
    polygons_number = int(lines[0])
    polygons = []
    print("Polygons nubmer", polygons_number, file=sys.stderr)
    cursor = 1
    for p in range(polygons_number):
        polygon = []
        vertices = int(lines[cursor])
        print("Polygon {0} Vertices {1}".format(p, vertices), file=sys.stderr)
        cursor += 1
        for v in range(vertices):
            line = lines[cursor]
            cursor += 1
            coords = re.split("[ ,]", line)
            print("Vertex {0} Coords: {1}".format(v, coords), file=sys.stderr)
            x = parse_vertex(coords[0])
            y = parse_vertex(coords[1])
            polygon.append([x, y])
        polygons.append(polygon)

    skeletons_number = int(lines[cursor])
    skeletons = []
    print("Skeletons", skeletons_number, file=sys.stderr)
    cursor += 1

    for s in range(skeletons_number):
        line = lines[cursor]
        cursor += 1
        coords = re.split("[ ,]", line)
        print("Vertex {0} Coords: {1}".format(s, coords), file=sys.stderr)
        x1 = parse_vertex(coords[0])
        y1 = parse_vertex(coords[1])
        x2 = parse_vertex(coords[2])
        y2 = parse_vertex(coords[3])
        skeletons.append([[x1, y1], [x2, y2]])
    max_x = max(map(lambda polygon: max(map(lambda vertex: vertex[0], polygon)), polygons))
    min_x = min(map(lambda polygon: min(map(lambda vertex: vertex[0], polygon)), polygons))
    max_y = max(map(lambda polygon: max(map(lambda vertex: vertex[1], polygon)), polygons))
    min_y = min(map(lambda polygon: min(map(lambda vertex: vertex[1], polygon)), polygons))
    print("X in [{0}, {1}], Y in [{2}, {3}]".format(min_x, min_y, max_x, max_y), file=sys.stderr)
    rescaled_polygons = [[
                             [v[0] - min_x, v[1] - min_y]
                             for v in p] for p in polygons]
    rescaled_skeletons = [[
                              [e[0][0] - min_x, e[0][1] - min_y],
                              [e[1][0] - min_x, e[1][1] - min_y]]
                          for e in skeletons]

    return str([rescaled_polygons, [], rescaled_skeletons])


lines = sys.stdin.readlines()
print("Lines\n", "".join(lines), file=sys.stderr)
print(to_js(lines))
