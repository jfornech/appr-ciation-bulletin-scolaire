import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

global appreciation
appreciation = {'trimestre':'', 'investissement':'', 'travail':'', 'comportement':'', 'conseil':''}


class Handler:
    "Définition méthodes"

    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def on_about(self, button):
        about.show_all()

    def on_quitter(self, *args):
        Gtk.main_quit(*args)

    def on_checkbutton_trimestre_clicked (self, button ):
        trimestre = button.get_label()
        if button.get_active():
            appreciation['trimestre'] = trimestre
        else:
            appreciation['trimestre'] = ""
        text.set_text(appreciation.get('trimestre') + ', ' + appreciation.get('investissement')+ '. ' + appreciation.get('travail')+ '. ' + appreciation.get('comportement')+ '. ' + appreciation.get('conseil'))

    def on_conseils_clicked (self, button ):
        conseil = button.get_label()
        if button.get_active():
            appreciation['conseil'] = conseil
        else:
            appreciation['conseil'] = ""
        text.set_text(appreciation.get('trimestre') + ', ' + appreciation.get('investissement')+ '. ' + appreciation.get('travail')+ '. ' + appreciation.get('comportement')+ '. ' + appreciation.get('conseil'))


    def on_checkbutton_investissement_clicked(self, button):
        investissement = button.get_label()
        if button.get_active():
            appreciation['investissement'] = investissement
        else:
            appreciation['investissement'] = ""
        text.set_text(appreciation.get('trimestre') + ', ' + appreciation.get('investissement')+ '. ' + appreciation.get('travail')+ '. ' + appreciation.get('comportement')+ '. ' + appreciation.get('conseil'))


    def on_checkbutton_comportement_clicked (self, button ):
        comportement = button.get_label()
        if button.get_active():
            appreciation['comportement'] = comportement
        else:
            appreciation['comportement'] = ""

        text.set_text(appreciation.get('trimestre') + ', ' + appreciation.get('investissement')+ '. ' + appreciation.get('travail')+ '. ' + appreciation.get('comportement')+ '. ' + appreciation.get('conseil'))

    def on_checkbutton_travail_clicked (self, button ):
        travail = button.get_label()
        if button.get_active():
            appreciation['travail'] = travail
        else:
            appreciation['travail'] = ""

        text.set_text(appreciation.get('trimestre') + ', ' + appreciation.get('investissement')+ '. ' + appreciation.get('travail')+ '. ' + appreciation.get('comportement')+ '. ' + appreciation.get('conseil'))



builder = Gtk.Builder()
builder.add_from_file("bulletin_test.glade")
builder.connect_signals(Handler())
about = builder.get_object("aboutdialog")

window = builder.get_object("window1")
window.connect("delete-event", Gtk.main_quit)
#window = Gtk.Window(title='Hello world')

text = builder.get_object("entry1")
text_nom_eleve = builder.get_object("nom_eleve")

window.show_all()
Gtk.main()
