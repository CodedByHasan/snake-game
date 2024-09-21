import sys
import pytest
from unittest.mock import patch

sys.path.append('../src')

from snake_game.scoreboard import Scoreboard


@pytest.fixture
def scoreboard():
    return Scoreboard()

def test_scoreboard_init(scoreboard):
    assert scoreboard.score == 0
    assert scoreboard.color() == ("white", "white")
    assert scoreboard.speed() == 0 # fastest
    assert scoreboard.pos() == (0,260)


def test_score_increase(scoreboard):
    initial_score = scoreboard.score
    scoreboard.increase_score()

    assert scoreboard.score == initial_score + 1


