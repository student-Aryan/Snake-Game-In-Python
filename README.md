🐍 Enhanced Snake Game In Python

A modern twist on the classic Snake game, built with Python and Pygame. This version features vibrant emoji graphics for both the snake and the food, dynamic sound effects, and a user-friendly GUI interface.


## 🎮 Features

* **Emoji Graphics**: The snake and food are represented using customizable emoji images, adding a fun visual element.
* **Sound Effects**: Enjoy background music and sound effects for eating food and game over events.
* **High Score Tracking**: The game keeps track of the highest score achieved.
* **GUI Interface**: Start the game with an intuitive GUI start screen using `pygame_gui`.
* **Responsive Controls**: Smooth and responsive controls for an enjoyable gaming experienc
  
🚀 Getting Started

Prerequisites

Ensure you have the following installed:

* Python 3.10 and above
* Pygame
* pygame\_gui

### Installation

1. **Clone the repository**:([YouTube][2])

   ```bash
   git clone https://github.com/yourusername/enhanced-snake-game.git
   cd enhanced-snake-game
   ```

2. **Install dependencies**:

   ```bash
   pip install pygame pygame_gui
   ```
   
3. **Add Assets**:

   Place your emoji images and sound files in the project directory:

   * `snake.png`: Image representing the snake segment.
   * `Food.png`: Image representing the food.
   * `eat.wav`: Sound played when the snake eats food.
   * `gameover.wav`: Sound played when the game is over.
   * `background.mp3`: Background music for the game.

  *Ensure these files are named exactly as above or update the filenames in the code accordingly.
   
🕹️ Usage

Run the game using the following command:

Use the arrow keys to control the snake:

* **Left Arrow**: Move left
* **Right Arrow**: Move right
* **Up Arrow**: Move up
* **Down Arrow**: Move down

Avoid colliding with the walls or the snake's own body. Eat the food to grow longer and increase your score.

📝 Customization

* **Changing Emojis**: Replace `snake.png` and `Food.png` with your preferred emoji images. Ensure they are square images for best results.
* **Adjusting Size**: Modify the `snake_block` variable in the code to increase or decrease the size of the snake and food.
* **Sound Effects**: Replace the sound files with your own to customize the game's audio experience.

📄 License

This project is licensed under the [MIT License](LICENSE).

🙌 Acknowledgments

* [Pygame](https://www.pygame.org/) for providing the game development library.
* [pygame\_gui](https://pygame-gui.readthedocs.io/en/latest/) for the GUI components.
* Emoji images sourced from [EmojiOne](https://www.emojione.com/) or [Twemoji](https://twemoji.twitter.com/).
* Sound effects obtained from [FreeSound](https://freesound.org/).

*Feel free to contribute to this project by submitting issues or pull requests. Your feedback and improvements are welcome!*
