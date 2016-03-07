#!/usr/bin/env python2

import tempfile
import sys
import os
import math


def applyExpFilter(initial, CPx, CPy):
    abs_init = math.fabs(initial)
    if CPx == CPy:
        return initial
    elif CPx == 0.5:
        filtered = 2 * abs_init * (1 - abs_init) * CPy + math.pow(abs_init, 2)
    else:
        tmp = (math.sqrt(math.pow(CPx, 2) + (1 - 2 * CPx) * abs_init) - CPx) / (1 - 2 * CPx)
        filtered = 2 * tmp * (1-tmp) * CPy + math.pow(tmp, 2)
    if initial < 0:
        filtered = -filtered
    return filtered


def applyLinearFilter(initial, points):
    prev_point = [-1, -1]

    for i in range(len(points)):
        if i > 0:
            prev_point = points[i-1]
        if points[i][0] > initial:
            next_point = points[i]
            break
    else:
        try:
            prev_point = points[-1]
        except IndexError:
            prev_point = [-1, -1]
        next_point = [1, 1]

    xRange = next_point[0] - prev_point[0]
    yRange = next_point[1] - prev_point[1]
    base   = prev_point[1]
    xDiff  = initial - prev_point[0]

    filtered = base + (xDiff * yRange)/xRange
    return filtered

def testRange():
    r = -1.0
    while r <= 1.0:
        yield r
        r += 0.005

def runExpFilter(builder, out_file):
    parts = builder.rstrip(';').split(';')
    if len(parts) != 3 or 'ARXF' not in parts[0]:
        print 'Bad exp filter builder : '+builder
        return False
    CPx = float(parts[1])
    CPy = float(parts[2])

    for i in testRange():
        filtered = applyExpFilter(i, CPx, CPy)
        out_file.write(str(i) + ' ' + str(filtered) + '\n')
    return True

def runLinearFilter(builder, out_file):
    parts = builder.rstrip(';').split(';')
    if len(parts) == 0 or 'ARMF' not in parts[0]:
        print 'Bad multipoint filter builder : '+builder
        return False

    points = []
    for i in range(1, len(parts)):
        index = i-1
        new_point_str = parts[i].split('>')
        if len(new_point_str) != 2:
            print 'Bad multipoint filter builder (point '+str(i)+' has bad syntax) : '+builder
            return False
        new_point = [float(new_point_str[0]), float(new_point_str[1])]
        if i > 1:
            old_point = points[index-1]
            if new_point[0] <= old_point[0] or new_point[1] < old_point[1]:
                print 'Bad multipoint filter builder (point '+str(i)+' is out of order) : '+builder
                return False
        points.append(new_point)

    for i in testRange():
        filtered = applyLinearFilter(i, points)
        out_file.write(str(i) + ' ' + str(filtered) + '\n')
    return True

def runFilter(builder, out_file):
    parts = builder.split(';')
    if len(parts) == 0:
        print 'Bad builder: '+builder
        return False
    name = parts[0]
    if 'ARMF' in name:
        return runLinearFilter(builder, out_file)
    elif 'ARXF' in name:
        return runExpFilter(builder, out_file)
    else:
        print 'Bad filter name: ' + name
        return False

def main():

    plots = []

    for i in range(1, len(sys.argv)):
        builder = sys.argv[i]

        out_file_fd, fname = tempfile.mkstemp()
        out_file = os.fdopen(out_file_fd, 'wb')

        the_plot={'fname': fname,
                  'builder': builder,
              }
        if runFilter(builder, out_file):
            plots.append(the_plot)
        out_file.close()

    if not plots:
        print 'Usage : '+sys.argv[0]+' [builder_1 [builder_2 [...builder_N]]]'
        sys.exit(0)


    gnuplot_args = 'plot [-1:1] '
    for i in range(len(plots)):
        plot = plots[i]
        last = (i == (len(plots)-1))
        fname = plot['fname']
        builder = plot['builder']
        gnuplot_args += '"'+fname+'" using 1:2 w lines t "'+builder+'"'
        if not last:
            gnuplot_args += ', '

    os.system('gnuplot -e \''+gnuplot_args+'\' -p')

    for plot in plots:
        os.remove(plot['fname'])


if __name__ == '__main__':
    main()
