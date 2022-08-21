create_library_set \
    -name sslvm40 \
    -timing " \
        /Users/leonidnidekker/Dropbox/asic/the_flow/testing_source/lib/test_file_ss_0p81v_m40c.lib \
        /Users/leonidnidekker/Dropbox/asic/the_flow/testing_source/lib/test_file_1_worst_case.lib" \
    -si " \
        /Users/leonidnidekker/Dropbox/asic/the_flow/testing_source/cdb/test_file_ss_0p81v_m40c.cdb \
        /Users/leonidnidekker/Dropbox/asic/the_flow/testing_source/cdb/test_file_1_worst_case.cdb"
create_library_set \
    -name ffhv0 \
    -timing " \
        /Users/leonidnidekker/Dropbox/asic/the_flow/testing_source/lib/test_file_ff_0p99v_0c.lib \
        /Users/leonidnidekker/Dropbox/asic/the_flow/testing_source/lib/test_file_1_best_case.lib" \
    -si " \
        /Users/leonidnidekker/Dropbox/asic/the_flow/testing_source/cdb/test_file_ff_0p99v_0c.cdb \
        /Users/leonidnidekker/Dropbox/asic/the_flow/testing_source/cdb/test_file_1_best_case.cdb"

create_timing_condition \
    -name sslvm40 \
    -library_sets "sslvm40"
create_timing_condition \
    -name ffhv0 \
    -library_sets "ffhv0"

create_rc_corner \
    -name cw_m40 \
    -temperature -40 \
    -qrc_tech /Users/leonidnidekker/Dropbox/asic/the_flow/testing_source/qrc/qrcTech.cworst
create_rc_corner \
    -name cb_0 \
    -temperature 0 \
    -qrc_tech /Users/leonidnidekker/Dropbox/asic/the_flow/testing_source/qrc/qrcTech.cbest

create_delay_corner \
    -name sslvm40cw_s \
    -timing_condition sslvm40 \
    -rc_corner cw_m40
create_delay_corner \
    -name sslvm40cw_h \
    -timing_condition sslvm40 \
    -rc_corner cw_m40
create_delay_corner \
    -name ffhv0cb_h \
    -timing_condition ffhv0 \
    -rc_corner cb_0

create_constraint_mode \
    -name func \
    -sdc_files "../in/sdc/func.tcl ../in/sdc/scan.tcl"
create_constraint_mode \
    -name scan \
    -sdc_files "../in/sdc/scan.tcl"

create_analysis_view \
    -name func_sslvm40cw_s \
    -constraint_mode func \
    -delay_corner sslvm40cw_s
create_analysis_view \
    -name func_sslvm40cw_h \
    -constraint_mode func \
    -delay_corner sslvm40cw_h
create_analysis_view \
    -name scan_sslvm40cw_s \
    -constraint_mode scan \
    -delay_corner sslvm40cw_s
create_analysis_view \
    -name scan_sslvm40cw_h \
    -constraint_mode scan \
    -delay_corner sslvm40cw_h
create_analysis_view \
    -name scan_ffhv0cb_h \
    -constraint_mode scan \
    -delay_corner ffhv0cb_h

set_analysis_view -setup " func_sslvm40cw_s scan_sslvm40cw_s" -hold " func_sslvm40cw_s scan_sslvm40cw_s  func_sslvm40cw_h scan_sslvm40cw_h scan_ffhv0cb_h "
