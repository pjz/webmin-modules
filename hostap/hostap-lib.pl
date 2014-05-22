=head1 hostap-lib.pl

  Functions for configuring the basics of hostapd

=cut

BEGIN { push(@INC, ".."); };
use WebminCore;
init_config();

=head2 get_hostapd_config()

return a reference to the hostapd config options as a hash. 

=cut

sub get_hostapd_config()
{
	my $lref = &read_file_lines($config{'hostapd_config'});
	my %config;
	my $lnum = 0;
	foreach my $line (@$lref) {
		if ($line =~ /^[^#]+=/) {
			my ($k, $v) = split(/=/, $line, 2);
			if ($k) {
				$config{$k} = $v;
			}
		}
		$lnum++;
	}
	return \%config;
}


=head2 set_hostapd_config(changedvals)

Change the configuration options listed as keys in hash that changedvals references to their corresponding values

=cut
sub set_hostapd_config
{
	my %changedvals = %{shift()};
	my $lref = &read_file_lines($config{'hostapd_config'});
	my $lnum = 0;
	foreach my $line (@$lref) {
		if ($line =~ /^[^#]+=/) {
			my ($n, $v) = split(/\s+/, $line, 2);
			if (exists($changedvals{$n})) {
				# we're at the config line, set it
				${$lref}[$lnum] = $n."=".$changedvals{$n};
			}
		}
		$lnum++;
	}
	flush_file_lines($config{'hostapd_config'})

}



