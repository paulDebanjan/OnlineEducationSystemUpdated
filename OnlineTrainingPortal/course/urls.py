from django.urls import path
from . import views

#slug=course slug
#slug2 = module slug
#slug3 = material slug
#slug4 = question slug

app_name = "course"
urlpatterns = [
    path(
        route='',
        view=views.CourseListView.as_view(),
        name='home'
    ),
    # path(
    #     route='corporateTraining/',
    #     view=views.CorporateTrainingView.as_view(),
    #     name='corporateTraining'
    # ),
    # path(
    #     route='enrollForm/<slug>/',
    #     view=views.CourseEnrollFormView.as_view(),
    #     name='enrollForm'
    # ),
    path(
        route='adminCourseList/',
        view=views.AdminCourseList.as_view(),
        name='adminCourseList'
    ),
    path(
        route='module_crate/<slug:slug>/',
        view=views.CreateModuleView.as_view(),
        name='module_crate'
    ),
    path(
        route='enrol_form/<slug:slug>/',
        view=views.StudenEnrolFormView.as_view(),
        name='enrol_form'
    ),
    path(
        route='module_update/<slug:slug>/<int:pk>/',
        view=views.UpdateModuleView.as_view(),
        name='module_update'
    ),
    path(
        route='module_delete/<slug:slug>/<int:pk>/',
        view=views.DeleteModuleView.as_view(),
        name='module_delete'
    ),
    path(
        route='element_list/<slug:slug>/<slug:slug2>/',
        view=views.ModuleElementListView.as_view(),
        name='element_list'
    ),
    path(
        route='question_list/<slug:slug>/<slug:slug2>/<slug:slug3>/',
        view=views.QuestionListView.as_view(),
        name='question_list'
    ),
    path(
        route='question_add/<slug:slug>/<slug:slug2>/<slug:slug3>/',
        view=views.QuestionCreateView.as_view(),
        name='question_add'
    ),
    path(
        route='question_update/<slug:slug>/<slug:slug2>/<slug:slug3>/<int:question_pk>/',
        view=views.question_change,
        name='question_update'
    ),
    path(
        route='element_create/<slug:slug>/<slug:slug2>/',
        view=views.MaterialCreateView.as_view(),
        name='element_create'
    ),
    path(
        route='element_update/<slug:slug>/<slug:slug2>/<int:pk>/',
        view=views.MaterialUpdateView.as_view(),
        name = 'element_update'
    ),
    # path(
    #     route='element_update/<slug:slug>/<slug:slug2>/<slug:slug3>/',
    #     view=views.MaterialUpdateView.as_view(),
    #     name='element_update'
    # ),
    path(
        route='element_delete/<slug:slug>/<slug:slug2>/<int:pk>/',
        view=views.MaterialDeleteView.as_view(),
        name='element_delete'
    ),
    path(
        route='permissionList/<slug:slug>/',
        view=views.PermissionListView.as_view(),
        name='permissionList'
    ),
    path(
        route='permissionCreate/<slug:slug>/',
        view=views.PermissionCreateView.as_view(),
        name='permissionCreate'
    ),
    path(
        route='module_list/<slug:slug>/',
        view=views.ModuleListView.as_view(),
        name='module_list'
    ),
    
    path(
        route='permissionDelete/<slug:slug>/<int:pk>/',
        view=views.PermissionDeleteView.as_view(),
        name='permissionDelete'
    ),
    path(
        route='permissionUpdate/<slug:slug>/<int:pk>/',
        view=views.PermissionUpdateView.as_view(),
        name='permissionUpdate'
    ),
    
    path(
        route='create/',
        view=views.CourseCreateView.as_view(),
        name='courseCreate'
    ),
    path(
        route='update/<slug:slug>',
        view=views.CourseUpdateView.as_view(),
        name='courseUpdate'
    ),
    path(
        route='delete/<slug:slug>',
        view=views.CourseDeleteView.as_view(),
        name='courseDelete'
    ),
    
    path(
        route='scheduleList/<slug:slug>/',
        view=views.CourseScheduleList.as_view(),
        name='scheduleList'
    ),

    path(
        route='schedule/create/<slug:slug>/',
        view=views.CourseScheduleCreateView.as_view(),
        name='scheduleCreate'
    ),
    path(
        route='schedule/update/<slug:slug>/<int:pk>/',
        view=views.CourseScheduleUpdateView.as_view(),
        name='scheduleUpdate'
    ),
    path(
        route='schedule/delete/<slug:slug>/<int:pk>/',
        view=views.CourseScheduleDeleteView.as_view(),
        name='scheduleDelete'
    ),
    path(
        route='<slug:slug>/',
        view=views.CourseDetailView.as_view(),
        name='detailView'
    ),
    path(
        route='quiz/<pk>/',
        view= views.quiz_view,
        name="quiz_view"
    ),
    path(
        route="quiz/<pk>/data",
        view = views.quiz_data_view,
        name = "quiz-data-view"
    )
]