import numpy as ny
from dac_read import *

def readRamens2d(direction,file):

	# direction='./dac_s/'
	# file='qq.0???.*.dac'
	filename=direction+file
	data,x,y,z=dac_read4d(filename)

	varDictionary={}
	varDictionary.update({"ro":data[:,0,:,0,:]})
	varDictionary.update({"ei":data[:,1,:,0,:]})
	varDictionary.update({"vx":data[:,2,:,0,:]})
	varDictionary.update({"vy":data[:,3,:,0,:]})
	varDictionary.update({"vz":data[:,4,:,0,:]})
	varDictionary.update({"bx":data[:,5,:,0,:]})
	varDictionary.update({"by":data[:,6,:,0,:]})
	varDictionary.update({"bz":data[:,7,:,0,:]})
	varDictionary.update({"psi":data[:,8,:,0,:]})
	varDictionary.update({"pr":data[:,9,:,0,:]})
	varDictionary.update({"te":data[:,10,:,0,:]})

	vx=data[:,2,:,0,:]
	vy=data[:,3,:,0,:]
	vz=data[:,4,:,0,:]
	bx=data[:,5,:,0,:]
	by=data[:,6,:,0,:]
	bz=data[:,7,:,0,:]
	ex,ey,ez,sx,sy,sz=efields(vx,vy,vz,bx,by,bz)

	varDictionary.update({"ex":ex})
	varDictionary.update({"ey":ey})
	varDictionary.update({"ez":ez})
	varDictionary.update({"sx":sx})
	varDictionary.update({"sy":sy})
	varDictionary.update({"sz":sz})

	return x,y,z,varDictionary


def efields(vx,vy,vz,bx,by,bz):
	ex=-vy*bz+vz*by
	ey=-vz*bx+vx*bz
	ez=-vx*by+vy*bx

	sx=ey*bz-ez*by
	sy=ez*bx-ex*bz
	sz=ex*by-ey*bx

	return (ex,ey,ez,sx,sy,sz)