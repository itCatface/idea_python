#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Copyright (C) 2016 Spreadtrum
Created on Jan 18, 2016
2016.03.11 -- add ytag parser
'''

YTAG = 0
YTAG_MAGIC = 0xf00e789a
YTAG_VERSION = 0x00000001
YTAG_TAG_PROPERTY = 0x05
YTAG_TAG_NEWFILE_BEGIN = 0x10
YTAG_TAG_NEWFILE_END = 0x11
YTAG_TAG_RAWDATA = 0x12
YTAG_STRUCT_SIZE = 0x08
ytag_folder = 'ytag'
merged = 'android.log'
logpath = ''
id_token_len = 1
logdict = {'M': 'main.log', 'S': 'system.log', 'R': 'radio.log', 'E': 'events.log', 'C': 'crash.log', }

# ylog tool script
from ctypes import *
import sys
import zlib
import os
import traceback
import os
import re
import sys
import optparse
import shutil
import struct


class FileHeader(Structure):
    _fields_ = [('m', c_int), ('r', c_char * 64), ('v', c_int), ('re', c_char * 24), ]


class BlockHeader(Structure):
    _fields_ = [('m', c_int), ('seq', c_uint), ('l', c_int)]


class FileTail(Structure):
    _fields_ = [('m', c_int), ('seq', c_uint), ('l', c_int), ('v', c_int), ('r', c_char * 64), ('re', c_char * 24), ]


debugmode = False


def unzipit(yzip):
    global debugmode
    try:
        logfile = yzip + ".log"
        if not os.path.isfile(yzip):
            return
        g = open(logfile, "wb")
        z = zlib.decompressobj()
        with open(yzip, 'rb') as file:
            result = []
            x = FileHeader()
            while file.readinto(x) == sizeof(x):
                if x.m != 0x2E2E:
                    if debugmode:
                        print('format error')
                    pass
                else:
                    pass
                break;
            block = BlockHeader()
            bc = 1
            offset = 0;
            bsize = sizeof(BlockHeader)
            rbsize = file.readinto(block)
            got_file_tail = False
            while rbsize == bsize:
                bc = bc + 1
                if block.m != 0x5A5A:
                    if block.m == 0xB5B5:
                        if debugmode:
                            print('get Tail')
                        got_file_tail = True
                        file.read(sizeof(FileTail) - sizeof(BlockHeader))
                    else:
                        if block.m == 0x2E2E:
                            if debugmode:
                                print('get Head')
                            file.read(sizeof(FileHeader) - sizeof(BlockHeader))
                        else:
                            if debugmode:
                                print('\nblock format error')
                                print(block.m)
                                print(block.seq)
                                print(offset)
                            pass
                else:
                    if debugmode:
                        print('\n')
                        print(block.seq)
                        print(offset)
                        print(block.l)
                    bbuf = file.read(block.l)
                    got = zlib.decompress(bbuf)
                    g.write(got)
                offset = file.tell()
                rbsize = file.readinto(block)
            if got_file_tail:
                if debugmode:
                    print('\nfile ended!')
                pass
            if debugmode:
                print('\nno more data !')
    except:
        traceback.print_exc()
        pass


# Python version check
ver = sys.version_info

if ver[0] == 3:
    mopen = open
else:
    def mopen(file, mode='rb', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
        return open(file, mode + 'b')


class ytag_fd(object):
    pass


def ytag_extract_file_ytfd(file_name):
    if file_name not in ytfd_file:
        file_name_entry = ytag_fd()  # create a new class object
        file_name_entry.ytfds = {}
        file_name_entry.name = os.path.join(ytag_folder_abspath, file_name)
        file_name_entry.count = 0
        ytfd_file[file_name] = file_name_entry
    else:
        ytfd_file[file_name].count = ytfd_file[file_name].count + 1
    count = ytfd_file[file_name].count
    ytfd = ytag_fd()  # create a new class object
    ytfd.name = os.path.join(ytag_folder_abspath, '%04d.%s' % (count, file_name))
    ytfd.fd = open(ytfd.name, 'wb')
    ytfd.size = 0
    ytfd_file[file_name].ytfds[count] = ytfd
    return ytfd


def ytag_extract_file(fd_src, ytfd):
    while True:
        ytag = fd_src.read(8)
        if len(ytag) == 8:
            ytags = struct.unpack('<II', ytag)
            tag = ytags[0]
            dlen = ytags[1]
            if dlen < YTAG_STRUCT_SIZE:
                print('Fatal dlen = %d at pos %d' % (dlen, fd_src.tell()))
                return -1
            dlen = dlen - YTAG_STRUCT_SIZE
            if tag == YTAG_TAG_RAWDATA:  # file data
                if dlen == 0:
                    continue
                rdata = fd_src.read(dlen)
                ytfd.fd.write(rdata)
                rdlen = len(rdata)
                ytfd.size = ytfd.size + rdlen
                if rdlen != dlen:
                    print('Fatal rdlen = %d, but dlen = %d at pos %d' % (rdlen, dlen, fd_src.tell()))
                    return -1
            elif tag == YTAG_TAG_NEWFILE_BEGIN:  # begin of a new file
                if dlen == 0:
                    new_file_name = 'ytag_' + merged
                else:
                    new_file_name = fd_src.read(dlen).decode('utf-8')  # python3 use decode() to remove "b''", 'utf-8' let us can decode chinese character
                if ytag_extract_file(fd_src, ytag_extract_file_ytfd(new_file_name)) < 0:
                    return -1
            elif tag == YTAG_TAG_NEWFILE_END or tag == YTAG_MAGIC:  # end of a file or ytag file magic
                if dlen > 0:
                    rdata = fd_src.read(dlen)
                if tag == YTAG_TAG_NEWFILE_END:
                    ytfd.fd.close()
                    return 0
            else:
                print(('Fatal tag = 0x%08x at pos %d does not support' % (tag, fd_src.tell())))
                return -1
        elif len(ytag) == 0:
            return 0
        else:
            print(('Fatal len(ytag) = %d at pos %d' % (len(ytag), fd_src.tell())))
            return -1


def ytag_parse(ytag_logfile):
    global ytfd_file
    ytfd_file = {}
    sys.setrecursionlimit(90000)  # otherwise will meet "RuntimeError: maximum recursion depth exceeded in cmp"
    with open(os.path.join(analyzer_relative_path, ytag_logfile), 'rb') as fd_src:
        ytag_extract_file(fd_src, ytag_extract_file_ytfd(merged))
    for file_name in ytfd_file:
        ytfds = ytfd_file[file_name].ytfds
        for ytfd_index in ytfds:
            ytfd = ytfds[ytfd_index]
            ytfd.fd.close()  # must close, otherwise can't work in windows python
            if ytfd.size == 0:
                os.remove(ytfd.name)
                ytfd_file[file_name].count = ytfd_file[file_name].count - 1
            else:
                ytfd_latest = ytfd
        if ytfd_file[file_name].count == 0:
            os.rename(ytfd_latest.name, ytfd_file[file_name].name)


def merge_logs(files, output):
    with open(output, 'wb') as alllog:
        for f in files:
            with open(os.path.join(analyzer_relative_path, f), 'rb') as sublog:
                shutil.copyfileobj(sublog, alllog)


def split_log(infiles, logdict):
    fddict = {}
    keys = list(logdict.keys())
    last_token = ''
    for key in keys:
        fddict[key] = mopen(os.path.join(analyzer_relative_path, logdict[key]), 'w', encoding='utf8', errors='replace')

    for eachfile in infiles:
        # print eachfile
        unzipit(eachfile)
        with mopen(os.path.join(analyzer_relative_path, eachfile + ".log"), 'r', encoding='utf8', errors='replace') as f:
            for line in f.readlines():
                if line[0:id_token_len] in keys:
                    fddict[line[0:id_token_len]].write(line[id_token_len:])
                    last_token = line[0:id_token_len]
                else:
                    if len(last_token) > 0:
                        fddict[last_token].write(line[0:])

    for key in keys:
        fddict[key].close()
        if os.stat(os.path.join(analyzer_relative_path, logdict[key])).st_size == 0:
            os.remove(os.path.join(analyzer_relative_path, logdict[key]))


def main():
    global analyzer_relative_path
    global ytag_folder_abspath
    global debugmode
    os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
    analyzer_relative_path = '.' + os.sep
    parser = optparse.OptionParser()
    parser.add_option('-r', dest='remove', default=False, action='store_true', help='remove the original log files')
    parser.add_option('-m', dest='merge', default=False, action='store_true', help='merge all the log files')
    parser.add_option('-R', dest='reverse', default=True, action='store_false', help='sort the files reverse')
    parser.add_option('-d', dest='debug', default=False, action='store_true', help='output some debug info')
    options, args = parser.parse_args()
    print('args:', args, 'if not args:', (not args))

    if not args:
        allfiles = os.listdir(os.path.join(analyzer_relative_path, logpath))
        pat = re.compile('.*\.?[0-9]+$')
        logfilenames = [f for f in allfiles if pat.match(f)]
    else:
        logfilenames = args

    logfilenames.sort(reverse=options.reverse)

    if options.debug:
        debugmode = True
        print(logfilenames)

    if options.merge or (not logdict or YTAG):
        if options.merge:  # First priority checking
            merge_logs(logfilenames, os.path.join(analyzer_relative_path, merged))
        elif YTAG:  # Second priority checking
            ytag_folder_abspath = os.path.join(analyzer_relative_path, ytag_folder)
            if os.access(ytag_folder_abspath, os.F_OK):
                shutil.rmtree(ytag_folder_abspath)
            os.mkdir(ytag_folder_abspath)
            tmp_file = os.path.join(ytag_folder_abspath, 'temp.log')
            merge_logs(logfilenames, tmp_file)
            ytag_parse(tmp_file)
            os.remove(tmp_file)
        else:  # Last priority checking
            merge_logs(logfilenames, os.path.join(analyzer_relative_path, merged))
    else:
        split_log(logfilenames, logdict)

    if options.remove:
        for log in logfilenames:
            os.remove(os.path.join(analyzer_relative_path, log))
        os.remove(sys.argv[0])


if __name__ == '__main__':
    main()
