# -*- coding: utf-8 -*-
"""
 ***************************************************************************
    MBG

    Processing
                             -------------------
        begin                : 2017-07-01
        copyright            : (C) 2017 by HGE-IPH
        email                : martinbiancho@hotmail.com
 ***************************************************************************

 ***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************
"""

def classFactory(iface):
    from .MGB import MGB
    return MGB(iface)
