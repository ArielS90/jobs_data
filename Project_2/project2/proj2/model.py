#from forms import  AddForm , DelForm
from flask import Flask,render_template, url_for, redirect, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, text
from flask_migrate import Migrate
######################################
#### SET UP OUR SQLite DATABASE #####
####################################

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
# Connects our Flask App to our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:M1keD8nJ0e@localhost:5432/project2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)
#####################################
####################################
###################################
def postprocessor(result):
    raw = result.split('(')[2].strip('),')
    return raw

# We inherit from db.Model class
class Jf_Q1(db.Model):

    __tablename__ = 'jf_q1'

    #########################################
    ## CREATE THE COLUMNS FOR THE TABLE ####
    #######################################

    # Primary Key column, unique id for each puppy
    id = db.Column(db.Integer,primary_key=True)
    respondent_id = db.Column(db.Text)
    good_job = db.Column(db.Numeric)
    mediocre_job = db.Column(db.Numeric)
    bad_job = db.Column(db.Numeric)
    highwellbeing = db.Column(db.Numeric)
    moderatewellbeing = db.Column(db.Numeric)
    lowwellbeing = db.Column(db.Numeric)
    working = db.Column(db.Numeric)

    # This sets what an instance in this table will have
    # Note the id will be auto-created for us later, so we don't add it here!
    def __init__(self,respondent_id,good_job,mediocre_job,bad_job,highwellbeing,moderatewellbeing,lowwellbeing,working):
        self.respondent_id = respondent_id
        self.good_job = good_job
        self.mediocre_job = mediocre_job
        self.bad_job = bad_job
        self.highwellbeing = highwellbeing
        self.moderatewellbeing = moderatewellbeing
        self.lowwellbeing = lowwellbeing
        self.working = working

    # def __repr__(self):

#############################################################

# We inherit from db.Model class
class Jf_Q2(db.Model):

    __tablename__ = 'jf_q2'

    #########################################
    ## CREATE THE COLUMNS FOR THE TABLE ####
    #######################################

    # Primary Key column, unique id for each puppy
    id = db.Column(db.Integer,primary_key=True)
    good_job = db.Column(db.Numeric)
    bad_job = db.Column(db.Numeric)
    working = db.Column(db.Numeric)
    age = db.Column(db.Numeric)

    # This sets what an instance in this table will have
    # Note the id will be auto-created for us later, so we don't add it here!
    def __init__(self,good_job,bad_job,working):
        self.good_job = good_job
        self.bad_job = bad_job
        self.working = working
        self.age = age

    # def __repr__(self):



# We inherit from db.Model class
class Jf_Q3(db.Model):

    __tablename__ = 'jf_q3'

    #########################################
    ## CREATE THE COLUMNS FOR THE TABLE ####
    #######################################

    # Primary Key column, unique id for each puppy
    id = db.Column(db.Integer,primary_key=True)
    good_job = db.Column(db.Numeric)
    working = db.Column(db.Numeric)
    company_size = db.Column(db.Numeric)
    income_level = db.Column(db.String)
    
    age = db.Column(db.Numeric)

    # This sets what an instance in this table will have
    # Note the id will be auto-created for us later, so we don't add it here!
    def __init__(self,good_job,bad_job,working):
        self.good_job = good_job
        self.working = working
        self.income_level = income_level
        self.income_level = income_level

#########################################
########### routes
###########################################




@app.route('/')
def index():
    return render_template('home.html')


@app.route('/doughnut_chart')
def doughnut_chart():

 
    values = []
    labels =['good', 'mediocre','bad']
    colors = ['rgba(0, 153, 0, 0.9)', 'rgba(0,153,153,0.9)','rgba(102,0,51,0.9)']

    # good_high = db.session.query(func.sum(Jf_Q1.highwellbeing)/func.sum(Jf_Q1.good_job)).\
    #     filter(Jf_Q1.working==1).filter(Jf_Q1.good_job==1)
    good_high = db.session.query(func.sum(Jf_Q1.highwellbeing)/func.sum(Jf_Q1.good_job)).\
        filter(Jf_Q1.working==1).filter(Jf_Q1.good_job==1)
    
    good_mod = db.session.query(func.sum(Jf_Q1.moderatewellbeing)/func.sum(Jf_Q1.good_job)).\
        filter(Jf_Q1.working==1).filter(Jf_Q1.good_job==1)

    good_low = db.session.query(func.sum(Jf_Q1.lowwellbeing)/func.sum(Jf_Q1.good_job)).\
        filter(Jf_Q1.working==1).filter(Jf_Q1.good_job==1)

    # ugly hack to strip the value from the object returned
    values.append(postprocessor(str(good_high[0])))
    values.append(postprocessor(str(good_mod[0])))
    values.append(postprocessor(str(good_low[0])))
    #[print(type(v)) for v in values]
   
    #values = ['82.48%','14.93%','1.96%']
    return render_template('doughnut_chart.html', values=values,labels=labels, colors=colors)
    

@app.route('/line_chart')
def line_chart():

    good_values = []
    bad_values = []
    labels =['18-29', '30-39','40-49','50-59','60-69','70 and older']


################
###### queries for good jobs by age
#######################

    g_18_29 = """
    select
    to_char(sum(good_job) filter(where age between 18 and 29)
        / sum(good_job)*100,'0.99')
    from jf_q2
    where working = 1
    """

    good_18_29 = db.session.execute(text(g_18_29))
    for g_result_18_29 in good_18_29:
        good_values.append(g_result_18_29[0])


    g_30_39 = """
    select
    to_char(sum(good_job) filter(where age between 30 and 39)
        / sum(good_job)*100,'00.99')
    from jf_q2
    where working = 1
    """

    good_30_39 = db.session.execute(text(g_30_39))
    for g_result_30_39 in good_30_39:
        good_values.append(g_result_30_39[0])
    


    g_40_49 = """
    select
    to_char(sum(good_job) filter(where age between 40 and 49)
        / sum(good_job)*100,'00.99')
    from jf_q2
    where working = 1
    """

    good_40_49 = db.session.execute(text(g_40_49))
    for g_result_40_49 in good_40_49:
        good_values.append(g_result_40_49[0])
  


    g_50_59 = """
    select
    to_char(sum(good_job) filter(where age between 50 and 59)
        / sum(good_job)*100,'00.99')
    from jf_q2
    where working = 1
    """

    good_50_59 = db.session.execute(text(g_50_59))
    for g_result_50_59 in good_50_59:
        good_values.append(g_result_50_59[0])
 


    g_60_69 = """
    select
    to_char(sum(good_job) filter(where age between 60 and 69)
        / sum(good_job)*100,'00.99')
    from jf_q2
    where working = 1
    """

    good_60_69 = db.session.execute(text(g_60_69))
    for g_result_60_69 in good_60_69:
        good_values.append(g_result_60_69[0])

    g_70_100 = """
    select
    to_char(sum(good_job) filter(where age between 70 and 100)
        / sum(good_job)*100,'0.99')
    from jf_q2
    where working = 1
    """

    good_70_100 = db.session.execute(text(g_70_100))
    for g_result_70_100 in good_70_100:
        good_values.append(g_result_70_100[0])


################
###### queries for bad jobs by age
#######################

    b_18_29 = """
    select
    to_char(sum(bad_job) filter(where age between 18 and 29)
        / sum(bad_job)*100,'00.99')
    from jf_q2
    where working = 1
    """

    bad_18_29 = db.session.execute(text(b_18_29))
    for b_result_18_29 in bad_18_29:
        bad_values.append(b_result_18_29[0])


    b_30_39 = """
    select
    to_char(sum(bad_job) filter(where age between 30 and 39)
        / sum(bad_job)*100,'00.99')
    from jf_q2
    where working = 1
    """

    bad_30_39 = db.session.execute(text(b_30_39))
    for b_result_30_39 in bad_30_39:
        bad_values.append(b_result_30_39[0])
    


    b_40_49 = """
    select
    to_char(sum(bad_job) filter(where age between 40 and 49)
        / sum(bad_job)*100,'00.99')
    from jf_q2
    where working = 1
    """

    bad_40_49 = db.session.execute(text(b_40_49))
    for b_result_40_49 in bad_40_49:
        bad_values.append(b_result_40_49[0])
  


    b_50_59 = """
    select
    to_char(sum(bad_job) filter(where age between 50 and 59)
        / sum(bad_job)*100,'00.99')
    from jf_q2
    where working = 1
    """

    bad_50_59 = db.session.execute(text(b_50_59))
    for b_result_50_59 in bad_50_59:
        bad_values.append(b_result_50_59[0])
 


    b_60_69 = """
    select
    to_char(sum(bad_job) filter(where age between 60 and 69)
        / sum(bad_job)*100,'00.99')
    from jf_q2
    where working = 1
    """

    bad_60_69 = db.session.execute(text(b_60_69))
    for b_result_60_69 in bad_60_69:
        bad_values.append(b_result_60_69[0])

    b_70_100 = """
    select
    to_char(sum(bad_job) filter(where age between 70 and 100)
        / sum(bad_job)*100,'0.99')
    from jf_q2
    where working = 1
    """

    bad_70_100 = db.session.execute(text(b_70_100))
    for b_result_70_100 in bad_70_100:
        bad_values.append(b_result_70_100[0])

    return render_template('line_chart.html', good_values=good_values,bad_values=bad_values,labels=labels)



#############################################################



@app.route('/bar_chart')
def bar_chart():

    bottom_20_list = []
    middle_2049_list = []
    middle_5089_list = []
    top_90_list = []
    group_labels = ["Bottom 20% Income","Middle 21%-49% Income","Middle 50%-89% Income","Top 90% Income"]

    bottom_20 = """
    select
        to_char(sum(good_job) filter(where company_size <=20)/ sum(good_job)*100,'0.99'),
        to_char(sum(good_job) filter(where company_size between 21 and 499)/ sum(good_job)*100,'00.99'),
	    to_char(sum(good_job) filter(where company_size >=500) / sum(good_job)*100,'00.99')
    from jf_q3
    where working = 1
    and
    income_level = 'Bottom 20%'
    """

    bottom20 = db.session.execute(text(bottom_20))
    for b_20_res in bottom20:
        [bottom_20_list.append(b) for b in b_20_res]

    middle_2449 = """
    select
    to_char(sum(good_job) filter(where company_size <=20)/ sum(good_job)*100,'00.99'),
    to_char(sum(good_job) filter(where company_size between 21 and 499)/ sum(good_job)*100,'00.99'),
	to_char(sum(good_job) filter(where company_size >=500) / sum(good_job)*100,'00.99')
    from jf_q3
    where working = 1
    and
    income_level ='Middle 21%-49%'
    """

    middle2049 = db.session.execute(text(middle_2449))
    for m_2449_res in middle2049:
        [middle_2049_list.append(b) for b in m_2449_res]

    middle_5089 = """
    select
    to_char(sum(good_job) filter(where company_size <=20)/ sum(good_job)*100,'00.99'),
    to_char(sum(good_job) filter(where company_size between 21 and 499)/ sum(good_job)*100,'00.99'),
	to_char(sum(good_job) filter(where company_size >=500) / sum(good_job)*100,'00.99')
    from jf_q3
    where working = 1
    and
    income_level ='Middle 50%-89%'
    """

    middle5089 = db.session.execute(text(middle_5089))
    for m_5089_res in middle5089:
        [middle_5089_list.append(b) for b in m_5089_res]


    top_90 = """
    select
    to_char(sum(good_job) filter(where company_size <=20)/ sum(good_job)*100,'00.99'),
    to_char(sum(good_job) filter(where company_size between 21 and 499)/ sum(good_job)*100,'00.99'),
	to_char(sum(good_job) filter(where company_size >=500) / sum(good_job)*100,'00.99')
    from jf_q3
    where working = 1
    and
    income_level ='Top 90%'
    """
    top90 = db.session.execute(text(top_90))
    for t_90_res in top90:
        [top_90_list.append(b) for b in t_90_res]


    m2049 = []
    m2049.append(bottom_20_list[0])
    m2049.append(middle_2049_list[0]) 
    m2049.append(middle_5089_list[0]) 
    m2049.append(top_90_list[0])      

    m5089 = [] 
    m5089.append(bottom_20_list[1])
    m5089.append(middle_2049_list[1])
    m5089.append(middle_5089_list[1])
    m5089.append(top_90_list[1]) 
    

    t90 = []
    t90.append(bottom_20_list[2])
    print(bottom_20_list[2])
    t90.append(middle_2049_list[2])
    print(middle_2049_list[2])
    t90.append(middle_5089_list[2])
    print(middle_5089_list[2])
    t90.append(top_90_list[2])
    print (top_90_list[2])

    return render_template('bar_chart.html',
        #bottom_20_list=bottom_20_list,
        m2049=m2049,
        m5089=m5089,
        t90=t90,
        group_labels=group_labels)


if __name__ == '__main__':
    app.run(debug=True)


