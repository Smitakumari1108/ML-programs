import os
import pickle
import streamlit as st
import pandas as pd

# Load data
with open('courses.pkl', 'rb') as f:
    courses_list = pickle.load(f)

with open('similarity.pkl', 'rb') as f:
    similarity = pickle.load(f)

# Recommendation function
def recommend(course):
    try:
        index = courses_list[courses_list['course_name'] == course].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_course_names = [courses_list.iloc[i[0]].course_name for i in distances[1:7]]
        return recommended_course_names
    except IndexError:
        return ["Course not found. Please select a valid course."]

# Streamlit UI
st.markdown("<h2 style='text-align: center; color: blue;'>Coursera Course Recommendation System</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: black;'>Find similar courses from a dataset of over 3,000 courses from Coursera!</h4>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: black;'>Web App created by Sagar Bapodara</h4>", unsafe_allow_html=True)

course_list = courses_list['course_name'].values
selected_course = st.selectbox("Type or select a course you like:", course_list)

if st.button('Show Recommended Courses'):
    recommended_courses = recommend(selected_course)

    if "Course not found" in recommended_courses:
        st.error(recommended_courses[0])
    else:
        st.write("### Recommended Courses based on your interests:")
        for course in recommended_courses:
            st.write(f"- {course}")

st.markdown("<h6 style='text-align: center; color: red;'>Copyright reserved by Coursera and Respective Course Owners</h6>", unsafe_allow_html=True)
