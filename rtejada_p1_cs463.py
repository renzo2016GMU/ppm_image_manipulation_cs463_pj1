# /*
#  ============================================================================
#  Name        : rtejada_p1.py
#  Author      : Renzo Tejada
#  Copyright   : N/A open source
#  Description : CS 463 - Project 1, Image Smashing (Python version)
#  Professor   : Mark Snyder
#  ============================================================================
#  */
import io
import unittest
import shutil
import sys
import os
import time
import importlib

def width(thisgrid):
    "simply get length on grid object, a 2d list"
    width=len(thisgrid[0])
    return width
    
def height(grid):
    "simply get length on grid object, a 2d list"    
    height = len(grid)
    return height

def energy_at(grid,r,c):# Given a grid of RGB triplets, calculate the energy gradient at that location. 
        "Case one if cur node is an interior node"
        w=width(grid)
        h=height(grid)
        #print(r,c)
        switch=False
        corner_case=False
        e=0
        if( ((r==0 and c==0) or (r==h-1 and c==w-1)) or ((r==0 and c==w-1) or (c==0 and r==h-1))):
            corner_case=True

        if (0<r and r<h-1 and 0<c and c<w-1):
            switch=True
#             print("inside node case",grid[r][c][0])
#             print(grid[r][c][])
            Rx = pow((grid[r][c-1][0] - grid[r][c+1][0]),2)
            Ry = pow((grid[r][c-1][1] - grid[r][c+1][1]),2)
            Rz = pow((grid[r][c-1][2] - grid[r][c+1][2]),2) 
            
            R1 = pow((grid[r-1][c][0] - grid[r+1][c][0]),2)
            R2 = pow((grid[r-1][c][1] - grid[r+1][c][1]),2)
            R3 = pow((grid[r-1][c][2] - grid[r+1][c][2]),2) 
            sum = Rx + Ry + Rz
            sum2= R1 + R2 + R3
            overall_energy=sum+sum2
#             print("overall Energy is", overall_energy)  
            return overall_energy
#         #print("border pixel cases...")
#         #print("inside node case",grid[r][c])
        #none border cases
        "in case target node is located in an edge of the grid"
        if (r==0 and (c!=0 or c!=w-1) and switch==False) and (corner_case==False):
#             #print("case 1")
            switch=True
            "left edge of grid"
            Rx = pow((grid[r][c-1][0] - grid[r][c+1][0]),2)
            Ry = pow((grid[r][c-1][1] - grid[r][c+1][1]),2)
            Rz = pow((grid[r][c-1][2] - grid[r][c+1][2]),2) 
            
            R1 = pow((grid[h-1][c][0] - grid[r+1][c][0]),2)
            R2 = pow((grid[h-1][c][1] - grid[r+1][c][1]),2)
            R3 = pow((grid[h-1][c][2] - grid[r+1][c][2]),2)
            sum = Rx + Ry + Rz
            sum2= R1 + R2 + R3
            overall_energy=sum+sum2
#             #print("overall Energy is", overall_energy)  
#             #print("(grid[h-1][c][0] - grid[r+1][c][0])",grid[h-1][c][0] , grid[r+1][c][0])
            return overall_energy
        
        if r==h-1 and (c!=0 or c!=w-1 and switch==False)and (corner_case==False):
            "right edge of grid"
            #print("case 2")
            switch=True
            Rx = pow((grid[r][c-1][0] - grid[r][c+1][0]),2)
            Ry = pow((grid[r][c-1][1] - grid[r][c+1][1]),2)
            Rz = pow((grid[r][c-1][2] - grid[r][c+1][2]),2) 
             
            R1 = pow((grid[0][c][0] - grid[r-1][c][0]),2)
            R2 = pow((grid[0][c][1] - grid[r-1][c][1]),2)
            R3 = pow((grid[0][c][2] - grid[r-1][c][2]),2)
            sum = Rx + Ry + Rz
            sum2= R1 + R2 + R3
            overall_energy=sum+sum2
#             #print("overall Energy is", overall_energy)
            return overall_energy  
        if c==0 and (r!=0 or r!=h-1 and switch==False) and (corner_case==False):
#             #print("case 3")
            switch=True
            "upper edge of grid"
            Rx = pow((grid[r][w-1][0] - grid[r][c+1][0]),2)
            Ry = pow((grid[r][w-1][1] - grid[r][c+1][1]),2)
            Rz = pow((grid[r][w-1][2] - grid[r][c+1][2]),2) 
             
            R1 = pow((grid[r-1][c][0] - grid[r+1][c][0]),2)
            R2 = pow((grid[r-1][c][1] - grid[r+1][c][1]),2)
            R3 = pow((grid[r-1][c][2] - grid[r+1][c][2]),2) 
            sum = Rx + Ry + Rz
            sum2= R1 + R2 + R3
            overall_energy=sum+sum2
#             #print("overall Energy is", overall_energy)  
#             #print("(grid[h-1][c][0] - grid[r+1][c][0])",grid[h-1][c][0] , grid[r+1][c][0])
            return overall_energy
        if c==w-1 and (r!=0 or r!=h-1 and switch==False)and (corner_case==False):
            "Bottom edge of grid"  
            switch=True
#             #print("target node",grid[r][c])
# #             #print(grid[r][c].index(0, ))
            Rx = pow((grid[r][c-1][0] - grid[r][0][0]),2)
            Ry = pow((grid[r][c-1][1] - grid[r][0][1]),2)
            Rz = pow((grid[r][c-1][2] - grid[r][0][2]),2) 
            
            R1 = pow((grid[r-1][c][0] - grid[r+1][c][0]),2)
            R2 = pow((grid[r-1][c][1] - grid[r+1][c][1]),2)
            R3 = pow((grid[r-1][c][2] - grid[r+1][c][2]),2) 
            sum = Rx + Ry + Rz
            sum2= R1 + R2 + R3
            overall_energy=sum+sum2
#             #print("overall Energy is", overall_energy)
            return overall_energy
        if switch==False:
#             #print("corner cases")
            if c==0 and r == 0:
#                 print("UL corner")
                Rx = pow((grid[r][c+1][0] - grid[r][w-1][0]),2)
                Ry = pow((grid[r][c+1][1] - grid[r][w-1][1]),2)
                Rz = pow((grid[r][c+1][2] - grid[r][w-1][2]),2) 
                
                R1 = pow((grid[h-1][c][0] - grid[r+1][c][0]),2)
                R2 = pow((grid[h-1][c][1] - grid[r+1][c][1]),2)
                R3 = pow((grid[h-1][c][2] - grid[r+1][c][2]),2)
                sum = Rx + Ry + Rz
                sum2= R1 + R2 + R3
                overall_energy=sum+sum2
#                 print("overall Energy is", overall_energy)
                return overall_energy
          
            if c==w-1 and r == 0:
                "Corder cases grid UL C"
                Rx = pow((grid[r][c-1][0] - grid[r][0][0]),2)
                Ry = pow((grid[r][c-1][1] - grid[r][0][1]),2)
                Rz = pow((grid[r][c-1][2] - grid[r][0][2]),2) 
                
                R1 = pow((grid[h-1][c][0] - grid[r+1][c][0]),2)
                R2 = pow((grid[h-1][c][1] - grid[r+1][c][1]),2)
                R3 = pow((grid[h-1][c][2] - grid[r+1][c][2]),2)
                sum = Rx + Ry + Rz
                sum2= R1 + R2 + R3
                overall_energy=sum+sum2
                #print(grid[r][c-1], grid[r][0])
                #print(grid[h-1][c], grid[r+1][c]) 
                #print("overall Energy is", overall_energy)
                return overall_energy
                
            if c==0 and r == h-1:
                "Corder cases grid UL UR"
                Rx = pow((grid[r][c+1][0] - grid[r][w-1][0]),2)
                Ry = pow((grid[r][c+1][1] - grid[r][w-1][1]),2)
                Rz = pow((grid[r][c+1][2] - grid[r][w-1][2]),2) 
                
                R1 = pow((grid[r-1][c][0] - grid[0][c][0]),2)
                R2 = pow((grid[r-1][c][1] - grid[0][c][1]),2)
                R3 = pow((grid[r-1][c][2] - grid[0][c][2]),2)
                sum = Rx + Ry + Rz
                sum2= R1 + R2 + R3
                overall_energy=sum+sum2
#                 print(grid[r][c+1],grid[r][w-1])
#                 print(grid[r-1][c], grid[0][c])
#                 print("overall Energy is", overall_energy)
                return overall_energy
                
            if c==w-1 and r == h-1:
                "Corder cases grid BL"
                Rx = pow((grid[r][c-1][0] - grid[r][0][0]),2)
                Ry = pow((grid[r][c-1][1] - grid[r][0][1]),2)
                Rz = pow((grid[r][c-1][2] - grid[r][0][2]),2) 
#                 print(grid[r][c-1], grid[r][0])
                R1 = pow((grid[r-1][c][0] - grid[0][c][0]),2)
                R2 = pow((grid[r-1][c][1] - grid[0][c][1]),2)
                R3 = pow((grid[r-1][c][2] - grid[0][c][2]),2)
#                 print(grid[r-1][c],grid[0][c])
                sum = Rx + Ry + Rz
                sum2= R1 + R2 + R3
                overall_energy=sum+sum2
#                 print("overall Energy is", overall_energy)
                return overall_energy
    
def energy(grid):
    "Get right height and width of grid then use energy at helper function" 
    num_col=width(grid)
    num_row=height(grid)
    "Allocate memory for new grid of energy"
    grid_energy=[[-1]*num_col for i in range(num_row)]
    for i in range(0,num_row):
        for j in range(0,num_col):
            "Iterate in each node of grid to calculate energy"
            grid_energy[i][j]=energy_at(grid,i,j)
#         #print(grid_energy)
    return grid_energy

# energy(grid)

def find_vertical_path(grid):
    num_col=width(grid)
    num_row=height(grid)
    w=width(grid)
    h=height(grid)
    "get energy of grid"
    new_grid = energy(grid)
    " create grid that holds energy and closest path to bottom"
    grid_nodes=[[[-1,-2,-3]]*num_col for i in range(num_row)]
    for i in range(0,num_row):
        for j in range(0,num_col):
            grid_nodes[i][j]=[i*num_row+j, -111,-222]
    "Allocated memory and set values to -111, and 222 which will be used a flags"
    for i in range(0,num_row):
        for j in range(0,num_col):
            grid_nodes[i][j][0]=new_grid[i][j]
            #sets the boottom nodes distance equal to themselfs
            if(i==(height(grid)-1)):
                grid_nodes[i][j][1]=new_grid[i][j]     
#         ##print(grid_nodes)
    "Post C: bottom node already hold their weight"
    #algorithm to find best path from up down
    bottom=-1
    right=-1
    left=-1
    for i in range((height(grid)-2),-1,-1):
#             ##print("value of i is:",i)
        for j in range(0,w):
            if(j==0):
#                     ##print("====>Only check bottom and left", i, j)
                bottom=grid_nodes[i+1][j][1]
                right=grid_nodes[i+1][j+1][1]

                if(bottom<=right):
                    grid_nodes[i][j][1]=bottom+grid_nodes[i][j][0]
                    "WRITE CHEAPEST PATH in node"
                    grid_nodes[i][j][2]=(i+1,j)
                else:
                    grid_nodes[i][j][1]=right+grid_nodes[i][j][0]
                    grid_nodes[i][j][2]=(i+1,j+1)
                    
            elif(j<w-1 and j>0):
                " SEE THIS PIC-> [_]"
#                     print("j and i:",j,i)
                bottom=grid_nodes[i+1][j][1]
                right=grid_nodes[i+1][j+1][1]
                left=grid_nodes[i+1][j-1][1]
#                     ##print(bottom, right)
                if(bottom<right and bottom<left):#    3<5 y 3 7
                    grid_nodes[i][j][1]=bottom+grid_nodes[i][j][0]
                    grid_nodes[i][j][2]=(i+1,j)
                elif(left==bottom and right>left):
                    grid_nodes[i][j][1]=right+grid_nodes[i][j][0]
                    grid_nodes[i][j][2]=(i+1,j-1)
                elif(right<bottom and right<left):
                    grid_nodes[i][j][1]=right+grid_nodes[i][j][0]
                    grid_nodes[i][j][2]=(i+1,j+1)
                else:
                    grid_nodes[i][j][1]=left+grid_nodes[i][j][0]
                    grid_nodes[i][j][2]=(i+1,j-1)
            else:
#                     print("==>At the edge right of the grid", i, j)
                bottom=grid_nodes[i+1][j][1]
                left=grid_nodes[i+1][j-1][1]
#                     ##print(bottom, right)
                if(bottom<left):
                    grid_nodes[i][j][1]=bottom+grid_nodes[i][j][0]
                    grid_nodes[i][j][2]=(i+1,j)
#                         print(grid_nodes[i][j],grid_nodes[i][j][2])
                else:

                    if(j==h-2):
                        grid_nodes[i][j][1]=bottom+grid_nodes[i][j][0]
                        grid_nodes[i][j][2]=(i+1,j-1)
                        
                    else:      
                        grid_nodes[i][j][1]=left+grid_nodes[i][j][0]
                        grid_nodes[i][j][2]=(i+1,j-1)

    w=width(grid_nodes)
    min=10000000
    results=[]
    target=()
    y=-5
    ii=-1
    jj=-1
    i=0
    t=0
    for j in range(0,w):
#             print(j)
        if (min>grid_nodes[i][j][1]):
            min=grid_nodes[i][j][1]
            target=grid_nodes[i][j][2]
            jj=grid_nodes[i][j][2][1]
            t=t+1
            s=j
#                 print(min,"min")
    if(jj==-1):
        results.append((0,0))
        results.append(grid_nodes[0][0][2])    
#         print("case 1")
    else:
        results.append((i,s))
#         print(jj)
        if (t>1):
            results.append(grid_nodes[i][jj][2])
        else:
            results.append(grid_nodes[i][0][2])    
#     print("results",results)
    i=i+1
    j=jj
#     print("values of i and j ", i, j)
    while(grid_nodes[i][jj][2]!=-222):
        results.append(grid_nodes[i][jj][2])
        jj=grid_nodes[i][jj][2][1]
        i=i+1
#         #print(results)
        #print(grid_nodes)
    return results

def find_horizontal_path(grid):
        #print(grid)
        t=matrixTranspose(grid)
#        return_l=[()]
        t=find_vertical_path(t)
        #print("t00 is :",t[0])
        t2=[]
        x1=-1
        y2=-1
        len1=len(t)
        for i in range (0,len1):
            #print("i is :",i)
            x1=t[i][0]
            y2=t[i][1]
            t[i]=(y2,x1)
#             t[i][0]=t[i][1]
#             t[i][1]=t[i][0]
        #print(t)
        return t
        
def matrixTranspose(grid):
    w=width(grid)
    h=height(grid)
    num_row=width(grid)
    z=0
    z=h
    transposed=[[[-1,-2,-3]]*h for i in range(w)]
    h=w
    w=z
    for i in range(0,h):
        for j in range(0,w):
            transposed[i][j]=[i*num_row+j, -111,-222]
    for t in range(h):
        for tt in range(w):
            transposed[t][tt] = grid[tt][t]
    #print(transposed)
    return transposed


# def remove_vertical_path(grid,path): Given a grid and a specific path, directly modify this grid to remove each location of the path 
# from the grid. This will have the effect of reducing it from an RxC sized grid to a Rx(C-1) sized grid. Though we’ve made the change
# in place, go ahead and return a reference to the grid too.

def remove_vertical_path(grid,path):
    temp=grid
    rang_path=int(len(path))
    n_w=width(grid)-1
    n_h=height(grid)-1
    "First recognize pattern"
    t_col=[]
    t_row=[]
    for i in range (0,rang_path):
        t_col.append(int(path[i][1]))
        t_row.append(int(path[i][0]))
    "cur holds the target culumns"
    if(sum(t_col)==0):
        "Easy case targe is left edge"
#         #print("easy case!!!!")
        for i in range (0,n_h+1):
            #print("before:", grid[i])
            for j in range (0, n_w):
                #print("n_w",n_w)
                grid[i][j] = (grid[i][j+1])
            grid[i].pop()
            #print(i,j)
            #print("after :", grid[i]) 
        return grid
    else:
        #print("not simple case",t_col)
        i=0
        t_col.reverse()
        x=t_col.pop()
        r1=-1
        
        for rows in range (0,n_h+1):
            skipmethisiteration=False
            matchfound=False
            for cols in range (0,n_w):
#                 print("!!!! r:",rows,"c", cols,"x-next_target",x,"not sure:", r1,"!!!")
                if(cols==x and (r1<rows or (x==n_h-1)) and skipmethisiteration==False):
#                     print("MATCH FOUND", x)
                    #print("BEFORE:", grid[rows])
                    r1=rows;
                    grid[rows][x]=grid[rows][x+1]
                    matchfound=True;
                    if t_col:
                        x=t_col.pop()
                        skipmethisiteration=True
                elif (matchfound==False and cols==n_w-1):
                    #print("NOOOOO  MATCH FOUND")
                    if(x==n_w):
                        #print("Dont worry about it. in nxt lies it will be popped")
                        if t_col:
                            x=t_col.pop()
                elif (matchfound==True):
                    grid[rows][cols]=grid[rows][cols+1]
            r1=-1
            grid[rows].pop()
#             #print("A:", grid[rows])
#             #print("--->end of insideloop:",x )
        #print("after :", grid[i]) 
#         printgrid(grid)
    return grid;

def remove_horizontal_path(grid,path):
#     print(path)
    n_path=[]
    for i in range (0, len(path)):
        n_path.append((path[i][1],path[i][0]))       #         x=path[i][1]
#     print(n_path)    
    path=n_path
     
    grid=matrixTranspose(grid) 
    grid=remove_vertical_path(grid, path)
    grid=matrixTranspose(grid)
    return grid

def grid_to_ppm(grid,filename):
    f=open(filename,"w")
    str1="P3 "
    str1+=str(width(grid))
    str1+=" "
    str1+=str(height(grid))
    str1+=" "
    str1+=str("255 ")
#     f.write(width(grid),"\n")
    for row in range(0, height(grid)):
        for col in range (0, width(grid)):
#             print(grid[row][col][0])
            for t in range(0,3):
                str1+=str(grid[row][col][t])
                str1+=" "
#     print(str1)
    f.write(str1)
    f.close()
    return f

def ppm_to_grid(filename):
    with open(filename, 'r') as ppm:
        data = ppm.read()
        values = data.split()
        num_row = int(values[2])
        num_col = int(values[1])
        max_value = int(values[3])
#         print("----------------------------------------------------------------------------------------------------------------------------")
#         print("---------------------------------------------------------------PPM----------------------------------------------------------")
#         print("----------------------------------------------------------------------------------------------------------------------------")
#         print("num_row:", num_row,"num_col",num_col)
        offset=3;
        totat_elements_grid=num_row*num_col
    #     #print(type(data))
    #     #print(totat_elements_grid)
        totat_elements_grid=(totat_elements_grid*3)
        
        row=[]
        for j in range(0,totat_elements_grid,3):
            i=j+4
# `
            rgb=(int(values[i]), int(values[i+1]), int(values[i+2]))
#             print(rgb)
            row.append(rgb) 

        k=0
        it=0;
    #     grid = [ [(0,0,0)] * num_col ] * num_row
        grid=[[(0,0,0)]*num_col for i in range(num_row)]
        grid[0][0]=(2,2,2)
#         print(grid[0][0])
#         print("number of rows and col",num_row, num_col)
        for i in range(0,num_row):
            for j in range(0,num_col):
#                 print(i,j )
                grid[i][j]=row[k]
#                 print(grid[i][j])
                k+=1
#             print("*******************************gsize: ",len(grid[i]))
#         printgrid(grid)
    return grid
    


























# print( remove_vertical_path(g1, [(0,0),(1,0),(2,0),(3,0)]))
# g = build_grid(8,4,(1,1,1))
        # we'll consider these spots as the path,


        # so we put other values at those spots.
# for (r,c) in path:
#     g[r][c] = (9,9,9)
#############################For Testing#############################For Testing#############################For Testing#############################For Testing#############################For Testing

# 
# def printgrid(grid):
#     w=width(grid)
#     h=height(grid)
#     p=[]
#     print("_________________ 0 _____________ 1 _____________ 2 ______________ 3 ____________ 4 ___________ +")
#     for i in range (0,h):
#         for j in range (0, w):
#             p.append(grid[i][j])
#         print("| ",i,p)
#         p=[]
#     print("_________________ 0 _____________ 1 _____________ 2 ______________ 3 ____________ 4 ___________ +")    
#     print("********************")
# TEMP_FILE = ".deletable_temp_file.txt"
# def make_file(msg,filename=".deletable_temp_file.txt"):
#     f = open(filename,'w')
#     f.write(msg)
#     f.close()
# 
# 
# def build_grid(r,c,val):
#     ans = []
#     for ri in range(r):
#         row = []
#         for ci in range(c):
#             row.append(val)
#         ans.append(row)
#     return ans
# 
# 
# g1=[[(100, 75,200),(100,100,200),(100,100,200),(100,100,200),(200,125,200)],
#          [(150, 30,180),(150, 50,180),(100,120,180),(100,120,180),(100,120,180)],
#          [(100, 75,100),(100, 80,100),(100, 85,100),(100, 95,100),(100,110,100)],
#          [(200,100, 10),(200,100, 10),(200,100, 10),(210,200, 10),(255,  0, 10)]
#          ]
# 
# 
# g2= [[( 78, 209,  79), ( 63, 118, 247), ( 92, 175,  95), (243,  73, 183), (210, 109, 104), (252, 101, 119)],
#           [(224, 191, 182), (108,  89,  82), ( 80, 196, 230), (112, 156, 180), (176, 178, 120), (142, 151, 142)],
#           [(117, 189, 149), (171 ,231, 153), (149, 164, 168), (107, 119,  71), (120, 105, 138), (163, 174, 196)],
#           [(163, 222, 132), (187 ,117, 183), ( 92, 145,  69), (158, 143,  79), (220,  75, 222), (189,  73, 214)],
#           [(211, 120, 173), (188 ,218, 244), (214, 103,  68), (163, 166, 246), ( 79, 125, 246), (211, 201,  98)]
#          ]
# 
# 
# g3= [[(  0, 100, 200), (  0,  80, 200), (  0, 100, 200)],
#           [(100,  25, 200), (100,  15, 200), (100,  25, 200)],
#           [(200,  95, 255), (200, 110, 255), (200, 100, 255)],
#           [(200, 100, 255), (200,  95, 255), (200, 100, 255)],
#           [(255,  70, 200), (255, 100, 200), (255, 100, 200)]
#          ]
# 
# 
# g4= [[(255, 101, 51), (255, 101, 153), (255, 101, 255)],
#           [(255, 153, 51), (255, 153, 153), (255, 153, 255)],
#           [(255, 203, 51), (255, 204, 153), (255, 205, 255)],
#           [(255, 255, 51), (255, 255, 153), (255, 255, 255)]
#      ]
# 
# g5= [
#         [(0,0,0),(0,0,0),(10,20,30),(0,0,0),(0,0,0),(0,0,0)],
#         [(0,0,0),(2,3,4),( 1, 1, 1),(5,6,7),(0,0,0),(0,0,0)],
#         [(0,0,0),(0,0,0),(60,50,40),(0,0,0),(0,0,0),(0,0,0)],
#         [(0,0,0),(0,0,0),( 0, 0, 0),(0,0,0),(0,0,0),(0,0,0)]
#         ]
# 
# # the (1,1,1) nodes comprise the best vertical path to remove.
# g6= [
#         [(0,0,0),(0,0,0),(1,1,1),(0,0,0),(0,0,0),(0,0,0)],
#         [(0,0,0),(0,0,0),(0,0,0),(1,1,1),(0,0,0),(0,0,0)],
#         [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(1,1,1),(0,0,0)],
#         [(0,0,0),(0,0,0),(0,0,0),(1,1,1),(0,0,0),(0,0,0)]
#         ]
# 
# # the (1,1,1) nodes comprise the best horizontal path to remove.
# g7=[[(1,1,1),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)],
#         [(0,0,0),(1,1,1),(0,0,0),(1,1,1),(0,0,0),(0,0,0)],
#         [(1,1,1),(0,0,0),(1,1,1),(0,0,0),(1,1,1),(0,0,0)],
#         [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(1,1,1)]
#         ]
# # Read file an store every number from Start of file to EOF in data.list
# # get dimmensions of the ppm file
# # seize of picture
# # class grid:
# #     def __init__(self):
# #         self.width = 0
# #         self.width = 0
# 
# 
# # ef test_find_vertical_path_3(self):
# 
# # printgrid(g)
# # ans = [(0, 0), (1, 0), (2, 0), (3, 1), (4, 0)]
# # print("remove_ver_path")
# # remove_vertical_path(g, [(0,0),(1,1),(2,2),(3,1),(4,0),(5,0),(6,1),(7,2)])      
# # p3=[(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0)]
# # print("fjaskfjdsahfksaasffdsafdafdafda")
# # printgrid(p3)
# # g3 = build_grid(8,4,(1,1,1))
# # printgrid(g3)
# # for (r,c) in p3:
# #     g3[r][c] = (9,9,9)
# # printgrid(g3)
# # printgrid(remove_vertical_path(g3, [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0)]))
# 
# 
# 
# # print("*********g2************")
# # p2=[(0,0),(1,1),(2,2),(3,1),(4,0),(5,0),(6,1),(7,2)]    
# # g2 = build_grid(8,4,(1,1,1))
# # for (r,c) in p2:
# #             g2[r][c] = (9,9,9)
# # printgrid(g2)
# # path4 = [(0,2),(1,1),(2,2),(3,3),(4,3),(5,2),(6,1),(7,2)]
# # g4 = build_grid(8,4,(1,1,1))
# # printgrid(remove_vertical_path(g2, p2))
# #         # we'll consider these spots as the path: wandering around
# #         # so we put other values at those spots.
# # for (r,c) in path4:
# #     g4[r][c] = (9,9,9)
# # print("!!!!!!!!!!!4")
# # printgrid(g4)
# # print("---------------------------------------")
# # printgrid(remove_vertical_path(g4, path4))
# # 
# # p3=[(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0)]
# # print("***************g3")
# # g3 = build_grid(8,4,(1,1,1))
# # for (r,c) in p3:
# #     g3[r][c] = (9,9,9)
# # printgrid(g3)
# # printgrid(remove_vertical_path(g3, [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0)]))
# # ##Test5
# # g1=[[(100, 75,200),(100,100,200),(100,100,200),(100,100,200),(200,125,200)],
# #          [(150, 30,180),(150, 50,180),(100,120,180),(100,120,180),(100,120,180)],
# #          [(100, 75,100),(100, 80,100),(100, 85,100),(100, 95,100),(100,110,100)],
# #          [(200,100, 10),(200,100, 10),(200,100, 10),(210,200, 10),(255,  0, 10)]
# #          ]
# # 
# # print("----------------------------------------")
# # print("g1 vertical path:",find_vertical_path(g1))
# # printgrid(g1)
# # got = remove_vertical_path(g1,find_vertical_path(g1))
# # expected = [[(100, 75, 200), (100, 100, 200), (100, 100, 200), (200, 125, 200)], [(150, 50, 180), (100, 120, 180), (100, 120, 180), (100, 120, 180)], [(100, 75, 100), (100, 85, 100), (100, 95, 100), (100, 110, 100)], [(200, 100, 10), (200, 100, 10), (210, 200, 10), (255, 0, 10)]]
# # printgrid(got)
# # printgrid(expected)
# # 
# # if(expected==got):
# #     print("test 5 passed!")
# # else:
# #     print("fail")
# 
# 
# def test_remove_vertical_path_6(x):
#     g2= [[( 78, 209,  79), ( 63, 118, 247), ( 92, 175,  95), (243,  73, 183), (210, 109, 104), (252, 101, 119)],
#           [(224, 191, 182), (108,  89,  82), ( 80, 196, 230), (112, 156, 180), (176, 178, 120), (142, 151, 142)],
#           [(117, 189, 149), (171 ,231, 153), (149, 164, 168), (107, 119,  71), (120, 105, 138), (163, 174, 196)],
#           [(163, 222, 132), (187 ,117, 183), ( 92, 145,  69), (158, 143,  79), (220,  75, 222), (189,  73, 214)],
#           [(211, 120, 173), (188 ,218, 244), (214, 103,  68), (163, 166, 246), ( 79, 125, 246), (211, 201,  98)]
#          ]
#     
#     
#     g = g2
#     printgrid(g2)
#     got = remove_vertical_path(g,find_vertical_path(g))
#    
#     expected = [[(78, 209, 79), (63, 118, 247), (92, 175, 95), (210, 109, 104), (252, 101, 119)], [(224, 191, 182), (108, 89, 82), (80, 196, 230), (112, 156, 180), (142, 151, 142)], [(117, 189, 149), (171, 231, 153), (149, 164, 168), (120, 105, 138), (163, 174, 196)], [(163, 222, 132), (187, 117, 183), (158, 143, 79), (220, 75, 222), (189, 73, 214)], [(211, 120, 173), (188, 218, 244), (163, 166, 246), (79, 125, 246), (211, 201, 98)]]
#     if(got==expected):
#         print("test 6 passed!")
#     else:
#          print("fail")
#          
# def test_remove_vertical_path_7(self):
#         g3= [[(  0, 100, 200), (  0,  80, 200), (  0, 100, 200)],
#           [(100,  25, 200), (100,  15, 200), (100,  25, 200)],
#           [(200,  95, 255), (200, 110, 255), (200, 100, 255)],
#           [(200, 100, 255), (200,  95, 255), (200, 100, 255)],
#           [(255,  70, 200), (255, 100, 200), (255, 100, 200)]
#          ]
#         g4= [[(255, 101, 51), (255, 101, 153), (255, 101, 255)],
#           [(255, 153, 51), (255, 153, 153), (255, 153, 255)],
#           [(255, 203, 51), (255, 204, 153), (255, 205, 255)],
#           [(255, 255, 51), (255, 255, 153), (255, 255, 255)]
#      ]
#     
#         g = g3
#         got = remove_vertical_path(g,find_vertical_path(g))
#         expected = [[(0, 80, 200), (0, 100, 200)], [(100, 15, 200), (100, 25, 200)], [(200, 110, 255), (200, 100, 255)], [(200, 100, 255), (200, 100, 255)], [(255, 100, 200), (255, 100, 200)]]
# #         self.assertEquals(expected, got)
#         if(got==expected):
#             print("test 7 passed!")
#         else:
#             print("fail")         
#          
# def test_remove_vertical_path_8(self):
#     g4= [[(255, 101, 51), (255, 101, 153), (255, 101, 255)],
#           [(255, 153, 51), (255, 153, 153), (255, 153, 255)],
#           [(255, 203, 51), (255, 204, 153), (255, 205, 255)],
#           [(255, 255, 51), (255, 255, 153), (255, 255, 255)]
#      ]
#     g = g4
#     got = remove_vertical_path(g,find_vertical_path(g))
#     expected = [[(255, 101, 153), (255, 101, 255)], [(255, 153, 153), (255, 153, 255)], [(255, 204, 153), (255, 205, 255)], [(255, 255, 153), (255, 255, 255)]]
#     if(got==expected):
#         print("test 8 passed!")
#     else:
#          print("fail")
# 
# test_remove_vertical_path_8(4)
# # test_remove_vertical_path_6(4)
# # test_remove_vertical_path_7(4)
# def test_remove_horizontal_path_1(self):
#         # an 8x4 grid of (1,1,1)'s.
#         g = build_grid(4,7,(1,1,1))
#         # we'll consider these spots as the path: top line
#         path = [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6)]
#         # so we put other values at those spots.
#         for (r,c) in path:
#             g[r][c] = (9,9,9)
#         # let's remove all the 9's
#         printgrid(g)
#         g = remove_horizontal_path(g,path)
#         # and then we expect a narrower grid.
#         expected = build_grid(3,7,(1,1,1))
#         printgrid(expected)
#         printgrid(g)
#         if(expected==g):
#             print("test 1 passed!")
#         else:
#             print("fail")
#         
#     
#     # remove a manually created path (not the "best" path).
# def test_remove_horizontal_path_2(self):
#     # an 8x4 grid of (1,1,1)'s.
#     g = build_grid(4,7,(1,1,1))
#     # we'll consider these spots as the path: bottom line
#     path = [(3,0),(3,1),(3,2),(3,3),(3,4),(3,5),(3,6)]
#     # so we put other values at those spots.
#     for (r,c) in path:
#         g[r][c] = (9,9,9)
#     # let's remove all the 9's
#     g = remove_horizontal_path(g,path)
#     # and then we expect a narrower grid.
#     expected = build_grid(3,7,(1,1,1))
#     if(expected==g):
#         print("test 2 passed!")
#     else:
#         print("fail2")
# 
# # remove a manually created path (not the "best" path).
# def test_remove_horizontal_path_3(self):
#     # an 8x4 grid of (1,1,1)'s.
#     g = build_grid(4,7,(1,1,1))
#     # we'll consider these spots as the path: toggling rows
#     path = [(0,0),(1,1),(0,2),(1,3),(1,4),(0,5),(1,6)]
#     # so we put other values at those spots.
#     for (r,c) in path:
#         g[r][c] = (9,9,9)
#     # let's remove all the 9's
#     g = remove_horizontal_path(g,path)
#     # and then we expect a narrower grid.
#     expected = build_grid(3,7,(1,1,1))
#     if(expected==g):
#         print("test 3 passed!")
#     else:
#         print("fail3")
# 
# # remove a manually created path (not the "best" path).
# def test_remove_horizontal_path_4(self):
#     # an 8x4 grid of (1,1,1)'s.
#     g = build_grid(4,7,(1,1,1))
#     # we'll consider these spots as the path: toggling interior
#     path = [(1,0),(2,1),(1,2),(2,3),(1,4),(2,5),(1,6)]
#     # so we put other values at those spots.
#     for (r,c) in path:
#         g[r][c] = (9,9,9)
#     # let's remove all the 9's
#     g = remove_horizontal_path(g,path)
#     # and then we expect a narrower grid.
#     expected = build_grid(3,7,(1,1,1))
#     if(expected==g):
#         print("test 4 passed!")
#     else:
#         print("fail4")
# 
# # remove a manually created path (not the "best" path).
# def test_remove_horizontal_path_5(self):
#     # an 8x4 grid of (1,1,1)'s.
#     g = build_grid(7,7,(1,1,1))
#     # we'll consider these spots as the path: all in unique rows
#     path = [(0,0),(1,1),(2,2),(3,3),(4,4),(5,5),(6,6)]
#     # so we put other values at those spots.
#     for (r,c) in path:
#         g[r][c] = (9,9,9)
#     # let's remove all the 9's
#     printgrid(g)
#     g = remove_horizontal_path(g,path)
#     # and then we expect a narrower grid.
#     expected = build_grid(6,7,(1,1,1))
#     
#     if(expected==g):
#         print("test 5 passed!")
#     else:
#         print("fail5")
#         
#         printgrid(expected)
#         printgrid(g)
# 
# # test our given grids
# def test_remove_horizontal_path_6(self):
#     g = g1()
#     got = remove_horizontal_path(g,find_horizontal_path(g))
#     expected = [[(100, 75, 200), (100, 100, 200), (100, 100, 200), (100, 100, 200), (200, 125, 200)], [(100, 75, 100), (100, 80, 100), (100, 85, 100), (100, 95, 100), (100, 110, 100)], [(200, 100, 10), (200, 100, 10), (200, 100, 10), (210, 200, 10), (255, 0, 10)]]
#     self.assertEquals(expected, got)
# 
# # test our given grids
# def test_remove_horizontal_path_7(self):
#     g = g2()
#     got = remove_horizontal_path(g,find_horizontal_path(g))
#     expected = [[(78, 209, 79), (63, 118, 247), (92, 175, 95), (243, 73, 183), (210, 109, 104), (252, 101, 119)], [(224, 191, 182), (108, 89, 82), (149, 164, 168), (112, 156, 180), (120, 105, 138), (142, 151, 142)], [(163, 222, 132), (187, 117, 183), (92, 145, 69), (158, 143, 79), (220, 75, 222), (189, 73, 214)], [(211, 120, 173), (188, 218, 244), (214, 103, 68), (163, 166, 246), (79, 125, 246), (211, 201, 98)]]
#     self.assertEquals(expected, got)
# 
# # test our given grids
# def test_remove_horizontal_path_8(self):
#     g = g3()
#     got = remove_horizontal_path(g,find_horizontal_path(g))
#     expected = [[(0, 100, 200), (0, 80, 200), (0, 100, 200)], [(100, 25, 200), (100, 15, 200), (100, 25, 200)], [(200, 95, 255), (200, 110, 255), (200, 100, 255)], [(255, 70, 200), (255, 100, 200), (255, 100, 200)]]
#     self.assertEquals(expected, got)
# 
# # test our given grids
# def test_remove_horizontal_path_9(self):
#     g = g4()
#     got = remove_horizontal_path(g,find_horizontal_path(g))
#     expected = [[(255, 153, 51), (255, 153, 153), (255, 153, 255)], [(255, 203, 51), (255, 204, 153), (255, 205, 255)], [(255, 255, 51), (255, 255, 153), (255, 255, 255)]]
#     self.assertEquals(expected, got)
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# #     def test_find_vertical_path_4(self):
# 
# # test_remove_horizontal_path_1(1)
# # test_remove_horizontal_path_2(2)
# # test_remove_horizontal_path_3(3)
# # test_remove_horizontal_path_4(4)
# # test_remove_horizontal_path_5(4)
# def from_file(filename):
#     f = open (filename)
#     s = f.read()
#     f.close()
#     return s
# 
# 
#     
# #---------------------------------------------------------------------
# 
# # def test_ppm_to_grid_1(self):
# #     # we want to have an existing ppm file, and read it to a grid,
# #     # lastly checking that the grid we got matches what is expected.
# #     
# #     filename = ".temp_file.ppm"
# #     expected = g1()
# #     
# #     # put a ppm file's contents into a string. 
# #     s = "P3\n5\n4\n255\n100\n75\n200\n100\n100\n200\n100\n100\n200\n100\n100\n200\n200\n125\n200\n150\n30\n180\n150\n50\n180\n100\n120\n180\n100\n120\n180\n100\n120\n180\n100\n75\n100\n100\n80\n100\n100\n85\n100\n100\n95\n100\n100\n110\n100\n200\n100\n10\n200\n100\n10\n200\n100\n10\n210\n200\n10\n255\n0\n10\n"
# #     
# #     # put that string into a file.
# #     make_file(s,filename)
# #     
# #     # call student's code.
# #     got = ppm_to_grid(filename)
# #     
# #     # check that they read it successfully
# #     self.assertEquals(expected, got)
# #     
# # def test_ppm_to_grid_2(self):
# #     # we want to have an existing ppm file, and read it to a grid,
# #     # lastly checking that the grid we got matches what is expected.
# #     
# #     filename = ".temp_file.ppm"
# #     expected = g2()
# #     
# #     # put a ppm file's contents into a string. 
# #     s = "P3\n6\n5\n255\n78\n209\n79\n63\n118\n247\n92\n175\n95\n243\n73\n183\n210\n109\n104\n252\n101\n119\n224\n191\n182\n108\n89\n82\n80\n196\n230\n112\n156\n180\n176\n178\n120\n142\n151\n142\n117\n189\n149\n171\n231\n153\n149\n164\n168\n107\n119\n71\n120\n105\n138\n163\n174\n196\n163\n222\n132\n187\n117\n183\n92\n145\n69\n158\n143\n79\n220\n75\n222\n189\n73\n214\n211\n120\n173\n188\n218\n244\n214\n103\n68\n163\n166\n246\n79\n125\n246\n211\n201\n98\n"
# #     
# #     # put that string into a file.
# #     make_file(s,filename)
# #     
# #     # call student's code.
# #     got = ppm_to_grid(filename)
# #     
# #     # check that they read it successfully
# #     self.assertEquals(expected, got)
# #     
# # def test_ppm_to_grid_3(self):
# #     # we want to have an existing ppm file, and read it to a grid,
# #     # lastly checking that the grid we got matches what is expected.
# #     
# #     filename = ".temp_file.ppm"
# #     expected = g3()
# #     
# #     # put a ppm file's contents into a string. 
# #     s = "P3\n3\n5\n255\n0\n100\n200\n0\n80\n200\n0\n100\n200\n100\n25\n200\n100\n15\n200\n100\n25\n200\n200\n95\n255\n200\n110\n255\n200\n100\n255\n200\n100\n255\n200\n95\n255\n200\n100\n255\n255\n70\n200\n255\n100\n200\n255\n100\n200\n"
# #     
# #     # put that string into a file.
# #     make_file(s,filename)
# #     
# #     # call student's code.
# #     got = ppm_to_grid(filename)
# #     
# #     # check that they read it successfully
# #     self.assertEquals(expected, got)
# #     
# # def test_ppm_to_grid_4(self):
# #     # we want to have an existing ppm file, and read it to a grid,
# #     # lastly checking that the grid we got matches what is expected.
# #     
# #     filename = ".temp_file.ppm"
# #     expected = g4()
# #     
# #     # put a ppm file's contents into a string. 
# #     s = "P3\n3\n4\n255\n255\n101\n51\n255\n101\n153\n255\n101\n255\n255\n153\n51\n255\n153\n153\n255\n153\n255\n255\n203\n51\n255\n204\n153\n255\n205\n255\n255\n255\n51\n255\n255\n153\n255\n255\n255\n"
# #     
# #     # put that string into a file.
# #     make_file(s,filename)
# #     
# #     # call student's code.
# #     got = ppm_to_grid(filename)
# #     
# #     # check that they read it successfully
# #     self.assertEquals(expected, got)
# # 
# # #---------------------------------------------------------------------
# #     
# # 
# # # printgrid(ppm_to_grid("samp1.ppm"))
# 
# 
# def g1():
#     return [
#          [(100, 75,200),(100,100,200),(100,100,200),(100,100,200),(200,125,200)],
#          [(150, 30,180),(150, 50,180),(100,120,180),(100,120,180),(100,120,180)],
#          [(100, 75,100),(100, 80,100),(100, 85,100),(100, 95,100),(100,110,100)],
#          [(200,100, 10),(200,100, 10),(200,100, 10),(210,200, 10),(255,  0, 10)]
#          ]
# def g2():
#     return [[( 78, 209,  79), ( 63, 118, 247), ( 92, 175,  95), (243,  73, 183), (210, 109, 104), (252, 101, 119)],
#           [(224, 191, 182), (108,  89,  82), ( 80, 196, 230), (112, 156, 180), (176, 178, 120), (142, 151, 142)],
#           [(117, 189, 149), (171 ,231, 153), (149, 164, 168), (107, 119,  71), (120, 105, 138), (163, 174, 196)],
#           [(163, 222, 132), (187 ,117, 183), ( 92, 145,  69), (158, 143,  79), (220,  75, 222), (189,  73, 214)],
#           [(211, 120, 173), (188 ,218, 244), (214, 103,  68), (163, 166, 246), ( 79, 125, 246), (211, 201,  98)]
#          ]
# 
# def g3():
#     return [[(  0, 100, 200), (  0,  80, 200), (  0, 100, 200)],
#           [(100,  25, 200), (100,  15, 200), (100,  25, 200)],
#           [(200,  95, 255), (200, 110, 255), (200, 100, 255)],
#           [(200, 100, 255), (200,  95, 255), (200, 100, 255)],
#           [(255,  70, 200), (255, 100, 200), (255, 100, 200)]
#          ]
# 
# 
# def g4():
#     return [[(255, 101, 51), (255, 101, 153), (255, 101, 255)],
#           [(255, 153, 51), (255, 153, 153), (255, 153, 255)],
#           [(255, 203, 51), (255, 204, 153), (255, 205, 255)],
#           [(255, 255, 51), (255, 255, 153), (255, 255, 255)]
#      ]
# 
# # position (1,2) is interesting I guess.
# def g5():
#     return [
#         [(0,0,0),(0,0,0),(10,20,30),(0,0,0),(0,0,0),(0,0,0)],
#         [(0,0,0),(2,3,4),( 1, 1, 1),(5,6,7),(0,0,0),(0,0,0)],
#         [(0,0,0),(0,0,0),(60,50,40),(0,0,0),(0,0,0),(0,0,0)],
#         [(0,0,0),(0,0,0),( 0, 0, 0),(0,0,0),(0,0,0),(0,0,0)]
#         ]
# 
# # the (1,1,1) nodes comprise the best vertical path to remove.
# def g6():
#     return [
#         [(0,0,0),(0,0,0),(1,1,1),(0,0,0),(0,0,0),(0,0,0)],
#         [(0,0,0),(0,0,0),(0,0,0),(1,1,1),(0,0,0),(0,0,0)],
#         [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(1,1,1),(0,0,0)],
#         [(0,0,0),(0,0,0),(0,0,0),(1,1,1),(0,0,0),(0,0,0)]
#         ]
# 
# # the (1,1,1) nodes comprise the best horizontal path to remove.
# def g7():
#     return [
#         [(1,1,1),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)],
#         [(0,0,0),(1,1,1),(0,0,0),(1,1,1),(0,0,0),(0,0,0)],
#         [(1,1,1),(0,0,0),(1,1,1),(0,0,0),(1,1,1),(0,0,0)],
#         [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(1,1,1)]
#         ]
# 
# 
# 
# 
# 
# 
# # test_grid_to_ppm_1(1)
# def test_ppm_to_grid_1(self):
#         # we want to have an existing ppm file, and read it to a grid,
#         # lastly checking that the grid we got matches what is expected.
#         
#         filename = ".temp_file.ppm"
#         expected = g1()
#         
#         # put a ppm file's contents into a string. 
#         s = "P3\n5\n4\n255\n100\n75\n200\n100\n100\n200\n100\n100\n200\n100\n100\n200\n200\n125\n200\n150\n30\n180\n150\n50\n180\n100\n120\n180\n100\n120\n180\n100\n120\n180\n100\n75\n100\n100\n80\n100\n100\n85\n100\n100\n95\n100\n100\n110\n100\n200\n100\n10\n200\n100\n10\n200\n100\n10\n210\n200\n10\n255\n0\n10\n"
#         
#         # put that string into a file.
#         make_file(s,filename)
#         
#         # call student's code.
#         got = ppm_to_grid(filename)
#         
#         # check that they read it successfully
#         if(expected==got):
#             print("test 1 passed!")
#         else:
#             print("fail test 1 ppm2Grid")
#             printgrid(expected)
#             print("what I got")
#             printgrid(got)
# 
# 
# # test_ppm_to_grid_1(1)
# # ppm_to_grid("samp1.ppm")
# 
# 
# def grid_to_ppm(grid,filename):
#     f=open(filename,"w")
#     str1="P3 "
#     str1+=str(width(grid))
#     str1+=" "
#     str1+=str(height(grid))
#     str1+=" "
#     str1+=str("255 ")
# #     f.write(width(grid),"\n")
#     for row in range(0, height(grid)):
#         for col in range (0, width(grid)):
# #             print(grid[row][col][0])
#             for t in range(0,3):
#                 str1+=str(grid[row][col][t])
#                 str1+=" "
#     print(str1)
#     f.write(str1)
#     f.close()
#     return f
# 
# def test_grid_to_ppm_1(self):
#     filename = ".temp_file.ppm"
#     ppm = grid_to_ppm(g1(),filename)
#     s = from_file(filename)
#     tokens = s.split()
#     expected = ['P3', '5', '4', '255', '100', '75', '200', '100', '100', '200', '100', '100', '200', '100', '100', '200', '200', '125', '200', '150', '30', '180', '150', '50', '180', '100', '120', '180', '100', '120', '180', '100', '120', '180', '100', '75', '100', '100', '80', '100', '100', '85', '100', '100', '95', '100', '100', '110', '100', '200', '100', '10', '200', '100', '10', '200', '100', '10', '210', '200', '10', '255', '0', '10']
#     if(expected==tokens):
#         print("test 1 passed!")
#     else:
#         print("fail1")
#         printgrid(expected)
#         printgrid(tokens)
#      
#     
# def test_grid_to_ppm_2(self):
#     filename = ".temp_file.ppm"
#     ppm = grid_to_ppm(g2(),filename)
#     s = from_file(filename)
#     tokens = s.split()
#     expected = ['P3', '6', '5', '255', '78', '209', '79', '63', '118', '247', '92', '175', '95', '243', '73', '183', '210', '109', '104', '252', '101', '119', '224', '191', '182', '108', '89', '82', '80', '196', '230', '112', '156', '180', '176', '178', '120', '142', '151', '142', '117', '189', '149', '171', '231', '153', '149', '164', '168', '107', '119', '71', '120', '105', '138', '163', '174', '196', '163', '222', '132', '187', '117', '183', '92', '145', '69', '158', '143', '79', '220', '75', '222', '189', '73', '214', '211', '120', '173', '188', '218', '244', '214', '103', '68', '163', '166', '246', '79', '125', '246', '211', '201', '98']
#     self.assertEquals(expected, tokens)
#     
# def test_grid_to_ppm_3(self):
#     filename = ".temp_file.ppm"
#     ppm = grid_to_ppm(g3(),filename)
#     s = from_file(filename)
#     tokens = s.split()
#     expected = ['P3', '3', '5', '255', '0', '100', '200', '0', '80', '200', '0', '100', '200', '100', '25', '200', '100', '15', '200', '100', '25', '200', '200', '95', '255', '200', '110', '255', '200', '100', '255', '200', '100', '255', '200', '95', '255', '200', '100', '255', '255', '70', '200', '255', '100', '200', '255', '100', '200']
#     self.assertEquals(expected, tokens)
#     
# def test_grid_to_ppm_4(self):
#     filename = ".temp_file.ppm"
#     ppm = grid_to_ppm(g4(),filename)
#     s = from_file(filename)
#     tokens = s.split()
#     expected = ['P3', '3', '4', '255', '255', '101', '51', '255', '101', '153', '255', '101', '255', '255', '153', '51', '255', '153', '153', '255', '153', '255', '255', '203', '51', '255', '204', '153', '255', '205', '255', '255', '255', '51', '255', '255', '153', '255', '255', '255']
#     self.assertEquals(expected, tokens)
# 
# test_grid_to_ppm_1(1)
# 
# 
# 
# 
# 
# 
# 
# # def test_grid_to_ppm_1(self):
# #         filename = ".temp_file.ppm"
# #         ppm = grid_to_ppm(g1(),filename)
# #         s = from_file(filename)
# #         tokens = s.split()
# #         expected = ['P3', '5', '4', '255', '100', '75', '200', '100', '100', '200', '100', '100', '200', '100', '100', '200', '200', '125', '200', '150', '30', '180', '150', '50', '180', '100', '120', '180', '100', '120', '180', '100', '120', '180', '100', '75', '100', '100', '80', '100', '100', '85', '100', '100', '95', '100', '100', '110', '100', '200', '100', '10', '200', '100', '10', '200', '100', '10', '210', '200', '10', '255', '0', '10']
# #         self.assertEquals(expected, tokens)
# 
# 
#     
# def test_ppm_to_grid_2(self):
#     # we want to have an existing ppm file, and read it to a grid,
#     # lastly checking that the grid we got matches what is expected.
#     
#     filename = ".temp_file.ppm"
#     expected = g2()
#     
#     # put a ppm file's contents into a string. 
#     s = "P3\n6\n5\n255\n78\n209\n79\n63\n118\n247\n92\n175\n95\n243\n73\n183\n210\n109\n104\n252\n101\n119\n224\n191\n182\n108\n89\n82\n80\n196\n230\n112\n156\n180\n176\n178\n120\n142\n151\n142\n117\n189\n149\n171\n231\n153\n149\n164\n168\n107\n119\n71\n120\n105\n138\n163\n174\n196\n163\n222\n132\n187\n117\n183\n92\n145\n69\n158\n143\n79\n220\n75\n222\n189\n73\n214\n211\n120\n173\n188\n218\n244\n214\n103\n68\n163\n166\n246\n79\n125\n246\n211\n201\n98\n"
#     
#     # put that string into a file.
#     make_file(s,filename)
#     
#     # call student's code.
#     got = ppm_to_grid(filename)
#     
#     # check that they read it successfully
#     self.assertEquals(expected, got)
#     
# def test_ppm_to_grid_3(self):
#     # we want to have an existing ppm file, and read it to a grid,
#     # lastly checking that the grid we got matches what is expected.
#     
#     filename = ".temp_file.ppm"
#     expected = g3()
#     
#     # put a ppm file's contents into a string. 
#     s = "P3\n3\n5\n255\n0\n100\n200\n0\n80\n200\n0\n100\n200\n100\n25\n200\n100\n15\n200\n100\n25\n200\n200\n95\n255\n200\n110\n255\n200\n100\n255\n200\n100\n255\n200\n95\n255\n200\n100\n255\n255\n70\n200\n255\n100\n200\n255\n100\n200\n"
#     
#     # put that string into a file.
#     make_file(s,filename)
#     
#     # call student's code.
#     got = ppm_to_grid(filename)
#     
#     # check that they read it successfully
#     self.assertEquals(expected, got)
#     
# def test_ppm_to_grid_4(self):
#     # we want to have an existing ppm file, and read it to a grid,
#     # lastly checking that the grid we got matches what is expected.
#     
#     filename = ".temp_file.ppm"
#     expected = g4()
#     
#     # put a ppm file's contents into a string. 
#     s = "P3\n3\n4\n255\n255\n101\n51\n255\n101\n153\n255\n101\n255\n255\n153\n51\n255\n153\n153\n255\n153\n255\n255\n203\n51\n255\n204\n153\n255\n205\n255\n255\n255\n51\n255\n255\n153\n255\n255\n255\n"
#     
#     # put that string into a file.
#     make_file(s,filename)
#     
#     # call student's code.
#     got = ppm_to_grid(filename)
#     
#     # check that they read it successfully
#     self.assertEquals(expected, got)
#     
#     #----------------------------------------------------------
# 
# # s="P3\n5\n4\n255\n100\n75\n200\n100\n100\n200\n100\n100\n200\n100\n100\n200\n200\n125\n200\n150\n30\n180\n150\n50\n180\n100\n120\n180\n100\n120\n180\n100\n120\n180\n100\n75\n100\n100\n80\n100\n100\n85\n100\n100\n95\n100\n100\n110\n100\n200\n100\n10\n200\n100\n10\n200\n100\n10\n210\n200\n10\n255\n0\n10\n"
# # 
# # print(s)


