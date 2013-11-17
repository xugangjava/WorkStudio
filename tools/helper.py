#coding=gbk
import os,uuid


def Guid():
    return str(uuid.uuid4()).replace('-', '')


def FileExt(filename):
    return os.path.splitext(filename)[-1].lower()


def GuidFileName(filename):
    return Guid() + FileExt(filename)