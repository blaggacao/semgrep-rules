from frappe.model import Document
import frappe
from frappe import requires_permission

# ruleid: require-permission-decorator-on-conversion-methods
class MyDocument(Document):
	def _into_sales_invoice(self, so):
		...

# ok: require-permission-decorator-on-conversion-methods
class MyDocument(Document):
	@requires_permission("Sales Invoice", "create")
	def _into_sales_invoice(self, so):
		...

# ruleid: require-permission-decorator-on-conversion-methods
class MyDocument(Document):
	def _from_sales_invoice(self, so):
		...

# ok: require-permission-decorator-on-conversion-methods
class MyDocument(Document):
	@frappe.requires_permission("Sales Invoice", "read")
	def _from_sales_invoice(self, so):
		...
