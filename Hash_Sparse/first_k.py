import scipy as sp  
import scipy.sparse.linalg  
import scipy.io as sio   
import numpy as np  
import time  
import os  

def generateTestMat(size):  
        '''''generate a test matrix for k-eigenvalues problem 
        '  matlab and scipy.sparse.linalg.eigs seem use the same package ARPACK 
        '  this matrix has two diagnol lines, one is on the diagnol and the other is off 1 
        '''  
        A = sp.sparse.lil_matrix((size, size))  
        A[0,:size]=np.random.rand(size)  
        A.setdiag(np.random.rand(size))  
        A.setdiag(np.random.rand(size-1),1)  
        sio.savemat("A.mat",{"A":A},oned_as='row')  
        print("generate a test matrix,with size %s by %s" %(size,size))  
  
def calculateKEigs(tolerance=0):  
        if(os.path.exists(os.getcwd()+"/"+"A.mat")==False):  
                generateTestMat()  
        A=sio.loadmat("A.mat")["A"]  
        timeCheckin=time.clock()  
        vals, vecs = sp.sparse.linalg.eigs(A, k=3,tol=tolerance,which="SM")  
        print("first 3 eigenvalues cost %s seconds" % (time.clock()-timeCheckin))  
        print("first 3 eigenvalues are %s" % vals)  
        k=len(vals)  
        nRow,nCol=A.get_shape()  
        for i in range(0,k):  
                print("error of lamda is %s " % (np.linalg.norm(A.dot(vecs[:,i])-vals[i]*vecs[:,i])))  
        for i in range(0,k):  
                v=np.random.rand(nCol)  
                #v must be normalization  
                v=v/np.linalg.norm(v)  
                print("random error is %s " % (np.linalg.norm(A.dot(v)-vals[i]*v)))  
  
generateTestMat(1000)  
calculateKEigs(tolerance=0.001) 
