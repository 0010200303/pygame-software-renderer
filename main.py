from world import Camera, Transform, GameObject, Mesh, vec2, vec3
from math import sin
from ctypes import c_uint32, POINTER
import pygame

size = (800, 600)

pygame.init()
surface   = pygame.display.set_mode(size, pygame.RESIZABLE)
buffer    = (c_uint32 * (size[0] * size[1])).from_address(surface._pixels_address)
running   = True
time      = 0.0
fps_time  = 0.0

clock     = pygame.time.Clock()
camera    = Camera(Transform.identity(), 120.0, size, 0.001, 1000.0)

objects   = [
    GameObject(
        'suzanne',
        Transform(vec3(0.0, 0.0, -5.0), vec3(0.0, 0.0, 0.0), vec3.one()),
        Mesh.load_obj('meshes/suzanne.obj'),
        Transform(vec3.zero(), vec3(0.0, 1.0, 1.0), vec3.zero()),
        (255, 255, 255)
    ),
    GameObject(
        'suzanne',
        Transform(vec3(0.0, 0.0, 5.0), vec3(0.0, 0.0, 0.0), vec3.one()),
        Mesh.load_obj('meshes/suzanne.obj'),
        Transform(vec3.zero(), vec3(1.0, 1.0, 0.0), vec3.zero()),
        (255, 255, 255)
    ),
    GameObject(
        'suzanne',
        Transform(vec3(5.0, 0.0, 0.0), vec3(0.0, 0.0, 0.0), vec3.one()),
        Mesh.load_obj('meshes/suzanne.obj'),
        Transform(vec3.zero(), vec3(1.0, 1.0, 0.0), vec3.zero()),
        (255, 255, 255)
    ),
    GameObject(
        'suzanne',
        Transform(vec3(-5.0, 0.0, 0.0), vec3(0.0, 0.0, 0.0), vec3.one()),
        Mesh.load_obj('meshes/suzanne.obj'),
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
            buffer  = (c_uint32 * (size[0] * size[1])).from_address(surface._pixels_address)
            camera.resize(size)

    pygame.display.update()

    delta_time = clock.tick(60) / 1000.0
    time      += delta_time

    if time >= 5.0:
        quit(0)
    
    fps_time += delta_time
    if fps_time >= 1.0:
        print(f'FPS = {clock.get_fps()}')
        fps_time -= 1.0

    for obj in objects:
        obj.update(delta_time)

    camera.transform.rotation.y -= delta_time
    camera.update()

    camera.clear(surface)
    for obj in objects:
        obj.render_wireframe(surface, camera)