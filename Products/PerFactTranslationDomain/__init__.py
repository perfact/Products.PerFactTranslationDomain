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

from zope.component import provideUtility
from zope import interface
from zope.i18n.interfaces import IFallbackTranslationDomainFactory, \
    ITranslationDomain

@interface.implementer(ITranslationDomain)
class Dummy(object):
    """
    Dummy translation service that simply returnes a fixed string
    """
    # See zope.i18n.interfaces.ITranslationDomain
    domain = None

    def translate(self, msgid, mapping=None, context=None,
                  target_language=None, default=None, msgid_plural=None,
                  default_plural=None, number=None):
        return 'translated'

def pf_fallback(domain=u''):
    return Dummy()

interface.directlyProvides(pf_fallback, IFallbackTranslationDomainFactory,)
provideUtility(pf_fallback)
