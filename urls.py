from django.conf.urls import defaults
import home


urlpatterns = defaults.patterns(
  "",
  (".*",home.home_page),
)

handler404 = defaults.handler404
handler500 = defaults.handler500