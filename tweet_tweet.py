import pygtk
pygtk.require('2.0')
import gtk



class tweetMe:

    def hello(self, widget, data=None):
        print "Helloo"

    def on_btn_clicked(self, widget, textbuffer=None):
        import pdb;pdb.set_trace()
        startiter = textbuffer.get_start_iter()
        enditer = textbuffer.get_end_iter()
        data = textbuffer.get_text(startiter, enditer)

        pass


    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        # attach destroy signal to terminate the application
        self.window.connect("destroy", lambda w: gtk.main_quit())
        self.window.set_border_width(30)
        self.window.show()

        # a horizontal box to hold the buttons
        self.hbox = gtk.HBox()
        self.hbox.show()
        self.window.add(self.hbox)

        self.frame = gtk.Frame("Tweet Box")
        self.hbox.pack_start(self.frame)

        self.textview = gtk.TextView()
        self.hbox.pack_start(self.textview)

        self.textBox = gtk.TextView()
        #self.entry = gtk.Entry()
        #self.entry.set_max_length(100)
        self.textBox.set_editable(True)
        self.textBox.set_cursor_visible(True)
        self.textbuffer = self.textBox.get_buffer()

        self.textBox.set_left_margin(50)
#       self.textBox.set_top_margin(50)
#        self.textBox.set_bottom_margin(50)
        self.textBox.set_right_margin(50)


        self.hbox.pack_start(self.textBox)

 #       entry.connect("activate", self.enter_callback, entry)
        self.textBox.show()
#        entry_text = entry.get_text()

        # pick an image file you have in the working directory, or give
        # the full path, can be a .jpg, .png, ,gif, .bmp image file
        # (filenames are case sensitive on Ubuntu/Linux)
        self.image_file = "tweet.gif"
        self.image = gtk.Image()
        self.image.set_from_file(self.image_file)
        self.image.show()
        # create a button to contain the image widget
        # auto adjusts to image size
        self.tweet_button = gtk.Button()
        self.tweet_button.add(self.image)
        self.tweet_button.show()
        self.hbox.pack_start(self.tweet_button)

        self.tweet_button.connect("clicked", self.on_btn_clicked, self.textbuffer)

    def main(self):
        gtk.main()

if __name__ == "__main__":
    base = tweetMe()
    base.main()


