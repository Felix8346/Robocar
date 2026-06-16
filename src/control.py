import time

import sensors

last_error = 0.0
integral = 0.0
MAX_INTEGRAL = 250
MAX_SPEED = 100


def speed_correction(refreshrate_Hz, base_speed, kp, ki, kd, ks):
    global last_error, integral

    integral_reset = 0
    sleep_time_refresh = 1 / refreshrate_Hz

    status_right = sensors.right_is_over_black()
    status_middle = sensors.middle_is_over_black()
    status_left = sensors.left_is_over_black()

    error = sensors.calculate_error(status_left, status_middle, status_right)

    # if line is lost -> reset integral and use last error as current
    if error is None:
        error = last_error
        integral = integral_reset

    derivative = error - last_error

    integral = integral + error

    integral = max(-MAX_INTEGRAL, min(MAX_INTEGRAL, integral))

    correction = kp * error + kd * derivative + ki * integral

    dynamic_base_speed = base_speed - (abs(error) * ks)
    speed_left = dynamic_base_speed + round(correction)
    speed_right = dynamic_base_speed - round(correction)

    speed_left = max(-MAX_SPEED, min(MAX_SPEED, speed_left))
    speed_right = max(-MAX_SPEED, min(MAX_SPEED, speed_right))

    # Shows current error and speed for debugging
    print(f"Error: {error} | Speed Left: {speed_left} | Speed Right: {speed_right}")

    last_error = error

    time.sleep(sleep_time_refresh)

    return speed_left, speed_right


def reduce_turn_radius(speed_left, speed_right, turn_factor):
    MAX_SPEED = 100
    if speed_left < 0:
        speed_left_rear = speed_left * turn_factor
        speed_right_rear = speed_right
        speed_left_rear = max(-MAX_SPEED, min(MAX_SPEED, speed_left_rear))
        return speed_left_rear, speed_right_rear
    if speed_right < 0:
        speed_left_rear = speed_left
        speed_right_rear = speed_right * turn_factor
        speed_right_rear = max(-MAX_SPEED, min(MAX_SPEED, speed_right_rear))
        return speed_left_rear, speed_right_rear

    return speed_left, speed_right
