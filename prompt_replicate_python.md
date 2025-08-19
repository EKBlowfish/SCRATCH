# Prompt: Recreate the Scratch RPG Demo in Python

You are a Python game developer. Your task is to rebuild the Scratch project "Scratch RPG Demo" using Python and the Pygame library. Implement the following features based on the Scratch project:

## 1. Window and Timing
- Create a 480x360 window.
- Maintain a game clock to update animations and logic every frame.

## 2. Player Character
- Sprite animations for four directions: up (90), down (180), left (-90), right (0).
- Idle frames: `idle0`, `idle90`, `idle180`, `idle-90`.
- Walking animation: six frames per direction (`walk0`..`walk0.5`, etc.).
- Attack animation: six frames per direction (`AttackB0`..`AttackB0.5`, etc.).
- Variables:
  - `_Player X`, `_Player Y` for world position.
  - `#Player Dir` to store facing direction.
  - `_Cam X`, `_Cam Y` for camera.
- Keyboard controls:
  - Arrow keys move the character and update direction.
  - Space key triggers attack animation.
- Implement collision with solid tiles (see Tile section).

## 3. Tile Map
- Use a tile grid with tile IDs referencing the scratch tiles (tile000..tile378).
- Draw background tiles first, then the player, then foreground tiles.
- Tiles can be solid (`*Solid` variable in Scratch) preventing movement.

## 4. Text Engine
- Text box area defined by variables: Page L (-190), Page T (-100), Page R (220), Page B (-162).
- Line height 22px.
- Support for scenes named like `over:0:1` and system messages stored in lists/variables.

## 5. Store and Dialogue
- Include a store level, dialogue, and scenes as in Scratch project.
- Dialogue should display using the text engine.

## 6. UI and Lives
- Track player lives (`Lives` variable) starting at 3.
- Display lives and other UI elements in a separate sprite layer.

## 7. General Structure
- Separate modules/classes for Player, Tiles, TextEngine, Store, and UI.
- Use a main game loop to update and render each component.

