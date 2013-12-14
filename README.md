ansible-buildbot-ros
====================

Ansible playbook to set up [buildbot-ros](https://github.com/mikeferguson/buildbot-ros).

Example usage:

    sudo pip install ansible
    ansible-playbook -i hosts buildbot-ros.yaml -e @vars.yaml -K
    
This will attempt to SSH to the "build" host on your local network. You can change which host to
use by editing (or providing an alternative) hosts file. The Ansible hosts file format permits
specifying the user to SSH as, [see here for details](http://www.ansibleworks.com/docs/intro_inventory.html).

Note that at this time, there is no support for multiple slaves, and using a slave that's a different
machine from the master is untested.

If you just want to try this on your own machine, you can bypass the SSH details:

    ansible-playbook -i hosts-local buildbot-ros.yaml -e @vars.yaml -K
