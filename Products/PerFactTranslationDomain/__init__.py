#
# __init__.py   -  initialize PerFactTranslationDomain Product
#                  as default Service via Factory
#
# $Revision: 1.4 $
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
# $Id: __init__.py,v 1.4 2013/08/08 05:43:40 root Exp $

from PerFactTranslationDomain import PerFactTranslationDomain
from zope.component import provideUtility
from zope.component import queryUtility
from zope import interface
from zope.i18n.interfaces import ITranslationDomain
from zope.i18n.interfaces import IFallbackTranslationDomainFactory

import logging
LOG = logging.getLogger('PerFactTranslationService.init')

LOG.info('initializing ...')

## the following lines may be used to set up specific 
## tranlation domains
#domain=u'pf'
#perfact_translation = PerFactTranslationDomain(domain)
#provideUtility(perfact_translation, name=domain)
#
#if queryUtility(ITranslationDomain, name=domain) is None:
#    syslog.syslog('Translation domain NOT instantiated.')
 
## if we want to catch all domains, we use a TranslationDomainFactory
def pf_fallback(domain=u''):
    return PerFactTranslationDomain(domain)

interface.directlyProvides(pf_fallback,IFallbackTranslationDomainFactory,)
provideUtility(pf_fallback)

LOG.info('initialization done.')
