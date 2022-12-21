from user_interface import temperature_view
from user_interface import preassure_view
from user_interface import wind_speed_view

def create(device = 1):
    style = 'style="font-size:30px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '   <p {}>Temperature: {} c</p>\n'\
        .format(style, temperature_view(device))
    html += '   <p {}>Preassure: {} c</p>\n'\
        .format(style, temperature_view(device))
    html += '   <p {}>Wind speed: {} c</p>\n'\
        .format(style, temperature_view(device))
    
    with open('index.html', 'w') as page:
        page.write(html)

    return html

def new_create(data, device = 1):
    t, p, w = data
    style = 'style="font-size:30px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '   <p {}>Temperature: {} c</p>\n'\
        .format(style, t)                           # .format(style, temperature_view(device))
    html += '   <p {}>Preassure: {} c</p>\n'\
        .format(style, p)                           # .format(style, temperature_view(device))
    html += '   <p {}>Wind speed: {} c</p>\n'\
        .format(style, w)                           # .format(style, temperature_view(device))
    
    with open('new_index.html', 'w') as page:       # index.html
        page.write(html)

    return data