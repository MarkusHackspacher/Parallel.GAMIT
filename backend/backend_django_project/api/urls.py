from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

from django.conf import settings

urlpatterns = [
    path('antennas', views.AntennaList.as_view(), name='antennas_list'),
    path('antennas/<int:pk>', views.AntennaDetail.as_view(), name='antenna_detail'),
    path('apr-coords', views.AprCoordsList.as_view(), name='apr_coords_list'),
    path('apr-coords/<int:pk>', views.AprCoordsDetail.as_view(),
         name='apr_coords_detail'),
    path('aws-sync', views.AwsSyncList.as_view(), name='aws_sync_list'),
    path('aws-sync/<int:pk>', views.AwsSyncDetail.as_view(), name='aws_sync_detail'),
    path('campaigns', views.CampaignList.as_view(), name='campaign_list'),
    path('campaigns/<int:pk>', views.CampaignDetail.as_view(),
         name='campaign_detail'),
    path('countries', views.CountryList.as_view(), name='country_list'),
    path('countries/<int:pk>', views.CountryDetail.as_view(), name='country_detail'),
    path('data-sources', views.DataSourceList.as_view(), name='data_source_list'),
    path('data-sources/<int:pk>', views.DataSourceDetail.as_view(),
         name='data_source_detail'),
    path('earthquakes', views.EarthquakesList.as_view(), name='earthquakes_list'),
    path('earthquakes/<int:pk>', views.EarthquakesDetail.as_view(),
         name='earthquakes_detail'),
    path('endpoints', views.EndpointList.as_view(), name='endpoint_list'),
    path('endpoints/<int:pk>', views.EndpointDetail.as_view(),
         name='endpoint_detail'),
    path('endpoints-clusters', views.EndpointsClusterList.as_view(),
         name='endpoints_cluster_list'),
    path('endpoints-clusters/<int:pk>',
         views.EndpointsClusterDetail.as_view(), name='endpoints_cluster_detail'),
    path('etm-params', views.EtmParamsList.as_view(), name='etm_params_list'),
    path('etm-params/<int:pk>', views.EtmParamsDetail.as_view(),
         name='etm_params_detail'),
    path('etms', views.EtmsList.as_view(), name='etms_list'),
    path('etms/<int:pk>', views.EtmsDetail.as_view(), name='etms_detail'),
    path('events', views.EventsList.as_view(), name='events_list'),
    path('events/<int:pk>', views.EventsDetail.as_view(), name='events_detail'),
    path('executions', views.ExecutionsList.as_view(), name='executions_list'),
    path('executions/<int:pk>', views.ExecutionsDetail.as_view(),
         name='executions_detail'),
    path('health-check', views.HealthCheck.as_view(), name='health-check'),
    path('gamit-htc', views.GamitHtcList.as_view(), name='gamit_htc_list'),
    path('gamit-htc/<int:pk>', views.GamitHtcDetail.as_view(),
         name='gamit_htc_detail'),
    path('gamit-soln', views.GamitSolnList.as_view(), name='gamit_soln_list'),
    path('gamit-soln/<int:pk>', views.GamitSolnDetail.as_view(),
         name='gamit_soln_detail'),
    path('gamit-soln-excl', views.GamitSolnExclList.as_view(),
         name='gamit_soln_excl_list'),
    path('gamit-soln-excl/<int:pk>', views.GamitSolnExclDetail.as_view(),
         name='gamit_soln_excl_detail'),
    path('gamit-stats', views.GamitStatsList.as_view(), name='gamit_stats_list'),
    path('gamit-stats/<int:pk>', views.GamitStatsDetail.as_view(),
         name='gamit_stats_detail'),
    path('gamit-subnets', views.GamitSubnetsList.as_view(),
         name='gamit_subnets_list'),
    path('gamit-subnets/<int:pk>', views.GamitSubnetsDetail.as_view(),
         name='gamit_subnets_detail'),
    path('gamit-ztd', views.GamitZtdList.as_view(), name='gamit_ztd_list'),
    path('gamit-ztd/<int:pk>', views.GamitZtdDetail.as_view(),
         name='gamit_ztd_detail'),
    path('keys', views.KeysList.as_view(), name='keys_list'),
    path('keys/<int:pk>', views.KeysDetail.as_view(), name='keys_detail'),
    path('locks', views.LocksList.as_view(), name='locks_list'),
    path('locks/<int:pk>', views.LocksDetail.as_view(), name='locks_detail'),
    path('monument-types', views.MonumentTypeList.as_view(),
         name='monument_types_list'),
    path('monument-types/<int:pk>', views.MonumentTypeDetail.as_view(),
         name='monument_types_detail'),
    path('networks', views.NetworkList.as_view(), name='network_list'),
    path('networks/<int:pk>', views.NetworkDetail.as_view(), name='network_detail'),
    path('people', views.PersonList.as_view(), name='people_list'),
    path('people/<int:pk>', views.PersonDetail.as_view(), name='people_detail'),
    path('ppp-soln', views.PppSolnList.as_view(), name='ppp_soln_list'),
    path('ppp-soln/<int:pk>', views.PppSolnDetail.as_view(), name='ppp_soln_detail'),
    path('ppp-soln-excl', views.PppSolnExclList.as_view(),
         name='ppp_soln_excl_list'),
    path('ppp-soln-excl/<int:pk>', views.PppSolnExclDetail.as_view(),
         name='ppp_soln_excl_detail'),
    path('receivers', views.ReceiverList.as_view(), name='receiver_list'),
    path('receivers/<int:pk>', views.ReceiverDetail.as_view(),
         name='receiver_detail'),
    path('receivers', views.ReceiversList.as_view(), name='receivers_list'),
    path('receivers/<int:pk>', views.ReceiversDetail.as_view(),
         name='receivers_detail'),
    path('rinex', views.RinexList.as_view(), name='rinex_list'),
    path('rinex/<int:pk>', views.RinexDetail.as_view(), name='rinex_detail'),
    path('rinex-sources-info', views.RinexSourcesInfoList.as_view(),
         name='rinex_sources_info_list'),
    path('rinex-sources-info/<int:pk>', views.RinexSourcesInfoDetail.as_view(),
         name='rinex_sources_info_detail'),
    path('rinex-tank-struct', views.RinexTankStructList.as_view(),
         name='rinex_tank_struct_list'),
    path('rinex-tank-struct/<int:pk>', views.RinexTankStructDetail.as_view(),
         name='rinex_tank_struct_detail'),
    path('roles', views.RoleList.as_view(), name='role_list'),
    path('roles/<int:pk>', views.RoleDetail.as_view(), name='role_detail'),
    path('role-person-station', views.RolePersonStationList.as_view(),
         name='role_permission_list'),
    path('role-person-station/<int:pk>',
         views.RolePersonStationDetail.as_view(), name='role_permission_detail'),
    path('sources-formats', views.SourcesFormatsList.as_view(),
         name='sources_formats_list'),
    path('sources-formats/<int:pk>', views.SourcesFormatsDetail.as_view(),
         name='sources_formats_detail'),
    path('sources-servers', views.SourcesServersList.as_view(),
         name='sources_servers_list'),
    path('sources-servers/<int:pk>', views.SourcesServersDetail.as_view(),
         name='sources_servers_detail'),
    path('sources-stations', views.SourcesStationsList.as_view(),
         name='sources_stations_list'),
    path('sources-stations/<int:pk>', views.SourcesStationsDetail.as_view(),
         name='sources_stations_detail'),
    path('stacks', views.StacksList.as_view(), name='stacks_list'),
    path('stacks/<int:pk>', views.StacksDetail.as_view(), name='stacks_detail'),
    path('stationalias', views.StationaliasList.as_view(),
         name='stationalias_list'),
    path('stationalias/<int:pk>', views.StationaliasDetail.as_view(),
         name='stationalias_detail'),
    path('station-attached-files', views.StationAttachedFilesList.as_view(),
         name='station_attached_files_list'),
    path('station-attached-files/<int:pk>', views.StationAttachedFilesDetail.as_view(),
         name='station_attached_files_detail'),
    path('station-images', views.StationImagesList.as_view(),
         name='station_images_list'),
    path('station-images/<int:pk>', views.StationImagesDetail.as_view(),
         name='station_images_detail'),
    path('station-info', views.StationinfoList.as_view(), name='station_info_list'),
    path('station-info/<int:pk>', views.StationinfoDetail.as_view(),
         name='station_info_detail'),
    path('station-meta', views.StationMetaList.as_view(), name='station_meta_list'),
    path('station-meta/<int:station_id>',
         views.StationMetaDetail.as_view(), name='station_meta_detail'),
    path('station-roles', views.StationRolesList.as_view(),
         name='station_roles_list'),
    path('station-roles/<int:pk>', views.StationRolesDetail.as_view(),
         name='station_roles_detail'),
    path('station-status', views.StationStatusList.as_view(),
         name='station_status_list'),
    path('station-status/<int:pk>', views.StationStatusDetail.as_view(),
         name='station_status_detail'),
    path('station-types', views.StationTypeList.as_view(),
         name='station_types_list'),
    path('station-types/<int:pk>', views.StationTypeDetail.as_view(),
         name='station_types_detail'),
    path('stations', views.StationList.as_view(), name='station_list'),
    path('stations/<int:pk>', views.StationDetail.as_view(), name='station_detail'),
    path('station-codes/<int:network_api_id>',
         views.StationCodesList.as_view(), name='station_codes_list'),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('users', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('users/<int:pk>/photo', views.UserPhoto.as_view(), name='get_user_photo'),
    path('visits', views.VisitList.as_view(), name='visit_list'),
    path('visits/<int:pk>', views.VisitDetail.as_view(), name='visit_detail'),
    path('visit-attached-files', views.VisitAttachedFilesList.as_view(),
         name='visit_attached_files_list'),
    path('visit-attached-files/<int:pk>', views.VisitAttachedFilesDetail.as_view(),
         name='visit_attached_files_detail'),
    path('visit-images', views.VisitImagesList.as_view(), name='visit_images_list'),
    path('visit-images/<int:pk>', views.VisitImagesDetail.as_view(),
         name='visit_images_detail'),
    path('visit-gnss-data-files', views.VisitGNSSDataFilesList.as_view(),
         name='visit_gnss_data_files_list'),
    path('visit-gnss-data-files/<int:pk>', views.VisitGNSSDataFilesDetail.as_view(),
         name='visit_gnss_data_files_detail'),
]