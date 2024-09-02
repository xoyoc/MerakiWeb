import reflex as rx

COLOR_MERAKI="#A198C4"
COLOR_DEFAULT="#EDEDED"

buttonMeraki={
    "font_family":"Plus Jakarta Sans",
    "background": COLOR_MERAKI,
    "box_shadow": "0px 4px 4px rgba(0, 0, 0, 0.25)",
    "border_radius": "1.5em",
    "width": "11em",
    "min_width": "5em",
    "max_width": "30em",
    "height": "3em",
}
buttonDefault={
    "width": "11em",
    "min_width": "5em",
    "max_width": "30em",
    "height": "3em",
    "color": COLOR_MERAKI,
    "background": COLOR_DEFAULT,
    "border_radius": "1.5em",
}

BASE_STYLE={
    rx.el.body:{
        "color":COLOR_MERAKI, 
        "font_family":"Plus Jakarta Sans",
        "line_height":"1.5em",        
    },
    rx.text:{
        "color":COLOR_MERAKI, 
        "font_family":"Plus Jakarta Sans",
        "line_height":"1.5em",         
    },
    rx.heading:{
        "color":COLOR_MERAKI, 
        "font_family":"Plus Jakarta Sans",        
    },
    rx.icon:{
        "color":COLOR_MERAKI,
    }
}




