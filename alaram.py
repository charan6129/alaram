import streamlit as st
import datetime
import winsound

def alarm_clock():
    st.title("Alarm Clock ")
    st.markdown("---")

    st.sidebar.title("Set Alarm")
    alarm_hour = st.sidebar.slider("Hour", 0, 12, 0)
    alarm_minute = st.sidebar.slider("Minute", 0, 59, 0)
    alarm_period = st.sidebar.radio("AM/PM", ["AM", "PM"])

    if st.sidebar.button("Set Alarm"):
        set_alarm(alarm_hour, alarm_minute, alarm_period)

def set_alarm(hour, minute, period):
    if period == "PM":
        hour += 12

    st.info(f"Alarm set for {hour % 24}:{minute:02d} {period}")

    while True:
        now = datetime.datetime.now()
        current_hour = now.hour
        current_minute = now.minute

        if hour == current_hour and minute == current_minute:
            for _ in range(10):  # Beep 5 times
                winsound.Beep(1000, 200)  # Frequency = 1000Hz, Duration = 200ms
            break

if __name__ == "__main__":
    alarm_clock()
