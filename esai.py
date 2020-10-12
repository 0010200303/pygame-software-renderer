from typing import Union, Tuple, List
from math import sqrt, cos, sin, inf

class vec2:
    def __init__(self, x : float, y : float):
        self.x, self.y = x, y
    
    def __add__(self, operand : Union['vec2', float]) -> 'vec2':
        if isinstance(operand, vec2):
            return vec2(self.x + operand.x, self.y + operand.y)
        elif isinstance(operand, float):
            return vec2(self.x + operand, self.y + operand)
        else:
            raise TypeError('vec2 or float expected')
    
    def __sub__(self, operand : Union['vec2', float]) -> 'vec2':
        if isinstance(operand, vec2):
            return vec2(self.x - operand.x, self.y - operand.y)
        elif isinstance(operand, float):
            return vec2(self.x - operand, self.y - operand)
        else:
            raise TypeError('vec2 or float expected')
    
    def __mul__(self, operand : Union['vec2', float]) -> 'vec2':
        if isinstance(operand, vec2):
            return vec2(self.x * operand.x, self.y * operand.y)
        elif isinstance(operand, float):
            return vec2(self.x * operand, self.y * operand)
        else:
            raise TypeError('vec2 or float expected')
    
    def __div__(self, operand : Union['vec2', float]) -> 'vec2':
        if isinstance(operand, vec2):
            return vec2(self.x / operand.x, self.y / operand.y)
        elif isinstance(operand, float):
            return vec2(self.x / operand, self.y / operand)
        else:
            raise TypeError('vec2 or float expected')
    
    def magnitude(self) -> float:
        return sqrt(self.x * self.x + self.y * self.y)
    
    @staticmethod
    def zero() -> 'vec2':
        return vec2(0.0, 0.0)
    
    @staticmethod
    def one() -> 'vec2':
        return vec2(1.0, 1.0)
    
    @staticmethod
    def distance(a : 'vec2', b : 'vec2') -> float:
        return sqrt((b.x - a.x) ** 2 + (b.y - a.y) ** 2)
    
    @staticmethod
    def lerp(a : 'vec2', b : 'vec2', time : float) -> 'vec2':
        return vec2(
            a.x + time * (b.x - a.x),
            a.y + time * (b.y - a.y)
        )
    
    def to_vec3(self) -> 'vec3':
        return vec3(self.x, self.y, 0.0)
    
    def to_vec4(self) -> 'vec4':
        return vec4(self.x, self.y, 0.0, 0.0)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    
    def __repr__(self) -> str:
        return f"vec2({self.x}, {self.y})"

class vec3:
    def __init__(self, x : float, y : float, z : float):
        self.x, self.y, self.z = x, y, z
    
    def __add__(self, operand : Union['vec3', float]) -> 'vec3':
        if isinstance(operand, vec3):
            return vec3(self.x + operand.x, self.y + operand.y, self.z + operand.z)
        elif isinstance(operand, float):
            return vec3(self.x + operand, self.y + operand, self.z + operand)
        else:
            raise TypeError('vec3 or float expected')
    
    def __sub__(self, operand : Union['vec3', float]) -> 'vec3':
        if isinstance(operand, vec3):
            return vec3(self.x - operand.x, self.y - operand.y, self.z - operand.z)
        elif isinstance(operand, float):
            return vec3(self.x - operand, self.y - operand, self.z - operand)
        else:
            raise TypeError('vec3 or float expected')
    
    def __mul__(self, operand : Union['vec3', float]) -> 'vec3':
        if isinstance(operand, vec3):
            return vec3(self.x * operand.x, self.y * operand.y, self.z * operand.z)
        elif isinstance(operand, float):
            return vec3(self.x * operand, self.y * operand, self.z * operand)
        else:
            raise TypeError('vec3 or float expected')
    
    def __div__(self, operand : Union['vec3', float]) -> 'vec3':
        if isinstance(operand, vec3):
            return vec3(self.x / operand.x, self.y / operand.y, self.z / operand.z)
        elif isinstance(operand, float):
            return vec3(self.x / operand, self.y / operand, self.z / operand)
        else:
            raise TypeError('vec3 or float expected')
    
    def magnitude(self) -> float:
        return sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
    
    @staticmethod
    def zero() -> 'vec3':
        return vec3(0.0, 0.0, 0.0)
    
    @staticmethod
    def one() -> 'vec3':
        return vec3(1.0, 1.0, 1.0)
    
    @staticmethod
    def distance(a : 'vec3', b : 'vec3') -> float:
        return sqrt((b.x - a.x) ** 2 + (b.y - a.y) ** 2 + (b.z - a.z) ** 2)
    
    @staticmethod
    def lerp(a : 'vec3', b : 'vec3', time : float) -> 'vec3':
        return vec3(
            a.x + time * (b.x - a.x),
            a.y + time * (b.y - a.y),
            a.z + time * (b.z - a.z)
        )
    
    def to_vec2(self) -> 'vec2':
        return vec2(self.x, self.y)
    
    def to_vec4(self) -> 'vec4':
        return vec4(self.x, self.y, self.z, 0.0)

    def to_homogenous(self) -> 'vec4':
        return vec4(self.x, self.y, self.z, 1.0)
    
    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"
    
    def __repr__(self) -> str:
        return f"vec3({self.x}, {self.y}, {self.z})"

class vec4:
    def __init__(self, x : float, y : float, z : float, w : float):
        self.x, self.y, self.z, self.w = x, y, z, w
    
    def __add__(self, operand : Union['vec4', float]) -> 'vec4':
        if isinstance(operand, vec4):
            return vec4(self.x + operand.x, self.y + operand.y, self.z + operand.z, self.w + operand.w)
        elif isinstance(operand, float):
            return vec4(self.x + operand, self.y + operand, self.z + operand, self.w + operand.w)
        else:
            raise TypeError('vec4 or float expected')
    
    def __sub__(self, operand : Union['vec4', float]) -> 'vec4':
        if isinstance(operand, vec4):
            return vec4(self.x - operand.x, self.y - operand.y, self.z - operand.z, self.w - operand.w)
        elif isinstance(operand, float):
            return vec4(self.x - operand, self.y - operand, self.z - operand, self.w - operand)
        else:
            raise TypeError('vec4 or float expected')
    
    def __mul__(self, operand : Union['vec4', float]) -> 'vec4':
        if isinstance(operand, vec4):
            return vec4(self.x * operand.x, self.y * operand.y, self.z * operand.z, self.w * operand.w)
        elif isinstance(operand, float):
            return vec4(self.x * operand, self.y * operand, self.z * operand, self.w * operand)
        else:
            raise TypeError('vec4 or float expected')
    
    def __div__(self, operand : Union['vec4', float]) -> 'vec4':
        if isinstance(operand, vec4):
            return vec4(self.x / operand.x, self.y / operand.y, self.z / operand.z, self.w / operand.w)
        elif isinstance(operand, float):
            return vec4(self.x / operand, self.y / operand, self.z / operand, self.w / operand)
        else:
            raise TypeError('vec4 or float expected')
    
    def magnitude(self) -> float:
        return sqrt(self.x * self.x + self.y * self.y + self.z * self.z + self.w * self.w)
    
    @staticmethod
    def zero() -> 'vec4':
        return vec4(0.0, 0.0, 0.0, 0.0)
    
    @staticmethod
    def one() -> 'vec4':
        return vec4(1.0, 1.0, 1.0, 1.0)
    
    @staticmethod
    def distance(a : 'vec4', b : 'vec4') -> float:
        return sqrt((b.x - a.x) ** 2 + (b.y - a.y) ** 2 + (b.z - a.z) ** 2 + (b.w - a.w) ** 2)
    
    @staticmethod
    def lerp(a : 'vec4', b : 'vec4', time : float) -> 'vec4':
        return vec4(
            a.x + time * (b.x - a.x),
            a.y + time * (b.y - a.y),
            a.z + time * (b.z - a.z),
            a.w + time * (b.w - a.w)
        )
    
    def to_vec2(self) -> 'vec2':
        return vec2(self.x, self.y)
    
    def to_vec3(self) -> 'vec3':
        return vec3(self.x, self.y, self.z)

    def to_cartesian(self) -> 'vec3':
        return vec3(self.x / self.w, self.y / self.w, self.z / self.w)
    
    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z}, {self.w})"
    
    def __repr__(self) -> str:
        return f"vec4({self.x}, {self.y}, {self.z}, {self.w})"

class mat4:
    def __init__(self, a : float, b : float, c : float, d : float, e : float, f : float, g : float, h : float, i : float, j : float, k : float, l : float, m : float, n : float, o : float, p : float):
        self.a, self.b, self.c, self.d, self.e, self.f, self.g, self.h, self.i, self.j, self.k, self.l, self.m, self.n, self.o, self.p = a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p

    def __mul__(self, operand : Union[vec4, 'mat4']) -> Union[vec4, 'mat4']:
        if isinstance(operand, mat4):
            return mat4(
                self.a * operand.a + self.b * operand.e + self.c * operand.i + self.d * operand.m,
                self.a * operand.b + self.b * operand.f + self.c * operand.j + self.d * operand.n,
                self.a * operand.c + self.b * operand.g + self.c * operand.k + self.d * operand.o,
                self.a * operand.d + self.b * operand.h + self.c * operand.l + self.d * operand.p,
                self.e * operand.a + self.f * operand.e + self.g * operand.i + self.h * operand.m,
                self.e * operand.b + self.f * operand.f + self.g * operand.j + self.h * operand.n,
                self.e * operand.c + self.f * operand.g + self.g * operand.k + self.h * operand.o,
                self.e * operand.d + self.f * operand.h + self.g * operand.l + self.h * operand.p,
                self.i * operand.a + self.j * operand.e + self.k * operand.i + self.l * operand.m,
                self.i * operand.b + self.j * operand.f + self.k * operand.j + self.l * operand.n,
                self.i * operand.c + self.j * operand.g + self.k * operand.k + self.l * operand.o,
                self.i * operand.d + self.j * operand.h + self.k * operand.l + self.l * operand.p,
                self.m * operand.a + self.n * operand.e + self.o * operand.i + self.p * operand.m,
                self.m * operand.b + self.n * operand.f + self.o * operand.j + self.p * operand.n,
                self.m * operand.c + self.n * operand.g + self.o * operand.k + self.p * operand.o,
                self.m * operand.d + self.n * operand.h + self.o * operand.l + self.p * operand.p
            )
        elif isinstance(operand, vec4):
            return vec4(
                self.a * operand.x + self.b * operand.y + self.c * operand.z + self.d * operand.w,
                self.e * operand.x + self.f * operand.y + self.g * operand.z + self.h * operand.w,
                self.i * operand.x + self.j * operand.y + self.k * operand.z + self.l * operand.w,
                self.m * operand.x + self.n * operand.y + self.o * operand.z + self.p * operand.w
            )
        else:
            raise TypeError('vec4 or mat4 expected')
    
    def invert(self) -> 'mat4':
        inverse = mat4(
             self.f * self.k * self.p - self.f * self.l * self.o - self.j * self.g * self.p + self.j * self.h * self.o + self.n * self.g * self.l - self.n * self.h * self.k,
            -self.b * self.k * self.p + self.b * self.l * self.o + self.j * self.c * self.p - self.j * self.d * self.o - self.n * self.c * self.l + self.n * self.d * self.k,
             self.b * self.g * self.p - self.b * self.h * self.o - self.f * self.c * self.p + self.f * self.d * self.o + self.n * self.c * self.h - self.n * self.d * self.g,
            -self.b * self.g * self.l + self.b * self.h * self.k + self.f * self.c * self.l - self.f * self.d * self.k - self.j * self.c * self.h + self.j * self.d * self.g,
            -self.e * self.k * self.p + self.e * self.l * self.o + self.i * self.g * self.p - self.i * self.h * self.o - self.m * self.g * self.l + self.m * self.h * self.k,
             self.a * self.k * self.p - self.a * self.l * self.o - self.i * self.c * self.p + self.i * self.d * self.o + self.m * self.c * self.l - self.m * self.d * self.k,
            -self.a * self.g * self.p + self.a * self.h * self.o + self.e * self.c * self.p - self.e * self.d * self.o - self.m * self.c * self.h + self.m * self.d * self.g,
             self.a * self.g * self.l - self.a * self.h * self.k - self.e * self.c * self.l + self.e * self.d * self.k + self.i * self.c * self.h - self.i * self.d * self.g,
             self.e * self.j * self.p - self.e * self.l * self.n - self.i * self.f * self.p + self.i * self.h * self.n + self.m * self.f * self.l - self.m * self.h * self.j,
            -self.a * self.j * self.p + self.a * self.l * self.n + self.i * self.b * self.p - self.i * self.d * self.n - self.m * self.b * self.l + self.m * self.d * self.j,
             self.a * self.f * self.p - self.a * self.h * self.n - self.e * self.b * self.p + self.e * self.d * self.n + self.m * self.b * self.h - self.m * self.d * self.f,
            -self.a * self.f * self.l + self.a * self.h * self.j + self.e * self.b * self.l - self.e * self.d * self.j - self.i * self.b * self.h + self.i * self.d * self.f,
            -self.e * self.j * self.o + self.e * self.k * self.n + self.i * self.f * self.o - self.i * self.g * self.n - self.m * self.f * self.k + self.m * self.g * self.j,
             self.a * self.j * self.o - self.a * self.k * self.n - self.i * self.b * self.o + self.i * self.c * self.n + self.m * self.b * self.k - self.m * self.c * self.j,
            -self.a * self.f * self.o + self.a * self.g * self.n + self.e * self.b * self.o - self.e * self.c * self.n - self.m * self.b * self.g + self.m * self.c * self.f,
             self.a * self.f * self.k - self.a * self.g * self.j - self.e * self.b * self.k + self.e * self.c * self.j + self.i * self.b * self.g - self.i * self.c * self.f
        )
        
        determinant = self.a * inverse.a + self.b * inverse.e + self.c * inverse.i + self.d * inverse.m
        if determinant == 0:
            raise Exception("Matrix can't be inverted.")
        determinant = 1.0 / determinant

        return mat4(
            inverse.a * determinant, inverse.b * determinant, inverse.c * determinant, inverse.d * determinant,
            inverse.e * determinant, inverse.f * determinant, inverse.g * determinant, inverse.h * determinant,
            inverse.i * determinant, inverse.j * determinant, inverse.k * determinant, inverse.l * determinant,
            inverse.m * determinant, inverse.n * determinant, inverse.o * determinant, inverse.p * determinant
        )
    
    @staticmethod
    def identity() -> 'mat4':
        return mat4(
            1.0, 0.0, 0.0, 0.0,
            0.0, 1.0, 0.0, 0.0,
            0.0, 0.0, 1.0, 0.0,
            0.0, 0.0, 0.0, 1.0
        )
    
    @staticmethod
    def translation(vec : vec3) -> 'mat4':
        return mat4(
            1.0, 0.0, 0.0, vec.x,
            0.0, 1.0, 0.0, vec.y,
            0.0, 0.0, 1.0, vec.z,
            0.0, 0.0, 0.0, 1.0
        )
    
    @staticmethod
    def rotation_x(theta : float) -> 'mat4':
        return mat4(
            1.0, 0.0,         0.0,        0.0,
            0.0,  cos(theta), sin(theta), 0.0,
            0.0, -sin(theta), cos(theta), 0.0,
            0.0, 0.0,         0.0,        1.0
        )
    
    @staticmethod
    def rotation_y(theta : float) -> 'mat4':
        return mat4(
            cos(theta),  0.0, sin(theta), 0.0,
            0.0,         1.0, 0.0,        0.0,
            -sin(theta), 0.0, cos(theta), 0.0,
            0.0,         0.0, 0.0,        1.0
        )
    
    @staticmethod
    def rotation_z(theta : float) -> 'mat4':
        return mat4(
            cos(theta), -sin(theta), 0.0, 0.0,
            sin(theta),  cos(theta), 0.0, 0.0,
            0.0,         0.0,        1.0, 0.0,
            0.0,         0.0,        0.0, 1.0
        )
    
    @staticmethod
    def scale(vec : vec3) -> 'mat4':
        return mat4(
            vec.x, 0.0,   0.0,   0.0,
            0.0,   vec.y, 0.0,   0.0,
            0.0,   0.0,   vec.z, 0.0,
            0.0,   0.0,   0.0,   1.0
        )
    
    @staticmethod
    def projection(fov : float, aspect_ratio : float, far : float, near : float) -> 'mat4':
        return mat4(
            fov * aspect_ratio, 0.0, 0.0,                       0.0,
            0.0,                fov, 0.0,                       0.0,
            0.0,                0.0, (far + near)/(far - near), (2 * near * far)/(near-far),
            0.0,                0.0, 1.0,                       0.0
        )

    def __str__(self) -> str:
        values  = [self.a, self.b, self.c, self.d, self.e, self.f, self.g, self.h, self.i, self.j, self.k, self.l, self.m, self.n, self.o, self.p]
        length  = max(map(lambda v: len(str(v)), values))
        strings = list(map(lambda v: str(v).rjust(length), values))
        row0    = ', '.join(strings[ 0: 4])
        row1    = ', '.join(strings[ 4: 8])
        row2    = ', '.join(strings[ 8:12])
        row3    = ', '.join(strings[12:16])
        return f'[{row0}]\n[{row1}]\n[{row2}]\n[{row3}]'
    
    def __repr__(self) -> str:
        values = [self.a, self.b, self.c, self.d, self.e, self.f, self.g, self.h, self.i, self.j, self.k, self.l, self.m, self.n, self.o, self.p]
        return "mat4(%s)"  % (', '.join(map(lambda v: str(v), values)), )

class Mesh:
    def __init__(self, triangles : List[Tuple[vec3, vec3, vec3]]):
        self.triangles  = triangles
    
    @staticmethod
    def load_obj(path : str) -> 'Mesh':
        with open(path, 'r') as fp:
            lines = fp.read().splitlines()
            fp.close()
        
        in_vertices : List[vec3] = []
        in_indices  : List[Tuple[int, int, int]] = []
        
        for line in lines:
            if line.startswith('v'):
                in_vertices.append(vec3(*tuple(map(lambda v: float(v), line.split(' ')[1:]))))
            elif line.startswith('f'):
                line = map(lambda v: v.split('/')[0], line.split(' ')[1:])
                in_indices.append(tuple(map(lambda v: int(v), line)))
        
        out_triangles = []

        for a, b, c in in_indices:
            out_triangles.append([in_vertices[a - 1], in_vertices[b - 1], in_vertices[c - 1]])
        
        return Mesh(out_triangles)
    
    def __str__(self) -> str:
        return f"(Mesh, {len(self.triangles)} tri(s))"
    
    def __repr__(self) -> str:
        return f"(Mesh, {len(self.triangles)} tri(s))"