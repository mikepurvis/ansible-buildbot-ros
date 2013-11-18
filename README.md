ansible-buildbot-ros
====================

Ansible playbook to set up [buildbot-ros](https://github.com/mikeferguson/buildbot-ros). Far from
complete at present, but the basic usage is (will be):

    pip install ansible
    ansible-playbook -i hosts buildbot-ros.yaml -K
    
By default, it operates on localhost, creating a `buildbot` user with the homedir in `/opt/buildbot`.
