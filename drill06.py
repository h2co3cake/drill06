from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global running
    global x, y
    global hand_x, hand_y
    global LR

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_MOUSEMOTION:
            hand_x, hand_y = event.x + 20, KPU_HEIGHT - 1 - event.y - 30

        elif event.type == SDL_MOUSEBUTTONDOWN:
            if x < event.x:
                x, y, LR = event.x, KPU_HEIGHT - 1 - event.y, 1

            elif event.x < x:
                x, y, LR = event.x, KPU_HEIGHT - 1 - event.y, 0

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
x1, y1 = KPU_WIDTH // 2, KPU_HEIGHT // 2
hand_x, hand_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
LR = 1
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    hand.draw_now(hand_x, hand_y)
    character.clip_draw(frame * 100, 100 * LR, 100, 100, x1, y1)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8

    if x1 < x and y1 < y:
        x1 += 10
        y1 += 10
 

    delay(0.05)

close_canvas()