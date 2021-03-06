from esai import vec2, vec3, vec4, mat4, Mesh, homogeneous_to_cartesian, cartesian_to_homogeneous
from math import pi
from typing import Tuple, List
import pygame.draw as draw
from threading import Thread

class Transform:
    def __init__(self, position : vec3, rotation : vec3, scale : vec3):
        self.position = position
        self.rotation = rotation
        self.scale    = scale
    
    def get_model_view(self) -> mat4:
        matrix = mat4.translation(self.position)

        if (self.rotation.x != 0.0): matrix @= mat4.rotation_x(self.rotation.x)
        if (self.rotation.y != 0.0): matrix @= mat4.rotation_y(self.rotation.y)
        if (self.rotation.z != 0.0): matrix @= mat4.rotation_z(self.rotation.z)
        if self.scale.x != 1.0 or self.scale.y != 1.0 or self.scale.z != 1.0:
            matrix @= mat4.scale(self.scale)
        
        return matrix
    
    @staticmethod
    def identity() -> 'Transform':
        return Transform(vec3.zero(), vec3.zero(), vec3.one())
    
    @staticmethod
    def zero() -> 'Transform':
        return Transform(vec3.zero(), vec3.zero(), vec3.zero())
    
    def __str__(self) -> str:
        return f"(position={self.position}, rotation={self.rotation}, scale={self.scale})"
    
    def __repr__(self) -> str:
        return f"Transform({repr(self.position)}, {repr(self.rotation)}, {repr(self.scale)})"

class Camera:
    def __init__(self, transform : Transform, fov : float, size : Tuple[int, int], clip_near : float, clip_far : float):
        self.transform   = transform
        self.fov         = fov
        self.size        = size
        self.half_size   = (size[0] // 2, size[1] // 2)
        self.clip_near   = clip_near
        self.clip_far    = clip_far
        self.view_matrix = mat4.identity()
        self.update_projection()
        self.update()
    
    def update(self):
        self.view_matrix = self.transform.get_model_view().invert()

    def update_projection(self):
        self.projection_matrix = mat4.projection(
            (180.0 - self.fov) * pi / 180.0,
            min(self.size) / max(self.size),
            self.clip_far, self.clip_near
        )
        self.clip = (self.clip_far - self.clip_near) / 2.0 + self.clip_near
    
    def transform_viewport(self, vec : vec3) -> Tuple[Tuple[int, int], float]:
        return (
            int((vec.x + 1.0) * self.half_size[0]),
            int((vec.y + 1.0) * self.half_size[1])
        ), (vec.z + 1.0) * self.clip
    
    def clear(self, surface):
        surface.fill((0,0,0))

    def render_wireframe(self, surface, transform : Transform, mesh : Mesh):
        mvp = self.projection_matrix @ self.view_matrix @ transform.get_model_view()

        h_to_c = homogeneous_to_cartesian
        c_to_h = cartesian_to_homogeneous
        draw_lines = draw.lines
        trans_viewport = self.transform_viewport

        for a, b, c in mesh.triangles:
            a, b, c = h_to_c(mvp * c_to_h(a)), h_to_c(mvp * c_to_h(b)), h_to_c(mvp * c_to_h(c))

            clip_a = (a.x > 1.0 or a.y > 1.0 or a.z > 1.0 or a.x < -1.0 or a.y < -1.0 or a.z < -1.0)
            clip_b = (b.x > 1.0 or b.y > 1.0 or b.z > 1.0 or b.x < -1.0 or b.y < -1.0 or b.z < -1.0)
            clip_c = (c.x > 1.0 or c.y > 1.0 or c.z > 1.0 or c.x < -1.0 or c.y < -1.0 or c.z < -1.0)
            
            if (3 - (clip_a + clip_b + clip_c)) > 1:
                if clip_a:
                    draw_lines(surface, (255, 255, 255), True, [trans_viewport(b)[0], trans_viewport(c)[0]], 1)
                elif clip_b:
                    draw_lines(surface, (255, 255, 255), True, [trans_viewport(a)[0], trans_viewport(c)[0]], 1)
                elif clip_c:
                    draw_lines(surface, (255, 255, 255), True, [trans_viewport(a)[0], trans_viewport(b)[0]], 1)
                else:
                    draw_lines(surface, (255, 255, 255), True, [trans_viewport(a)[0], trans_viewport(b)[0], trans_viewport(c)[0]], 1)
    
    def resize(self, size : Tuple[int, int]):
        self.size      = size
        self.half_size = (size[0] // 2, size[1] // 2)
        self.update_projection()
    
    def __str__(self):
        return f"<Camera at {self.transform.position}, fov={self.fov}, size={self.size}>"
    
    def __repr__(self):
        return f"<Camera at {self.transform.position}, fov={self.fov}, size={self.size}>"

class GameObject:
    def __init__(self, name : str, transform : Transform, mesh : Mesh, bias : Transform, color : Tuple[int, int, int]):
        self.name      = name
        self.transform = transform
        self.mesh      = mesh
        self.bias      = bias
        self.color     = color
    
    def render_wireframe(self, surface, camera: Camera):
        camera.render_wireframe(surface, self.transform, self.mesh)
    
    def render_solid(self, surface, camera: Camera):
        camera.render_solid(surface, self.transform, self.mesh, self.color)
    
    def update(self, delta_time : float):
        self.transform.position += self.bias.position * delta_time
        self.transform.rotation += self.bias.rotation * delta_time
        self.transform.scale    += self.bias.scale    * delta_time
    
    def __str__(self):
        return f"<GameObject '{self.name}' at {self.transform.position}>"
    
    def __repr__(self):
        return f"<GameObject '{self.name}' at {self.transform.position}>"