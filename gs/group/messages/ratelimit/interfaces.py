# -*- coding: utf-8 -*-
from zope.interface import Interface
from zope.schema import Int


class IGSMessageRateLimit(Interface):
    postsPerDay = Int(title=u'Posts per day',
      description=u'How many posts should be allowed per person, per 24 hour '
                  u'period.',
      default=256,
      min=1)
