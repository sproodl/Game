#This is the options file to turn on/off dev options and the menu etc.

init python:
    config.developer = True

    ## These control the width and height of the screen.

    config.screen_width = 800
    config.screen_height = 600

    ## This controls the title of the window, when Ren'Py is
    ## running in a window.

    config.window_title = u"PunktPunktPunkt"

    # These control the name and version of the game, that are reported
    # with tracebacks and other debugging logs.
    config.name = "PunktPunktPunkt"
    config.version = "0.1"

    ## We then want to call a theme function. themes.roundrect is
    ## a theme that features the use of rounded rectangles. It's
    ## the only theme we currently support.
    ##
    ## The theme function takes a number of parameters that can
    ## customize the color scheme.
    theme.roundrect(                                    
        ## The color of an idle widget face.
        widget = "#000",
        ## The color of a focused widget face.
        widget_hover = "#fc2676",
        ## The color of the text in a widget.
        widget_text = "#fff",
        ## The color of the text in a selected widget. (For example, the current value of a preference.)
        widget_selected = "#fff",
        ## The color of a disabled widget face. 
        disabled = "#ffb0cd",
        ## The color of disabled widget text.
        disabled_text = "#fff",
        ## The color of informational labels.
        label = "#fff",
        ## The color of a frame containing widgets.
        frame = "#fff",
        ## The background of the main menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        
        mm_root = "#fff0", #"#f8c821",
        
       
        ## If this is True, the in-game window is rounded. If False,
        ## the in-game window is square.
        
        rounded_window = True,

        ## And we're done with the theme. The theme will customize
        ## various styles, so if we want to change them, we should
        ## do so below.            
        )


    #########################################


    #########################################
    ## These settings let you customize the window containing the
    ## dialogue and narration, by replacing it with an image.

    ## The background of the window. In a Frame, the two numbers
    ## are the size of the left/right and top/bottom borders,
    ## respectively.
    
    ##to do: CHANGE THIS ACCORDING TO REGIME##########
    style.say_who_window.background = Frame("images/charnamebox.png", 16, 34)
    style.window.background = None

    ## Margin is space surrounding the window, where the background
    ## is not drawn.
  
    style.say_who_window.top_padding = 0
    style.say_who_window.bottom_padding = 0
    style.say_who_window.left_padding = 32
    style.say_who_window.right_padding = 8
    
    ## Padding is space inside the window, where the background is drawn. 
    
    style.window.left_padding = 40
    style.window.right_padding = 40
    style.window.top_padding = 29
    style.window.bottom_padding = 10

    ## This is the minimum height of the window, including the margins and padding.
    
    style.say_who_window.xminimum = 20
    #style.window.yminimum = 200


    #########################################
    ## These let you customize the default font used for text in Ren'Py.

    ## The file containing the default font.

    #style.default.font = "uabsans.ttf"
    #style.default.line_overlap_split = 2
    #style.default.line_spacing = 1
    
    
    ## The default size of text.

    # style.default.size = 22 # für die DejaVuSans.ttf
    style.default.size = 26
    
    ## Note that these only change the size of some of the text. Other
    ## buttons have their own styles.

    #########################################
    ## These let you customize the default font used for text in Ren'Py.

    ## The file containing the default font.

    ##to do: UNIFONT BENUTZEN###
    #style.default.font = "uabsans.ttf"
    #style.default.line_overlap_split = 2
    #style.default.line_spacing = 1
    
    
    ## The default size of text.

    # style.default.size = 22 # für die DejaVuSans.ttf
    style.default.size = 26
    
    ## Note that these only change the size of some of the text. Other
    ## buttons have their own styles.

    #########################################
    ## These settings let you change some of the sounds that are used by
    ## Ren'Py.

    ## Set this to False if the game does not have any sound effects.

    config.has_sound = True

    ## Set this to False if the game does not have any music.

    config.has_music = True

    ## Set this to False if the game does not have voicing.

    config.has_voice = False

    ## Sounds that are used when button and imagemaps are clicked.

    # style.button.activate_sound = "click.wav"
    # style.imagemap.activate_sound = "click.wav"

    ## Sounds that are used when entering and exiting the game menu.

    # config.enter_sound = "click.wav"
    #config.exit_sound = "sound/button_click.ogg"

    ## A sample sound that can be played to check the sound volume.

    # config.sample_sound = "click.wav"

    ## Music that is played while the user is at the main menu.

    config.main_menu_music = False

    #########################################
    ## Default values of Preferences.

    ## Note: These options are only evaluated the first time a
    ## game is run. To have them run a second time, delete
    ## game/saves/persistent

    ## Should we start in fullscreen mode?

    config.default_fullscreen = True

    ## The default text speed in characters per second. 0 is infinite.

    config.default_text_cps = 30

    #########################################



