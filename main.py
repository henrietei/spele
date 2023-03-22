import pygame as pg
#from pygame .locals import * 

# Initializing Color
red = (255,0,0)
green = (0, 255, 0)
blue = (0,0,255)
 
# Drawing Rectangle


def main():
    screen = pg.display.set_mode((480, 720))
    #screen.draw.text("hello world", (20, 100))
    font = pg.font.Font(None, 100)
    clock = pg.time.Clock()
    input_box = pg.Rect(90,540,300,90)
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False
    #pg.draw.rect(screen, color1, pg.Rect(30, 30, 60, 60))
    #pg.display.flip()
    


    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        print(text)
                        text = ''
                        
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((222, 220, 220))
        # Render the current text.
        txt_surface = font.render(text, True, color)
        #screen.draw.text("hello\nworld", bottomright=(500, 400), align="left")
        #txt_surface = font.render("text", True, color)
        # Resize the box if the text is too long.
        #width = max(200, txt_surface.get_width()+10)
        width=300
        height=90
        input_box.w = width
        input_box.h = height
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pg.draw.rect(screen, color, input_box, 2)
        pg.draw.rect(screen, red, pg.Rect(30, 30, 60, 60))
        #txt_surface = font.render("text", True, color)
        

        

        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pg.init()
    main()

    pg.quit()

