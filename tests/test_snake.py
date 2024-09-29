import sys
import os
from unittest.mock import patch, MagicMock
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from snake_game.snake import Snake
from snake_game.constants import (
    STARTING_POSITIONS,
    MOVE_DISTANCE,
    UP,
    DOWN,
    LEFT,
    RIGHT,
)


@pytest.fixture
def mock_turtle():
    # Mock the Turtle class and Screen class to avoid GUI initialization
    with patch("snake_game.snake.Turtle", MagicMock()) as mock_turtle:
        mock_turtle.return_value.heading.return_value = UP  # Default heading
        mock_turtle.return_value.setheading = MagicMock()
        yield mock_turtle


@pytest.fixture
def snake(mock_turtle):
    return Snake()


def test_init(snake, mock_turtle):
    assert len(snake.segments) == len(STARTING_POSITIONS)
    assert snake.head == snake.segments[0]
    assert mock_turtle.call_count == len(STARTING_POSITIONS)


def test_up(snake):
    snake.head.heading.return_value = UP
    snake.up()
    assert snake.head.heading() == UP


def test_down(snake):
    snake.head.heading.return_value = DOWN
    snake.down()
    assert snake.head.heading() == DOWN


def test_left(snake):
    snake.head.heading.return_value = LEFT
    snake.left()
    assert snake.head.heading() == LEFT


def test_right(snake):
    snake.head.heading.return_value = RIGHT
    snake.right()
    assert snake.head.heading() == RIGHT


def test_extend(snake):
    initial_length = len(snake.segments)
    snake.extend()

    assert len(snake.segments) == initial_length + 1
    assert snake.segments[-1].position() == snake.segments[-2].position()


@pytest.mark.parametrize(
    "initial_heading, new_direction, expected_heading",
    [
        (UP, DOWN, UP),
        (DOWN, UP, DOWN),
        (LEFT, RIGHT, LEFT),
        (RIGHT, LEFT, RIGHT),
    ],
)
def test_opposite_direction(snake, initial_heading, new_direction, expected_heading):
    """
    Test that the snake cannot turn in the opposite direction.
    """
    snake.head.heading.return_value = initial_heading
    snake.head.setheading(initial_heading)

    if new_direction == UP:
        snake.up()
    elif new_direction == DOWN:
        snake.down()
    elif new_direction == LEFT:
        snake.left()
    elif new_direction == RIGHT:
        snake.right()

    assert snake.head.heading() == expected_heading
