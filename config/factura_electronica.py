# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals
# from frappe import _
# import frappe


# def get_data():
#     return [
#         {
#             "label": _("Configuración"),
#             "items": [
#                 {
#                     "type": "doctype",
#                     "name": "Configuracion Factura Electronica",
#                     "description": _("Configuracion para factura electronicas"),
#                     "onboard": 1,
#                 },
#                 {
#                     "type": "doctype",
#                     "name": "FEL Catalogo Frases",
#                     "description": _("FEL Catalogo Frases"),
#                     "onboard": 1,
#                 },
#                 {
#                     "type": "doctype",
#                     "name": "Tax Category GT",
#                     "description": _("Tax Category GT"),
#                     "onboard": 1
#                 },
#                 {
#                     "type": "doctype",
#                     "name": "Catalog Of Taxable Units",
#                     "description": _("Catalog Of Taxable Units"),
#                     "dependencies": ["Tax Category GT"],
#                     "onboard": 1
#                 },
#             ]
#         },
#         {
#             "label": _("Registro Facturas Electronicas"),
#             "items": [
#                 {
#                     "type": "doctype",
#                     "name": "Envios Facturas Electronicas",
#                     "description": _("Encuentre todas las facturas generadas detalladamente."),
#                     "onboard": 1,
#                 },
#                 {
#                     "type": "doctype",
#                     "name": "Envio FEL",
#                     "description": _("Registro estado de las peticion FEL"),
#                     "onboard": 1
#                 }
#             ]
#         },
#         {
#             "label": _("Batches"),
#             "items": [
#                 {
#                     "type": "doctype",
#                     "name": "Batch Electronic Invoice",
#                     "description": _("Batch generator for electronic invoicing"),
#                     "onboard": 1
#                 },
#                 {
#                     "type": "doctype",
#                     "name": "Batch Status",
#                     "description": _("Batch Status"),
#                     "onboard": 1
#                 }
#             ]
#         },
#         {
#             "label": _("Taxes"),
#             "items": [
#                 {
#                     "type": "doctype",
#                     "name": "Tax Retention Guatemala",
#                     "description": _("Tax Retention Guatemala"),
#                     "onboard": 1
#                 },
#                 {
#                     "type": "doctype",
#                     "name": "Consumable Acquisition Record",
#                     "description": _("Consumable Acquisition Record"),
#                     "onboard": 1
#                 },
#                 {
#                     "type": "doctype",
#                     "name": "VAT Exemption Record",
#                     "description": _("VAT Exemption Record"),
#                     "onboard": 1
#                 },
#                 {
#                     "type": "doctype",
#                     "name": "VAT Declaration",
#                     "description": _("VAT Declaration"),
#                     "onboard": 1
#                 },
#                 {
#                     "type": "doctype",
#                     "name": "Public Writ",
#                     "description": _("Public Writ"),
#                     "onboard": 1
#                 },
#                 {
#                     "type": "doctype",
#                     "name": "SAT Form",
#                     "description": _("SAT Form"),
#                     "onboard": 1
#                 },
#                 # {
#                 #     "type": "doctype",
#                 #     "name": "FAUCA",
#                 #     "description": _("FAUCA"),
#                 #     "onboard": 1
#                 # },
#                 {
#                     "type": "doctype",
#                     "name": "Unique Customs Declaration",
#                     "description": _("Unique Customs Declaration"),
#                     "onboard": 1
#                 }
#             ]
#         },
#         {
#             "label": _("Reports"),
#             "items": [
#                 {
#                     "type": "report",
#                     "label": _("Purchase and Sales Ledger Tax Declaration Report"),
#                     "name": "Purchase and Sales Ledger Tax Declaration",
#                     "is_query_report": True,
#                     "dependencies": ["Sales Invoice", "Purchase Invoice"],
#                     "onboard": 1
#                 },
#                 {
#                     "type": "report",
#                     "label": _("VAT and Income Tax Retention Report"),
#                     "name": "VAT and Income Tax Retention Report",
#                     "is_query_report": True,
#                     "onboard": 1
#                 },
#                 {
#                     "type": "report",
#                     "label": _("VAT Payable and Receivable Conciliation"),
#                     "name": "VAT Payable and Receivable Conciliation",
#                     "is_query_report": True,
#                     "onboard": 1
#                 },
#                 {
#                     "type": "report",
#                     "label": _("GT General Ledger"),
#                     "name": "GT General Ledger",
#                     "is_query_report": True,
#                     "onboard": 1
#                 },
#                 {
#                     "type": "report",
#                     "label": _("GT Purchase Ledger"),
#                     "name": "GT Purchase Ledger",
#                     "is_query_report": True,
#                     "onboard": 1
#                 },
#                 {
#                     "type": "report",
#                     "label": _("GT Sales Ledger"),
#                     "name": "GT Sales Ledger",
#                     "is_query_report": True,
#                     "onboard": 1
#                 },
#                 {
#                     "type": "report",
#                     "label": _("GT Journal"),
#                     "name": "GT Journal",
#                     "is_query_report": True,
#                     "onboard": 1
#                 }
#             ]
#         }
#     ]
