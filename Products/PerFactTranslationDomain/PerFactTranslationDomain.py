#
# PerFactTranslationDomain  -  TranslationDomain using an acquired 
#                              translation_service,
#                              in DB_Utils provided in zI18N Subfolder
#
# $Revision: 1.5 $
#
# Copyright (C) 2013 Nils Jungclaus <nils.jungclaus@perfact.de>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# $Id: PerFactTranslationDomain.py,v 1.5 2016/06/08 16:45:33 root Exp $

from zope.interface import implements
from zope.i18n.interfaces import ITranslationDomain
from zope.i18n import interpolate

import logging

LOG = logging.getLogger('PerFactTranslationService')

class PerFactTranslationDomain(object):
    """This is a simple implementation of the ITranslationDomain
       that uses the translation_service found in the acquisition path,
       in DB_Utils usually the one implemented in the zI18N folder.
    """
    implements(ITranslationDomain)

    # See zope.i18n.interfaces.ITranslationDomain
    domain = None

    def __init__(self, domain):
        """Initializes the object. No arguments are needed."""
        # LOG.info('PFTranslationdomain.initialized as '+str(domain))
        # domain is usually "default"
        self.domain = domain

    def translate(self, msgid, mapping=None, context=None,
                  target_language=None, default=None):
        '''See interface ITranslationDomain'''
        # LOG.info('translate called with '+str((msgid, mapping, context, target_language, default)))
        if context is None:
            LOG.warn("no context!")
            return None # no translation

        # Find a placeful translation service
        request = context.REQUEST.other

        if request.has_key('_translation_service_cache'):
            translation_service = request['_translation_service_cache']
            # LOG.info('Found translation_service in request cache...')
        else:
            # LOG.info('Find translation_service by acquisition')
            translation_service = getattr(context.other['PARENTS'][0], 'translation_service', None)
            # LOG.info(str(translation_service))
            request['_translation_service_cache'] = translation_service

        if translation_service is None:
            # LOG.info('No translation service found, falling back to null translation')
            # no translation, keep orig msgid
            translation_service = self.null_translation
        text = translation_service(domain=None, msgid=msgid, 
                                   mapping=mapping, 
                                   target_language=target_language,
                                   default=default)
        return interpolate(text, mapping)

    def null_translation(*args, **kw):
        if kw['default'] is None:
            default = unicode(kw['msgid'])
        else:
            default = kw['default']
        return default
