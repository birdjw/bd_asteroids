# Asteroids Game - Boot.dev Learning Project

A classic Asteroids game built with Python and Pygame as part of the Boot.dev curriculum to learn multi-file project structure and working with external libraries.

## 🎮 About The Game

This is a recreation of the classic Atari Asteroids game where you pilot a spaceship through an asteroid field, shooting and splitting asteroids while trying to survive as long as possible.

### Gameplay
- Control a triangular spaceship in 2D space
- Rotate left/right and move forward/backward
- Shoot bullets to destroy asteroids
- Large asteroids split into smaller ones when hit
- Game ends when your ship collides with an asteroid

### Controls
- `A` - Rotate left
- `D` - Rotate right
- `W` - Move forward
- `S` - Move backward
- `SPACE` - Shoot

## 🛠️ Technologies Used

- **Python** (71.6%) - Main game logic and object-oriented programming
- **Pygame** - Game engine for rendering, input handling, and sprite management
- **HTML/JavaScript/CSS** (25.4%) - Supporting files from the virtual environment

## 📚 Key Learning Objectives

This project demonstrates proficiency in several important Python development concepts:

### 1. **Multi-File Project Structure**
The codebase is organized into separate modules, each with a specific responsibility:
- `main.py` - Game loop and initialization
- `player.py` - Player spaceship logic
- `asteroid.py` - Asteroid behavior and splitting
- `shot.py` - Bullet mechanics
- `circleshape.py` - Base class for circular game objects
- `asteroidfield.py` - Asteroid spawning system
- `constants.py` - Centralized game configuration

### 2. **Object-Oriented Programming**
- **Inheritance**: All game objects (`Player`, `Asteroid`, `Shot`) inherit from the `CircleShape` base class
- **Polymorphism**: Each subclass implements its own `draw()` and `update()` methods
- **Encapsulation**: Game objects manage their own position, velocity, and behavior
- **Class containers**: Using Pygame's sprite group system with class-level container attributes

### 3. **Working with External Libraries**
- **Pygame integration**: Leveraging Pygame's sprite system, collision detection, and rendering
- **Dependency management**: Using `requirements.txt` to specify project dependencies
- **Virtual environment**: Understanding isolation of project dependencies

### 4. **Game Development Patterns**
- **Game loop**: Implementing the classic update-draw loop at 60 FPS
- **Delta time (dt)**: Frame-rate independent movement and updates
- **Sprite groups**: Managing collections of game objects (`updatable`, `drawable`, `asteroids`, `shots`)
- **Collision detection**: Circle-based collision using distance calculations

### 5. **Vector Mathematics**
- Using `pygame.Vector2` for position and velocity
- Rotation transformations for ship orientation
- Velocity calculations for movement and projectiles

### 6. **Game Mechanics Implementation**
- **Shot cooldown system**: Limiting fire rate with `shot_limiter`
- **Asteroid splitting**: Creating smaller asteroids with randomized angles
- **Edge spawning**: Asteroids spawn from screen edges with random velocities
- **Continuous spawning**: Timer-based asteroid generation

## 🚀 Running the Game

### Prerequisites
- Python 3.12+
- pip

### Installation
```bash
# Clone the repository
git clone https://github.com/birdjw/bd_asteroids.git
cd bd_asteroids

# Create and activate virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the game
python main.py
```

## 🎯 Code Highlights

### Collision Detection
The game implements circular collision detection in `circleshape.py`:
```python
def collision_check(self, Asteroid):
    radii_sum = self.radius + Asteroid.radius
    if self.position.distance_to(Asteroid.position) <= radii_sum:
        return True
    else:
        return False
```

### Asteroid Splitting Mechanic
When hit, asteroids split into two smaller asteroids moving in different directions:
```python
def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
        return
    else:
        random_angle = random.uniform(20, 50)
        new_angle_1 = self.velocity.rotate(random_angle)
        new_angle_2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        # Create two new smaller asteroids...
```

### Player Movement with Rotation
The player ship uses vector rotation for directional movement:
```python
def move(self, dt):
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    self.position += forward * PLAYER_SPEED * dt
```

## 🧠 What I Learned

Through building this project, I gained hands-on experience with:

1. **Project Architecture** - How to structure a multi-file Python project with clear separation of concerns
2. **Pygame Library** - Working with a real-world game development library including sprites, rendering, and input handling
3. **OOP Design Patterns** - Creating reusable base classes and extending them with specific behavior
4. **Game Math** - Vector operations, rotations, and collision detection algorithms
5. **Dependency Management** - Using virtual environments and requirements files for reproducible builds
6. **Game Loop Architecture** - Implementing the standard game development pattern of input → update → render

## 📝 License

This is a learning project created as part of the Boot.dev curriculum.

## 🙏 Acknowledgments

- [Boot.dev](https://boot.dev) for the excellent project-based curriculum
- Atari for the original Asteroids game concept
- Pygame community for the excellent game development library
