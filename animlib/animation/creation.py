from __future__ import annotations

import numpy as np
from abc import ABC, abstractmethod

from typing import TYPE_CHECKING

from manim import*


class ShowPartial(Animation, ABC):
    """
    Abstract class for ShowCreation and ShowPassingFlash
    """
    CONFIG = {
        "should_match_start": False,
    }

    def begin(self) -> None:
        super().begin()
        if not self.should_match_start:
            self.mobject.lock_matching_data(self.mobject, self.starting_mobject)

    def finish(self) -> None:
        super().finish()
        self.mobject.unlock_data()

    def interpolate_submobject(
        self,
        submob: VMobject,
        start_submob: VMobject,
        alpha: float
    ) -> None:
        submob.pointwise_become_partial(
            start_submob, *self.get_bounds(alpha)
        )

    @abstractmethod
    def get_bounds(self, alpha: float) -> tuple[float, float]:
        raise Exception("Not Implemented")


class ShowCreation(ShowPartial):
    CONFIG = {
        "lag_ratio": 1,
    }

    def get_bounds(self, alpha: float) -> tuple[float, float]:
        return (0, alpha)