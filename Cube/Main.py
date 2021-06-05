from Cube.Header import Cube

cube = Cube()
c = cube.createCube(36)

area = cube.cubeArea(c)
volume = cube.cubeVolume(c)
lado = cube.cubeSide(c)

print(f'A area do cubo é: {area}')
print(f'O volume do cubo é: {volume}')
print(f'Os lados do cubo medem: {lado}')