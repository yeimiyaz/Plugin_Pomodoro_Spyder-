# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © 2024, Yeimi P
#
# Licensed under the terms of the MIT license
# ----------------------------------------------------------------------------
"""
Spyder Pomodoro Timer Main Widget.
"""
# Third party imports
import qtawesome as qta


# Spyder imports
from spyder.api.config.decorators import on_conf_change
from spyder.api.translations import get_translation

from spyder.api.widgets.status import BaseTimerStatus
from spyder.utils.icon_manager import ima

from spyder.api.widgets.toolbars import ApplicationToolbar

# Third party imports
import qtawesome as qta

# --- Constants
# ------ Time limits by default
POMODORO_DEFAULT = 25 * 60 * 1000  # 25 mins in milliseconds
INTERVAL = 1000

# Localization
_ = get_translation("spyder_pomodoro_timer.spyder")

class PomodoroTimerToolbar(ApplicationToolbar):
    """Toolbar to add buttons to control our timer."""
    ID = 'pomodoro_timer_toolbar'


class PomodoroTimerStatus(BaseTimerStatus):
    """Status bar widget to display the pomodoro timer"""
    ID = "pomodoro_timer_status"
    CONF_SECTION = "spyder_pomodoro_timer"

    def __init__(self, parent):
        super().__init__(parent)
        self.value = "25:00"
        
        # Actual time limits
        self.pomodoro_limit = POMODORO_DEFAULT
        self.countdown = self.pomodoro_limit
        self._interval = INTERVAL
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(self._interval)
        self.pause = True

    def get_tooltip(self):
        """Override api method."""
        return "I am the Pomodoro timer!"
    def get_icon(self):
        return qta.icon("mdi.av-timer", color=ima.MAIN_FG_COLOR)
    
    # ---- BaseTimerStatus API
    def get_value(self):
        """Get current time of the timer"""
        return self.value
    
    def display_time(self):
        """Calculate the time that should be displayed."""
        minutes = int((self.countdown / (1000 * 60)) % 60)
        seconds = int((self.countdown / 1000) % 60)
        return f"{minutes:02d}:{seconds:02d}"
    
    def update_timer(self):
        """Updates the timer and the current widget. Also, update the
        task counter if a task is set."""
    
        if self.countdown > 0 and not self.pause:
            # Update the current timer by decreasing the current running time by one second
            self.countdown -= INTERVAL
            self.value = self.display_time()