import unittest
import util


class TestUtil(unittest.TestCase):

    def setUp(self):
        pass

    def test_negative_bounds(self):
        qt = util.QuadTree(2, [-100, -100], [-10, -10])
        qt.add([-97, -90])
        qt.add([-20, -10])
        qt.add([-20.34, -50.123])
        self.assertTrue(len(qt.root.quads) == 4)


    def test_simple_find(self):
        qt = util.QuadTree(1, [-100, -100], [100, 100])
        pts = [ [-90, -90], 
            [-10, 10],
            [10, -10], 
            [90, 90] ]

        for pt in pts:
            qt.add(pt)

        pt1 = [-105, -100] # should match -90, -90
        pt2 = [-12, -5]    # match -10, 10 (diff't quadrants)
        pt3 = [10, -5]     # match 10, -10

        self.assertTrue(qt.find_nearest(pt1) == pts[0])
        self.assertTrue(qt.find_nearest(pt2) == pts[1])
        self.assertTrue(qt.find_nearest(pt3) == pts[2])

    def test_obj_find(self):


        class SimplePoint(object):
            def __init__(self, x, y):
                self.x = x
                self.y = y

            def __str__(self):
                return "{x}, {y}".format(x=self.x, y=self.y)

        # def as_pt(pt):
        #     return [pt.x, pt.y]

        qt = util.QuadTree(1, [0, 0], [100, 100], lambda obj: [obj.x, obj.y])
        sp1 = SimplePoint(10, 20)
        sp2 = SimplePoint(90, 90)
        sp3 = [5, 5]
        qt.add(sp1)
        qt.add(sp2)
        self.assertTrue(qt.find_nearest(sp3) == sp1)

    def test_large_find(self):
        qt = util.QuadTree(20, [0, 0], [10000, 10000])
        import numpy
        to_x = numpy.random.rand(1000) * 10000
        to_y = numpy.random.rand(1000) * 10000
        to_pts = numpy.column_stack((to_x, to_y))

        from_x = numpy.random.rand(1000) * 10000
        from_y = numpy.random.rand(1000) * 10000
        from_pts = numpy.column_stack((from_x, from_y))
        for pt in to_pts:
            qt.add(pt)
        near_pts_qt = [qt.find_nearest(from_pt) for from_pt in from_pts]
        near_pts_normal = [util.get_nearest_point(from_pt, to_pts) for from_pt in from_pts]
        #make sure these 2 arrays match
        a = numpy.array(near_pts_qt)
        b = numpy.array(near_pts_normal)
        self.assertTrue(numpy.sum((a[:,0] - b[:,0]) + (a[:,1] - b[:,1])) == 0.0)

    def test_overlaps(self):
        r1 = [-20, 100]
        r2 = [0, 10]
        r3 = [-100, -50]
        r4 = [-100, -10]
        self.assertTrue(util.overlaps(r1, r2))
        self.assertTrue(not util.overlaps(r2, r3))
        self.assertTrue(util.overlaps(r1, r4))

    def test_bounds(self):
        bds1 = util.Bounds([0, 0], [100, 100])
        pt1 = [10, 25]
        pt2 = [200, 200]
        self.assertTrue(util.get_dist_to_bounds(pt1, bds1) == pt1[0])
        self.assertTrue(util.get_dist_to_bounds(pt2, bds1) == util.point_dist(pt2, bds1.get_corners()[3]))
        self.assertTrue(util.contains(pt1, bds1))
        self.assertTrue(not util.contains(pt2, bds1))

    def runTest(self):
        pass

if __name__ == '__main__':
    unittest.main()

