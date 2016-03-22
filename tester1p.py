    # STUDENTS: TO USE:
# 
# The following command will test all test cases on your file:
# 
#   python3 <thisfile.py> <your_one_file.py>
# 
# *NOTE* on windows, you may need to use the python command instead of python3.
# 
# You can also limit the tester to only the functions you want tested.
# Just add as many functions as you want tested on to the command line at the end.
# Example: to only run tests associated with func1, func2, and func3, run this command:
# 
#   python3 <thisfile.py> <your_one_file.py> func1 func2 func3
# 


# INSTRUCTOR: TO PREPARE:
#  - add test cases to class AllTests. The test case functions' names must
#    follow a convention: to test a function named foobar, the test must be
#    named "test_foobar_#", where # may be any digits at the end, such as
#    "test_foobar_13".
# - any extra-credit tests must be named "test_extra_credit_foobar_#"
# 
# - name all required definitions in REQUIRED_DEFNS. Do not include any
#   unofficial helper functions. If you want to make helper definitions
#   to use while testing, those can also be added there for clarity.
# 
# # TO IMPLEMENT (not yet a feature):
# to run on either a single file or all .py files in a folder (recursively):
#   python3 <thisfile.py> <your_one_file.py>
#   python3 <thisfile.py> <dir_of_files>
# 
# A work in progress by Mark Snyder, Oct. 2015.

import unittest
import shutil
import sys
import os
import time
import importlib

############################################################################
############################################################################
# BEGIN SPECIALIZATION SECTION (the only part you need to modify beyond 
# adding new test cases).

# name all expected definitions; if present, their definition (with correct
# number of arguments) will be used; if not, a decoy complainer function
# will be used, and all tests on that function should fail.
    
REQUIRED_DEFNS = ["width","height","energy_at","energy", "find_vertical_path","find_horizontal_path","remove_vertical_path","remove_horizontal_path","ppm_to_grid","grid_to_ppm"]

# things inside of classes that we also want to use as test names (the classes' methods)
SUB_DEFNS = []

RENAMED_FILE = "student"

# END SPECIALIZATION SECTION
############################################################################
############################################################################


#BEGIN EXTRAS SECTION
TEMP_FILE = ".deletable_temp_file.txt"
def make_file(msg,filename=".deletable_temp_file.txt"):
    f = open(filename,'w')
    f.write(msg)
    f.close()

def from_file(filename):
    f = open (filename)
    s = f.read()
    f.close()
    return s


# in case we have code that modifies a grid incorrectly or when it's not supposed
# to, each of these functions will create and offer a brand new deep copy of the grid.
def g1():
    return [
         [(100, 75,200),(100,100,200),(100,100,200),(100,100,200),(200,125,200)],
         [(150, 30,180),(150, 50,180),(100,120,180),(100,120,180),(100,120,180)],
         [(100, 75,100),(100, 80,100),(100, 85,100),(100, 95,100),(100,110,100)],
         [(200,100, 10),(200,100, 10),(200,100, 10),(210,200, 10),(255,  0, 10)]
         ]


def g2():
    return [[( 78, 209,  79), ( 63, 118, 247), ( 92, 175,  95), (243,  73, 183), (210, 109, 104), (252, 101, 119)],
          [(224, 191, 182), (108,  89,  82), ( 80, 196, 230), (112, 156, 180), (176, 178, 120), (142, 151, 142)],
          [(117, 189, 149), (171 ,231, 153), (149, 164, 168), (107, 119,  71), (120, 105, 138), (163, 174, 196)],
          [(163, 222, 132), (187 ,117, 183), ( 92, 145,  69), (158, 143,  79), (220,  75, 222), (189,  73, 214)],
          [(211, 120, 173), (188 ,218, 244), (214, 103,  68), (163, 166, 246), ( 79, 125, 246), (211, 201,  98)]
         ]


def g3():
    return [[(  0, 100, 200), (  0,  80, 200), (  0, 100, 200)],
          [(100,  25, 200), (100,  15, 200), (100,  25, 200)],
          [(200,  95, 255), (200, 110, 255), (200, 100, 255)],
          [(200, 100, 255), (200,  95, 255), (200, 100, 255)],
          [(255,  70, 200), (255, 100, 200), (255, 100, 200)]
         ]


def g4():
    return [[(255, 101, 51), (255, 101, 153), (255, 101, 255)],
          [(255, 153, 51), (255, 153, 153), (255, 153, 255)],
          [(255, 203, 51), (255, 204, 153), (255, 205, 255)],
          [(255, 255, 51), (255, 255, 153), (255, 255, 255)]
     ]

# position (1,2) is interesting I guess.
def g5():
    return [
        [(0,0,0),(0,0,0),(10,20,30),(0,0,0),(0,0,0),(0,0,0)],
        [(0,0,0),(2,3,4),( 1, 1, 1),(5,6,7),(0,0,0),(0,0,0)],
        [(0,0,0),(0,0,0),(60,50,40),(0,0,0),(0,0,0),(0,0,0)],
        [(0,0,0),(0,0,0),( 0, 0, 0),(0,0,0),(0,0,0),(0,0,0)]
        ]

# the (1,1,1) nodes comprise the best vertical path to remove.
def g6():
    return [
        [(0,0,0),(0,0,0),(1,1,1),(0,0,0),(0,0,0),(0,0,0)],
        [(0,0,0),(0,0,0),(0,0,0),(1,1,1),(0,0,0),(0,0,0)],
        [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(1,1,1),(0,0,0)],
        [(0,0,0),(0,0,0),(0,0,0),(1,1,1),(0,0,0),(0,0,0)]
        ]

# the (1,1,1) nodes comprise the best horizontal path to remove.
def g7():
    return [
        [(1,1,1),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)],
        [(0,0,0),(1,1,1),(0,0,0),(1,1,1),(0,0,0),(0,0,0)],
        [(1,1,1),(0,0,0),(1,1,1),(0,0,0),(1,1,1),(0,0,0)],
        [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(1,1,1)]
        ]


# used for building RxC grids filled with copies of val.
def build_grid(r,c,val):
    ans = []
    for ri in range(r):
        row = []
        for ci in range(c):
            row.append(val)
        ans.append(row)
    return ans

# END EXTRAS SECTION

############################################################################
############################################################################



# enter batch mode by giving a directory to work on.
BATCH_MODE = (sys.argv[1] in ["."] or os.path.isdir(sys.argv[1]))



# This class contains multiple "unit tests" that each check
# various inputs to specific functions, checking that we get
# the correct behavior (output value) from completing the call.
class AllTests (unittest.TestCase):
    
    
    #---------------------------------------------------------------------
    
    # width of a few different grids. We generate some large ones for the
    # last couple of tests.
    
    def test_width_1(self): self.assertEqual (5, width(g1()))
    def test_width_2(self): self.assertEqual (6, width(g2()))
    def test_width_3(self): self.assertEqual (3, width(g3()))
    def test_width_4(self): self.assertEqual (3, width(g4()))
    def test_width_5(self): g = build_grid( 31,1000,(1,1,1)); self.assertEqual (1000, width(g))
    def test_width_6(self): g = build_grid(123,  27,(1,1,1)); self.assertEqual (  27, width(g))

    #---------------------------------------------------------------------
    
    # height of a few different grids. We generate some large ones for the
    # last couple of tests.
    
    def test_height_1(self): self.assertEqual (4, height(g1()))
    def test_height_2(self): self.assertEqual (5, height(g2()))
    def test_height_3(self): self.assertEqual (5, height(g3()))
    def test_height_4(self): self.assertEqual (4, height(g4()))
    def test_height_5(self): g = [[(1,1,1)]*1000]*31; self.assertEqual (31, height(g))
    def test_height_6(self): g = [[(1,1,1)]*27]*123; self.assertEqual (123, height(g))

    #---------------------------------------------------------------------
    
    # energy_at: we consider corners, edges, and interior pieces. After
    # looking at a couple of grids, not too much extra is worth testing
    # for our assignment.
    
    def test_energy_at_1 (self): self.assertEqual (46925, energy_at(g1(),0,0)) # corner
    def test_energy_at_2 (self): self.assertEqual (67950, energy_at(g1(),0,4)) # corner
    def test_energy_at_3 (self): self.assertEqual (23025, energy_at(g1(),3,0)) # corner
    def test_energy_at_4 (self): self.assertEqual (30325, energy_at(g1(),3,4)) # corner
    def test_energy_at_5 (self): self.assertEqual (17400, energy_at(g1(),1,0)) # left edge
    def test_energy_at_6 (self): self.assertEqual (39300, energy_at(g1(),0,2)) # top edge
    def test_energy_at_7 (self): self.assertEqual (67725, energy_at(g1(),2,4)) # right edge
    def test_energy_at_8 (self): self.assertEqual (23050, energy_at(g1(),3,3)) # bottom edge
    def test_energy_at_9 (self): self.assertEqual (21000, energy_at(g1(),1,1)) # interior
    def test_energy_at_10(self): self.assertEqual (17625, energy_at(g1(),1,2)) # interior
    def test_energy_at_11(self): self.assertEqual (48025, energy_at(g1(),2,3)) # interior
    
    def test_energy_at_12(self): self.assertEqual (  29, energy_at(g5(),1,0))
    def test_energy_at_13(self): self.assertEqual (1429, energy_at(g5(),0,1))
    def test_energy_at_14(self): self.assertEqual (3527, energy_at(g5(),1,2))
    def test_energy_at_15(self): self.assertEqual (   3, energy_at(g5(),2,2))
    def test_energy_at_16(self): self.assertEqual (   0, energy_at(g5(),2,4))
    def test_energy_at_17(self): self.assertEqual (3500, energy_at(g5(),3,2))
    def test_energy_at_18(self): self.assertEqual (   0, energy_at(g5(),3,3))

    #---------------------------------------------------------------------
    
    # energy function is really just a combo usage of energy_at.
    
    def test_energy_1(self):
        ans = [[46925, 34525, 39300, 58025, 67950], [17400, 21000, 17625, 10025, 30825], [37200, 34000, 39525, 48025, 67725], [23025, 10400, 20325, 23050, 30325]]
        self.assertEqual (ans, energy(g1()))
    def test_energy_2(self):
        ans = [[57685, 50893, 91370, 25418, 33055, 37246], [15421, 56334, 22808, 54796, 11641, 25496], [12344, 19236, 52030, 17708, 44735, 20663], [17074, 23678, 30279, 80663, 37831, 45595], [32337, 30796, 4909, 73334, 40613, 36556]]
        self.assertEqual (ans, energy(g2()))
    def test_energy_3(self):
        ans = [[26450, 31250, 30050], [43150, 43925, 43125], [18750, 19450, 18875], [6700, 6150, 6075], [43025, 44150, 43925]]
        self.assertEqual (ans, energy(g3()))
    def test_energy_4(self):
        ans = [[20808, 52020, 20808], [20808, 52225, 21220], [20809, 52024, 20809], [20808, 52225, 21220]]
        self.assertEqual (ans, energy(g4()))
    def test_energy_5(self):
        ans = [[0, 1429, 3, 1510, 0, 0], [29, 3, 3527, 3, 110, 0], [0, 7729, 3, 7810, 0, 0], [0, 0, 3500, 0, 0, 0]]
        self.assertEqual (ans, energy(g5()))
    def test_energy_6(self):
        ans = [[0, 3, 0, 3, 0, 0], [0, 0, 6, 0, 6, 0], [0, 0, 0, 3, 0, 3], [0, 0, 6, 0, 6, 0]]
        self.assertEqual (ans, energy(g6()))
    
    #---------------------------------------------------------------------
    
    def test_find_vertical_path_1(self):
        ans = [(0, 1), (1, 0), (2, 1), (3, 1)]
        self.assertEqual (ans,find_vertical_path(g1()))
        
    def test_find_vertical_path_2(self):
        ans = [(0, 3), (1, 4), (2, 3), (3, 2), (4, 2)]
        self.assertEqual (ans,find_vertical_path(g2()))
        
    def test_find_vertical_path_3(self):
        ans = [(0, 0), (1, 0), (2, 0), (3, 1), (4, 0)]
        self.assertEqual (ans,find_vertical_path(g3()))
        
    def test_find_vertical_path_4(self):
        ans = [(0, 0), (1, 0), (2, 0), (3, 0)]
        self.assertEqual (ans,find_vertical_path(g4()))
        
    def test_find_vertical_path_5(self):
        ans = [(0, 4), (1, 5), (2, 4), (3, 3)]
        self.assertEqual (ans,find_vertical_path(g5()))
        
    def test_find_vertical_path_6(self):
        ans = [(0, 0), (1, 0), (2, 0), (3, 0)]
        self.assertEqual (ans,find_vertical_path(g6()))
            
    def test_find_vertical_path_7(self):
        ans = [(0, 0), (1, 1), (2, 0), (3, 1)]
        self.assertEqual (ans,find_vertical_path(g7()))
    
    # I want those seven cases to be worth two points each. Run 'em again.
    def test_find_vertical_path_1again(self): self.test_find_vertical_path_1()
    def test_find_vertical_path_2again(self): self.test_find_vertical_path_2()
    def test_find_vertical_path_3again(self): self.test_find_vertical_path_3()
    def test_find_vertical_path_4again(self): self.test_find_vertical_path_4()
    def test_find_vertical_path_5again(self): self.test_find_vertical_path_5()
    def test_find_vertical_path_6again(self): self.test_find_vertical_path_6()
    def test_find_vertical_path_7again(self): self.test_find_vertical_path_7()
    
    #---------------------------------------------------------------------
    
    def test_find_horizontal_path_1(self):
        ans = [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4)]
        self.assertEqual (ans,find_horizontal_path(g1()))
        
    def test_find_horizontal_path_2(self):
        ans = [(2, 0), (2, 1), (1, 2), (2, 3), (1, 4), (2, 5)]
        self.assertEqual (ans,find_horizontal_path(g2()))
        
    def test_find_horizontal_path_3(self):
        ans = [(3, 0), (3, 1), (3, 2)]
        self.assertEqual (ans,find_horizontal_path(g3()))
        
    def test_find_horizontal_path_4(self):
        ans = [(0, 0), (0, 1), (0, 2)]
        self.assertEqual (ans,find_horizontal_path(g4()))
        
    def test_find_horizontal_path_5(self):
        ans = [(2, 0), (3, 1), (2, 2), (3, 3), (2, 4), (1, 5)]
        self.assertEqual (ans,find_horizontal_path(g5()))
        
    def test_find_horizontal_path_6(self):
        ans = [(0, 0), (1, 1), (0, 2), (1, 3), (0, 4), (0, 5)]
        self.assertEqual (ans,find_horizontal_path(g6()))
            
    def test_find_horizontal_path_7(self):
        ans = [(0, 0), (1, 1), (0, 2), (1, 3), (0, 4), (1, 5)]
        self.assertEqual (ans,find_horizontal_path(g7()))
    
    def test_find_horizontal_path_1again(self): self.test_find_horizontal_path_1()
    def test_find_horizontal_path_2again(self): self.test_find_horizontal_path_2()
    def test_find_horizontal_path_3again(self): self.test_find_horizontal_path_3()
    def test_find_horizontal_path_4again(self): self.test_find_horizontal_path_4()
    def test_find_horizontal_path_5again(self): self.test_find_horizontal_path_5()
    #---------------------------------------------------------------------
    
    def test_remove_vertical_path_1(self):
        orig = g1()
        path = [(0,0),(1,0),(2,0),(3,0)]
        next = remove_vertical_path(orig,path)
        # just check that they are returning a reference to the original.
        # we don't actually care in this test if they properly removed.
        self.assertEquals(orig, next)
    
    # remove a manually created path (not the "best" path).
    def test_remove_vertical_path_2(self):
        # an 8x4 grid of (1,1,1)'s.
        g = build_grid(8,4,(1,1,1))
        # we'll consider these spots as the path,
        path = [(0,0),(1,1),(2,2),(3,1),(4,0),(5,0),(6,1),(7,2)]
        # so we put other values at those spots.
        for (r,c) in path:
            g[r][c] = (9,9,9)
        # let's remove all the 9's
        remove_vertical_path(g,path)
        # and then we expect a narrower grid.
        expected = build_grid(8,3,(1,1,1))
        self.assertEquals(expected, g)
    
    # remove a manually created path (not the "best" path).
    def test_remove_vertical_path_3(self):
        # an 8x4 grid of (1,1,1)'s.
        g = build_grid(8,4,(1,1,1))
        # we'll consider these spots as the path: the far left edge
        path = [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0)]
        # so we put other values at those spots.
        for (r,c) in path:
            g[r][c] = (9,9,9)
        # let's remove all the 9's
        remove_vertical_path(g,path)
        # and then we expect a narrower grid.
        expected = build_grid(8,3,(1,1,1))
        self.assertEquals(expected, g)
    
    # remove a manually created path (not the "best" path).
    def test_remove_vertical_path_4(self):
        # an 8x4 grid of (1,1,1)'s.
        g = build_grid(8,4,(1,1,1))
        # we'll consider these spots as the path: wandering around
        path = [(0,2),(1,1),(2,2),(3,3),(4,3),(5,2),(6,1),(7,2)]
        # so we put other values at those spots.
        for (r,c) in path:
            g[r][c] = (9,9,9)
        # let's remove all the 9's
        remove_vertical_path(g,path)
        # and then we expect a narrower grid.
        expected = build_grid(8,3,(1,1,1))
        self.assertEquals(expected, g)
    
    # test our given grids
    def test_remove_vertical_path_5(self):
        g = g1()
        got = remove_vertical_path(g,find_vertical_path(g))
        expected = [[(100, 75, 200), (100, 100, 200), (100, 100, 200), (200, 125, 200)], [(150, 50, 180), (100, 120, 180), (100, 120, 180), (100, 120, 180)], [(100, 75, 100), (100, 85, 100), (100, 95, 100), (100, 110, 100)], [(200, 100, 10), (200, 100, 10), (210, 200, 10), (255, 0, 10)]]
        self.assertEquals(expected, got)
    
    def test_remove_vertical_path_6(self):
        g = g2()
        got = remove_vertical_path(g,find_vertical_path(g))
        expected = [[(78, 209, 79), (63, 118, 247), (92, 175, 95), (210, 109, 104), (252, 101, 119)], [(224, 191, 182), (108, 89, 82), (80, 196, 230), (112, 156, 180), (142, 151, 142)], [(117, 189, 149), (171, 231, 153), (149, 164, 168), (120, 105, 138), (163, 174, 196)], [(163, 222, 132), (187, 117, 183), (158, 143, 79), (220, 75, 222), (189, 73, 214)], [(211, 120, 173), (188, 218, 244), (163, 166, 246), (79, 125, 246), (211, 201, 98)]]
        self.assertEquals(expected, got)
    
    def test_remove_vertical_path_7(self):
        g = g3()
        got = remove_vertical_path(g,find_vertical_path(g))
        expected = [[(0, 80, 200), (0, 100, 200)], [(100, 15, 200), (100, 25, 200)], [(200, 110, 255), (200, 100, 255)], [(200, 100, 255), (200, 100, 255)], [(255, 100, 200), (255, 100, 200)]]
        self.assertEquals(expected, got)
    
    def test_remove_vertical_path_8(self):
        g = g4()
        got = remove_vertical_path(g,find_vertical_path(g))
        expected = [[(255, 101, 153), (255, 101, 255)], [(255, 153, 153), (255, 153, 255)], [(255, 204, 153), (255, 205, 255)], [(255, 255, 153), (255, 255, 255)]]
        self.assertEquals(expected, got)
    
    # I want those eight cases to be worth two points each. Run 'em again.
    def test_remove_vertical_path_1again(self): self.test_remove_vertical_path_1()
    def test_remove_vertical_path_2again(self): self.test_remove_vertical_path_2()
    def test_remove_vertical_path_3again(self): self.test_remove_vertical_path_3()
    def test_remove_vertical_path_4again(self): self.test_remove_vertical_path_4()
    def test_remove_vertical_path_5again(self): self.test_remove_vertical_path_5()
    def test_remove_vertical_path_6again(self): self.test_remove_vertical_path_6()
    def test_remove_vertical_path_7again(self): self.test_remove_vertical_path_7()
    def test_remove_vertical_path_8again(self): self.test_remove_vertical_path_8()
    

    #---------------------------------------------------------------------
    
    # remove a manually created path (not the "best" path).
    def test_remove_horizontal_path_1(self):
        # an 8x4 grid of (1,1,1)'s.
        g = build_grid(4,7,(1,1,1))
        # we'll consider these spots as the path: top line
        path = [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6)]
        # so we put other values at those spots.
        for (r,c) in path:
            g[r][c] = (9,9,9)
        # let's remove all the 9's
        g = remove_horizontal_path(g,path)
        # and then we expect a narrower grid.
        expected = build_grid(3,7,(1,1,1))
        self.assertEquals(expected, g)
    
    # remove a manually created path (not the "best" path).
    def test_remove_horizontal_path_2(self):
        # an 8x4 grid of (1,1,1)'s.
        g = build_grid(4,7,(1,1,1))
        # we'll consider these spots as the path: bottom line
        path = [(3,0),(3,1),(3,2),(3,3),(3,4),(3,5),(3,6)]
        # so we put other values at those spots.
        for (r,c) in path:
            g[r][c] = (9,9,9)
        # let's remove all the 9's
        g = remove_horizontal_path(g,path)
        # and then we expect a narrower grid.
        expected = build_grid(3,7,(1,1,1))
        self.assertEquals(expected, g)
    
    # remove a manually created path (not the "best" path).
    def test_remove_horizontal_path_3(self):
        # an 8x4 grid of (1,1,1)'s.
        g = build_grid(4,7,(1,1,1))
        # we'll consider these spots as the path: toggling rows
        path = [(0,0),(1,1),(0,2),(1,3),(1,4),(0,5),(1,6)]
        # so we put other values at those spots.
        for (r,c) in path:
            g[r][c] = (9,9,9)
        # let's remove all the 9's
        g = remove_horizontal_path(g,path)
        # and then we expect a narrower grid.
        expected = build_grid(3,7,(1,1,1))
        self.assertEquals(expected, g)
    
    # remove a manually created path (not the "best" path).
    def test_remove_horizontal_path_4(self):
        # an 8x4 grid of (1,1,1)'s.
        g = build_grid(4,7,(1,1,1))
        # we'll consider these spots as the path: toggling interior
        path = [(1,0),(2,1),(1,2),(2,3),(1,4),(2,5),(1,6)]
        # so we put other values at those spots.
        for (r,c) in path:
            g[r][c] = (9,9,9)
        # let's remove all the 9's
        g = remove_horizontal_path(g,path)
        # and then we expect a narrower grid.
        expected = build_grid(3,7,(1,1,1))
        self.assertEquals(expected, g)
    
    # remove a manually created path (not the "best" path).
    def test_remove_horizontal_path_5(self):
        # an 8x4 grid of (1,1,1)'s.
        g = build_grid(7,7,(1,1,1))
        # we'll consider these spots as the path: all in unique rows
        path = [(0,0),(1,1),(2,2),(3,3),(4,4),(5,5),(6,6)]
        # so we put other values at those spots.
        for (r,c) in path:
            g[r][c] = (9,9,9)
        # let's remove all the 9's
        g = remove_horizontal_path(g,path)
        # and then we expect a narrower grid.
        expected = build_grid(6,7,(1,1,1))
        self.assertEquals(expected, g)
    
    # test our given grids
    def test_remove_horizontal_path_6(self):
        g = g1()
        got = remove_horizontal_path(g,find_horizontal_path(g))
        expected = [[(100, 75, 200), (100, 100, 200), (100, 100, 200), (100, 100, 200), (200, 125, 200)], [(100, 75, 100), (100, 80, 100), (100, 85, 100), (100, 95, 100), (100, 110, 100)], [(200, 100, 10), (200, 100, 10), (200, 100, 10), (210, 200, 10), (255, 0, 10)]]
        self.assertEquals(expected, got)
    
    # test our given grids
    def test_remove_horizontal_path_7(self):
        g = g2()
        got = remove_horizontal_path(g,find_horizontal_path(g))
        expected = [[(78, 209, 79), (63, 118, 247), (92, 175, 95), (243, 73, 183), (210, 109, 104), (252, 101, 119)], [(224, 191, 182), (108, 89, 82), (149, 164, 168), (112, 156, 180), (120, 105, 138), (142, 151, 142)], [(163, 222, 132), (187, 117, 183), (92, 145, 69), (158, 143, 79), (220, 75, 222), (189, 73, 214)], [(211, 120, 173), (188, 218, 244), (214, 103, 68), (163, 166, 246), (79, 125, 246), (211, 201, 98)]]
        self.assertEquals(expected, got)
    
    # test our given grids
    def test_remove_horizontal_path_8(self):
        g = g3()
        got = remove_horizontal_path(g,find_horizontal_path(g))
        expected = [[(0, 100, 200), (0, 80, 200), (0, 100, 200)], [(100, 25, 200), (100, 15, 200), (100, 25, 200)], [(200, 95, 255), (200, 110, 255), (200, 100, 255)], [(255, 70, 200), (255, 100, 200), (255, 100, 200)]]
        self.assertEquals(expected, got)
    
    # test our given grids
    def test_remove_horizontal_path_9(self):
        g = g4()
        got = remove_horizontal_path(g,find_horizontal_path(g))
        expected = [[(255, 153, 51), (255, 153, 153), (255, 153, 255)], [(255, 203, 51), (255, 204, 153), (255, 205, 255)], [(255, 255, 51), (255, 255, 153), (255, 255, 255)]]
        self.assertEquals(expected, got)
    
    def test_remove_horizontal_path_1again(self): self.test_remove_horizontal_path_1()
    def test_remove_horizontal_path_6again(self): self.test_remove_horizontal_path_6()
    def test_remove_horizontal_path_7again(self): self.test_remove_horizontal_path_7()
    def test_remove_horizontal_path_8again(self): self.test_remove_horizontal_path_8()
    def test_remove_horizontal_path_9again(self): self.test_remove_horizontal_path_9()

    #---------------------------------------------------------------------
    
    def test_grid_to_ppm_1(self):
        filename = ".temp_file.ppm"
        ppm = grid_to_ppm(g1(),filename)
        s = from_file(filename)
        tokens = s.split()
        expected = ['P3', '5', '4', '255', '100', '75', '200', '100', '100', '200', '100', '100', '200', '100', '100', '200', '200', '125', '200', '150', '30', '180', '150', '50', '180', '100', '120', '180', '100', '120', '180', '100', '120', '180', '100', '75', '100', '100', '80', '100', '100', '85', '100', '100', '95', '100', '100', '110', '100', '200', '100', '10', '200', '100', '10', '200', '100', '10', '210', '200', '10', '255', '0', '10']
        self.assertEquals(expected, tokens)
        
    def test_grid_to_ppm_2(self):
        filename = ".temp_file.ppm"
        ppm = grid_to_ppm(g2(),filename)
        s = from_file(filename)
        tokens = s.split()
        expected = ['P3', '6', '5', '255', '78', '209', '79', '63', '118', '247', '92', '175', '95', '243', '73', '183', '210', '109', '104', '252', '101', '119', '224', '191', '182', '108', '89', '82', '80', '196', '230', '112', '156', '180', '176', '178', '120', '142', '151', '142', '117', '189', '149', '171', '231', '153', '149', '164', '168', '107', '119', '71', '120', '105', '138', '163', '174', '196', '163', '222', '132', '187', '117', '183', '92', '145', '69', '158', '143', '79', '220', '75', '222', '189', '73', '214', '211', '120', '173', '188', '218', '244', '214', '103', '68', '163', '166', '246', '79', '125', '246', '211', '201', '98']
        self.assertEquals(expected, tokens)
        
    def test_grid_to_ppm_3(self):
        filename = ".temp_file.ppm"
        ppm = grid_to_ppm(g3(),filename)
        s = from_file(filename)
        tokens = s.split()
        expected = ['P3', '3', '5', '255', '0', '100', '200', '0', '80', '200', '0', '100', '200', '100', '25', '200', '100', '15', '200', '100', '25', '200', '200', '95', '255', '200', '110', '255', '200', '100', '255', '200', '100', '255', '200', '95', '255', '200', '100', '255', '255', '70', '200', '255', '100', '200', '255', '100', '200']
        self.assertEquals(expected, tokens)
        
    def test_grid_to_ppm_4(self):
        filename = ".temp_file.ppm"
        ppm = grid_to_ppm(g4(),filename)
        s = from_file(filename)
        tokens = s.split()
        expected = ['P3', '3', '4', '255', '255', '101', '51', '255', '101', '153', '255', '101', '255', '255', '153', '51', '255', '153', '153', '255', '153', '255', '255', '203', '51', '255', '204', '153', '255', '205', '255', '255', '255', '51', '255', '255', '153', '255', '255', '255']
        self.assertEquals(expected, tokens)
        
    #---------------------------------------------------------------------
    
    def test_ppm_to_grid_1(self):
        # we want to have an existing ppm file, and read it to a grid,
        # lastly checking that the grid we got matches what is expected.
        
        filename = ".temp_file.ppm"
        expected = g1()
        
        # put a ppm file's contents into a string. 
        s = "P3\n5\n4\n255\n100\n75\n200\n100\n100\n200\n100\n100\n200\n100\n100\n200\n200\n125\n200\n150\n30\n180\n150\n50\n180\n100\n120\n180\n100\n120\n180\n100\n120\n180\n100\n75\n100\n100\n80\n100\n100\n85\n100\n100\n95\n100\n100\n110\n100\n200\n100\n10\n200\n100\n10\n200\n100\n10\n210\n200\n10\n255\n0\n10\n"
        
        # put that string into a file.
        make_file(s,filename)
        
        # call student's code.
        got = ppm_to_grid(filename)
        
        # check that they read it successfully
        self.assertEquals(expected, got)
        
    def test_ppm_to_grid_2(self):
        # we want to have an existing ppm file, and read it to a grid,
        # lastly checking that the grid we got matches what is expected.
        
        filename = ".temp_file.ppm"
        expected = g2()
        
        # put a ppm file's contents into a string. 
        s = "P3\n6\n5\n255\n78\n209\n79\n63\n118\n247\n92\n175\n95\n243\n73\n183\n210\n109\n104\n252\n101\n119\n224\n191\n182\n108\n89\n82\n80\n196\n230\n112\n156\n180\n176\n178\n120\n142\n151\n142\n117\n189\n149\n171\n231\n153\n149\n164\n168\n107\n119\n71\n120\n105\n138\n163\n174\n196\n163\n222\n132\n187\n117\n183\n92\n145\n69\n158\n143\n79\n220\n75\n222\n189\n73\n214\n211\n120\n173\n188\n218\n244\n214\n103\n68\n163\n166\n246\n79\n125\n246\n211\n201\n98\n"
        
        # put that string into a file.
        make_file(s,filename)
        
        # call student's code.
        got = ppm_to_grid(filename)
        
        # check that they read it successfully
        self.assertEquals(expected, got)
        
    def test_ppm_to_grid_3(self):
        # we want to have an existing ppm file, and read it to a grid,
        # lastly checking that the grid we got matches what is expected.
        
        filename = ".temp_file.ppm"
        expected = g3()
        
        # put a ppm file's contents into a string. 
        s = "P3\n3\n5\n255\n0\n100\n200\n0\n80\n200\n0\n100\n200\n100\n25\n200\n100\n15\n200\n100\n25\n200\n200\n95\n255\n200\n110\n255\n200\n100\n255\n200\n100\n255\n200\n95\n255\n200\n100\n255\n255\n70\n200\n255\n100\n200\n255\n100\n200\n"
        
        # put that string into a file.
        make_file(s,filename)
        
        # call student's code.
        got = ppm_to_grid(filename)
        
        # check that they read it successfully
        self.assertEquals(expected, got)
        
    def test_ppm_to_grid_4(self):
        # we want to have an existing ppm file, and read it to a grid,
        # lastly checking that the grid we got matches what is expected.
        
        filename = ".temp_file.ppm"
        expected = g4()
        
        # put a ppm file's contents into a string. 
        s = "P3\n3\n4\n255\n255\n101\n51\n255\n101\n153\n255\n101\n255\n255\n153\n51\n255\n153\n153\n255\n153\n255\n255\n203\n51\n255\n204\n153\n255\n205\n255\n255\n255\n51\n255\n255\n153\n255\n255\n255\n"
        
        # put that string into a file.
        make_file(s,filename)
        
        # call student's code.
        got = ppm_to_grid(filename)
        
        # check that they read it successfully
        self.assertEquals(expected, got)
    
    #---------------------------------------------------------------------
    
    
# This class digs through AllTests, counts and builds all the tests,
# so that we have an entire test suite that can be run as a group.
class TheTestSuite (unittest.TestSuite):
    # constructor.
    def __init__(self,wants):
        # find all methods that begin with "test".
        fs = []
        want_all = wants==None
        
        for func in AllTests.__dict__:
            # append regular tests
            # drop any digits from the end of str(func).
            dropnum = str(func)
            while dropnum[-1] in "1234567890":
                dropnum = dropnum[:-1]
            
            if func in ['__doc__', '__module__']:
                continue
            # check if we want this one.
            want_this_one = want_all
            if wants != None:
                for w in wants:
                    is_ec = dropnum==("test_extra_credit_"+w+"_")
                    if is_ec:
                        want_this_one = False
                        break
                    is_test = dropnum==("test_"+w+"_")
                    check = is_test and ((not is_ec) or (is_ec and (not BATCH_MODE)))
                    want_this_one = want_this_one or check
            
            if want_this_one:
                fs.append(AllTests(str(func)))
        
        # call parent class's constructor.
        unittest.TestSuite.__init__(self,fs)

class TheExtraCreditTestSuite (unittest.TestSuite):
        # constructor.
        def __init__(self,wants):
            # find all methods that begin with "test".
            fs = []
            want_all = wants==None
            for func in AllTests.__dict__:
                want_this_one = want_all
                if wants != None:
                    for w in wants:
                        is_ec = (str(func).startswith("test_extra_credit_"+w))
                        want_this_one = want_this_one or is_ec
                
                if BATCH_MODE and want_this_one:
                    fs.append(AllTests(str(func)))
            
            # call parent class's constructor.
            unittest.TestSuite.__init__(self,fs)

# all (non-directory) file names, regardless of folder depth,
# under the given directory 'dir'.
def files_list(dir):
    info = os.walk(dir)
    filenames = []
    for (dirpath,dirnames,filez) in info:
#        print(dirpath,dirnames,filez)
        if dirpath==".":
            continue
        for file in filez:
            filenames.append(os.path.join(dirpath,file))
#        print(dirpath,dirnames,filez,"\n")
#        filenames.extend(os.path.join(dirpath, filez))
    return filenames

def main():
    if len(sys.argv)<2:
        raise Exception("needed student's file name as command-line argument:"\
            +"\n\t\"python3 tester4L.py gmason76_2xx_L4.py\"")
    want_all = len(sys.argv) <=2
    wants = []
    
    # remove batch_mode signifiers from want-candidates.
    want_candidates = sys.argv[2:]
    for i in range(len(want_candidates)-1,-1,-1):
        if want_candidates[i] in ['.'] or os.path.isdir(want_candidates[i]):
            del want_candidates[i]
    
    if not want_all:
        print("args: ",sys.argv)
        for w in want_candidates:
            if w in REQUIRED_DEFNS:
                wants.append(w)
            elif w in SUB_DEFNS:
                wants.append(w)
            else:
                raise Exception("asked to limit testing to unknown function '%s'."%w)
    else:
        wants = None # signifies that we want them all.
    
    if not BATCH_MODE:
        run_file(sys.argv[1],wants)
    else:
        filenames = files_list(sys.argv[1])
    
#         print(filenames)
    
        results = []
        for filename in filenames:
            try:
                print("\n\n\nRUNNING: "+filename)
                (tag, passed,tried,ec) = run_file(filename,wants)
                results.append((tag,passed,tried,ec))
            except SyntaxError as e:
                results.append((filename+"_SYNTAX_ERROR",0,1))    
            except ValueError as e:
                return (filename+"_VALUE_ERROR",0,1)
            except TypeError as e:
                return (filename+"_TYPE_ERROR",0,1)
            except ImportError as e:
                results.append((filename+"_IMPORT_ERROR_TRY_AGAIN    ",0,1))    
            except Exception as e:
                return (filename+str(e.__reduce__()[0]),0,1)
            
        print("\n\n\nGRAND RESULTS:\n")
        for (tag, passed, tried, ec) in results:
            print(("%.0f%%  (%d/%d, %dEC) - " % (passed/tried*100 + ec, passed, tried, ec))+tag)

# this will group all the tests together, prepare them as 
# a test suite, and run them.
def run_file(filename,wants=[]):
    
    # move the student's code to a valid file.
    shutil.copyfile(filename,"student.py")
    # wait half a second for file I/O to catch up...
        
    # import student's code, and *only* copy over the expected functions
    # for later use.
    import imp
    count = 0
    while True:
        try:
            import student
            imp.reload(student)
            break
        except ImportError as e:
            print("import error getting student.. trying again. "+os.getcwd(), os.path.exists("student.py"))
            time.sleep(0.5)
            count+=1
            if count>3:
                raise ImportError("too many attempts at importing!")
        except SyntaxError as e:
            results.append((filename+"_SYNTAX_ERROR",0,1))    
        except ValueError as e:
            return (filename+"_VALUE_ERROR",0,1)
        except TypeError as e:
            return (filename+"_TYPE_ERROR",0,1)
        except ImportError as e:
            results.append((filename+"_IMPORT_ERROR_TRY_AGAIN    ",0,1))    
        except Exception as e:
            return (filename+str(e.__reduce__()[0]),0,1)
        except Exception as e:
            print("didn't get to import student yet... " + e)
    # but we want to re-load this between student runs...
    # the imp module helps us force this reload.s
    
    import student
    imp.reload(student)
    
    # make a global for each expected definition.
    def decoy(name):
        return (lambda x: "<no '%s' definition found>" % name)
        
    for fn in REQUIRED_DEFNS:
        globals()[fn] = decoy(fn)
        try:
            globals()[fn] = getattr(student,fn)
        except:
            print("\nNO DEFINITION FOR '%s'." % fn)    
    
    # create an object that can run tests.
    runner1 = unittest.TextTestRunner()
    
    # define the suite of tests that should be run.
    suite1 = TheTestSuite(wants)
    
    # let the runner run the suite of tests.
    ans = runner1.run(suite1)
    num_errors   = len(ans.__dict__['errors'])
    num_failures = len(ans.__dict__['failures'])
    num_tests    = ans.__dict__['testsRun']
    num_passed   = num_tests - num_errors - num_failures
    # print(ans)
    
    
    if BATCH_MODE:
        # do the same for the extra credit.
        runnerEC = unittest.TextTestRunner()
        suiteEC = TheExtraCreditTestSuite(wants)
        ansEC = runnerEC.run(suiteEC)
        num_errorsEC   = len(ansEC.__dict__['errors'])
        num_failuresEC = len(ansEC.__dict__['failures'])
        num_testsEC    = ansEC.__dict__['testsRun']
        num_passedEC   = num_testsEC - num_errorsEC - num_failuresEC
        print(ansEC)
    else:
        num_passedEC = 0
    
    # remove our temporary file.
    os.remove("student.py")
    if os.path.exists("__pycache__"):
        shutil.rmtree("__pycache__")
    
    tag = ".".join(filename.split(".")[:-1])
    return (tag, num_passed, num_tests,num_passedEC)

# this determines if we were imported (not __main__) or not;
# when we are the one file being run, perform the tests! :)
if __name__ == "__main__":
    main()