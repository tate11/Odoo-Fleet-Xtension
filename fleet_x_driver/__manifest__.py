# -*- coding: utf-8 -*-
{
    'name': "Fleet Xtension - Driver",
    'summary': "Driver addon for Fleet management Xtension",
    'author': "Salton Massally<smassally@idtlabd.sl>, DeneroTeam <dhaval@deneroteam.com>",
    'website': "hhtp://idtlabs.sl",
    'category': 'Managing vehicles and drivers',
    'version': '10.0.2018.06.15.1',
    'depends': ['fleet_x', 'fleet_x_issue'],
    'data': [
        'views/fleet_drivers.xml',
        'views/cron.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True

}
