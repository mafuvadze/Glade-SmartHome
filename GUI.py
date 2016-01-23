import sys
try:
 	import pygtk
  	pygtk.require("2.0")
except:
  	pass
try:
	import gtk
  	import gtk.glade
except:
	sys.exit(1)

class GUI:
	
	def __init__(self):
		
		#Set the Glade file
		self.gladefile = "GUI.glade"  
	        self.wTree = gtk.glade.XML(self.gladefile) 
		
		#Create our dictionay and connect it
		dic = { "on_share_clicked" : self.on_share_clicked,
			"on_unshare_clicked" : self.on_unshare_clicked,
			"on_set_clicked" : self.on_set_clicked,
			"on_stateToggle_clicked" : self.on_share_clicked,
			"on_MainWindow_destroy" : gtk.main_quit }
		self.wTree.signal_autoconnect(dic)

	def on_share_clicked(self, widget):
		print "share clicked"

	def on_unshare_clicked(self, widget):
		print "unshare clicked"

	def on_set_clicked(self, widget):
		print "set clicked"
	
	def on_stateToggle_clicked(self, widget):
		print "state toggled"


if __name__ == "__main__":
	hwg = HellowWorldGTK()
	gtk.main()
