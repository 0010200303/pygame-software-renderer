from world import Camera, Transform, GameObject, Mesh, vec2, vec3
from math import sin
import pygame

size = (800, 600)

pygame.init()
surface   = pygame.display.set_mode(size, pygame.RESIZABLE)
running   = True
time      = 0.0
fps_count = 0
fps_time  = 0.0

clock     = pygame.time.Clock()
camera    = Camera(Transform.identity(), 120.0, size, 0.001, 1000.0)

objects   = [
    GameObject(
        'cube',
        Transform(vec3(0.0, 0.0, -5.0), vec3(0.0, 0.0, 0.0), vec3.one()),
        Mesh.load_obj('meshes/cube.obj'),
        Transform(vec3.zero(), vec3(0.0, 1.0, 1.0), vec3.zero()),
        (255, 255, 255)
    ),
    GameObject(
        'cube',
        Transform(vec3(0.0, 0.0, 5.0), vec3(0.0, 0.0, 0.0), vec3.one()),
        Mesh.load_obj('meshes/cube.obj'),
        Transform(vec3.zero(), vec3(1.0, 1.0, 0.0), vec3.zero()),
        (255, 255, 255)
    ),
    GameObject(
        'icosphere',
        Transform(vec3(5.0, 0.0, 0.0), vec3(0.0, 0.0, 0.0), vec3.one()),
        Mesh.load_obj('meshes/icosphere.obj'),
        Transform(vec3.zero(), vec3(1.0, 1.0, 0.0), vec3.zero()),
        (255, 255, 255)
    ),
    GameObject(
        'icosphere',
        Transform(vec3(-5.0, 0.0, 0.0), vec3(0.0, 0.0, 0.0), vec3.one()),
        Mesh.load_obj('meshes/icosphere.obj'),
        Transform(vec3.zero(), vec3(1.0, 1.0, 0.0), vec3.zero()),
        (255, 255, 255)
    )
]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            size    = (event.w, event.h)
            surface = pygame.display.set_mode(size, pygame.RESIZABLE)
            camera.resize(size)
    
    delta_time = clock.tick(240) / 1000.0
    fps_time  += delta_time
    time      += delta_time

    fps_count += 1
    if fps_time >= 1.0:
        print(f'FPS = {fps_count}')
        fps_time -= 1.0
        fps_count = 0

    for obj in objects:
        obj.update(delta_time)

    camera.transform.rotation.y -= delta_time

    camera.clear(surface)
    for obj in objects:
        obj.render_wireframe(surface, camera)

    pygame.display.update()