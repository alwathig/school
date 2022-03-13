from email.policy import default
from odoo import models, fields, api, _


# Student
class Student(models.Model):
    _name = "school.student"
    name = fields.Char(required=True)
    number = fields.Integer()
    description = fields.Text()
    birth_date = fields.Date()
    cv = fields.Html(string="Resume")
    gender = fields.Selection(selection=[("male","Male"),("female","Female")],default="male")
    fees = fields.Float(help="Enter the reset of fees for this student", digits=(4,6))
    image = fields.Binary()
    is_regiser = fields.Boolean()
    year = fields.Datetime()
    currency_id = fields.Many2one("res.currency", default=lambda self: self.env.company.currency_id)
    
    room = fields.Many2one("school.room")
    status = fields.Selection([("draft","Draft"), ("not_paid","Not Paid"), ("paid","Paid")], default="draft")

    _sql_constraints = [
        ('unique_number','unique(number)','Number Cannot be deplcated!'),
        ('check_fees','check(fees > 100)', 'Fees must be bigger than 0')
    ]

    def create_invoice(self):
        pass

    def cancel(self):
        pass

    def view_invoices(self):
        pass

    def action_view_invoice(self):
        pass

# Lesson
class Lesson(models.Model):
    _name = "school.lesson"
    name = fields.Char()
    number = fields.Integer()
    content = fields.Html()
    time = fields.Datetime()
    # releational field
    subject_id = fields.Many2one("school.subject")

class Subject(models.Model):
    _name = "school.subject"
    name = fields.Char()
    # relatoinal field
    lessons = fields.One2many("school.lesson","subject_id")

class Teacher(models.Model):
    _name = "school.teacher"
    name = fields.Char()
    subjects = fields.Many2many("school.subject")

class Room(models.Model):
    _name = "school.room"
    name = fields.Char()
    students = fields.One2many("school.student", "room")