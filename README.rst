===============================
``gs.group.messages.ratelimit``
===============================
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Set the maximum posting rate in a group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Author: `Michael JasonSmith`_
:Contact: Michael JasonSmith <mpj17@onlinegroups.net>
:Date: 2013-03-22
:Organization: `GroupServer.org`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 3.0 New Zealand License`_
  by `OnlineGroups.Net`_.

Introduction
============

This package provides the administrator-interface to the posting-rate
system. The posting rate is the number of posts a member can make to
a group in a particular time-period. However, while the underlying code
supports an arbitary time-period, this user-interface is simplified by
always using 24-hours as the period.

See Also
========

The code that stops people from exceeding the posing rate is in
``gs.group.type.discussion``.

Resources
=========

- Code repository: https://source.iopen.net/groupserver/gs.group.messages.ratelimit
- Questions and comments to http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. _GroupServer: http://groupserver.org/
.. _GroupServer.org: http://groupserver.org/
.. _OnlineGroups.Net: https://onlinegroups.net
.. _Michael JasonSmith: http://groupserver.org/p/mpj17
.. _Creative Commons Attribution-Share Alike 3.0 New Zealand License:
   http://creativecommons.org/licenses/by-sa/3.0/nz/
