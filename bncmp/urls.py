from django.contrib import admin
from django.urls import path
from cmiis import views as ViewsCMIIS
from stolen_forcemajeure import views as ViewsSFM
from sparepart_mgt import views as ViewsSPMGT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ViewsCMIIS.index, name = 'index'),
    path('stolen-forcemajeure/', ViewsCMIIS.index, name = "sfm"),
    path('stolen-forcemajeure/dashboard', ViewsSFM.dashboard, name = "dashboard"),
    path('stolen-forcemajeure/tracker', ViewsSFM.tracker, name = "tracker"),
    path('stolen-forcemajeure/sites', ViewsSFM.sites, name = "sites"),
    path('sparepart-mgt/', ViewsSPMGT.index, name = "sparepart"),
    path('sparepart-mgt/dimensioning/', ViewsSPMGT.dimensioning, name = "dimensioning"),
    path('sparepart-mgt/inventory/', ViewsSPMGT.inventory, name = "inventory"),
]
