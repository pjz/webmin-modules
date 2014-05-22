#!/usr/bin/perl

require 'hostap-lib.pl';

ReadParse();

error_setup($text{'save_error'});

if (! $in{'cancel'}) {

	my %changes = ();
 
	# validate input
        my $ssid_len = length($in{'ssid'});
        if (($ssid_len <= 0) || (32 < $ssid_len)) { error($text{'ssid_wrong_length'}); }
        $in{'ssid'} =~ /[\w ]+/ || error($text{'ssid_bad_characters'});
	$changes{'ssid'} = $in{'ssid'};

        $in{'wpa_passphrase'} =~ /[\w ]+/ || error($text{'passphrase_bad_characters'});
	$changes{'wpa_passphrase'} = $in{'wpa_passphrase'};

        &set_hostapd_config(\%changes);

}

&redirect('')
