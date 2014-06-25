# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014 credativ Ltd (<http://credativ.co.uk>).
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
        'name' : 'Email tracking reference',
        'version' : '0.1',
        'author' : 'credativ Ltd',
        'description' : """
        Sends tracking references to customer. Wait 24 hours if tracking reference is not available.
        """,
        'website' : 'http://credativ.co.uk',
        'depends' : [
            'connector',
            'stock'
            ],
        'init_xml' : [
            ],
        'update_xml' : [
           
            ],
        'data' : [
           'email_tracking_data.xml'
            ],
        'installable' : True,
        'active' : False,
}
