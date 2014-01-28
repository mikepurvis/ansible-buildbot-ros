#!/usr/bin/env python

import sys, subprocess

## @brief Call a command
## @param command Should be a list
def call(command, envir=None, verbose=True, return_output=False):
    print('Executing command "%s"' % ' '.join(command))
    helper = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True, env=envir)
    if return_output:
        res = ''
    while True:
        output = helper.stdout.readline().decode('utf8', 'replace')
        if helper.returncode is not None or not output:
            break
        if verbose:
            sys.stdout.write(output)
        if return_output:
            res += output

    helper.wait()
    if helper.returncode != 0:
        msg = 'Failed to execute command "%s" with return code %d' % (command, helper.returncode)
        print('/!\  %s' % msg)
        raise BuildException(msg)
    if return_output:
        return res

