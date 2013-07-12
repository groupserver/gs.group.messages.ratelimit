# -*- coding: utf-8 -*-
from zope.cachedescriptors.property import Lazy
from zope.component import createObject
from zope.formlib import form
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile
from gs.group.base import GroupForm
from interfaces import IGSMessageRateLimit


class ChangeMessageRateLimit(GroupForm):
    label = u'Change the posting rate'
    pageTemplateFileName = 'browser/templates/changeratelimit.pt'
    template = ZopeTwoPageTemplateFile(pageTemplateFileName)
    form_fields = form.Fields(IGSMessageRateLimit, render_context=False)

    def __init__(self, context, request):
        super(ChangeMessageRateLimit, self).__init__(context, request)

    @Lazy
    def mailingList(self):
        retval = createObject('groupserver.MailingListInfo', self.context)
        assert retval
        return retval

    def setUpWidgets(self, ignore_request=False):
        data = {'postsPerDay': self.get_postsPerDay()}
        self.widgets = form.setUpWidgets(
            self.form_fields, self.prefix, self.context,
            self.request, form=self, data=data,
            ignore_request=ignore_request)

    def get_postsPerDay(self):
        groupList = self.mailingList.mlist
        senderlimit = groupList.getProperty('senderlimit', 512)
        senderinterval = groupList.getProperty('senderinterval', 86400)

        # convert 'old' system to posts per second, then per day (rounded)
        postsPerSecond = float(senderlimit) / float(senderinterval)
        postsPerDay = int(postsPerSecond * 86400)

        return postsPerDay

    @form.action(label=u'Change', failure='handle_change_action_failure')
    def handle_change(self, action, data):
        groupList = self.mailingList.mlist
        val = data['postsPerDay']
        if not groupList.hasProperty('senderlimit'):
            groupList.manage_addProperty('senderlimit', val, 'int')
        else:
            groupList.manage_changeProperties(senderlimit=val)

        if not groupList.hasProperty('senderinterval'):
            groupList.manage_addProperty('senderinterval', 86400, 'int')
        else:
            groupList.manage_changeProperties(senderinterval=86400)

        self.status = (u'Posting rate limit has been changed to %s per day.'
                       % val)

    def handle_change_action_failure(self, action, data, errors):
        if len(errors) == 1:
            self.status = u'<p>There is an error:</p>'
        else:
            self.status = u'<p>There are errors:</p>'
