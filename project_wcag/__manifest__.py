# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo SA, Open Source Enterprise Management Solution, third party addon
#    Copyright (C) 2021- Vertel AB (<https://vertel.se>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "Project WCAG",
    'summary': 'Project WCAG',
    'author': 'Vertel AB',
    'category': 'Project',
    "version": "14.0.0.1.0",
    'license': 'AGPL-3',
    'website': 'https://vertel.se/',
    "description": """
        Adds fields to fill wcag criteria on a project task.
    """,
    "depends": [
        "project",
    ],
    "data": [
        "security/ir.model.access.csv",
        "wizard/add_rules_to_project_wizard.xml",
        "views/project_task_view.xml",
        "views/project_view.xml",
        "data/wcag_rules.xml",
        "data/create_wcag_task.xml",
        "data/server_action.xml",
    ],
    "demo": [],
    "installable": True,
    "application": False,
}
