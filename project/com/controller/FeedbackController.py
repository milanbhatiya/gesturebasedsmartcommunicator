from project import app
from flask import Flask,render_template,request
from project.com.dao.FeedbackDAO import FeedbackDAO
from project.com.vo.FeedbackVO import FeedbackVO

@app.route('/viewFeedback')
def viewFeedback():
    return render_template('admin/viewFeedback.html')

@app.route('/addFeedback')
def addFeedback():
    feedbackDAO = FeedbackDAO()
    feedbackVO = FeedbackVO()

    feedbackText = request.form['feedbackText']
    feedbackRating = request.form['feedbackRating']

    feedbackVO.feedbackText=feedbackText
    feedbackVO.feedbackRating=feedbackRating
    return render_template('admin/viewFeedback.html')

