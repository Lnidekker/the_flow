create_library_set \
    -name func_sslvm40cw_s \
    -timing " \
        /Users/leonidnidekker/Dropbox/asic/the_flow/testing_source/lib/test_file_ss_0p81v_m40c.lib \
        /Users/leonidnidekker/Dropbox/asic/the_flow/testing_source/lib/test_file_1_worst_case.lib" \
    -si " \
        /Users/leonidnidekker/Dropbox/asic/the_flow/testing_source/cdb/test_file_ss_0p81v_m40c.cdb \
        /Users/leonidnidekker/Dropbox/asic/the_flow/testing_source/cdb/test_file_1_worst_case.cdb"
create_library_set \
    -name func_sslvm40cw_h \
    -timing " \
        /Users/leonidnidekker/Dropbox/asic/the_flow/testing_source/lib/test_file_ss_0p81v_m40c.lib \
        /Users/leonidnidekker/Dropbox/asic/the_flow/testing_source/lib/test_file_1_worst_case.lib" \
    -si " \
        /Users/leonidnidekker/Dropbox/asic/the_flow/testing_source/cdb/test_file_ss_0p81v_m40c.cdb \
        /Users/leonidnidekker/Dropbox/asic/the_flow/testing_source/cdb/test_file_1_worst_case.cdb"
create_library_set \
    -name scan_sslvm40cw_s \
    -timing " \
        /Users/leonidnidekker/Dropbox/asic/the_flow/testing_source/lib/test_file_ss_0p81v_m40c.lib \
        /Users/leonidnidekker/Dropbox/asic/the_flow/testing_source/lib/test_file_1_worst_case.lib" \
    -si " \
        /Users/leonidnidekker/Dropbox/asic/the_flow/testing_source/cdb/test_file_ss_0p81v_m40c.cdb \
        /Users/leonidnidekker/Dropbox/asic/the_flow/testing_source/cdb/test_file_1_worst_case.cdb"
create_library_set \
    -name scan_sslvm40cw_h \
    -timing " \
        /Users/leonidnidekker/Dropbox/asic/the_flow/testing_source/lib/test_file_ss_0p81v_m40c.lib \
        /Users/leonidnidekker/Dropbox/asic/the_flow/testing_source/lib/test_file_1_worst_case.lib" \
    -si " \
        /Users/leonidnidekker/Dropbox/asic/the_flow/testing_source/cdb/test_file_ss_0p81v_m40c.cdb \
        /Users/leonidnidekker/Dropbox/asic/the_flow/testing_source/cdb/test_file_1_worst_case.cdb"
create_library_set \
    -name scan_ffhv0cb_h \
    -timing " \
        /Users/leonidnidekker/Dropbox/asic/the_flow/testing_source/lib/test_file_ff_0p99v_0c.lib \
        /Users/leonidnidekker/Dropbox/asic/the_flow/testing_source/lib/test_file_1_best_case.lib" \
    -si " \
        /Users/leonidnidekker/Dropbox/asic/the_flow/testing_source/cdb/test_file_ff_0p99v_0c.cdb \
        /Users/leonidnidekker/Dropbox/asic/the_flow/testing_source/cdb/test_file_1_best_case.cdb"

create_timing_condition \
    -name func_sslvm40cw_s \
    -library_sets "func_sslvm40cw_s"
create_timing_condition \
    -name func_sslvm40cw_h \
    -library_sets "func_sslvm40cw_h"
create_timing_condition \
    -name scan_sslvm40cw_s \
    -library_sets "scan_sslvm40cw_s"
create_timing_condition \
    -name scan_sslvm40cw_h \
    -library_sets "scan_sslvm40cw_h"
create_timing_condition \
    -name scan_ffhv0cb_h \
    -library_sets "scan_ffhv0cb_h"

create_rc_corner \
    -name func_sslvm40cw_s \
    -temperature -40 \
    -qrc_tech /Users/leonidnidekker/Dropbox/asic/the_flow/testing_source/qrc/qrcTech.cworst
create_rc_corner \
    -name func_sslvm40cw_h \
    -temperature -40 \
    -qrc_tech /Users/leonidnidekker/Dropbox/asic/the_flow/testing_source/qrc/qrcTech.cworst
create_rc_corner \
    -name scan_sslvm40cw_s \
    -temperature -40 \
    -qrc_tech /Users/leonidnidekker/Dropbox/asic/the_flow/testing_source/qrc/qrcTech.cworst
create_rc_corner \
    -name scan_sslvm40cw_h \
    -temperature -40 \
    -qrc_tech /Users/leonidnidekker/Dropbox/asic/the_flow/testing_source/qrc/qrcTech.cworst
create_rc_corner \
    -name scan_ffhv0cb_h \
    -temperature 0 \
    -qrc_tech /Users/leonidnidekker/Dropbox/asic/the_flow/testing_source/qrc/qrcTech.cbest

create_delay_corner \
    -name func_sslvm40cw_s \
    -timing_condition func_sslvm40cw_s \
    -rc_corner func_sslvm40cw_s
create_delay_corner \
    -name func_sslvm40cw_h \
    -timing_condition func_sslvm40cw_h \
    -rc_corner func_sslvm40cw_h
create_delay_corner \
    -name scan_sslvm40cw_s \
    -timing_condition scan_sslvm40cw_s \
    -rc_corner scan_sslvm40cw_s
create_delay_corner \
    -name scan_sslvm40cw_h \
    -timing_condition scan_sslvm40cw_h \
    -rc_corner scan_sslvm40cw_h
create_delay_corner \
    -name scan_ffhv0cb_h \
    -timing_condition scan_ffhv0cb_h \
    -rc_corner scan_ffhv0cb_h

create_constraint_mode \
    -name func_sslvm40cw_s \
    -sdc_files "../in/sdc/./sdc_dir/sdc_dir_file.sdc ../in/sdc/constraint_1.sdc ../in/sdc/constraint_2.sdc"
create_constraint_mode \
    -name func_sslvm40cw_h \
    -sdc_files "../in/sdc/./sdc_dir/sdc_dir_file.sdc ../in/sdc/constraint_1.sdc ../in/sdc/constraint_2.sdc"
create_constraint_mode \
    -name scan_sslvm40cw_s \
    -sdc_files "../in/sdc/constraint_3.sdc ../in/sdc/constraint_4.sdc"
create_constraint_mode \
    -name scan_sslvm40cw_h \
    -sdc_files "../in/sdc/constraint_3.sdc ../in/sdc/constraint_4.sdc"
create_constraint_mode \
    -name scan_ffhv0cb_h \
    -sdc_files "../in/sdc/constraint_3.sdc ../in/sdc/constraint_4.sdc"

create_analysis_view \
    -name func_sslvm40cw_s \
    -constraint_mode func_sslvm40cw_s \
    -delay_corner func_sslvm40cw_s
create_analysis_view \
    -name func_sslvm40cw_h \
    -constraint_mode func_sslvm40cw_h \
    -delay_corner func_sslvm40cw_h
create_analysis_view \
    -name scan_sslvm40cw_s \
    -constraint_mode scan_sslvm40cw_s \
    -delay_corner scan_sslvm40cw_s
create_analysis_view \
    -name scan_sslvm40cw_h \
    -constraint_mode scan_sslvm40cw_h \
    -delay_corner scan_sslvm40cw_h
create_analysis_view \
    -name scan_ffhv0cb_h \
    -constraint_mode scan_ffhv0cb_h \
    -delay_corner scan_ffhv0cb_h

set_analysis_view -setup " func_sslvm40cw_s scan_sslvm40cw_s" -hold " func_sslvm40cw_s scan_sslvm40cw_s  func_sslvm40cw_h scan_sslvm40cw_h scan_ffhv0cb_h "
