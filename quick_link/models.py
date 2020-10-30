from django.db import models
REASON = (('ed', 'Educational use'), ('pu', 'Professional use'), ('pu', 'personal use'))
MICROSOFT = (('w', 'ms-word'), ('e', 'ms-excel'), ('p', 'ms-powerpoint'), ('ps', 'more'))
GRAPHIC = (('c', 'corel draw'), ('p', 'photoshop'), ('cd', 'graphic design'), ('pxs', 'more'))
PROFRAMMING = (('b', 'basic'), ('v', 'visual-studio'), ('p', 'python'), ('pss', 'more'))
GENDER = (('ma', 'Male'), ('fe', 'Female'), ('ni', 'No Idea'))
SEMESTER = (('f', 'first'), ('s', 'second'))
DURATION = (('a', '1 month intensive training'), ('b', '2 months graphic design training'), ('c', '1.5 months of basic programming'),
            ('d', '2 months app development'), ('e', '4 months professional graphics design'), ('f', '2.5 months of ms office training'),
('g', '2 months visual studio basics'),('h', '4 months AI training'), ('i', '3 months genetic programming'),( 'j', '3 months web development/hosting'),
            ('k', 'machine learning (3 months)'), ('l', '6 months advance AI training'), ('m', '2 months python basic'))
KNOWLEDGE = (('n', 'no'), ('y', 'yes, specify'))
MONTH = (('ee', '1 month'), ('re', '2-3 months'), ('nif', '1-2 weeks'))
LEVEL = (('ese', '100L'), ('ref', '200L'), ('nidf', '300L'), ('ref', '200L'), ('nidf', '300L'),
         ('rek', '400L'), ('nsif', '500L'))


class Complaint(models.Model):
    name = models.CharField(max_length=20)
    phone = models.PositiveIntegerField()
    email = models.EmailField()
    complaint = models.TextField()

    def __str__(self):
        return self.name


class Enrol(models.Model):
    #image = models.ImageField()
    name = models.CharField(max_length=50)


class Enroldetail(models.Model):
    name = models.CharField(max_length=50)
    enrol = models.ForeignKey(Enrol, on_delete=models.CASCADE)
    parent_guardian_contact_name = models.CharField(max_length=50)
    parent_guardian_contact_no = models.PositiveIntegerField()
    applicant_contact_no = models.PositiveIntegerField()
    contact_address = models.CharField(max_length=50)
    state_of_origin = models.CharField(max_length=50)
    lga = models.CharField(max_length=50)
    gender = models.CharField(choices=GENDER, max_length=20)
    email = models.EmailField()
    date_of_birth = models.DateTimeField()
    name_of_institution = models.CharField(max_length=50)
    department = models.CharField(max_length=20)
    level = models.CharField(max_length=20, choices=LEVEL)
    reason_for_application = models.CharField(max_length=20, choices=REASON)
    semester = models.CharField(max_length=20, choices=SEMESTER)
    date_of_admission = models.DateTimeField()
    microsoft = models.CharField(max_length=10, choices=MICROSOFT)
    mmore = models.CharField(max_length=30, null=True, blank=True)
    graphic = models.CharField(max_length=10, choices=GRAPHIC)
    gmore = models.CharField(max_length=30, null=True, blank=True)
    programming = models.CharField(max_length=10, choices=PROFRAMMING)
    pmore = models.CharField(max_length=30, null=True, blank=True)
    duration = models.CharField(max_length=10, choices=DURATION)
    more = models.CharField(max_length=400, null=True, blank=True)
    Knowledge = models.CharField(max_length=10, choices=KNOWLEDGE)
    specify = models.CharField(max_length=30, null=True, blank=True)
    experience_months = models.CharField(max_length=20, choices=MONTH, null=True, blank=True)
    where_trained = models.CharField(max_length=30, null=True, blank=True)
    year_trained = models.IntegerField(null=True, blank=True)
    admission_date = models.DateTimeField(null=True, blank=True)
    course = models.CharField(max_length=30, null=True, blank=True)
    group_no = models.IntegerField(null=True, blank=True)
    paid_fees = models.IntegerField(null=True, blank=True)
    completion_date = models.DateTimeField(null=True, blank=True)
    date_of_commencement = models.IntegerField(null=True, blank=True)
    classes_days = models.CharField(max_length=50, null=True, blank=True)
    classes_hours = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name





# Create your models here.
