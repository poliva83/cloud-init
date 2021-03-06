# vi: ts=4 expandtab
#
#    Copyright (C) 2012 Canonical Ltd.
#    Copyright (C) 2012 Hewlett-Packard Development Company, L.P.
#    Copyright (C) 2012 Yahoo! Inc.
#
#    Author: Scott Moser <scott.moser@canonical.com>
#    Author: Juerg Haefliger <juerg.haefliger@hp.com>
#    Author: Joshua Harlow <harlowja@yahoo-inc.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License version 3, as
#    published by the Free Software Foundation.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import types

import six


if six.PY3:
    _NAME_TYPES = (
        types.ModuleType,
        types.FunctionType,
        types.LambdaType,
        type,
    )
else:
    _NAME_TYPES = (
        types.TypeType,
        types.ModuleType,
        types.FunctionType,
        types.LambdaType,
        types.ClassType,
    )


def obj_name(obj):
    if isinstance(obj, _NAME_TYPES):
        return six.text_type(obj.__name__)
    else:
        if not hasattr(obj, '__class__'):
            return repr(obj)
        else:
            return obj_name(obj.__class__)
