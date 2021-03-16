#!/usr/bin/env python
#!coding: utf-8

import sys, os, re, shutil
from optparse import OptionParser

def list_changed_path(ws, rev):
    if not re.search(":", rev):
        rev = str(int(rev)-1) + ":" + rev
        # rev += ":HEAD"
    pwd = os.getcwd()
    try:
        os.chdir(ws)
        rev_to = rev.split(':')[1]

        # svn updateを発行
        print ('svn update -r%s ....' % rev_to)
        os.popen('svn update -r%s .' % rev_to)

        print ('svn diff -r%s --summarize ....' % rev)
        svnfd = os.popen('svn diff -r%s --summarize .' % rev)

        overwrite = []

        for line in svnfd:
            mo = re.match(r'^\s*([AMD])\s*(.*)$', line.strip())
            if mo:
                print (line.strip())
                if mo.group(1) in ['A', 'M']:
                    overwrite.append(mo.group(2).strip(" \n"))
        svnfd.close()
    finally:
        os.chdir(pwd)
        
    overwrite.sort()
    return overwrite

def yes_no_input():
    while True:
        choice = input("処理を続行しますか？ [Y/N]: ").lower()
        if choice in ['y']:
            return True
        elif choice in ['n']:
            return False

if __name__ == '__main__':
    parser = OptionParser(usage="%prog <workspace> <rev>[:<rev>] <target>")
    (options, args) = parser.parse_args()
    if len(args) != 3:
        parser.error("引数が3つではありません。 svncheckoutdir rev[:rev] outpudir")

    # if not yes_no_input():
    #     sys.exit()

    ws,rev,target = args
    
    # clean target dir
    if os.path.exists(target):
        for root, dirs, files in os.walk(target, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
    else:
        os.makedirs(target)
    
    # parse svn diff summary
    overwrite = list_changed_path(ws, rev)
    
    # copy added/modified files
    for p in overwrite:
        s = os.path.join(ws, p)
        d = os.path.join(target, p)
        if os.path.isfile(s):
            if not os.path.exists(os.path.dirname(d)):
                os.makedirs(os.path.dirname(d))
            shutil.copy2(s, d)
        elif os.path.isdir(s):
            if not os.path.exists(d):
                os.makedirs(d)

    # input("Enterキーを押すと終了します")