#!/usr/bin/perl

require 'hostap-lib.pl';

ui_print_header(undef, $text{'index_title'},'', undef, 1, 1);

%conf = %{get_hostapd_config()};

print ui_form_start("save.cgi");

print ui_table_start( 'Configuration' );

print ui_table_row($text{'ssid'}, ui_textbox("ssid", $conf{'ssid'},'ssid'), 32);

print ui_table_row($text{'wpa_passphrase'}, ui_password("wpa_passphrase", $conf{'wpa_passphrase'}, 40));

print ui_columns_end();

print ui_form_end([ [ undef, $text{'save_config'} ], [ 'cancel', $text{'cancel_config_changes'} ] ]);


