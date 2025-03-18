# -*- coding: utf-8 -*-

from odoo import models, fields

class LibraryBookCategory(models.Model):
  _name = 'library.book.category'
  _description = 'Book Category'

  name = fields.Char(string='Name', required=True)

  _sql_constraints = [
    ('name_unique', 'unique(name)', 'Name must be unique!')
  ]