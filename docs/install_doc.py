#!/usr/bin/env python3

import argparse
import os
import shutil
import subprocess
import sys

def _generate_alchemy_doc(sdk_root):
    here = os.getcwd()
    ret = True
    os.chdir(sdk_root)
    subprocess.check_call('./build.sh -p native -A libARController_doc'.split())
    os.chdir(here)
    return ret

def _copy_doc(sdk_root):
    doc_root = os.path.join(sdk_root, 'out', 'arsdk-native', 'build', 'libARController_doc', 'gen', 'reference')
    here = os.getcwd()

    projects = os.listdir(doc_root)

    for proj in projects:
        mds = os.listdir(os.path.join(doc_root, proj))
        for md in mds:
            in_path = os.path.join(doc_root, proj, md)
            if md == 'index.md':
                out_dir = os.path.join(here, 'reference', proj, 'source')
            else:
                out_dir = os.path.join(here, 'reference', proj, 'source', 'includes')
            out_path = os.path.join(out_dir, md)
            if not os.path.exists(out_dir):
                os.makedirs(out_dir)
            shutil.copyfile(in_path, out_path)
        description_file = os.path.join(here, 'reference', proj, 'source', 'includes', '_description.md')
        if not os.path.exists(description_file):
            open(description_file, 'w').close()

def update_doc(args_=None):
    parser = argparse.ArgumentParser(description='Update documentation from SDK.')
    parser.add_argument('sdk', help='The root dir of the SDK')

    args = parser.parse_args(args_)

    if not _generate_alchemy_doc(args.sdk):
        print('Unable to generate documentation')
        sys.exit(1)

    _copy_doc(args.sdk)


if __name__ == '__main__':
    update_doc()
