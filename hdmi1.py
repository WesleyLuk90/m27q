from m27q import MonitorControl
import time

with MonitorControl() as m:
    m.switch_to_hdmi_1()