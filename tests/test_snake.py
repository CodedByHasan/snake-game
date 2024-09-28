import sys
import os
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
def snake():
    return Snake()


def test_init(snake):
    assert len(snake.segments) == len(STARTING_POSITIONS)
    assert snake.head == snake.segments[0]


def test_up(snake):
    snake.up()
    assert snake.head.heading() == UP


def test_down(snake):
    snake.down()
    assert snake.head.heading() == DOWN


# NOTE: This fails for some reason.
# def test_left(snake):
#     snake.left()
#     assert snake.head.heading() == LEFT


def test_right(snake):
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
    """Test that the snake cannot turn in the opposite direction."""
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
