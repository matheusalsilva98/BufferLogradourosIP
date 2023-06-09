# -*- coding: utf-8 -*-

"""
/***************************************************************************
 GrupoIPExtracaoDeEstradas
                                 A QGIS plugin
 Buffer de Logradouros
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2023-04-16
        copyright            : (C) 2023 by GrupoIPExtracaoDeEstradas
        email                : marcio.souza@ime.eb.br
                               matheus.silva@ime.eb.br
                               romeu.peris@ime.eb.br
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

__author__ = 'Grupo IP Extração De Estradas'
__date__ = '2023-04-16'
__copyright__ = '(C) 2023 by Grupo IP Extração De Estradas'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

import os
import sys
import inspect

from qgis.core import QgsProcessingAlgorithm, QgsApplication
from .grupo_ip_extracao_de_estradas_provider import GrupoIPExtracaoDeEstradasProvider

cmd_folder = os.path.split(inspect.getfile(inspect.currentframe()))[0]

if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)


class BufferLogradourosPuglin(object):

    def __init__(self):
        self.provider = None

    def initProcessing(self):
        """Init Processing provider for QGIS >= 3.8."""
        self.provider = GrupoIPExtracaoDeEstradasProvider()
        QgsApplication.processingRegistry().addProvider(self.provider)

    def initGui(self):
        self.initProcessing()

    def unload(self):
        QgsApplication.processingRegistry().removeProvider(self.provider)
