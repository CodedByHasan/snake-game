import sys
import os
from unittest.mock import patch
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from snake_game.scoreboard import Scoreboard


@pytest.fixture
def scoreboard():
    return Scoreboard()


def test_scoreboard_init(scoreboard):
    assert scoreboard.score == 0
    assert scoreboard.color() == ("white", "white")
    assert scoreboard.speed() == 0  # fastest
    assert scoreboard.pos() == (0, 260)
    assert scoreboard.isvisible() is False


def test_increase_score(scoreboard):
    initial_score = scoreboard.score
    scoreboard.increase_score()

    assert scoreboard.score == initial_score + 1


def test_update_scoreboard(scoreboard):
    with patch.object(scoreboard, 'clear') as mock_clear, \
         patch.object(scoreboard, 'write') as mock_write:

        scoreboard.update_scoreboard()

        mock_clear.assert_called_once()
        mock_write.assert_called_once_with(
            "Score: 0", align="center", font=("Arial", 24, "normal")
        )
